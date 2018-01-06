%set_gcc_version 5

Name: nspec
Version: 15.5547
Release: alt2
Summary: Nspec Universal SPM & Spectroscopy Software - Nano Scan Technologies Ltd.
Summary(ru_RU.UTF-8): Nspec - универсальная программа для СЗМ и спектроскопии для приборов фирмы НСТ
License: BSD 4-clause: Nano Scan Technologies Ltd., 2008-2016
Group: Sciences/Other
URL: http://www.nanoscantech.ru/en/
Packager: Alexei Mezin <alexvm@altlinux.org>
Vendor: ALT Linux Team

Source: %name-%version.tar.gz

BuildPreReq: gcc5 gcc5-c++ 
BuildRequires(pre): rpm-macros-qt4


# Automatically added by buildreq on Fri Dec 15 2017
# optimized out: fontconfig fontconfig-devel gcc-c++ glib2-devel glibc-kernheaders-generic glibc-kernheaders-x86 libGL-devel libGLU-devel libICE-devel libSM-devel libX11-devel libXmu-devel libXt-devel libatk-devel libcairo-devel libfreetype-devel libgdk-pixbuf libgdk-pixbuf-devel libgio-devel libgtk+2-devel libgtkglext-devel libpango-devel libpangox-compat libpangox-compat-devel libqt5-concurrent libqt5-core libqt5-gui libqt5-network libqt5-opengl libqt5-script libqt5-widgets libstdc++-devel libusb-compat pkg-config python-base python-modules python3 python3-base python3-module-yieldfrom qt5-base-devel zlib-devel
## QT5 deps
##BuildRequires: bzlib-devel i586-libxcb kf5-kimageformats libgwyddion-devel libqt5-svg libusb-compat-devel libusb-devel qt5-declarative-devel qt5-imageformats qt5-script-devel ruby ruby-stdlibs selinux-policy

## QT4 deps
BuildRequires: gcc-c++ glibc-devel-static libgwyddion-devel libqt4-webkit-devel libusb-compat-devel libusb-devel phonon-devel ruby ruby-stdlibs selinux-policy


%description
Nspec is a control program for Scanning Probe Microscopes and Spectroscopy Systems
by Nano Scan Technologies Ltd.

%description -l ru_RU.UTF-8
Nspec это программа управления Сканирующими Зондовыми Микроскопами и Спектроскопическими системами
фирмы Нано Скан Технология.

%package  gwyddion-plugin
Summary: Plugin for easy data transfer from NSpec to Gwyddion
Requires: gwyddion
Group: Sciences/Other

%description gwyddion-plugin
This plugin enables transfer of the current data frame from Nspec to Gwyddion in one click.

%description -l ru_RU.UTF-8  gwyddion-plugin
Этот плагин позволяет передавать данные из Nspec в Gwyddion в одно нажатие кнопки.


%package plugin-lithography
Summary: Probe lithography support
Requires: nspec
Group: Sciences/Other

%description plugin-lithography
This plugin adds probe lithography support to Nspec software.

%description -l ru_RU,UTF-8 plugin-lithography
Пдлагин добавляет поддержку зондовой литографии в программу Nspec.


%prep
%setup

%build
echo -e "%version-%release\n" >> src/data/nst_build.txt
%qmake_qt4 "CONFIG += no_external_deps" nst.pro
%make

cd gwy_proxy/gcc_make
make -f Makefile.linux

%install
install -D -m0644 lib/linux/nst-udev.rules %buildroot/%_sysconfdir/udev/rules.d/99-nst.rules
install -D -m0644 lib/linux/99-shuttle_ignore_xorg.conf %buildroot/%_sysconfdir/X11/xorg.conf.d/99-shuttle_ignore_xorg.conf
install -m 755 -d %buildroot/%_bindir/
install -m 755 -d %buildroot/%_libdir/nspec
install -m 755 -d %buildroot/%_pixmapsdir/
install -m 755 -d %buildroot/%_desktopdir/
install -m 755 -d %buildroot/%_datadir/mime/packages/
install -m 644 lib/linux/ALT_RPM/%name.svg %buildroot/%_pixmapsdir/
install -m 644 lib/linux/%name.desktop %buildroot/%_desktopdir/
install -m 644 lib/linux/ALT_RPM/%name.xml %buildroot/%_datadir/mime/packages/

## install main binary
cp bin/nspec %buildroot/%_bindir

## install litho plugin
cp bin/liblitho* %buildroot/%_libdir/nspec

# gwy proxy install
install -m 755 -d %buildroot/%_libdir/gwyddion/modules/
cp gwy_proxy/gcc_make/nst_proxy.so %buildroot/%_libdir/gwyddion/modules



%files
%_bindir/%name
%_desktopdir/%name.desktop
%_sysconfdir/udev/rules.d/99-nst.rules
%_sysconfdir/X11/xorg.conf.d/99-shuttle_ignore_xorg.conf
%_pixmapsdir/%name.svg
%_datadir/mime/packages/%name.xml
##%attr(777, root, root) %dir /opt/nspec
##/opt/nspec/nspec

%files gwyddion-plugin
%_libdir/gwyddion/modules/*.so

%files plugin-lithography
%_libdir/nspec/*

%changelog
* Sat Jan 06 2018 Alexei Mezin <alexvm@altlinux.org> 15.5547-alt2
- spec file fixes

* Sat Jan 06 2018 Alexei Mezin <alexvm@altlinux.org> 15.5547-alt1
- Update to new version
- Lithography plugin build

* Fri Dec 15 2017 Alexei Mezin <alexvm@altlinux.org> 15.5540-alt1
- Back to qt4
- Code fixes

* Fri Dec 15 2017 Alexei Mezin <alexvm@altlinux.org> 15.5537-alt1
- Some minor bugs fixed.
- Switch to qt5

* Thu Dec 14 2017 Alexei Mezin <alexvm@altlinux.org> 15.5536-alt1
- Update to new non-LTS version

* Sat Mar 04 2017 Alexei Mezin <alexvm@altlinux.org> 14.5437-alt1
- Update to new version

* Thu Jan 05 2017 Alexei Mezin <alexvm@altlinux.org> 14.5436-alt2
- Minor build fixes and spec cleanup

* Wed Jan 04 2017 Alexei Mezin <alexvm@altlinux.org> 14.5436-alt1
- Update to new version

* Sat Nov 05 2016 Alexei Mezin <alexvm@altlinux.org> 14.5420-alt1
- Update to new version

* Wed Jun 01 2016 Alexei Mezin <alexvm@altlinux.org> 14.5033-alt1
- Project version fixes
- Minor spec and scripts update

* Tue May 31 2016 Alexei Mezin <alexvm@altlinux.org> 14.5028-alt1
- Update to new version
- Add Xorg rules for ShuttlePro

* Fri Apr 15 2016 Alexei Mezin <alexei@nanoscantech.ru> 14.4896-alt1
- New major number, new numeration rules
- add release info into About dialog

* Tue Mar 22 2016 Alexei Mezin <alexeivm@altlinux.org> 10.6.4823-alt2
- Fix external dependencies

* Tue Mar 22 2016 Alexei Mezin <alexeivm@altlinux.org> 10.6.4823-alt1
- New version

* Sat Mar 05 2016 Alexei Mezin <alexeivm@altlinux.org> 10.6.4804-alt1
- New version
- OpenGL bugs fixed
- gwy_proxy Makefile fix

* Sun Feb 07 2016 Alexei Mezin <alexeivm@altlinux.org> 10.6.4788-alt0.1
- Rebuild for ALT

* Thu Feb 04 2016 Alexei Mezin <alexei@nanoscantech.ru> 10.6.4788-alt1
- Program update
- Binary file moved to /usr/bin
- Program configuration files now in $HOME

* Wed Dec 23 2015 Alexei Mezin <alexei@nanoscantech.com> 10.6.4761-alt1
- New build with RPM fixes 
- MIME types support

* Sun Dec 20 2015 Alexei Mezin <alexei@nanoscantech.com> 10.6-alt0
- Initial build for ALT Linux

