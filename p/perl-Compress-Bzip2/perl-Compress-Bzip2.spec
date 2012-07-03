%define dist Compress-Bzip2
Name: perl-%dist
Version: 2.09
Release: alt4

Summary: Interface to Bzip2 compression library
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source: %dist-%version.tar.gz

# Automatically added by buildreq on Fri Oct 07 2011
BuildRequires: bzlib-devel perl-devel

%description
The Compress::Bzip2 module provides a Perl interface to the Bzip2
compression library.

%prep
%setup -q -n %dist-%version

%build
export BUILD_BZLIB=0
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README
%perl_vendor_archlib/Compress
%perl_vendor_autolib/Compress

%changelog
* Fri Oct 07 2011 Alexey Tourbin <at@altlinux.ru> 2.09-alt4
- rebuilt for perl-5.14

* Tue Oct 04 2011 Alexey Tourbin <at@altlinux.ru> 2.09-alt3
- rebuilt

* Sat Nov 06 2010 Vladimir Lettiev <crux@altlinux.ru> 2.09-alt2.1
- rebuilt with perl 5.12

* Mon Oct 13 2008 Alexey Tourbin <at@altlinux.ru> 2.09-alt2
- Compress/Bzip2.pm: removed AutoLoader
- fixed directory packaging

* Sat Aug 27 2005 Andrey Brindeew <abr@altlinux.org> 2.09-alt1
- 2.09

* Mon Nov 24 2003 Andrey Brindeew <abr@altlinux.ru> 1.02-alt2
- Url and Summary tag was fixed

* Wed Jul 30 2003 Andrey Brindeew <abr@altlinux.ru> 1.02-alt1
- First build for ALT Linux

