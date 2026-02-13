import { Inter } from 'next/font/google'
import './globals.css'
import Navbar from '@/components/Navbar'
import Footer from '@/components/Footer'
import WhatsAppButton from '@/components/WhatsAppButton'

const inter = Inter({ subsets: ['latin'] })

export const metadata = {
  title: 'ElevateWealthServices - Smart Financial Solutions',
  description: 'Mutual Funds, Insurance & Trading Services under one trusted platform. AMFI-registered distributor serving investors across India.',
  keywords: 'mutual funds, insurance, trading, financial services, AMFI, investment advisory',
}

export default function RootLayout({ children }) {
  return (
    <html lang="en" className="scroll-smooth">
      <body className={inter.className}>
        <Navbar />
        <main className="min-h-screen">
          {children}
        </main>
        <Footer />
        <WhatsAppButton />
      </body>
    </html>
  )
}
