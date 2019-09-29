BuildRequires: chrpath
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-mageia-compat
BuildRequires: gcc-c++
# END SourceDeps(oneline)
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
# %%name is ahead of its definition. Predefining for rpm 4.0 compatibility.
%define name faudio
%define uname   FAudio

%define major   0
%define libname lib%{name}%{major}
%define devname lib%{name}-devel

Name:           faudio
Version:        19.04
Release:        alt1_1
Summary:        FAudio, accuracy-focused XAudio reimplementation for open platforms
Group:          System/Libraries
License:        zlib
URL:            https://fna-xna.github.io
Source0:        https://github.com/FNA-XNA/FAudio/archive/%{version}/%{uname}-%{version}.tar.gz

BuildRequires:  ccmake cmake ctest
BuildRequires:  pkgconfig(sdl2)
Source44: import.info

%description
FAudio is an XAudio reimplementation that focuses solely on developing
fully accurate DirectX Audio runtime libraries for the FNA project,
including XAudio2, X3DAudio, XAPO, and XACT3.

%package -n %{libname}
Summary:        FAudio, accuracy-focused XAudio reimplementation for open platforms
Group:          System/Libraries

%description -n %{libname}
FAudio is an XAudio reimplementation that focuses solely on developing
fully accurate DirectX Audio runtime libraries for the FNA project,
including XAudio2, X3DAudio, XAPO, and XACT3.

%package -n %{devname}
Summary:        Development files for the FAudio library
Group:          Development/C
Requires:       %{libname} = %{version}-%{release}
Provides:       %{name}-devel = %{version}-%{release}

%description -n %{devname}
Headers and shared library for FAudio.

%prep
%setup -q -n %{uname}-%{version}


%build
%{mageia_cmake}
%make_build

%install
%makeinstall_std -C build
# kill rpath
for i in `find %buildroot{%_bindir,%_libdir,/usr/libexec,/usr/lib,/usr/sbin} -type f -perm -111 ! -name '*.la' `; do
	chrpath -d $i ||:
done

%files -n %{libname}
%doc README
%doc --no-dereference LICENSE
%{_libdir}/lib%{uname}.so.%{major}
%{_libdir}/lib%{uname}.so.%{major}.%{version}

%files -n %{devname}
%{_includedir}/F*.h
%{_libdir}/cmake/%{uname}/
%{_libdir}/lib%{uname}.so


%changelog
* Sun Sep 29 2019 Igor Vlasenko <viy@altlinux.ru> 19.04-alt1_1
- new version

