%define dist Image-Xbm
Name: perl-%dist
Version: 1.08
Release: alt3

Summary: Load, create, manipulate and save xbm image files.
License: LGPL
Group: Development/Perl

URL: %CPAN %dist
Source: %dist-%version.tar.gz

Patch0: perl-Image-Xbm-1.08-cpan-7439-filehandle.patch
Patch1: perl-Image-Xbm-1.08-alt-perlio.patch
Patch2: perl-Image-Xbm-1.08-alt-no-gensym.patch

BuildArch: noarch

# Automatically added by buildreq on Fri Nov 11 2011
BuildRequires: perl-Image-Base perl-devel

%description
This class module provides basic load, manipulate and save functionality
for the xbm file format. It inherits from Image::Base which provides
additional manipulation functionality.

%prep
%setup -q -n %dist-%version
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%dir %perl_vendor_privlib/Image
%perl_vendor_privlib/Image/Xbm.pm

%changelog
* Fri Nov 11 2011 Alexey Tourbin <at@altlinux.ru> 1.08-alt3
- rebuilt

* Sat Apr 16 2005 Alexey Tourbin <at@altlinux.ru> 1.08-alt2
- alt-perlio.patch: use PerlIO::scalar instead of IO::String
- alt-no-gensym.patch: use autovivification instead of Symbol::gensym

* Thu Dec 16 2004 Alexey Tourbin <at@altlinux.ru> 1.08-alt1.1
- allow new() to accept filehandles (patch from cpan #7439)

* Thu Dec 16 2004 Alexey Tourbin <at@altlinux.ru> 1.08-alt1
- initial revision
- license: LGPL
