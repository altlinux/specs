%define dist Expect
Name: perl-%dist
Version: 1.21
Release: alt1

Summary: Perl Expect interface
License: GPL
Group: Development/Perl

URL: %CPAN %dist
Source: %dist-%version.tar.gz

BuildArch: noarch

BuildRequires: /dev/pts

# Automatically added by buildreq on Tue Apr 27 2010
BuildRequires: perl-IO-Tty perl-devel

%description
Expect.pm is built to either spawn a process or take an existing filehandle
and interact with it such that normally interactive tasks can be done
without operator assistance. This concept makes more sense if you are
already familiar with the versatile Tcl version of Expect.

%prep
%setup -q -n %dist-%version

%build
%perl_vendor_build

%install
%perl_vendor_install
mkdir -p %buildroot{%_bindir,%_man1dir}
cp -p examples/kibitz/kibitz %buildroot%_bindir/kibitz.pl
cp -p examples/kibitz/kibitz.man %buildroot%_man1dir/kibitz.pl.1

%files
%doc Changes README test.pl
%perl_vendor_privlib/Expect*
%_bindir/kibitz.pl
%_man1dir/kibitz.pl.1*

%changelog
* Tue Apr 27 2010 Alexey Tourbin <at@altlinux.ru> 1.21-alt1
- 1.15 -> 1.21

* Sat Feb 19 2005 ALT QA Team Robot <qa-robot@altlinux.org> 1.15-alt3.1
- Rebuilt with rpm-build-perl-0.5.1.

* Tue Sep 30 2003 Grigory Milev <week@altlinux.ru> 1.15-alt3
- don't make test after build, because we don't have acces to pty on build server

* Wed Nov 06 2002 Stanislav Ievlev <inger@altlinux.ru> 1.15-alt2
- rebuild with new perl

* Wed Apr 10 2002 Grigory Milev <week@altlinux.ru> 1.15-alt1
- new version released

* Tue Sep 25 2001 Grigory Milev <week@altlinux.ru> 1.12-alt1
- New version released.

* Tue Aug 21 2001 Grigory Milev <week@altlinux.ru> 1.11-alt1
- First build for Sisyphus

