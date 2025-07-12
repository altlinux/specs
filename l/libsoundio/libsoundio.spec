%define sover	2
%define	libname	libsoundio%sover
%define	devel	libsoundio-devel

Name:		libsoundio
Version:	2.0.0
Release:	alt2
Summary:	C library for cross-platform real-time audio input and output
Group:		Sound
License:	MIT
URL:		http://libsound.io/
VCS:		https://github.com/andrewrk/libsoundio
Source:		%name-%version.tar

BuildRequires(pre): rpm-macros-cmake
BuildRequires:  gcc-c++
BuildRequires:	ccmake cmake ctest
BuildRequires:	pkgconfig(alsa)
BuildRequires:	pkgconfig(jack)
BuildRequires:	pkgconfig(libpulse)

%description
C library providing cross-platform audio input and output. The API is suitable
for real-time software such as digital audio workstations as well as consumer
software such as music players.

This library is an abstraction; however in the delicate balance between
performance and power, and API convenience, the scale is tipped closer to the
former. Features that only exist in some sound backends are exposed.


%package -n	%libname
Summary:	Library files for %name
Group:		System/Libraries
Obsoletes:	libsoundio-%{_lib}soundio1 < 1.1.0-2

%description -n	%libname
This package contains the library files for %name.

%package	devel
Summary:	Development files for %name
Group:		Development/C++
Requires:	%libname = %EVR
Provides:	soundio-devel = %EVR
Obsoletes:	libsoundio-%{_lib}soundio-devel < 1.1.0-2
Obsoletes:	libsoundio-%{_lib}soundio-static-devel < 1.1.0-2

%description	devel
The %devel package contains libraries and header files for
developing applications that use %name.

%prep
%setup

%build
%cmake  -DBUILD_STATIC_LIBS=FALSE
%cmake_build

%install
%cmake_install

%files
%doc LICENSE README.md
%_bindir/*

%files -n %libname
%_libdir/*.so.%sover
%_libdir/*.so.%sover.*

%files devel
%_includedir/*
%_libdir/*.so

%changelog
* Sat Jul 12 2025 Anton Midyukov <antohami@altlinux.org> 2.0.0-alt2
- fix FTBFS, cleanup spec
- add VCS

* Tue Feb 25 2020 Igor Vlasenko <viy@altlinux.ru> 2.0.0-alt1_2
- fixed build

* Wed Nov 20 2019 Igor Vlasenko <viy@altlinux.ru> 2.0.0-alt1_1
- update by mgaimport

* Sat Jun 16 2018 Igor Vlasenko <viy@altlinux.ru> 1.1.0-alt1_2
- fixed build

* Sun Mar 18 2018 Igor Vlasenko <viy@altlinux.ru> 1.1.0-alt1_1
- new version

