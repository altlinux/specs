%define dist Image-Base
Name: perl-%dist
Version: 1.16
Release: alt1

Summary: Base class for image manipulation
License: LGPL
Group: Development/Perl

URL: %CPAN %dist
Source: http://www.cpan.org/authors/id/K/KR/KRYDE/Image-Base-1.16.tar.gz

BuildArch: noarch

# Automatically added by buildreq on Wed Mar 09 2011
BuildRequires: perl-devel

%description
Image::Base is a base class for loading, manipulating and saving images.
This class should not be used directly. Known inheritors are Image::Xbm
and Image::Xpm.

%prep
%setup -q -n %dist-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README
%dir %perl_vendor_privlib/Image
%perl_vendor_privlib/Image/Base.pm

%changelog
* Mon Sep 19 2011 Igor Vlasenko <viy@altlinux.ru> 1.16-alt1
- automated CPAN update

* Wed Mar 09 2011 Alexey Tourbin <at@altlinux.ru> 1.15-alt1
- 1.12 -> 1.15

* Thu Jan 13 2011 Alexey Tourbin <at@altlinux.ru> 1.12-alt1
- 1.07 -> 1.12

* Fri Jul 31 2009 Alexey Tourbin <at@altlinux.ru> 1.07-alt2
- rebuilt

* Thu Dec 16 2004 Alexey Tourbin <at@altlinux.ru> 1.07-alt1
- initial revision
- license: LGPL
