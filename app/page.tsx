'use client';

import { useState, useEffect } from 'react';
import { useAuthState } from 'react-firebase-hooks/auth';
import { signInWithPopup, GoogleAuthProvider, signOut } from 'firebase/auth';
import { auth } from '../firebase';
import axios from 'axios';

export default function Home() {
  const [user] = useAuthState(auth);
  const [message, setMessage] = useState('');
  const [chatHistory, setChatHistory] = useState<Array<{ message: string; response: string }>>([]);

  const signIn = () => {
    const provider = new GoogleAuthProvider();
    signInWithPopup(auth, provider);
  };

  const handleSignOut = () => {
    signOut(auth);
  };

  const sendMessage = async () => {
    if (message.trim() === '') return;

    try {
      const response = await axios.get(`http://your-backend-url/api/v1/loilibre_rag/${encodeURIComponent(message)}`);
      setChatHistory([...chatHistory, { message, response: response.data.response }]);
      setMessage('');
    } catch (error) {
      console.error('Error sending message:', error);
    }
  };

  return (
    <div className="min-h-screen bg-gray-100 p-4">
      <div className="max-w-2xl mx-auto bg-white rounded-lg shadow-md p-6">
        <h1 className="text-2xl font-bold mb-4">Loilibre Chat</h1>
        {user ? (
          <>
            <button onClick={handleSignOut} className="bg-red-500 text-white px-4 py-2 rounded mb-4">Sign Out</button>
            <div className="mb-4 h-64 overflow-y-auto border border-gray-300 rounded p-2">
              {chatHistory.map((chat, index) => (
                <div key={index} className="mb-2">
                  <p className="font-bold">You: {chat.message}</p>
                  <p>Assistant: {chat.response}</p>
                </div>
              ))}
            </div>
            <div className="flex">
              <input
                type="text"
                value={message}
                onChange={(e) => setMessage(e.target.value)}
                className="flex-grow border border-gray-300 rounded-l px-4 py-2"
                placeholder="Type your message..."
              />
              <button onClick={sendMessage} className="bg-blue-500 text-white px-4 py-2 rounded-r">Send</button>
            </div>
          </>
        ) : (
          <button onClick={signIn} className="bg-blue-500 text-white px-4 py-2 rounded">Sign In with Google</button>
        )}
      </div>
    </div>
  );
}