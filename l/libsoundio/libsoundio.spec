# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-mageia-compat
BuildRequires: gcc-c++
# END SourceDeps(oneline)
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%define major	1
%define	libname	libsoundio%{major}
%define	devel	libsoundio-devel

Name:		libsoundio
Version:	1.1.0
Release:	alt1_2
Summary:	C library for cross-platform real-time audio input and output
Group:		Sound
License:	MIT
URL:		http://libsound.io/
Source0:	https://github.com/andrewrk/libsoundio/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires:	ccmake cmake ctest
BuildRequires:	pkgconfig(alsa)
BuildRequires:	pkgconfig(jack)
BuildRequires:	pkgconfig(libpulse)
Source44: import.info

%description
C library providing cross-platform audio input and output. The API is suitable
for real-time software such as digital audio workstations as well as consumer
software such as music players.

This library is an abstraction; however in the delicate balance between
performance and power, and API convenience, the scale is tipped closer to the
former. Features that only exist in some sound backends are exposed.


%package -n	%{libname}
Summary:	Library files for %{name}
Group:		System/Libraries
Requires:	%{name} = %{version}-%{release}
Obsoletes:	libsoundio-%{_lib}soundio1 < 1.1.0-2

%description -n	%{libname}
This package contains the library files for %{name}

%package -n	%{devel}
Summary:	Development files for %{name}
Group:		Development/C++
Requires:	%{libname} = %{version}-%{release}
Provides:	soundio-devel = %{version}-%{release}
Obsoletes:	libsoundio-%{_lib}soundio-devel < 1.1.0-2
Obsoletes:	libsoundio-%{_lib}soundio-static-devel < 1.1.0-2

%description -n	%{devel}
The %{devel} package contains libraries and header files for
developing applications that use %{name}.


%prep
%setup -q



%build
mkdir build
cd build
cmake .. -DCMAKE_INSTALL_PREFIX=/usr -DCMAKE_BUILD_TYPE=RelWithDebInfo
%make_build


%install
%makeinstall_std -C build


%files
%doc LICENSE README.md
%{_bindir}/*

%files -n %{libname}
%{_libdir}/*.so.%{major}
%{_libdir}/*.so.%{major}.*

%files -n %{devel}
%{_includedir}/*
%{_libdir}/*.so


%changelog
* Sat Jun 16 2018 Igor Vlasenko <viy@altlinux.ru> 1.1.0-alt1_2
- fixed build

* Sun Mar 18 2018 Igor Vlasenko <viy@altlinux.ru> 1.1.0-alt1_1
- new version

