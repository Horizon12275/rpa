// visit IRAS website (for managing taxes in Singapore)
https://www.iras.gov.sg/irashome/default.aspx

// increase timeout from default 10 seconds to 300 seconds
// to let user sign in, including using 2FA authentication
timeout 300

// log in to personal income tax using visual automation,
// instead of specifying XPath or other web identifiers
// that natively interact with web browser's backend
click ../.png/login_menu.png