Name: pigz
Version: 2.4
Release: alt1

Summary: Parallel Implementation of GZip
License: zlib
Group: Archiving/Compression
Url: http://zlib.net/pigz/
# http://git.altlinux.org/gears/p/pigz.git
Source: %name-%version-%release.tar

BuildRequires: zlib-devel

%description
pigz, which stands for Parallel Implementation of GZip, is a fully
functional replacement for gzip that exploits multiple processors
and multiple cores to the hilt when compressing data.

%prep
%setup -n %name-%version-%release

%build
%define _optlevel 3
%make_build CFLAGS='%optflags'

%install
install -pDm755 {,%buildroot%_bindir/}%name
install -pDm644 {,%buildroot%_man1dir/}%name.1
ln -sf {,%buildroot%_bindir/un}%name
ln -sf {,%buildroot%_man1dir/un}%name.1

%check
make test

%files
%doc README
%_bindir/*
%_man1dir/*

%changelog
* Fri Jan 05 2018 Michael Shigorin <mike@altlinux.org> 2.4-alt1
- 2.4

* Mon Oct 03 2016 Michael Shigorin <mike@altlinux.org> 2.3.4-alt1
- 2.3.4

* Wed Feb 04 2015 Michael Shigorin <mike@altlinux.org> 2.3.3-alt1
- 2.3.3

* Mon Jun 23 2014 Michael Shigorin <mike@altlinux.org> 2.3.1-alt1
- 2.3.1

* Thu Jun 13 2013 Dmitry V. Levin <ldv@altlinux.org> 2.3-alt1
- Updated to 2.3.
- Enabled test suite.

* Sun Apr 22 2012 Michael Shigorin <mike@altlinux.org> 2.2.4-alt1
- 2.2.4

* Sun Jul 11 2010 Michael Shigorin <mike@altlinux.org> 2.1.6-alt1
- TMC package update built for Sisyphus

* Sun Jan 24 2010 Led <led@altlinux.ru> 2.1.6-tmc1
- 2.1.6

* Sun Jul 26 2009 Led <led@altlinux.ru> 2.1.5-alt1
- 2.1.5

* Wed Nov 12 2008 Led <led@altlinux.ru> 2.1.4-alt1
- initial build
