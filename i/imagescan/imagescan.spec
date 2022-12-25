%define utsushi_version 0.65.0

Name:     imagescan
Version:  3.65.0
Release:  alt3

Summary:  EPSON Image Scan v3 front-end for scanners and all-in-ones
License:  GPL-3.0+
Group:    Other
Url:      http://download.ebz.epson.net/dsc/search/01/search/?OSC=LX

Packager: Andrey Cherepanov <cas@altlinux.org>

# Download manually from http://support.epson.net/linux/src/scanner/imagescanv3/common/
Source:   %{name}_%version.orig.tar.gz
Source1:  utsushi.desktop
Source2:  %name.watch

Patch1:   %name-alt-fix-name-in-version-file.patch
Patch2:   imagescan-alt-config-cleanup.patch
Patch3:   %name-alt-boost-1.73.0-compat.patch
Patch4:   %name-alt-check-sane-compatibility.patch

BuildRequires: gcc-c++
BuildRequires: ImageMagick-tools
BuildRequires: boost-filesystem-devel
BuildRequires: boost-program_options-devel
BuildRequires: boost-signals-devel
BuildRequires: bzlib-devel
BuildRequires: libgtkmm2-devel
BuildRequires: libjpeg-devel
BuildRequires: libsane-devel
BuildRequires: libtiff-devel
BuildRequires: libudev-devel
BuildRequires: libusb-devel
BuildRequires: libImageMagick-devel
BuildRequires: autoconf-archive
BuildRequires: xsltproc
BuildRequires: libltdl7-devel

Requires: %name-sane

%description
Image Scan v3 is Linux software for Epson scanners.

Image Scan v3 has own front-end, it allows to set various scanner
settings with graphical user interface and save the scanned images to
the various file type.

It supports USB and network connection for the network capable scanners.

Scanner can be controlled via not only own front-end but also command
line option.

%package sane
Summary: EPSON Image Scan v3 SANE driver for scanners and all-in-ones
Group: System/Configuration/Hardware

%description sane
SANE driver Image Scan v3 for Epson scanners.

It supports USB and network connection for the network capable scanners.

Scanner can be controlled via not only own front-end but also command
line option.

%prep
%setup -n utsushi-%utsushi_version
%patch1 -p2
%patch2 -p2
%patch3 -p2
%patch4 -p2
%ifarch %e2k
sed -ie "s|v = \\(utsushi::value (.*)\\);|v = sane::value (\\1);|" sane/handle.cpp
%endif

%build
%undefine _configure_gettext
%autoreconf
%configure \
    --libdir=%_libdir \
    --enable-shared \
    --disable-test-reports \
    --without-boost-unit-test-framework \
    --enable-sane-config \
    --enable-udev-config \
    --with-boost-libdir=%_libdir \
    --without-included-ltdl \
    --with-gtkmm \
    --with-jpeg \
    --with-magick \
    --with-magick-pp \
    --with-sane \
    --with-tiff
 
%make_build CXXFLAGS="-Wno-error=parentheses -Wno-error=deprecated-declarations -I../.." LDFLAGS="-lpthread"

%install
%makeinstall_std
rm -rf %buildroot%_includedir
find %buildroot%_libdir -name *.la -delete
find %buildroot%_libdir -name *.a -delete
install -Dm0644 lib/devices.conf %buildroot%_sysconfdir/utsushi/utsushi.conf
install -Dm0644 %SOURCE1 %buildroot%_desktopdir/utsushi.desktop

rm %buildroot%_bindir/utsushi
ln -s ../lib/utsushi/utsushi-main %buildroot%_bindir/utsushi
echo -e '#!/bin/sh\n%_bindir/utsushi $@' > %buildroot%_bindir/imagescan
chmod +x %buildroot%_bindir/imagescan

%find_lang utsushi

%files -f utsushi.lang
%doc AUTHORS NEWS README
%_libexecdir/utsushi/utsushi-scan-gtkmm
%config(noreplace) %_sysconfdir/utsushi/utsushi.conf
%config(noreplace) %_sysconfdir/utsushi/combo.conf
%dir %_libdir/utsushi
%_libdir/utsushi/lib*.so*
%exclude %_libdir/utsushi/libutsushi.so*
%exclude %_libdir/utsushi/libflt-all.so*
%exclude %_libdir/utsushi/libcnx-usb.so*
%exclude %_libdir/utsushi/libcnx-hexdump.so*
%_datadir/utsushi
%exclude %_datadir/utsushi/drivers
%_desktopdir/utsushi.desktop

%files sane
%_libexecdir/utsushi
%exclude %_libexecdir/utsushi/utsushi-scan-gtkmm
%_bindir/*
%_sysconfdir/sane.d/dll.d/utsushi
%_sysconfdir/udev/rules.d/utsushi-esci.rules
%_libdir/utsushi/sane
%_libdir/utsushi/libutsushi.so*
%_libdir/utsushi/libflt-all.so*
%_libdir/utsushi/libcnx-usb.so*
%_libdir/utsushi/libcnx-hexdump.so*
%_libdir/sane/libsane-utsushi.so*
%_datadir/utsushi/drivers

%changelog
* Sun Dec 25 2022 Andrey Cherepanov <cas@altlinux.org> 3.65.0-alt3
- FTBFS: fixed build with new version of sane package.

* Sat Jan 16 2021 Ilya Kurdyukov <ilyakurdyukov@altlinux.org> 3.65.0-alt2
- Added fix for Elbrus build.

* Sat Jan 16 2021 Andrey Cherepanov <cas@altlinux.org> 3.65.0-alt1
- New version.

* Fri Jul 31 2020 Andrey Cherepanov <cas@altlinux.org> 3.63.0-alt1
- New version.
- Add Exec value to desktop file.

* Wed Jun 10 2020 Aleksei Nikiforov <darktemplar@altlinux.org> 3.62.0-alt2
- Rebuilt with boost-1.73.0.

* Fri Feb 07 2020 Andrey Cherepanov <cas@altlinux.org> 3.62.0-alt1
- New version.

* Tue Nov 05 2019 Andrey Cherepanov <cas@altlinux.org> 3.61.0-alt1
- New version.

* Thu Sep 05 2019 Andrey Cherepanov <cas@altlinux.org> 3.59.2-alt2
- Comment example entries in config file.

* Fri Aug 23 2019 Andrey Cherepanov <cas@altlinux.org> 3.59.2-alt1
- New version.

* Fri Jul 12 2019 Andrey Cherepanov <cas@altlinux.org> 3.57.0-alt1
- New version.
- Use wrapper script instead of symlink because boost throw exception (ALT #36859).

* Fri Apr 12 2019 Andrey Cherepanov <cas@altlinux.org> 3.55.0-alt1
- New version
- Exclude SANE driver in separate package imagescan-sane.

* Sat Mar 30 2019 Andrey Cherepanov <cas@altlinux.org> 3.54.0-alt1
- New version.
- Package all shared libraries (ALT #36456).

* Wed Jan 09 2019 Andrey Cherepanov <cas@altlinux.org> 3.50.0-alt1
- New version.

* Mon Oct 29 2018 Andrey Cherepanov <cas@altlinux.org> 3.48.0-alt1
- Initial build for Sisyphus.
- Disable check.
