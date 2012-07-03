%define oname openal-soft

Name: openal
Summary: 3D Sound Library
Version: 1.13
Release: alt1
License: LGPLv2
Group: Sound
URL: http://www.openal.org

Source0: http://connect.creativelabs.com/openal/Downloads/%oname-%version.tbz2
Patch0: openal-soft-1.13-alt-config.patch

BuildRequires: cmake libalsa-devel libpulseaudio-devel

%description
OpenAL is a free 3D-audio library, with a programming interface similar
to that of OpenGL

%package -n lib%{name}1
Summary: Main library for OpenAL, a free 3D sound library
Group: Sound

%description -n lib%{name}1
This package contains the library needed to run programs dynamically
linked with OpenAL

%package -n lib%name-devel
Summary: Headers for developing programs that will use OpenAL
Group: Development/C
Requires: lib%{name}1 = %version-%release
Obsoletes: lib%{name}1-devel < %version
Provides: lib%{name}1-devel = %version-%release

%description -n lib%name-devel
This package contains the headers that programmers will need to develop
applications which will use OpenAL, a free 3D audio library

%prep
%setup -q -n %oname-%version
%patch0 -p1

%build
cmake \
	-DOSS=OFF \
	-DALSOFT_CONFIG=ON \
	-DCMAKE_INSTALL_PREFIX=%prefix \
%ifarch x86_64
	-DLIB_SUFFIX=64
%endif
#
%make

%install
%make DESTDIR=%buildroot install
rm -f %buildroot%_bindir/%name-info

%files -n lib%{name}1
%dir %_sysconfdir/%name
%config(noreplace) %_sysconfdir/%name/alsoft.conf
%_libdir/*.so.*

%files -n lib%name-devel
%_includedir/AL
%_libdir/*.so
%_pkgconfigdir/*.pc

%changelog
* Mon Mar 28 2011 Valery Inozemtsev <shrek@altlinux.ru> 1.13-alt1
- 1.13

* Fri Nov 05 2010 Valery Inozemtsev <shrek@altlinux.ru> 1.11.753-alt3
- rebuild

* Tue Mar 09 2010 Valery Inozemtsev <shrek@altlinux.ru> 1.11.753-alt2
- fixed %_bindir/openal-config attribute (closes: #23099)

* Sun Feb 28 2010 Valery Inozemtsev <shrek@altlinux.ru> 1.11.753-alt1
- 1.11.753

