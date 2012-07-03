%define dist Sub-Name
Name: perl-%dist
Version: 0.05
Release: alt3
Epoch: 1

Summary: (re)name a sub
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source: %dist-%version.tar.gz

# Automatically added by buildreq on Fri Oct 07 2011
BuildRequires: perl-devel

%description
subname NAME, CODEREF
Assigns a new name to referenced sub.

%prep
%setup -q -n %dist-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README
%perl_vendor_archlib/Sub
%perl_vendor_autolib/Sub

%changelog
* Fri Oct 07 2011 Alexey Tourbin <at@altlinux.ru> 1:0.05-alt3
- rebuilt for perl-5.14

* Fri Nov 12 2010 Vladimir Lettiev <crux@altlinux.ru> 1:0.05-alt2
- new release

* Mon Sep 20 2010 Alexey Tourbin <at@altlinux.ru> 1:0.05-alt1
- 0.04 -> 0.05
- built for perl-5.12

* Fri Nov 13 2009 Michael Bochkaryov <misha@altlinux.ru> 0.4-alt1
- 0.4 version

* Mon Oct 06 2008 Igor Vlasenko <viy@altlinux.ru> 0.03-alt1.1
- NMU fixing directory ownership violation

* Sun Apr 20 2008 Michael Bochkaryov <misha@altlinux.ru> 0.03-alt1
- updated to 0.03 version
- docs added to package

* Thu Mar 22 2007 Sir Raorn <raorn@altlinux.ru> 0.02-alt1
- first build for ALT Linux Sisyphus

