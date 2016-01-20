Name: pekwm
Version: 0.1.17
Release: alt2
Summary: Fast & lightweight window manager
License: GPLv2
Group: Graphical desktop/Other
Url: http://pekwm.org
Source: %name-%version.tar.bz2
source1: %name.png

# Automatically added by buildreq on Sun Sep 15 2013
# optimized out: fontconfig fontconfig-devel libICE-devel libX11-devel libXrender-devel libfreetype-devel libstdc++-devel pkg-config xorg-kbproto-devel xorg-randrproto-devel xorg-renderproto-devel xorg-xextproto-devel xorg-xproto-devel
BuildRequires: gcc-c++ imake libSM-devel libXext-devel libXft-devel libXinerama-devel libXpm-devel libXrandr-devel libjpeg-devel libpng-devel xorg-cf-files

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

%build
%autoreconf
%configure
%make_build

%install
%makeinstall_std
mkdir -p %buildroot/%_sysconfdir/X11/wmsession.d
install -pD -m644 %name.wmsession %buildroot/%_sysconfdir/X11/wmsession.d/08%name
install -D %SOURCE1 %buildroot%_iconsdir/hicolor/64x64/apps/%name.png

%files
%doc README
%_bindir/*
%_sysconfdir/%name
%_sysconfdir/X11/wmsession.d/*
%_datadir/%name
%_man1dir/%name.*
%_iconsdir/hicolor/64x64/apps/%name.png

%changelog
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
