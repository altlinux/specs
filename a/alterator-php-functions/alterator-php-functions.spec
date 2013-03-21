Name: alterator-php-functions
Version: 1.1
Release: alt1

Packager: Paul Wolneykien <manowar@altlinux.ru>

BuildArch: noarch

Source: %name-%version.tar.gz

Summary: Helps the base PHP configuration management
License: GPLv3
Group: System/Base

Requires: alterator-service-functions >= 2.0.0-alt1

%description
Helps the base PHP configuration management.

%prep
%setup -q

%install
%makeinstall

%files
%_bindir/*

%changelog
* Thu Mar 21 2013 Paul Wolneykien <manowar@altlinux.org> 1.1-alt1
- Require alterator-service-functions >= 2.0.0-alt1.
- Updated for new alterator-service-functions. (thx Mikhail Efremov).

* Mon Sep 03 2012 Paul Wolneykien <manowar@altlinux.ru> 1.0-alt3
- Try major PHP version if no ini file is found for the full
  version number.

* Tue Nov 16 2010 Paul Wolneykien <manowar@altlinux.ru> 1.0-alt2
- Fix the value write function.
- Do not redefine constants.

* Mon Nov 01 2010 Paul Wolneykien <manowar@altlinux.ru> 1.0-alt1
- Initial release
