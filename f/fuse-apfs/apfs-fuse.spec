%define _unpackaged_files_terminate_build 1

Name:    fuse-apfs
Version: 0.1.0
Release: alt3

Summary: FUSE driver for APFS (Apple File System)
License: GPL-2.0
Group:   Other
Url:     https://github.com/sgan81/apfs-fuse
Provides: apfs-fuse = %EVR
Obsoletes: apfs-fuse < %EVR

Source: %name-%version.tar
Patch:  %name-%version-alt.patch

BuildRequires: fuse
BuildRequires: libfuse3-devel
BuildRequires: libicu-devel
BuildRequires: bzlib-devel
BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: libattr-devel
BuildRequires: liblzfse-devel
BuildRequires: zlib-devel

%description
%summary

%prep
%setup
%patch0 -p1

%build
%cmake
%cmake_build

%install
%cmakeinstall_std

%files
%doc *.md
%_bindir/*

%changelog
* Tue Jul 02 2024 Artem Semenov <savoptik@altlinux.org> 0.1.0-alt3
- rename package

* Mon Jul 01 2024 Artem Semenov <savoptik@altlinux.org> 0.1.0-alt2
- Refactored build (thx Paul Wolneykien)

* Thu Jun 27 2024 Artem Semenov <savoptik@altlinux.org> 0.1.0-alt1
- Initial build for Sisyphus
