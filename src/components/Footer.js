import Link from 'next/link'
import { Mail, Phone, MapPin, TrendingUp } from 'lucide-react'

export default function Footer() {
  const currentYear = new Date().getFullYear()

  return (
    <footer className="bg-gradient-to-br from-gray-900 via-gray-800 to-gray-900 text-gray-300">
      {/* Main Footer */}
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-12">
        <div className="grid grid-cols-1 md:grid-cols-4 gap-8">
          {/* Company Info */}
          <div className="col-span-1 md:col-span-2">
            <div className="flex items-center space-x-2 mb-4">
              <div className="bg-gradient-to-br from-primary-500 to-primary-700 p-2 rounded-lg">
                <TrendingUp className="w-6 h-6 text-white" />
              </div>
              <span className="text-xl font-bold text-white">
                ElevateWealthServices
              </span>
            </div>
            <p className="text-gray-400 mb-4 leading-relaxed">
              Your trusted partner for Mutual Fund Advisory, Insurance Solutions, and Trading Services. Building wealth through informed financial decisions.
            </p>
            <div className="space-y-2">
              <div className="flex items-center space-x-2 text-sm">
                <Mail className="w-4 h-4 text-primary-400" />
                <a href="mailto:info@elevatewealthservices.com" className="hover:text-primary-400 transition-colors">
                  info@elevatewealthservices.com
                </a>
              </div>
              <div className="flex items-center space-x-2 text-sm">
                <Phone className="w-4 h-4 text-primary-400" />
                <a href="tel:+919876543210" className="hover:text-primary-400 transition-colors">
                  +91 98765 43210
                </a>
              </div>
              <div className="flex items-center space-x-2 text-sm">
                <MapPin className="w-4 h-4 text-primary-400" />
                <span>Ludhiana, Punjab, India</span>
              </div>
            </div>
          </div>

          {/* Quick Links */}
          <div>
            <h3 className="text-white font-semibold mb-4">Quick Links</h3>
            <ul className="space-y-2">
              <li>
                <Link href="/" className="hover:text-primary-400 transition-colors text-sm">
                  Home
                </Link>
              </li>
              <li>
                <Link href="/about" className="hover:text-primary-400 transition-colors text-sm">
                  About Us
                </Link>
              </li>
              <li>
                <Link href="/services" className="hover:text-primary-400 transition-colors text-sm">
                  Services
                </Link>
              </li>
              <li>
                <Link href="/contact" className="hover:text-primary-400 transition-colors text-sm">
                  Contact
                </Link>
              </li>
            </ul>
          </div>

          {/* Services */}
          <div>
            <h3 className="text-white font-semibold mb-4">Our Services</h3>
            <ul className="space-y-2">
              <li className="text-sm">Mutual Fund Distribution</li>
              <li className="text-sm">Life & Health Insurance</li>
              <li className="text-sm">General Insurance</li>
              <li className="text-sm">Trading & Brokerage</li>
            </ul>
          </div>
        </div>

        {/* AMFI Certification */}
        <div className="mt-8 pt-8 border-t border-gray-700">
          <div className="bg-gradient-to-r from-gray-800 to-gray-750 p-4 rounded-lg">
            <p className="text-sm font-semibold text-white mb-2">
              📜 AMFI-Registered Mutual Fund Distributor
            </p>
            <p className="text-xs text-gray-400">
              ARN: [Your ARN Number Here] | Valid till: [Validity Date]
            </p>
          </div>
        </div>

        {/* Legal Disclaimers */}
        <div className="mt-6 pt-6 border-t border-gray-700">
          <h4 className="text-white font-semibold mb-3 text-sm">Important Disclaimers</h4>
          
          <div className="space-y-3 text-xs text-gray-400 leading-relaxed">
            <p>
              <strong className="text-gray-300">Mutual Funds:</strong> Mutual Fund investments are subject to market risks. Read all scheme-related documents carefully before investing. Past performance is not indicative of future returns. ElevateWealthServices is an AMFI-registered Mutual Fund Distributor. We earn commissions on Regular Plans sold.
            </p>
            
            <p>
              <strong className="text-gray-300">Insurance:</strong> Insurance is the subject matter of solicitation. For more details on risk factors, terms, and conditions, please read the sales brochure carefully before concluding a sale. ElevateWealthServices is a registered insurance intermediary.
            </p>
            
            <p>
              <strong className="text-gray-300">Trading & Brokerage:</strong> Trading in securities markets carries inherent risks. Investors should trade based on their own research and risk appetite. Services provided in partnership with SEBI-registered brokers.
            </p>
          </div>
        </div>
      </div>

      {/* Bottom Bar */}
      <div className="border-t border-gray-700">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-6">
          <div className="flex flex-col md:flex-row justify-between items-center space-y-2 md:space-y-0">
            <p className="text-sm text-gray-400">
              © {currentYear} ElevateWealthServices. All rights reserved.
            </p>
            <div className="flex space-x-6 text-sm">
              <Link href="#" className="hover:text-primary-400 transition-colors">
                Privacy Policy
              </Link>
              <Link href="#" className="hover:text-primary-400 transition-colors">
                Terms of Service
              </Link>
            </div>
          </div>
        </div>
      </div>
    </footer>
  )
}
