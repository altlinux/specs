Name: checkduplicatelibrarysymbols
Version: 0.2
Release: alt1

Summary: Check for duplicate library symbols scripts

License: Public domain
Group: File tools
Url: http://altlinux.org

BuildArch: noarch

Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: %name-%version.tar

Requires: etersoft-build-utils

%description
Scripts for print out duplicated library symbols for a binary(s), library(s) or
packages (via hasher).

%prep
%setup

%install
mkdir -p %buildroot%_datadir/%name/
cp -a * %buildroot%_datadir/%name/

%files
%_datadir/%name/

%changelog
* Sun Dec 23 2018 Vitaly Lipatov <lav@altlinux.ru> 0.2-alt1
- improve check_deps_in_hasher.sh

* Sat Sep 08 2018 Vitaly Lipatov <lav@altlinux.ru> 0.1-alt1
- initial build for ALT Linux
