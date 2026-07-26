%define xdg_name org.%name.%name

Name: freac
Version: 1.1.7
Release: alt3.gitdfe19769

Summary: The fre:ac audio converter project

License: GPL-2.0
Group: Sound
URL: https://www.freac.org
VCS: https://github.com/enzo1982/freac

Source: %name-%version.tar

Patch: %name-%version-%release.patch

BuildRequires: gcc-c++
BuildRequires: libboca-devel
BuildRequires: libudev-devel

Provides: %name-doc = %EVR
Obsoletes: %name-doc < %EVR

%description
fre:ac is a free and open source audio converter.
It supports audio CD ripping and tag editing and
converts between various audio file formats.

%prep
%setup
%autopatch -p1

# remove subpackage dirs
rm -rfv boca smooth

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

# remove unnecessary link
rm -fv %buildroot%_libdir/lib%{name}*.so

%files
%doc COPYING
%_bindir/%{name}*
%_libdir/%name
%_libdir/lib%{name}*.so.*
%_datadir/%name
%_desktopdir/%xdg_name.desktop
%_iconsdir/hicolor/*/apps/%xdg_name.png
%_datadir/metainfo/%xdg_name.appdata.xml
%_docdir/%name

%changelog
* Sat Jul 25 2026 Alexander Kovalev <alexvk@altlinux.org> 1.1.7-alt3.gitdfe19769
- Update to git dfe19769.
- Move doc to main package.

* Sun Jan 25 2026 Alexander Kovalev <alexvk@altlinux.org> 1.1.7-alt2.git1a5d96f8
- Update to git 1a5d96f8.

* Tue Oct 14 2025 Alexander Kovalev <alexvk@altlinux.org> 1.1.7-alt1.git350d39ae
- Initial build for ALT.
