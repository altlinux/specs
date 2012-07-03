Packager: Denis Smirnov <mithraen@altlinux.ru>

Name: mithraen-scanutils
Version: 0.4
Release: alt3
License: GPL
Summary: Simple utility for easy scanning with ADF
Group: System/Kernel and hardware
BuildArch: noarch

Source: %name-%version.tar

Requires: sane xosd-utils ImageMagick ghostscript-utils
Requires: hplip-sane

%description
Simple utility for easy scanning with HP scanners with ADF supported by hpaio
sane backend.

%prep
%setup

%build
%install
%make_install install prefix=%buildroot

%files
%_bindir/*
%_desktopdir/%name.desktop
%_sysconfdir/sane.d/hplip.conf
%doc fvwm.txt

%changelog
* Sun Oct 24 2010 Denis Smirnov <mithraen@altlinux.ru> 0.4-alt3
- auto rebuild

* Tue Oct 19 2010 Denis Smirnov <mithraen@altlinux.ru> 0.4-alt2
- auto rebuild

* Mon Nov 17 2008 Denis Smirnov <mithraen@altlinux.ru> 0.4-alt1
- cleanup spec
- fix desktop file

* Fri Mar 28 2008 Denis Smirnov <mithraen@altlinux.ru> 0.3-alt2
- use update_menus/clean_menus macro in post/postun sections (thanks to viy@)

* Thu Jan 24 2008 Denis Smirnov <mithraen@altlinux.ru> 0.3-alt1
- Add desktop file
- More useful OSD info after scanning
- Add empty config-file for sane (it needs for scanner autodetection)

* Mon Aug 27 2007 Denis Smirnov <mithraen@altlinux.ru> 0.1-alt1
- first build for Sisyphus
