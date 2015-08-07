Name: speedcrunch
Version: 0.11
Release: alt1.1
Summary: A fast power user calculator
Group: Office
License: GPLv2
Url: http://www.speedcrunch.org/
Source0: %name-%version.tar.gz
Source1: %name.desktop

BuildRequires: ImageMagick-tools cmake doxygen fonts-ttf-dejavu fonts-type1-urw gcc-c++ libqt4-devel

%description
SpeedCrunch is a fast, high precision and powerful desktop calculator.
Among its distinctive features are a scrollable display, up to 50 decimal
precisions, unlimited variable storage, intelligent automatic completion
full keyboard-friendly and more than 15 built-in math function.

%prep
%setup -q

%build
export PATH=$PATH:%_qt4dir/bin
lrelease src/resources/locale/*.ts
cd src && \
cmake \
        -DCMAKE_INSTALL_PREFIX=%_prefix \
        -DCMAKE_SKIP_RPATH=YES \
        -DCMAKE_CXX_FLAGS:STRING="%optflags" \
        -DCMAKE_C_FLAGS:STRING="%optflags"
%make_build

%install
cd src
%make DESTDIR=%buildroot install
%__install -Dp -m 0644 %SOURCE1 %buildroot%_desktopdir/%name.desktop

# icons
%__mkdir -p %buildroot/{%_miconsdir,%_niconsdir,%_liconsdir}
cd ..
convert -resize 48x48 gfx/%name.svg %buildroot%_liconsdir/%name.png
convert -resize 32x32 gfx/%name.svg %buildroot%_niconsdir/%name.png
convert -resize 16x16 gfx/%name.svg %buildroot%_miconsdir/%name.png

# docs
cd doc && doxygen Doxyfile

%files
%doc doc/*.pdf doc/*.odt doc/*.docbook doc/html
%_bindir/%name
%_desktopdir/%name.desktop
%_miconsdir/%name.png
%_niconsdir/%name.png
%_liconsdir/%name.png

%changelog
* Fri Aug 07 2015 Motsyo Gennadi <drool@altlinux.ru> 0.11-alt1.1
- fix BuildRequires

* Fri Aug 07 2015 Motsyo Gennadi <drool@altlinux.ru> 0.11-alt1
- new version 0.11 (#31189)

* Tue Jul 26 2011 Motsyo Gennadi <drool@altlinux.ru> 0.10.1-alt3
- build without ugly script (#25953)

* Thu Nov 20 2008 Motsyo Gennadi <drool@altlinux.ru> 0.10.1-alt2
- delete post/postun scripts (new rpm)

* Thu Jun 05 2008 Motsyo Gennadi <drool@altlinux.ru> 0.10.1-alt1
- new version

* Wed Apr 02 2008 Motsyo Gennadi <drool@altlinux.ru> 0.10-alt1
- new version
- add CMAKE_C_FLAGS

* Tue Nov 27 2007 Motsyo Gennadi <drool@altlinux.ru> 0.9-alt1
- new version
- build with cmake

* Thu Aug 30 2007 Motsyo Gennadi <drool@altlinux.ru> 0.8-alt1
- new versuin
- add desktop file

* Sat Apr 14 2007 Denis Smirnov <mithraen@altlinux.ru> 0.7-alt1.beta2
- first build for Sisyphus

* Mon Mar 19 2007 Motsyo Gennadi <drool@altlinux.ru> 0.7-alt0.beta2.M24.2
- fix URL of a home site

* Tue Mar 13 2007 Motsyo Gennadi <drool@altlinux.ru> 0.7-alt0.beta2.M24.1
- initial build for ALT Linux (2.4 Master)

* Thu Feb 22 2007 Roland Wolters <wolters.liste@gmx.net> 0.7-0.9.beta2
- bumped version due to cvs problems

* Thu Feb 22 2007 Roland Wolters <wolters.liste@gmx.net> 0.7-0.4.beta2
- changed the version numbering

* Thu Feb 22 2007 Roland Wolters <wolters.liste@gmx.net> 0.7-beta2.3
- Added main category to desktop file

* Thu Feb 15 2007 Roland Wolters <wolters.liste@gmx.net> 0.7-beta2.2
- corrected spaces/tabs mixing in spec file
- corrected end-line-encoding

* Tue Feb 13 2007 Roland Wolters <wolters.liste@gmx.net> 0.7-beta2.1
- initial build

