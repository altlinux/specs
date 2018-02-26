Name: pigz
Version: 2.2.4
Release: alt1

Summary: Parallel Implementation of GZip
License: %bsdstyle
Group: Archiving/Compression

Url: http://zlib.net/%name
Source: %url/%name-%version.tar.gz
Packager: Led <led@altlinux.ru>

BuildRequires(pre): rpm-build-licenses
BuildRequires: zlib-devel

%description
%name, which stands for Parallel Implementation of GZip, is a fully
functional replacement for gzip that exploits multiple processors and
multiple cores to the hilt when compressing data.

%prep
%setup

%build
%define _optlevel 3
%make_build CFLAGS="%optflags"

%install
install -pDm755 {,%buildroot%_bindir/}%name
install -pDm644 {,%buildroot%_man1dir/}%name.1
ln -sf {,%buildroot%_bindir/un}%name
ln -sf {,%buildroot%_man1dir/un}%name.1

%files
%doc README
%_bindir/*
%_man1dir/*

%changelog
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
