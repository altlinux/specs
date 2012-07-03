%define dist Image-Xpm
Name: perl-%dist
Version: 1.12
Release: alt1

Summary: Load, create, manipulate and save xpm image files
License: GPL
Group: Development/Perl

URL: %CPAN %dist
Source: http://www.cpan.org/authors/id/S/SR/SREZIC/Image-Xpm-1.12.tar.gz

Patch1: perl-Image-Xpm-1.11-alt-perlio.patch
Patch2: perl-Image-Xpm-1.11-alt-no-gensym.patch

BuildArch: noarch

# Automatically added by buildreq on Thu Jun 10 2010
BuildRequires: perl-Image-Base perl-PerlIO perl-devel

%description
This class module provides basic load, manipulate and save functionality
for the xpm file format. It inherits from Image::Base which provides
additional manipulation functionality.

%prep
%setup -q -n %dist-%version
%patch1 -p1
%patch2 -p1

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README
%dir %perl_vendor_privlib/Image
%perl_vendor_privlib/Image/Xpm.pm

%changelog
* Mon Sep 19 2011 Igor Vlasenko <viy@altlinux.ru> 1.12-alt1
- automated CPAN update

* Thu Jun 10 2010 Alexey Tourbin <at@altlinux.ru> 1.11-alt1
- 1.09 -> 1.11

* Sat Apr 16 2005 Alexey Tourbin <at@altlinux.ru> 1.09-alt2
- alt-perlio.patch: use PerlIO::scalar instead of IO::String
- alt-no-gensym.patch: use autovivification instead of Symbol::gensym

* Thu Dec 16 2004 Alexey Tourbin <at@altlinux.ru> 1.09-alt1.1
- allow new() to accept filehandles (patch from cpan #7438)

* Thu Dec 16 2004 Alexey Tourbin <at@altlinux.ru> 1.09-alt1
- initial revision
- license: GPL
