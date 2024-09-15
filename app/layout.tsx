import './globals.css'
import type { Metadata } from 'next'

export const metadata: Metadata = {
  title: 'Loilibre Chat',
  description: 'A simple chat app for Loilibre',
}

export default function RootLayout({
  children,
}: {
  children: React.ReactNode
}) {
  return (
    <html lang="en">
      <body>{children}</body>
    </html>
  )
}