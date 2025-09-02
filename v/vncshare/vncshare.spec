Name:           vncshare
Version:        0.08
Release:        alt1
Summary:        VNC shared screens infrastructure
Group:          Networking/Remote access
Source:         %name-%version.tar
BuildArch:      noarch
License:        MIT

Requires:       /usr/bin/vncserver
BuildRequires:  /usr/bin/magick rpm-build-python3

%description
A set of tools for sharing speaker's PC screen / window among listeners PCs via VNC

%package        installers
Summary:        VNC shared screens infrastructure install tools
Group:          Graphical desktop/XFce
%description installers
Desktop and panel icons installer and GIO enabler for vncshare

%prep
%setup

%define sizes 16 32 48 64 96 128
%build
for F in VNC*.svg; do for S in %sizes; do
  mkdir -p ${S}x${S}/apps
  magick $F ${S}x${S}/apps/${F##.svg}.png
done; done

%install
for F in VNC*[A-Z]; do install -D $F %buildroot%_bindir/$F; done
for F in VNC*.desktop; do install -D $F %buildroot%_desktopdir/$F; done
for F in VNC*.svg; do install -D $F %buildroot%_iconsdir/hicolor/scalable/apps/$F; done
for F in */*/*.png; do
  install -D $F %buildroot%_iconsdir/hicolor/$F
done
for prog in *.py *.sh; do
 install -D $prog %buildroot%_libexecdir/%name-$prog
done

%files
%doc *.md
%_bindir/*
%_desktopdir/*
%_iconsdir/hicolor/*/apps/*

%files installers
%_libexecdir/*

%changelog
* Tue Sep 02 2025 Fr. Br. George <george@altlinux.org> 0.08-alt1
- Fix VNCSERVER standalone run

* Mon Sep 01 2025 Fr. Br. George <george@altlinux.ru> 0.07-alt1
- Fix VNCSERVER misdesigns

* Tue Aug 12 2025 Fr. Br. George <george@altlinux.org> 0.06-alt1
- Improve VNCSHARE with yad

* Wed Aug 06 2025 Fr. Br. George <george@altlinux.org> 0.05-alt1
- Provide VNCSERVER tray icon

* Wed Aug 06 2025 Fr. Br. George <george@altlinux.org> 0.04-alt1
- Provide XFCE panel deafult file patcher

* Sun Aug 03 2025 Fr. Br. George <george@altlinux.org> 0.03-alt1
- Provide XFCE panel files installer

* Thu Jul 31 2025 Fr. Br. George <george@altlinux.org> 0.02-alt1
- Provide desktop files
- Provide desktop files installer / enabler via GIO

* Wed Jul 30 2025 Fr. Br. George <george@altlinux.ru> 0.01-alt2
- Bugfix update

* Tue Jul 29 2025 Fr. Br. George <george@altlinux.org> 0.01-alt1
- Initial build for ALT
