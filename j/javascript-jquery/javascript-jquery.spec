%define oname jquery
Name: javascript-jquery
Version: 1.7.1
Release: alt1

Summary: jQuery is a new kind of JavaScript Library

Group: System/Libraries
License: LGPL
Url: http://jquery.com/

Source: http://code.jquery.com/jquery-%version.js

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

%files
%_jquerydir/*

%changelog
* Fri Jan 27 2012 Vitaly Lipatov <lav@altlinux.ru> 1.7.1-alt1
- initial build for ALT Linux Sisyphus

