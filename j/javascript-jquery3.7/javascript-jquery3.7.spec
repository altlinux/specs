%define oname jquery
Name: javascript-jquery3.7
Version: 3.7.1
Release: alt1

Summary: jQuery is a new kind of JavaScript Library

Group: System/Libraries
License: MIT
Url: http://jquery.com/

Source: http://code.jquery.com/jquery-%version.js
Source1: http://code.jquery.com/jquery-%version.min.js

BuildArch: noarch

BuildRequires(pre): rpm-macros-javascript >= 0.2

Requires: javascript-common
Conflicts: javascript-jquery > %version
Obsoletes: javascript-jquery <= %version

%description
jQuery is a fast and concise JavaScript Library that simplifies HTML
document traversing, event handling, animating, and Ajax interactions
for rapid web development. jQuery is designed to change the way that
you write JavaScript.

This is compatible build for application which are not ready yet
for JQuery 4.0/migrate.

%prep

%install
mkdir -p %buildroot%_jquerydir/
install -m644 %SOURCE0 %buildroot%_jquerydir/jquery.js
install -m644 %SOURCE1 %buildroot%_jquerydir/jquery.min.js

%files
%_jquerydir/*

%changelog
* Mon Aug 17 2026 L.A. Kostis <lakostis@altlinux.ru> 3.7.1-alt1
- Initial build for ALTLinux.
