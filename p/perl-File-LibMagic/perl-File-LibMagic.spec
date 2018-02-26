%define dist File-LibMagic
Name: perl-File-LibMagic
Version: 0.96
Release: alt2

Summary: Perl wrapper for libmagic
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source: %dist-%version.tgz

# Automatically added by buildreq on Fri Oct 07 2011
BuildRequires: libmagic-devel perl-devel zlib-devel

%description
The "File::LibMagic" is a simple perl interface to libmagic from
the file-4.x package from Christos Zoulas (ftp://ftp.astron.com/pub/file/).

%prep
%setup -q -n %dist-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README
%perl_vendor_archlib/File
%perl_vendor_autolib/File

%changelog
* Fri Oct 07 2011 Alexey Tourbin <at@altlinux.ru> 0.96-alt2
- rebuilt for perl-5.14

* Fri Sep 23 2011 Igor Vlasenko <viy@altlinux.ru> 0.96-alt1
- automated CPAN update

* Sat Nov 06 2010 Vladimir Lettiev <crux@altlinux.ru> 0.90-alt1.1
- rebuilt with perl 5.12

* Wed Feb 18 2009 Alexey Tourbin <at@altlinux.ru> 0.90-alt1
- 0.89 -> 0.90

* Wed Sep 03 2008 Igor Vlasenko <viy@altlinux.ru> 0.89-alt1
- removed perl dir ownership
- new version

* Fri Jun 01 2007 Igor Vlasenko <viy@altlinux.ru> 0.84-alt1
- first build for ALT Linux Sisyphus

