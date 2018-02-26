Name: hardinfo
Version: 0.4.2.3
Release: alt3

Summary: Information on your hardware devices

License: GPL
Group: System/Configuration/Hardware
Url: http://hardinfo.berlios.de/wiki/index.php/Main_Page

Packager: Ilya Mashkin <oddity@altlinux.ru>

Source: http://download.berlios.de/hardinfo/%name-%version.tar.bz2
Source1: %name.desktop
Patch: %name.patch
Patch1: %name-lib64.patch

# Automatically added by buildreq on Tue Jan 22 2008
BuildRequires: libgtk+2-devel libsoup-devel pciutils zlib-devel

%description
HardInfo is a system information and benchmark tool for Linux systems.

%prep
%setup -q
%patch
%patch1

%build
%set_automake_version 1.10
#set_autoconf_version 2.5

%__subst "s/gtk+-2.0/gtk+-2.0 gthread-2.0/g" configure
%configure
%make_build

%install
%makeinstall_std
install -D -m644 %SOURCE1 %buildroot%_desktopdir/%name.desktop

%files
%_bindir/*
%_datadir/%name/
%_libdir/%name/
%_desktopdir/*

%changelog
* Thu Sep 03 2009 Ilya Mashkin <oddity@altlinux.ru> 0.4.2.3-alt3
- fix desktop file
- add requires (Closes: #18700)

* Wed Aug 26 2009 Ilya Mashkin <oddity@altlinux.ru> 0.4.2.3-alt2
- Rebuild from orphaned

* Tue Jan 22 2008 Vitaly Lipatov <lav@altlinux.ru> 0.4.2.3-alt1
- new version 0.4.2.3 (with rpmrb script)
- update buildreq (build with libsoup)
- fix x86_64 issues (again bug #13118), thanks to ruslandh@

* Mon Oct 15 2007 Vitaly Lipatov <lav@altlinux.ru> 0.4.2.2-alt3
- fix /usr/lib using on x86_64 (fix bug #13118)

* Thu Oct 11 2007 Vitaly Lipatov <lav@altlinux.ru> 0.4.2.2-alt2
- fix build on x86_64

* Thu Oct 11 2007 Vitaly Lipatov <lav@altlinux.ru> 0.4.2.2-alt1
- new version 0.4.2.2 (with rpmrb script)
- fix MemFault in h_strdup_cprintf (fix bug #13072)

* Sun Jun 18 2006 Vitaly Lipatov <lav@altlinux.ru> 0.4.1-alt0.1
- initial build for ALT Linux Sisyphus
