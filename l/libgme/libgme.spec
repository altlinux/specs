%define		srcname game-music-emu

Summary:	Game Music Emulators library
Name:		libgme
Version:	0.5.5
Release:	alt1
Source0:	http://game-music-emu.googlecode.com/files/%{srcname}-%{version}.tbz2
License:	LGPLv2+
Group:		System/Libraries
Url:		http://code.google.com/p/game-music-emu/
Packager:	Motsyo Gennadi <drool@altlinux.ru>

# Automatically added by buildreq on Sun Sep 26 2010 (-bi)
BuildRequires: cmake gcc-c++

%description
This is a collection of video game music file emulators that supports a
variety of formats and systems.

%package -n %name-devel
Group: Development/C++
Summary: Game Music Emulators development library
Requires: %name = %version-%release
Provides: %name-devel = %version-%release

%description -n %name-devel
This is a collection of video game music file emulators that supports a
variety of formats and systems.

%prep
%setup -n %srcname-%version

%build
cmake \
	-DCMAKE_INSTALL_PREFIX=%prefix \
	-DCMAKE_CXX_FLAGS:STRING="%optflags" \
	-DCMAKE_C_FLAGS:STRING="%optflags"
%make_build

%install
%makeinstall_std
%if %_lib != lib
mv %buildroot%_prefix/lib/ %buildroot%_libdir
%endif

%files
%doc readme.txt gme.txt
%_libdir/%name.so.*

%files -n %name-devel
%doc changes.txt design.txt
%_libdir/%name.so
%_includedir/gme

%changelog
* Sun Sep 26 2010 Motsyo Gennadi <drool@altlinux.ru> 0.5.5-alt1
- initial build for ALT Linux from MDV package

