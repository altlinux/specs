%define oname jquery
Name: javascript-jquery
Version: 1.7.2
Release: alt1

Summary: jQuery is a new kind of JavaScript Library

Group: System/Libraries
License: LGPL
Url: http://jquery.com/

Source: http://code.jquery.com/jquery-%version.js
Source1: http://code.jquery.com/jquery-%version.min.js

BuildArch: noarch

BuildRequires: rpm-macros-javascript >= 0.2

Requires: javascript-common

%description
jQuery is a fast and concise JavaScript Library that simplifies HTML
document traversing, event handling, animating, and Ajax interactions
for rapid web development. jQuery is designed to change the way that
you write JavaScript.

%prep

%install
mkdir -p %buildroot%_jquerydir/
install -m644 %SOURCE0 %buildroot%_jquerydir/jquery.js
install -m644 %SOURCE1 %buildroot%_jquerydir/jquery.min.js

%files
%_jquerydir/*

%changelog
* Wed Aug 08 2012 Vitaly Lipatov <lav@altlinux.ru> 1.7.2-alt1
- 1.7.2 version
- add minified version

* Fri Jan 27 2012 Vitaly Lipatov <lav@altlinux.ru> 1.7.1-alt1
- initial build for ALT Linux Sisyphus

