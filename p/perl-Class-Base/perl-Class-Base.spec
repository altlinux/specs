%define module Class-Base

Name: perl-%module
Version: 0.04
Release: alt1

Summary: Class::Base - useful base class for deriving other modules
License: Perl
Group: Development/Perl

URL: %CPAN %module
Source: http://www.cpan.org/modules/by-module/Class/%module-%version.tar.gz

BuildArch: noarch

# Automatically added by buildreq on Sun Mar 25 2012
BuildRequires: perl-devel

%description
This module implements a simple base class from which other modules
can be derived, thereby inheriting a number of useful methods such as
new(), init(), params(), clone(), error() and debug().

%prep
%setup -n %module-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%perl_vendor_privlib/Class

%changelog
* Sun Mar 25 2012 Victor Forsiuk <force@altlinux.org> 0.04-alt1
- 0.04

* Mon Nov 22 2010 Igor Vlasenko <viy@altlinux.ru> 0.03-alt2.1
- repair after perl 5.12 upgrade using girar-nmu

* Thu Jul 26 2007 Victor Forsyuk <force@altlinux.org> 0.03-alt2
- Spec cleanups.

* Wed Aug 24 2005 Alexey Morozov <morozov@altlinux.org> 0.03-alt1
- Initial build for ALT Linux
