%define module	Convert-UUlib

Name: perl-%module
Version: 1.4
Release: alt2
Epoch: 2
Summary: Perl interface to the uulib library (a.k.a. uudeview/uuenview)

License: GPL or Artistic
Group: Development/Perl
Url: http://search.cpan.org/dist/%module/
Packager: Alexey Shabalin <shaba@altlinux.ru>

# BuildArch: noarch
Source: %module-%version.tar.gz
Patch1: Convert-UUlib-1.32-alt-system-libuu.patch
Patch2: Convert-UUlib-1.32-alt_strip_stuff_not_in_libuu.patch

# Automatically added by buildreq on Mon Oct 10 2011
BuildRequires: libuu-devel perl-devel

%description
The UUDeview library is a highly portable set of functions
that provide facilities for decoding uuencoded, xxencoded,
Base64 and BinHex-Encoded files as well as for encoding
binary files into all of these representations except BinHex.

%prep
%setup -q -n %module-%version
%patch1 -p1
%patch2 -p1

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README doc
%perl_vendor_archlib/Convert
%perl_vendor_autolib/Convert

%changelog
* Mon Oct 10 2011 Alexey Tourbin <at@altlinux.ru> 2:1.4-alt2
- rebuilt for perl-5.14

* Thu Jun 09 2011 Alexey Shabalin <shaba@altlinux.ru> 2:1.4-alt1.1
- new version 1.4

* Sat Nov 06 2010 Vladimir Lettiev <crux@altlinux.ru> 1:1.33-alt1.1
- rebuilt with perl 5.12

* Tue Jul 13 2010 Igor Vlasenko <viy@altlinux.ru> 1:1.33-alt1
- automated CPAN update

* Fri Oct 23 2009 Alexey Shabalin <shaba@altlinux.ru> 1:1.32-alt1
- new version 1.32
- build with system libuu

* Fri Oct 17 2008 Alexey Shabalin <shaba@altlinux.ru> 1:1.12-alt1
- new version 1.12

* Wed Jun 18 2008 Alexey Shabalin <shaba@altlinux.ru> 1:1.11-alt1
- new version 1.11

* Sat Jun 02 2007 Alexey Shabalin <shaba@altlinux.ru> 1:1.09-alt1
- new version 1.09

* Thu Feb 01 2007 Alexey Shabalin <shaba@altlinux.ru> 1:1.08-alt1
- new version 1.08

* Thu Dec 08 2005 Alexey Shabalin <shaba@altlinux.ru> 1:1.06-alt1
- new version 1.06
- 1.051 -> 1.06; raised epoch to deploy new version

* Mon Apr 25 2005 Alexey Shabalin <shaba@altlinux.ru> 1.051-alt1
- update Convert-UUlib-1.051

* Thu Oct 07 2004 Alexey Shabalin <shaba@altlinux.ru> 1.03-alt1
- update Convert-UUlib-1.03

* Wed Mar 17 2004 Alexey Shabalin <shaba@altlinux.ru> 1.01-alt1
- update Convert-UUlib-1.01

* Thu Dec 04 2003 Alexey Shabalin <shaba@altlinux.ru> 1.0-alt0.1
- First release for ALT
