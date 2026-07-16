Name:           asciimathml
# See versio in package.json
Version:        2.6.1
Release:        alt1
Summary:        Translate simple calculator-style math expressions on a webpage to MathML
Group:          Other
BuildArch:      noarch
Source:         %name-%version.tar
License:        MIT

%description
ASCIIMathML.js is a compact JavaScript program that translates
simple calculator-style math expressions on a webpage to MathML.

The resulting page can be displayed with any browser that can render MathML.

%prep
%setup

%install
mkdir -p %buildroot%_datadir/javascript
install ASCIIMathML.js LaTeXMathML.js %buildroot%_datadir/javascript/

%files
%doc *.md *.MD
%_datadir/javascript/*

%changelog
* Thu Jul 16 2026 Fr. Br. George <george@altlinux.org> 2.6.1-alt1
- Initial build for ALT
