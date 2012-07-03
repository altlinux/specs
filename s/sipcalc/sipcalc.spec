# Unpackaged files in buildroot should terminate build
%define _unpackaged_files_terminate_build 1

Name: sipcalc
Version: 1.1.5
Release: alt1

Summary: Advanced console-based ip subnet calculator
License: %bsd
Group: Networking/Other
Url: http://www.routemeister.net/projects/sipcalc/

Packager: Artem Zolochevskiy <azol@altlinux.ru>

Source: %name-%version.tar
Patch: %name-%version-%release.patch

BuildRequires(pre): rpm-build-licenses

%description
Sipcalc is an advanced console-based IP subnet calculator. It can take
multiple forms of input (IPv4/IPv6/interface/hostname) and output a multitude
of information about a given subnet.

%prep
%setup
%patch -p1

%build
%configure
%make_build --silent

%install
%make_install install DESTDIR=%buildroot

%files
%doc AUTHORS ChangeLog COPYING INSTALL NEWS README TODO
%_bindir/*
%_man1dir/*

%changelog
* Mon Jul 20 2009 Artem Zolochevskiy <azol@altlinux.ru> 1.1.5-alt1
- update to 1.1.5

* Mon Jul 20 2009 Artem Zolochevskiy <azol@altlinux.ru> 1.1.4-alt2
- fix FTBFS with GCC 4.4 (thx raorn@)

* Sun Oct 19 2008 Artem Zolochevskiy <azol@altlinux.ru> 1.1.4-alt1
- initial build for Sisyphus

