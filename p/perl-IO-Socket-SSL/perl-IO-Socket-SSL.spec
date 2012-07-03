%define dist IO-Socket-SSL
Name: perl-%dist
Version: 1.49
Release: alt1

Summary: SSL socket interface class
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source: %dist-%version.tar.gz
Patch: IO-Socket-SSL-1.49-alt-deps.patch

BuildArch: noarch

# Automatically added by buildreq on Mon Nov 14 2011
BuildRequires: perl-Encode perl-IO-Socket-INET6 perl-Net-IDN-Encode perl-Net-SSLeay perl-devel

%description
IO::Socket::SSL is a class implementing an object oriented
interface to SSL sockets. The class is a descendent of
IO::Socket::INET and provides a subset of the base class's
interface methods.

%prep
%setup -q -n %dist-%version
%patch -p1

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc BUGS Changes README
%perl_vendor_privlib/IO

%changelog
* Mon Nov 14 2011 Alexey Tourbin <at@altlinux.ru> 1.49-alt1
- 1.44 -> 1.49
- enabled dependency on Net::IDN::Encode

* Mon Sep 19 2011 Igor Vlasenko <viy@altlinux.ru> 1.44-alt1
- automated CPAN update

* Mon Mar 21 2011 Alexey Tourbin <at@altlinux.ru> 1.39-alt1
- 1.37 -> 1.39

* Fri Dec 24 2010 Alexey Tourbin <at@altlinux.ru> 1.37-alt1
- 1.33 -> 1.37

* Thu Apr 08 2010 Alexey Tourbin <at@altlinux.ru> 1.33-alt1
- 1.31 -> 1.33

* Tue Feb 16 2010 Alexey Tourbin <at@altlinux.ru> 1.31-alt1
- 1.26 -> 1.31

* Fri Jul 17 2009 Alexey Tourbin <at@altlinux.ru> 1.26-alt1
- 1.24 -> 1.26

* Wed Apr 22 2009 Alexey Tourbin <at@altlinux.ru> 1.24-alt1
- 1.16 -> 1.24
- enabled IPv6 support by default

* Wed Sep 24 2008 Alexey Tourbin <at@altlinux.ru> 1.16-alt1
- 1.15 -> 1.16

* Thu Sep 11 2008 Alexey Tourbin <at@altlinux.ru> 1.15-alt1
- 1.14 -> 1.15

* Tue Aug 05 2008 Alexey Tourbin <at@altlinux.ru> 1.14-alt1
- 1.13_5 -> 1.14

* Thu Apr 24 2008 Alexey Tourbin <at@altlinux.ru> 1.13_5-alt1
- 1.13_4 -> 1.13_5

* Sun Mar 09 2008 Alexey Tourbin <at@altlinux.ru> 1.13_4-alt1
- 0.95 -> 1.13_4
- SSL.pm (import): fixed inet4/inet6 setup (rt.cpan.org #33921)

* Sat Feb 19 2005 ALT QA Team Robot <qa-robot@altlinux.org> 0.95-alt1.1
- Rebuilt with rpm-build-perl-0.5.1.

* Mon Oct 20 2003 Grigory Milev <week@altlinux.ru> 0.95-alt1
- new version released

* Thu Jun 26 2003 Grigory Milev <week@altlinux.ru> 0.93-alt1
- new version released
- spec fixed due new macros

* Tue May 28 2002 Grigory Milev <week@altlinux.ru> 0.81-alt1
- new version released

* Mon Sep 03 2001 Grigory Milev <week@altlinux.ru> 0.80-alt1
- New version released.

* Tue Jul 31 2001 Grigory Milev <week@altlinux.ru> 0.79-alt1
- First build for Sisyphus

