Name: pekwm
Version: 0.2.1
Release: alt1
Summary: Fast & lightweight window manager
License: GPLv2
Group: Graphical desktop/Other
Url: http://pekwm.org
Source: %name-%version.tar.gz
source1: %name.png

# Automatically added by buildreq on Tue Nov 09 2021
# optimized out: cmake-modules fontconfig fontconfig-devel glibc-kernheaders-generic glibc-kernheaders-x86 libICE-devel libX11-devel libXau-devel libXrender-devel libcrypt-devel libfreetype-devel libgpg-error libsasl2-3 libstdc++-devel libxcb-devel pkg-config python3 python3-base sh4 xorg-proto-devel zlib-devel
BuildRequires: cmake flex gcc-c++ libSM-devel libXext-devel libXft-devel libXinerama-devel libXpm-devel libXrandr-devel libjpeg-devel libpng-devel

%description
pekwm is a window manager that once up on a time was based on the aewm++
window manager, but it has evolved enough that it no longer resembles
aewm++ at all. It has a much expanded feature-set, including window
grouping (similar to ion, pwm, or fluxbox), autoproperties, xinerama,
keygrabber that supports keychains, and much more.

%prep
%setup
cat > %name.wmsession <<@@@
NAME=PekWM
ICON=%_iconsdir/hicolor/64x64/apps/pekwm.png
EXEC=/usr/bin/pekwm
DESC=Fast & lightweight window manager
SCRIPT:
exec /usr/bin/pekwm
@@@
cat > %name.desktop <<@@@
[Desktop Entry]
Name=PekWM
Comment=Fast & lightweight window manager
Comment[ru]=Быстрый и легковесный оконный менеджер
Icon=%name
Exec=%name
Type=Application
@@@

%build
%add_optflags -std=c++14
#autoreconf
#configure
#make_build
%cmake
%cmake_build

%install
#makeinstall_std
%cmake_install
mkdir -p %buildroot/%_sysconfdir/X11/wmsession.d
install -pD -m644 %name.wmsession %buildroot/%_sysconfdir/X11/wmsession.d/08%name
install -pD -m644 %name.desktop %buildroot%_datadir/xsessions/%name.desktop
install -D %SOURCE1 %buildroot%_iconsdir/hicolor/64x64/apps/%name.png

%files
%doc *.md
%_bindir/*
%_sysconfdir/%name
%_sysconfdir/X11/wmsession.d/*
%_datadir/xsessions/%name.desktop
%_datadir/%name
%_man1dir/%{name}*
%_iconsdir/hicolor/64x64/apps/%name.png

%changelog
* Tue Apr 26 2022 Fr. Br. George <george@altlinux.org> 0.2.1-alt1
- Autobuild version bump to 0.2.1

* Tue Nov 09 2021 Fr. Br. George <george@altlinux.ru> 0.2.0-alt1
- Autobuild version bump to 0.2.0

* Tue Nov 02 2021 Igor Vlasenko <viy@altlinux.org> 0.1.17-alt4
- NMU: WM policy 2.0: added %name.desktop in xsessions
- fixed build

* Sun Apr 04 2021 Grigory Ustinov <grenka@altlinux.org> 0.1.17-alt3
- Fix build for gcc10.

* Wed Jan 20 2016 Fr. Br. George <george@altlinux.ru> 0.1.17-alt2
- Fix build

* Sun Sep 15 2013 Fr. Br. George <george@altlinux.ru> 0.1.17-alt1
- Autobuild version bump to 0.1.17
- Add selectwm icon

* Fri Apr 19 2013 Dmitry V. Levin (QA) <qa_ldv@altlinux.org> 0.1.13-alt2.git.c78330ee.1.qa1
- NMU: rebuilt for updated dependencies.

* Fri Sep 28 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.13-alt2.git.c78330ee.1
- Rebuilt with libpng15

* Mon May 30 2011 Egor Glukhov <kaman@altlinux.org> 0.1.13-alt2.git.c78330ee
- XShape support (Closes: #25689)

* Sun Mar 06 2011 Egor Glukhov <kaman@altlinux.org> 0.1.13-alt1.git.c78330ee
- Initial build for Sisyphus
