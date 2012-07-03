%define major       4.0.3
%define minor       2202
%define source      Squeak-%{major}.%{minor}-src
%define source_dir  4.1

Name: squeak-vm
Version: %{major}.%{minor}
Release: alt2
Summary: The Squeak virtual machine
Group: Development/Other
License: MIT
Url: http://squeakvm.org/unix
Packager: Sugar Development Team <sugar@packages.altlinux.org>

Source: http://ftp.squeak.org/%{source_dir}/unix-linux/%{source}.tar.gz

BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: pkg-config  
BuildRequires: freetype2-devel
BuildRequires: libdbus-devel
BuildRequires: gstreamer-devel
BuildRequires: libogg-devel  
BuildRequires: libvorbis-devel
BuildRequires: libspeex-devel
BuildRequires: libpango-devel
BuildRequires: libuuid-devel
BuildRequires: libalsa-devel
BuildRequires: libaudio-devel
BuildRequires: libpulseaudio-devel
BuildRequires: glib2-devel
BuildRequires: libxml2-devel
BuildRequires: libX11-devel
BuildRequires: libGL-devel

Obsoletes: squeak-vm-nonXOplugins

%description
Squeak is a full-featured implementation of the Smalltalk programming
language and environment based on (and largely compatible with) the original
Smalltalk-80 system.

This package contains just the Squeak virtual machine.

%prep
%setup -q -n %{source}

%build
mkdir bld
cd bld

../unix/cmake/configure \
    --prefix=%{prefix} \
    --bindir=%{_bindir} \
    --plgdir=%{_libdir}/squeak/%{major}-%{minor} \
    --mandir=%{_mandir}

%make_build

%set_verify_elf_method textrel=relaxed

%install
make -C bld install DESTDIR=%{buildroot}

# remove squeak.sh that fetches kdebase-libs
rm -f %{buildroot}/%{_bindir}/squeak.sh

# these files will be put in std RPM doc location
rm -rf %{buildroot}/%{prefix}/doc/squeak

# let packages that are depending on squeak-vm know about current lib directory
ln -s %{major}-%{minor} %{buildroot}/%{_libdir}/squeak/current

%files
%doc unix/ChangeLog unix/doc/{README*,LICENSE,*RELEASE_NOTES}
%{_bindir}/*
%dir %{_libdir}/squeak
%dir %{_libdir}/squeak/%{major}-%{minor}
%{_libdir}/squeak/current
%{_libdir}/squeak/%{major}-%{minor}/squeakvm
%{_libdir}/squeak/%{major}-%{minor}/so.*
%{_mandir}/man*/*

%changelog
* Fri May 07 2010 Aleksey Lim <alsroot@altlinux.org> 4.0.3.2202-alt2
- remove squeak.sh that fetches kdebase-libs

* Thu Apr 29 2010 Aleksey Lim <alsroot@altlinux.org> 4.0.3.2202-alt1
- intial v4 spec rework by Anton A. Vinogradov
- minor spec tweak
- fix x86_64 build

* Fri Jan 29 2010 Anton A. Vinogradov <arc@altlinux.org> 3.10.5-alt0.6
- enable Mpeg3Plugin build

* Wed Jan 27 2010 Anton A. Vinogradov <arc@altlinux.org> 3.10.5-alt0.5
- initial build for ALT Linux

