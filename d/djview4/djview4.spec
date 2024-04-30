Name: djview4
Version: 4.12.0
Release: alt4

Summary: DjVu viewers, encoders and utilities (QT4 based version)
License: GPLv2+
Group: Publishing
Url: http://djvu.sourceforge.net/djview4.html

# http://download.sourceforge.net/djvu/djview-%version.tar.gz
Source: djview-%version.tar

Patch1: djview-4.8-rh-include.patch
Patch2: djview-4.12-alt-disable-fseeko.patch

%def_disable static
%add_optflags -D_FILE_OFFSET_BITS=64

Provides: djvu-viewer = %EVR
Obsoletes: djvu-viewer < %EVR

BuildRequires: libdjvu-devel >= 3.5.25
BuildRequires: browser-plugins-npapi-devel

BuildRequires: ImageMagick-tools gcc-c++ libXt-devel libdjvu-devel libtiff-devel
BuildRequires: qt5-base-devel qt5-tools

%description
This package contains the djview4 viewer and browser plugin.
This new viewer relies on the DjVulibre library and the Qt4 toolkit.

Highlights:
- entirely based on the public djvulibre api.
- entirely written in portable Qt4.
- has been reported to work with Qt/Mac.
- should work with Qt/Windows as well.
- continuous scrolling of pages
- side-by-side display of pages
- ability to specify a url to the djview command
- all plugin and cgi options available from the command line
- all silly annotations implemented
- display thumbnails as a grid
- display outlines
- page names supported (see djvused command set-page-title)
- metadata dialog (see djvused command set-meta)
- implemented as reusable Qt widgets

%prep
%setup -n djview-%version
%patch1 -p1
%patch2 -p1

sed -i '/^#/d' desktopfiles/djvulibre-djview4.desktop
%ifarch %e2k
# Elbrus types are similar to x86_64
sed -i "s/defined(__x86_64__)/(defined(__x86_64__)||defined(__e2k__))/" nsdejavu/npsdk/prcpucfg.h
%endif

%build
export QTDIR=%_qt5_prefix
export QTMAKE=qmake-qt5
export PATH=$QTDIR/bin:$PATH
sh autogen.sh
%configure %{subst_enable static}
%make_build NSDEJAVU_LIBS='-lXt -lX11'

%install
%makeinstall_std

# Удаляем плагин для браузеров - увы, но современные браузеры его не поддерживают.
rm -f %buildroot%_libdir/mozilla/plugins/nsdejavu.so
rm -f %buildroot%_mandir/man1/nsdejavu.*

# Стираем файл .la, который нужен лишь libtool'у для генерации имён библиотек.
rm -f %buildroot%_libdir/mozilla/plugins/nsdejavu.la

install -Dpm644 desktopfiles/prebuilt-hi32-djview4.png \
	%buildroot%_niconsdir/djvulibre-djview4.png
install -Dpm644 desktopfiles/djvulibre-djview4.desktop \
	%buildroot%_desktopdir/djvulibre-djview4.desktop

mv %buildroot%_bindir/djview %buildroot%_bindir/djview4
ln -s %buildroot%_bindir/djview4 djview

%find_lang %name
%set_verify_elf_method strict

%files
%_bindir/djview*
%_mandir/man?/djview*
%_desktopdir/*.desktop
%_datadir/djvu/%name/
%_niconsdir/*
%_iconsdir/hicolor/32x32/mimetypes/*
%_iconsdir/hicolor/64x64/mimetypes/*
%_iconsdir/hicolor/scalable/mimetypes/*

%changelog
* Wed May 01 2024 Evgeny Sinelnikov <sin@altlinux.org> 4.12.0-alt4
- Removed obsolete deps from selinux-policy-alt.

* Tue Sep 19 2023 Artyom Bystrov <arbars@altlinux.org> 4.12.0-alt3.3
- Removed obsolete deps from BR (python3 packages).

* Sat Jul 17 2021 Ilya Kurdyukov <ilyakurdyukov@altlinux.org> 4.12.0-alt3.2
- Fixed build for Elbrus.

* Fri Jul 16 2021 Andrey Cherepanov <cas@altlinux.org> 4.12.0-alt3.1
- FTBFS: build without phonon-devel.
- Build with Qt5.

* Sun Mar 28 2021 Andrey Bergman <vkni@altlinux.org> 4.12.0-alt3
- Add patch disabling fseeko as non-LFS.

* Sun Mar 28 2021 Andrey Bergman <vkni@altlinux.org> 4.12.0-alt2
- Increase alt version.

* Thu Jan 28 2021 Andrey Bergman <vkni@altlinux.org> 4.12.0-alt1
- Updated to 4.12.0.

* Tue Dec 18 2018 Ivan A. Melnikov <iv@altlinux.org> 4.10.6-alt2
- Add -D_FILE_OFFSET_BITS=64 to optflags to fix FTBFS.

* Sun Mar 06 2016 Andrey Bergman <vkni@altlinux.org> 4.10.6-alt1
- Updated to 4.10.6.

* Mon Jan 11 2016 Andrey Bergman <vkni@altlinux.org> 4.10.5-alt1
- Updated to 4.10.5.

* Fri Jul 03 2015 Andrey Bergman <vkni@altlinux.org> 4.10.3-alt1
- Updated to 4.10.3. Removed unnecessary patch, added mime icons.

* Sat Apr 13 2013 Dmitry V. Levin <ldv@altlinux.org> 4.8-alt1
- Updated to 4.8.

* Wed Sep 30 2009 Alexey Gladkov <legion@altlinux.ru> 4.5-alt1.1
- NMU: Rebuilt with browser-plugins-npapi.

* Sun Jun 28 2009 Evgeny Sinelnikov <sin@altlinux.ru> 4.5-alt1
- Update to new release

* Mon Nov 24 2008 Evgeny Sinelnikov <sin@altlinux.ru> 4.4-alt1
- Update to new release

* Sun Jan 27 2008 Evgeny Sinelnikov <sin@altlinux.ru> 4.3-alt1
- Update to new release

* Wed Oct 10 2007 Evgeny Sinelnikov <sin@altlinux.ru> 4.1.2-alt1
- Initial release
