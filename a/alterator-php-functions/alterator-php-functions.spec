Name: alterator-php-functions
Version: 1.0
Release: alt2

Packager: Paul Wolneykien <manowar@altlinux.ru>

BuildArch: noarch

Source: %name-%version.tar.gz

Summary: Helps the base PHP configuration management
License: GPLv3
Group: System/Base

%description
Helps the base PHP configuration management.

%prep
%setup -q

%install
%makeinstall

%files
%_bindir/*

%changelog
* Tue Nov 16 2010 Paul Wolneykien <manowar@altlinux.ru> 1.0-alt2
- Fix the value write function.
- Do not redefine constants.

* Mon Nov 01 2010 Paul Wolneykien <manowar@altlinux.ru> 1.0-alt1
- Initial release
