%define dist XML-NamespaceSupport
Name: perl-%dist
Version: 1.11
Release: alt3

Summary: A simple generic namespace support class
License: GPL Artistic
Group: Development/Perl

URL: %CPAN %dist
Source: %dist-%version.tar.gz

BuildArch: noarch

# Automatically added by buildreq on Wed Nov 16 2011
BuildRequires: perl-Pod-Escapes perl-devel

%description
This module offers a simple to process namespaced XML names (unames)
from within any application that may need them. It also helps maintain
a prefix to namespace URI map, and provides a number of basic checks.

%prep
%setup -q -n %dist-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files 
%doc Changes README
%perl_vendor_privlib/XML

%changelog
* Wed Nov 16 2011 Alexey Tourbin <at@altlinux.ru> 1.11-alt3
- disabled build dependency on perl-Module-Install

* Wed Oct 26 2011 Alexey Tourbin <at@altlinux.ru> 1.11-alt2
- rebuilt as plain src.rpm

* Mon Mar 29 2010 Alexey Tourbin <at@altlinux.ru> 1.11-alt1
- 1.10 -> 1.11
- updated build dependencies for new Module::Install

* Wed Jul 22 2009 Alexey Tourbin <at@altlinux.ru> 1.10-alt1
- 1.09 -> 1.10

* Fri Jun 10 2005 Alexey Tourbin <at@altlinux.ru> 1.09-alt1
- 1.08 -> 1.09
- fixed description
- manual pages not packaged (use perldoc)

* Sat Feb 19 2005 ALT QA Team Robot <qa-robot@altlinux.org> 1.08-alt1.1
- Rebuilt with rpm-build-perl-0.5.1.

* Fri Mar 21 2003 Stanislav Ievlev <inger@altlinux.ru> 1.08-alt1
- 1.08

* Tue Nov 12 2002 Stanislav Ievlev <inger@altlinux.ru> 1.06-alt1
- Inital release
