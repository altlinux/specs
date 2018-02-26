Name: speedcrunch
Version: 0.10.1
Release: alt3
Summary: A fast power user calculator for KDE
Group: Office
License: GPLv2
Url: http://www.speedcrunch.org/
Source0: http://speedcrunch.googlecode.com/files/%name-%version.tar.gz
Source1: %name.desktop

BuildRequires: cmake >= 2.4.4 gcc-c++ /usr/bin/convert libqt4-devel libSM-devel libXcursor-devel libXi-devel libXinerama-devel libXrandr-devel

%description
SpeedCrunch is a fast, high precision and powerful desktop calculator.
Among its distinctive features are a scrollable display, up to 50 decimal
precisions, unlimited variable storage, intelligent automatic completion
full keyboard-friendly and more than 15 built-in math function.

%prep
%setup -q

%build
export PATH=$PATH:%_qt4dir/bin
cd src && \
cmake \
        -DCMAKE_INSTALL_PREFIX=%_prefix \
        -DCMAKE_SKIP_RPATH=YES \
        -DCMAKE_CXX_FLAGS:STRING="%optflags" \
        -DCMAKE_C_FLAGS:STRING="%optflags"
%make_build
lrelease i18n/*.ts \

%install
cd src
%make DESTDIR=%buildroot install
%__install -Dp -m 0644 %SOURCE1 %buildroot%_desktopdir/%name.desktop

# icons
%__mkdir -p %buildroot/{%_miconsdir,%_niconsdir,%_liconsdir}
cd ..
convert -resize 48x48 src/resources/%name.png %buildroot%_liconsdir/%name.png
convert -resize 32x32 src/resources/%name.png %buildroot%_niconsdir/%name.png
convert -resize 16x16 src/resources/%name.png %buildroot%_miconsdir/%name.png

%files
%doc ChangeLog* INSTALL.txt PACKAGERS HACKING.txt LISEZMOI README TRANSLATORS doc/*.pdf doc/*.odt
%_bindir/%name
%_desktopdir/%name.desktop
%_datadir/%name
%exclude %_datadir/%name/books/images/make_math_pngs.sh
%_miconsdir/%name.png
%_niconsdir/%name.png
%_liconsdir/%name.png

%changelog
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

