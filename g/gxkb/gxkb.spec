#April 01 2022:
#Version gxkb 0.9.4 released.
#* Removed ru and by flags. #StandWithUkraine

%def_enable appindicator

Name: gxkb
Version: 0.9.6
Release: alt1

Summary: X11 keyboard indicator and switcher
License: GPL-2.0
Group: System/X11
Url: http://sourceforge.net/projects/%name/

Vcs: https://github.com/zen-tools/gxkb.git
Source: http://download.sourceforge.net/%name/%name-%version.tar.gz
Source10: by.png
Source11: ru.png

Requires: setxkbmap xkeyboard-config

BuildRequires: libgtk+3-devel libxklavier-devel libwnck3-devel
%{?_enable_appindicator:BuildRequires: libayatana-appindicator3-devel}

%description
GXKB shows a flag of current keyboard in a systray area and allows you to
switch to another one. It's written in C and uses the GTK library.

%prep
%setup
cp %SOURCE10 %SOURCE11 data/flags
sed -i 's@bw\.png[[:space:]]*\\@&\n    by.png           \\@
        s@rs\.png[[:space:]]*\\@&\n    ru.png           \\@' data/flags/Makefile.am

%build
%configure %{subst_enable appindicator}
%make_build

%install
%makeinstall_std

%files
%_bindir/%name
%_desktopdir/%name.desktop
%_datadir/%name/
%_datadir/pixmaps/%name.xpm
%_man1dir/%name.1.*
%doc README* doc/AUTHORS doc/NEWS

%changelog
* Mon Oct 07 2024 Yuri N. Sedunov <aris@altlinux.org> 0.9.6-alt1
- 0.9.6

* Wed Feb 07 2024 Yuri N. Sedunov <aris@altlinux.org> 0.9.5-alt1
- 0.9.5
- enabled appindicator support
- restored ru and by flags

* Mon Oct 25 2021 Yuri N. Sedunov <aris@altlinux.org> 0.9.3-alt1
- 0.9.3

* Wed May 05 2021 Yuri N. Sedunov <aris@altlinux.org> 0.9.2-alt1
- 0.9.2

* Sun Apr 25 2021 Yuri N. Sedunov <aris@altlinux.org> 0.9.1-alt1
- 0.9.1

* Wed Dec 16 2020 Yuri N. Sedunov <aris@altlinux.org> 0.9.0-alt1
- 0.9.0 (ported to GTK3)

* Wed Jul 08 2020 Yuri N. Sedunov <aris@altlinux.org> 0.8.2-alt1
- 0.8.2

* Sat Jan 12 2019 Yuri N. Sedunov <aris@altlinux.org> 0.8.1-alt1
- 0.8.1

* Sun Aug 27 2017 Yuri N. Sedunov <aris@altlinux.org> 0.8.0-alt1
- 0.8.0

* Sat Mar 25 2017 Yuri N. Sedunov <aris@altlinux.org> 0.7.9-alt1
- 0.7.9

* Fri Dec 16 2016 Yuri N. Sedunov <aris@altlinux.org> 0.7.8-alt1
- 0.7.8

* Wed Sep 09 2015 Yuri N. Sedunov <aris@altlinux.org> 0.7.6-alt1
- 0.7.6

* Tue May 05 2015 Yuri N. Sedunov <aris@altlinux.org> 0.7.5-alt1
- 0.7.5

* Tue May 05 2015 Yuri N. Sedunov <aris@altlinux.org> 0.7.4-alt1
- 0.7.4

* Thu Oct 30 2014 Yuri N. Sedunov <aris@altlinux.org> 0.7.3-alt1
- first build for Sisyphus

