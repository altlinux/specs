%define xdg_name org.%name.%name

Name: freac
Version: 1.1.7
Release: alt1.git350d39ae

Summary: The fre:ac audio converter project

License: GPL-2.0
Group: Sound
URL: https://www.freac.org
VCS: https://github.com/enzo1982/freac

Packager: Alexander Kovalev <alexvk@altlinux.org>

Source: %name-%version.tar

Patch: %name-%version-%release.patch

BuildRequires: gcc-c++
BuildRequires: libboca-devel
BuildRequires: libudev-devel

%description
fre:ac is a free and open source audio converter.
It supports audio CD ripping and tag editing and
converts between various audio file formats.

%package doc
Summary: Documentation for fre:ac
Group: Documentation
BuildArch: noarch

%description doc
fre:ac is a free and open source audio converter.
This package contains documentation for fre:ac.

%prep
%setup
%autopatch -p1
find . -type f -exec sed -i 's|/usr/local|%_prefix|g' {} \;
sed -i 's|^LIBDIR = lib$|LIBDIR = %_lib|;
        s|(prefix)/lib$|(prefix)/%_lib|' Makefile-options
sed -i 's|(prefix)/lib |(prefix)/%_lib |' Makefile Makefile-commands
sed -i 's|../lib/|../%_lib/|' src/loader/*.cpp

%build
export CFLAGS="%optflags"
export CXXFLAGS="$CFLAGS"
export OBJCFLAGS="$CFLAGS"
export OBJCXXFLAGS="$CFLAGS"
%make_build

%install
%makeinstall_std

%files
%doc Readme* COPYING
%_bindir/%{name}*
%_libdir/%name
%_datadir/%name
%_desktopdir/%xdg_name.desktop
%_iconsdir/hicolor/*/apps/%xdg_name.png
%_datadir/metainfo/%xdg_name.appdata.xml

%files doc
%_docdir/%name

%changelog
* Tue Oct 14 2025 Alexander Kovalev <alexvk@altlinux.org> 1.1.7-alt1.git350d39ae
- Initial build for ALT.
