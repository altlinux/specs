# BEGIN SourceDeps(oneline):
BuildRequires: gcc-c++
# END SourceDeps(oneline)
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%define	libname	libsoundio1
%define	devel	libsoundio-devel
%define	static	libsoundio-devel-static

Name:		libsoundio
Version:	1.1.0
Release:	alt1_1
Summary:	C library for cross-platform real-time audio input and output
Group:		Sound

License:	MIT
URL:		http://libsound.io/
Source0:	https://github.com/andrewrk/libsoundio/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires:	ccmake cmake ctest
BuildRequires:	pkgconfig(alsa)
BuildRequires:	pkgconfig(jack)
BuildRequires:	libpulseaudio-devel
Source44: import.info

%description
C library providing cross-platform audio input and output. The API is suitable
for real-time software such as digital audio workstations as well as consumer
software such as music players.

This library is an abstraction; however in the delicate balance between
performance and power, and API convenience, the scale is tipped closer to the
former. Features that only exist in some sound backends are exposed.


%package	%{libname}
Group: Sound
Summary:	Library files for %{name}
Requires:	%{name}

%description	%{libname}
This package contains the library files for %{name}

%package        %{devel}
Group: Sound
Summary:	Development files for %{name}
Requires:	%{name}%{?_isa} = %{version}-%{release}

%description	%{devel}
The %{name}-%{devel} package contains libraries and header files for
developing applications that use %{name}.

%package	%{static}
Group: Sound
Summary:	Static deveopment files for %{name}

%description	%{static}
The %{name}-%{static} package contains the static libraries and header
files for developing applications that use %{name}.

%prep
%setup -q



%build
mkdir build
cd build
cmake .. -DCMAKE_INSTALL_PREFIX=/usr -DCMAKE_BUILD_TYPE=RelWithDebInfo
%make_build


%install
cd build
make install DESTDIR=%{buildroot}

%files
%doc LICENSE README.md
%{_bindir}/*

%files	%{libname}
%{_libdir}/*.so.*

%files	%{devel}
%{_includedir}/*
%{_libdir}/*.so

%files	%{static}
%{_libdir}/*.a


%changelog
* Sun Mar 18 2018 Igor Vlasenko <viy@altlinux.ru> 1.1.0-alt1_1
- new version

