%define _unpackaged_files_terminate_build 1

%def_with check

Name: atoms
Version: 2.0.2
Release: alt1

Summary: Open persistent Linux environments in a terminal
License: GPL-3.0-only
Group: System/Configuration/Other
Url: https://github.com/AtomsDevs/Atoms

Source: %name-%version.tar
Source1: submodules-%name-%version.tar

Patch: %name-%version-%release.patch

BuildRequires(pre): meson
BuildRequires(pre): rpm-build-vala

BuildRequires: vala-tools
BuildRequires: cmake
BuildRequires: pkgconfig(gee-0.8)
BuildRequires: pkgconfig(libpeas-2)
BuildRequires: pkgconfig(json-glib-1.0)
BuildRequires: pkgconfig(gtk4)
BuildRequires: pkgconfig(vte-2.91-gtk4)
BuildRequires: pkgconfig(singularity-1.0)

Requires: cpak

# need cpak, which needs go >= 1.26.7
ExcludeArch: riscv64

%if_with check
BuildRequires: /usr/bin/xvfb-run
%endif

%description
Atoms opens persistent Linux environments supplied by installed
providers. Work with several environments using terminal tiles and tabs
while keeping permissions, processes, and lifecycle controls close to
the active shell.

Every environment has private writable system and home layers. Atoms can
narrow its permission policy but cannot grant access beyond the
provider's permission ceiling.

%package devel
Summary: Development files for %name
Group: Development/Other
Requires: %name = %{version}-%{release}

%description devel
Development files for %name.

%prep
%setup -a1
%patch -p1

%build
%meson
%meson_build

%install
%meson_install

%find_lang %name

%check
xvfb-run %meson_test

%files -f %{name}.lang
%doc CONTRIBUTING.md LICENSE README.md
%_bindir/atoms
%_bindir/atoms-cli
%_libdir/atoms/providers/atoms-provider-cpak.plugin
%_libdir/atoms/providers/libatoms-provider-cpak.so
%_libdir/libatoms-core-2.so.2
%_libdir/libatoms-core-2.so.2.0.2
%_desktopdir/pm.mirko.Atoms.desktop
%_datadir/glib-2.0/schemas/pm.mirko.Atoms.gschema.xml
%_iconsdir/hicolor/scalable/apps/pm.mirko.Atoms.svg
%_iconsdir/hicolor/symbolic/apps/pm.mirko.Atoms-symbolic.svg
%_datadir/metainfo/pm.mirko.Atoms.metainfo.xml

%files devel
%dir %_includedir/atoms-core-2
%_includedir/atoms-core-2/atoms-core-2.h
%_libdir/libatoms-core-2.so
%_libdir/pkgconfig/atoms-core-2.pc
%_vapidir/atoms-core-2.vapi

%changelog
* Sat Sep 05 2026 Nikolay Strelkov <snk@altlinux.org> 2.0.2-alt1
- Initial build for Sisyphus
