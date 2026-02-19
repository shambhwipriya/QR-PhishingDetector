# QR Code Phishing Detector
A lightweight, browser-based QR code phishing detector that scans QR images, decodes embedded content, and performs basic security checks to identify potentially malicious or suspicious links.
This tool runs entirely on the client side and does not upload any data to external servers, ensuring privacy and fast performance.
## Features
- QR Code decoding from uploaded images
- Automatic URL extraction from QR codes
- Phishing detection using heuristic rules
+ Visual status classification: [Safe] [Suspicious] [Unknown]
- Clickable decoded links for verification
- Fully client-side operation (no backend required)
- Lightweight and fast
## How It Works
1. User uploads an image containing a QR code.
2. The application uses the jsQR library to decode the QR code.
3. If the decoded content is a URL, heuristic phishing checks are performed.
4. The result is displayed with security status and explanation.
## Technologies Used
- [ HTML5 ]
- [ CSS3 ]
- [ JavaScript (Vanilla) ]
- [ jsQR Library (QR decoding) ]
## Installation
No installation required. Simply download or clone the repository and open the HTML file in a web browser.
## Security and Privacy
- All processing happens locally in your browser.
- No image or data is uploaded to any server.
- No tracking or logging.
## Future Improvements
Possible enhancements include:
- Machine learning based phishing detection
- Real-time camera scanning
- Domain reputation lookup
- Integration with phishing databases
- Detailed risk scoring system
- Browser extension version
