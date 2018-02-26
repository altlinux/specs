Name: api-sanity-autotest
Version: 1.11
Release: alt1

Summary: API Sanity Autotest

Group: Development/Other
License: GPL/LGPL
Url: http://ispras.linux-foundation.org/index.php/API_Sanity_Autotest

Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: http://ispras.linux-foundation.org/images/1/16/Api-sanity-autotest-%version.tar
Requires: gcc binutils

BuildArch: noarch

%description
API Sanity Autotest is an automatic generator of basic unit tests for
shared C/C++ libraries. It helps to quickly generate simple ("sanity" or
"shallow"-quality) tests for all functions from the target library API
using their signatures and data type definitions straight from the library
header files ("Header-Driven Generation"). The quality of generated tests
allows to check absence of critical errors in simple use cases and can
be improved by involving of highly reusable specialized types for the
library. API Sanity Autotest can execute generated tests and detect
all kinds of emitted signals, early program exits, program hanging and
specified requirement failures. API Sanity Autotest can be considered
as a tool for out-of-box low-cost sanity checking of library API or as
a test development framework for initial generation of templates for
advanced tests.

%prep
%setup
chmod 644 LICENSE

%install
install -d %buildroot%_bindir
install -m0755 %name.pl %buildroot%_bindir/%name

%files
%doc LICENSE
%_bindir/%name

%changelog
* Tue Jul 27 2010 Vitaly Lipatov <lav@altlinux.ru> 1.11-alt1
- initial build for ALT Linux Sisyphus
