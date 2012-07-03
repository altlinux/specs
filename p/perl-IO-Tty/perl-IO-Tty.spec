%define dist IO-Tty
Name: perl-%dist
Version: 1.10
Release: alt2

Summary: interface to pseudo tty's
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source: %dist-%version.tar.gz

# always loaded when available
Requires: perl-IO-Stty

# Automatically added by buildreq on Sun Nov 20 2011
BuildRequires: perl-IO-Stty perl-devel

%description
IO::Tty and IO::Pty provide an interface to pseudo tty's

%prep
%setup -q -n %dist-%version

%build
%if "%([ -c /dev/tty ] || echo no)" == "no"
%def_without test
%endif

%perl_vendor_build

%install
%perl_vendor_install

%files
%doc ChangeLog README
%perl_vendor_archlib/IO
%perl_vendor_autolib/IO

%changelog
* Sun Nov 20 2011 Alexey Tourbin <at@altlinux.ru> 1.10-alt2
- added dependency on perl-IO-Stty

* Fri Oct 07 2011 Alexey Tourbin <at@altlinux.ru> 1.10-alt1
- 1.08 -> 1.10
- built for perl-5.14
- rebuilt as plain src.rpm

* Sat Nov 06 2010 Vladimir Lettiev <crux@altlinux.ru> 1.08-alt1.1
- rebuilt with perl 5.12

* Mon Feb 15 2010 Alexey Tourbin <at@altlinux.ru> 1.08-alt1
- 1.07 -> 1.08

* Sat Dec 20 2008 Alexey Tourbin <at@altlinux.ru> 1.07-alt1
- 1.02 -> 1.07

* Mon Apr 16 2007 ALT QA Team Robot <qa-robot@altlinux.org> 1.02-alt3.1.0
- Automated rebuild.

* Sat Feb 19 2005 ALT QA Team Robot <qa-robot@altlinux.org> 1.02-alt3.1
- Rebuilt with rpm-build-perl-0.5.1.

* Tue Sep 30 2003 Grigory Milev <week@altlinux.ru> 1.02-alt3
- don't make test after build, because we don't have acces to tty on build server

* Tue Nov 05 2002 Stanislav Ievlev <inger@altlinux.ru> 1.02-alt2
- rebuild with new perl

* Wed Apr 10 2002 Grigory Milev <week@altlinux.ru> 1.02-alt1
- new version-released

* Mon Oct  8 2001 Grigory Milev <week@altlinux.ru> 0.05-alt1
- new version released

* Tue Aug 21 2001 Grigory Milev <week@altlinux.ru> 0.04-alt1
- First build for Sisyphus
