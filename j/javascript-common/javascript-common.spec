Name: javascript-common
Version: 0.1
Release: alt1

Summary: Javascript libraries common package

Group: System/Libraries
License: GPL
Url: http://www.altlinux.org/JavaScript_Policy

Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: %name-%version.tar

BuildArch: noarch

BuildRequires: rpm-macros-javascript

%description
%summary

%prep
%setup

%install
mkdir -p %buildroot%_jsdir/

%files
%_jsdir/

%changelog
* Tue Oct 11 2011 Vitaly Lipatov <lav@altlinux.ru> 0.1-alt1
- initial build for ALT Linux Sisyphus

