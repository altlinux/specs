%define module Guard

Name: perl-%module
Version: 1.022
Release: alt2

Summary: Safe cleanup blocks for Perl
License: Perl
Group: Development/Perl

URL: %CPAN %module
Source: %module-%version.tar.gz

# Automatically added by buildreq on Sun Oct 09 2011
BuildRequires: perl-devel

%description
This module implements so-called "guards". A guard is something (usually an
object) that "guards" a resource, ensuring that it is cleaned up when expected.

%prep
%setup -n %module-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README
%perl_vendor_archlib/Guard*
%perl_vendor_autolib/Guard

%changelog
* Sun Oct 09 2011 Alexey Tourbin <at@altlinux.ru> 1.022-alt2
- rebuilt for perl-5.14

* Sun Jul 17 2011 Victor Forsiuk <force@altlinux.org> 1.022-alt1
- 1.022

* Sat Nov 06 2010 Vladimir Lettiev <crux@altlinux.ru> 1.021-alt1.1
- rebuilt with perl 5.12

* Wed Oct 07 2009 Victor Forsyuk <force@altlinux.org> 1.021-alt1
- Initial build.
