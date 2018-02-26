Name: iapetal
Version: 1.1
Release: alt1.qa1.1
Summary: A 2D space rescue game

Group: Games/Arcade
License: GPLv3+
Url: http://doc.jcomserv.net/index.php/Iapetal
Source0: http://downloads.jcomserv.net/%name-%version.tar.gz
Source1: iapetal.desktop

BuildArch: noarch
BuildRequires: desktop-file-utils
Requires: python-module-pygame python-module-pygtkglext icon-theme-hicolor

%description
Fly your lander carefully to rescue the scientists in the habitat module
from the falling asteroids.

%prep
%setup -q

%build
%install
mkdir -p $RPM_BUILD_ROOT%_bindir
mkdir -p $RPM_BUILD_ROOT%_datadir/iapetal

install -m 755 iapetal.py $RPM_BUILD_ROOT%_bindir/iapetal
install -m 755 iapetal-launcher.py $RPM_BUILD_ROOT%_bindir/iapetal-launcher
install -m 644 *.ogg $RPM_BUILD_ROOT%_datadir/iapetal/
install -m 644 *.png $RPM_BUILD_ROOT%_datadir/iapetal/

mkdir -p $RPM_BUILD_ROOT%_datadir/icons/hicolor/32x32/apps
install -p -m 644 habitat.png \
  $RPM_BUILD_ROOT%_datadir/icons/hicolor/32x32/apps

desktop-file-install \
  --dir $RPM_BUILD_ROOT%_datadir/applications %SOURCE1

%files
%doc COPYING TODO
%_bindir/*
%_datadir/iapetal
%_datadir/applications/iapetal.desktop
%_datadir/icons/hicolor/32x32/apps/habitat.png

%changelog
* Tue Oct 25 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.1-alt1.qa1.1
- Rebuild with Python-2.7

* Mon May 23 2011 Repocop Q. A. Robot <repocop@altlinux.org> 1.1-alt1.qa1
- NMU (by repocop). See http://www.altlinux.org/Tools/Repocop
- applied repocop fixes:
  * obsolete-call-in-post-gtk-update-icon-cache for iapetal

* Tue Dec 21 2010 Ilya Mashkin <oddity@altlinux.ru> 1.1-alt1
- Build for ALT Linux

* Wed Jul 14 2010 Jon Ciesla <limb@jcomserv.net> - 1.1-1
- New upstream, fixed rescue collision bugs.

* Wed Jun 09 2010 Jon Ciesla <limb@jcomserv.net> - 1.0-3
- More desktop file corrections.

* Tue May 18 2010 Jon Ciesla <limb@jcomserv.net> - 1.0-2
- Corrected desktop file.

* Thu May 06 2010 Jon Ciesla <limb@jcomserv.net> - 1.0-1
- First build.
