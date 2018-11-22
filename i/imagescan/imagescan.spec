%define utsushi_version 0.48.0

Name:     imagescan
Version:  3.48.0
Release:  alt1

Summary:  EPSON Image Scan v3 front-end for scanners and all-in-ones
License:  GPLv3
Group:    Other
Url:      http://download.ebz.epson.net/dsc/search/01/search/?OSC=LX

Packager: Andrey Cherepanov <cas@altlinux.org>

# Download manually from http://support.epson.net/linux/src/scanner/imagescanv3/common/
Source:   %{name}_%version.orig.tar.gz
Source1:  utsushi.desktop
Patch1:   %name-alt-libusb-fix-deprecated.patch

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

%description
Image Scan v3 is Linux software for Epson scanners.

Image Scan v3 has own front-end, it allows to set various scanner
settings with graphical user interface and save the scanned images to
the various file type.

It supports USB and network connection for the network capable scanners.

Scanner can be controlled via not only own front-end but also command
line option.

%prep
%setup -n utsushi-%utsushi_version
%patch1 -p2

%build
%undefine _configure_gettext
%configure \
    --enable-code-coverage \
    --enable-sane-config \
    --enable-test-reports \
    --enable-udev-config \
    --with-gtkmm \
    --with-boost-libdir=%_libdir \
    --with-jpeg \
    --with-magick \
    --with-sane \
    --with-tiff
 
%make_build CXXFLAGS="-Wno-error=parentheses" LDFLAGS="-lpthread"

%install
%makeinstall_std
rm -rf %buildroot%_includedir
find %buildroot%_libdir -name *.la -delete
find %buildroot%_libdir -name *.a -delete
install -Dm0644 %SOURCE1 %buildroot%_desktopdir/utsushi.desktop

%find_lang utsushi

%check
#%%make_build check

%files -f utsushi.lang
%doc AUTHORS NEWS README
%_bindir/*
%_sysconfdir/sane.d/dll.d/utsushi
%_sysconfdir/udev/rules.d/utsushi-esci.rules
%config(noreplace) %_sysconfdir/utsushi/combo.conf
%_libexecdir/utsushi
%_datadir/utsushi
%_desktopdir/utsushi.desktop

%changelog
* Mon Oct 29 2018 Andrey Cherepanov <cas@altlinux.org> 3.48.0-alt1
- Initial build for Sisyphus.
- Disable check.
