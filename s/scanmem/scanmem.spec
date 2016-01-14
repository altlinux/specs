Summary: Simple debugging utility
Name: scanmem
Version: 0.15.4
Release: alt1
Url: http://taviso.decsystem.org/
Source: %name-%version.tar
Packager: Valentin Rosavitskiy <valintinr@altlinux.org>
License: GPLv2
Group: Development/Debuggers

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

%prep
%setup

%build
./autogen.sh
%configure \
	--enable-gui
%make

%install
%makeinstall_std

%find_lang GameConqueror

%files
%_bindir/scanmem
%_man1dir/scanmem.1.*
%_libdir/libscanmem.so*
%doc ChangeLog COPYING NEWS README TODO

%files -n gameconqueror -f GameConqueror.lang
%_bindir/gameconqueror
%_datadir/gameconqueror/
%_datadir/applications/GameConqueror.desktop
%_mandir/man1/gameconqueror.1*
%_datadir/icons/hicolor/*/apps/GameConqueror.png
%_datadir/polkit-1/actions/org.freedesktop.gameconqueror.policy
%_datadir/appdata/GameConqueror.appdata.xml

%changelog
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

