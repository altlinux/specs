Name:           vncshare
Version:        0.02
Release:        alt1
Summary:        VNC shared screens infrastructure
Group:          Networking/Remote access
Source:         %name-%version.tar
BuildArch:      noarch
License:        MIT

Requires:       /usr/bin/vncserver
BuildRequires:  /usr/bin/magick

%package        GIO-install
Summary:        VNC shared screens infrastructure GIO install tool
Group:          Graphical desktop/XFce
%description GIO-install
Desktop icons installer and GIO enabler for vncshare

%description
A set of tools for sharing speaker's PC screen / window among listeners PCs via VNC

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
install -D xfce-desktop-install.sh %buildroot%_libexecdir/xfce-desktop-install.sh

%files
%doc *.md
%_bindir/*
%_desktopdir/*
%_iconsdir/hicolor/*/apps/*

%files GIO-install
%_libexecdir/*

%changelog
* Thu Jul 31 2025 Fr. Br. George <george@altlinux.org> 0.02-alt1
- Provide desktop files
- Provide desktop files installer / enabler via GIO

* Wed Jul 30 2025 Fr. Br. George <george@altlinux.ru> 0.01-alt2
- Bugfix update

* Tue Jul 29 2025 Fr. Br. George <george@altlinux.org> 0.01-alt1
- Initial build for ALT
