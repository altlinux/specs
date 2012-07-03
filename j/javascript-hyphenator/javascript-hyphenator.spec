%define oname Hyphenator%20
Name: javascript-hyphenator
Version: 4.0.0
Release: alt1

Summary: Javascript that implements client-side hyphenation of HTML-Documents

Group: System/Libraries
License: LGPL
Url: http://code.google.com/p/hyphenator/

Source: http://hyphenator.googlecode.com/files/%oname%version.tar

BuildArch: noarch

BuildRequires: rpm-macros-javascript

Requires: javascript-common

%description
Javascript that implements client-side hyphenation of HTML-Documents.
- automatically hyphenates texts on websites if either the webdeveloper
  has included the script on the website or you use it as a bookmarklet on any site.
- runs on any modern browser that supports JavaScript and the soft hyphen (&shy;).
- automatically breaks URLs on any browser that supports the zero width space.
- runs on the client in order that the HTML source of the website may be served clean
  and svelte and that it can respond to text resizings by the user.
- follows the ideas of unobtrusive JavaScript.
- has a documented API and is highly configurable to meet your needs.
- supports a wide range of languages.
- relies on Franklin M. Liangs hyphenation algorithm (PDF) commonly known from LaTeX and OpenOffice.

%prep
%setup -n "%oname%version"

%install
cd "Hyphenator %version"
mkdir -p %buildroot%_jsdir/
install -m644 Hyphenator.js %buildroot%_jsdir/

mkdir -p %buildroot%_jsdir/patterns/
install -m644 patterns/*.js %buildroot%_jsdir/patterns/

cp *.html ../

%files
%doc *.html
%_jsdir/*

%changelog
* Wed Oct 19 2011 Vitaly Lipatov <lav@altlinux.ru> 4.0.0-alt1
- initial build for ALT Linux Sisyphus

