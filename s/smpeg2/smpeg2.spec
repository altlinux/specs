Name: smpeg2
Version: 2.0.0
Release: alt4

Summary: SDL MPEG Player Library
License: LGPLv2
Group: Video

Url: http://icculus.org/smpeg/
Packager: Nazarov Denis <nenderus@altlinux.org>

Source0: %name-%version.tar

Patch1: %name-%version-debian-gcc-6.patch

Conflicts: smpeg-player

BuildRequires: chrpath
BuildRequires: gcc-c++
BuildRequires: libSDL2-devel

Requires: lib%name = %EVR

%description
SMPEG is a free MPEG1 video player library with sound support.  Video playback
is based on the ubiquitous Berkeley MPEG player, mpeg_play v2.2.  Audio is
played through a slightly modified mpegsound library, part of Splay v0.8.2.
SMPEG supports MPEG audio (MP3), MPEG-1 video, and MPEG system streams.

%package -n lib%name
Summary: Library for %name
Group: System/Libraries

%description -n lib%name
This package contains the library needed to run programs dynamically
linked with %name.

%package -n lib%name-devel
Summary: Headers for developing programs that will use %name
Group: Development/C

%description -n lib%name-devel
This package contains the headers that programmers will need to develop
applications which will use %name.

%prep
%setup
%patch1 -p1

%build
./autogen.sh
%configure --disable-static
%make_build

%install
%makeinstall_std
%__rm -rf %buildroot%_libdir/lib%name.la
chrpath -d %buildroot%_bindir/plaympeg
chrpath -d %buildroot%_libdir/lib%name-2.0.so.0.0.0

%files
%doc BUGS CHANGES COPYING README README.SDL_mixer TODO
%_bindir/plaympeg
%_man1dir/plaympeg.1.*

%files -n lib%name
%_libdir/lib%name-2.0.so.*

%files -n lib%name-devel
%_bindir/%name-config
%dir %_includedir/%name
%_includedir/%name/*.h
%_libdir/lib%name.so
%_aclocaldir/%name.m4

%changelog
* Thu Nov 16 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 2.0.0-alt4
- Fixed build with gcc-6.

* Mon Feb 01 2016 Nazarov Denis <nenderus@altlinux.org> 2.0.0-alt3
- Fix man file

* Wed Feb 05 2014 Nazarov Denis <nenderus@altlinux.org> 2.0.0-alt0.M70T.1
- Build for branch t7

* Fri Nov 01 2013 Nazarov Denis <nenderus@altlinux.org> 2.0.0-alt2
- Add conflicts on smpeg-player
- Add requires for lib%name-devel on lib%name

* Thu Oct 31 2013 Nazarov Denis <nenderus@altlinux.org> 2.0.0-alt1
- Initial build for ALT Linux
