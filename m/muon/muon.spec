%define __builddir %_target_platform

%define ver_major 0.1
%define _libexecdir %_prefix/libexec
%define pkgconf_ver 1.8.0

%def_disable check
%def_enable docs
%def_enable libpkgconf
%def_disable tracy

Name: muon
Version: %ver_major.0
Release: alt2

Summary: C-implemetation of Meson build system
License: GPL-3.0-only
Group: Development/Other
Url: https://github.com/annacrombie/muon

Vcs: https://github.com/annacrombie/muon.git
Source: %name-%version.tar
Source1: https://mochiro.moe/wrap/samurai-1.2-32-g81cef5d.tar.gz
Source2: https://mochiro.moe/wrap/meson-docs-0.64.1-19-g39c6fa4bc.tar.gz
Source3: %name.macros
Source4: %name.env

Requires: rpm-macros-%name = %EVR
Requires: pkgconf >= %pkgconf_ver ninja-build

BuildRequires: ninja-build libcurl-devel libarchive-devel
%{?_enable_libpkgconf:BuildRequires: libpkgconf-devel}
%{?_enable_docs:BuildRequires: python3-module-yaml scdoc}
%{?_enable_tracy:BuildRequires: pkgconfig(tracy) gcc-c++}
%{?_enable_check:BuildRequires: python3 gcc-c++ ...}

%description
Muon is an implementation of the meson build system in c99 with minimal
dependencies.

%package -n rpm-macros-%name
Summary: RPM macros for Muon build system
Group: Development/Other
BuildArch: noarch

%description -n rpm-macros-%name
This package provides RPM macros for Muon build system.

%package doc
Summary: Developer documentation for %name
Group: Development/C
Conflicts: %name < %version
BuildArch: noarch

%description doc
Developpment documentation for %name.

%prep
%setup -a1 -a2
mv samurai meson-docs subprojects/
mkdir %__builddir

%build
CC=gcc ./bootstrap.sh ./
CFLAGS="${CFLAGS:-%optflags %(getconf LFS_CFLAGS)}"; export CFLAGS;
./muon setup \
    -Dprefix=%{_prefix} \
    -Dbindir=%{_bindir} \
    -Dsamurai=enabled \
    %{?_disable_tracy:-Dtracy=disabled} \
    %__builddir
ninja-build %_smp_mflags -C %__builddir
cp -f %__builddir/muon ./

%install
DESTDIR=%buildroot ./muon -C %__builddir install
install -Dpm 0644 %SOURCE3 %buildroot%_rpmmacrosdir/%name
install -Dpm 0755 %SOURCE4 %buildroot%_rpmmacrosdir/%name.env

%check
./muon -C %__builddir test -R

%files
%_bindir/%name
%doc README.md

%files -n rpm-macros-%name
%_rpmmacrosdir/%name
%_rpmmacrosdir/%name.env

%if_enabled docs
%files doc
%_man1dir/%name.1*
%_man3dir/meson-reference.3*
%_man5dir/meson.build.5*
%endif


%changelog
* Thu Mar 30 2023 Yuri N. Sedunov <aris@altlinux.org> 0.1.0-alt2
- 0.1.0-187-gc7b33f70
- muon.macros: added %%muon_meson macros for experimental meson cli
  compatibility layer

* Tue Oct 11 2022 Yuri N. Sedunov <aris@altlinux.org> 0.1.0-alt1
- 0.1.0-5-gab1e044c

* Fri Oct 07 2022 Yuri N. Sedunov <aris@altlinux.org> 0.0.1-alt0.92
- updated to 2021ab4a

* Tue Aug 16 2022 Yuri N. Sedunov <aris@altlinux.org> 0.0.1-alt0.91
- updated to 6b2758d3

* Wed Aug 03 2022 Yuri N. Sedunov <aris@altlinux.org> 0.0.1-alt0.9
- first build for Sisyphus (27c87a5)



