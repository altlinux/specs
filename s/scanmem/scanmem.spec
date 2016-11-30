Summary: Simple debugging utility
Name: scanmem
Version: 0.15.8
Release: alt1
Url: http://taviso.decsystem.org/
Source: %name-%version.tar
Packager: Valentin Rosavitskiy <valintinr@altlinux.org>
License: GPLv2
Group: Development/Debuggers
Patch0: scanmem-0.15.4-alt2-fix-desktop-files.patch
Patch1: scanmem-0.15.4-alt-gameconqueror-libscanmem-soname.patch

BuildRequires: libreadline-devel intltool /proc

%description
scanmem is a simple interactive debugging utility for linux, used to
locate the address of a variable in an executing process. This can be
used for the analysis or modification of a hostile process on a
compromised machine, reverse engineering, or as a "pokefinder"
to cheat at video games.

%package -n gameconqueror
Group: Development/Debuggers
BuildArch: noarch
Summary: CheatEngline-alike interface for scanmem
Requires: %name = %version-%release

%description -n gameconqueror
GameConqueror aims to provide a CheatEngline-alike interface for
scanmem, it's user-friendly and easy to use.
GameConqueror is written in PyGTK.

%package -n lib%name
Summary: Library for %name
Group: System/Libraries

%description -n lib%name
This package contains shared library used by %name

%package -n lib%name-devel
Summary: Development package that includes the %name symlincs for sharedlib
Group: Development/C

%description -n lib%name-devel
The devel package contains the symlincs for sharedlib

%prep
%setup
%patch0 -p1
%patch1 -p1

%build
./autogen.sh
%configure \
	--enable-gui \
	--docdir=%_docdir/%name-%version \
	--disable-static \
	#
%make

%install
%makeinstall_std

%find_lang GameConqueror

%files
%_bindir/scanmem
%_man1dir/scanmem.1.*
%doc ChangeLog COPYING NEWS README TODO

%files -n lib%name
%_libdir/libscanmem.so.*

%files -n lib%name-devel
%_libdir/libscanmem.so

%files -n gameconqueror -f GameConqueror.lang
%_bindir/gameconqueror
%_datadir/gameconqueror/
%_datadir/applications/GameConqueror.desktop
%_mandir/man1/gameconqueror.1*
%_datadir/icons/hicolor/*/apps/GameConqueror.png
%_datadir/polkit-1/actions/org.freedesktop.gameconqueror.policy
%_datadir/appdata/GameConqueror.appdata.xml

%changelog
* Wed Nov 30 2016 Valentin Rosavitskiy <valintinr@altlinux.org> 0.15.8-alt1
- New version

* Wed May 11 2016 Gleb F-Malinovskiy <glebfm@altlinux.org> 0.15.4-alt4
- gameconqueror: fixed work without devel subpackage.

* Fri Mar 04 2016 Gleb F-Malinovskiy <glebfm@altlinux.org> 0.15.4-alt3
- Moved %%_libdir/libscanmem.so.1 to libscanmem.
- Dropped devel-static subpackage.

* Tue Mar 01 2016 Valentin Rosavitskiy <valintinr@altlinux.org> 0.15.4-alt2
- Minor packaging changes
- Fixed some repocop warnings
- Created subpackage lib%name and lib%name-devel and lib%name-devel-static

* Wed Jan 13 2016 Gleb F-Malinovskiy <glebfm@altlinux.org> 0.15.4-alt1
- Updated to 0.15.4.
- Packaged gameconqueror.

* Mon Aug 31 2015 Valentin Rosavitskiy <valintinr@altlinux.org> 0.15.2-alt1
- New version

* Fri Jun 20 2014 Valentin Rosavitskiy <valintinr@altlinux.org> 0.14-alt1
- New version

* Fri Oct 04 2013 Valentin Rosavitskiy <valintinr@altlinux.org> 0.13-alt1
- New version

* Sat Mar 02 2013 Valentin Rosavitskiy <valintinr@altlinux.org> 0.07-alt1
- Initial build

