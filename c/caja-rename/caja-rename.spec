%define _unpackaged_files_terminate_build 1

Name: caja-rename
Version: 25.1.1
Release: alt1

Summary: Batch renaming extension for Caja
License: GPLv3
Group: Graphical desktop/MATE
Url: https://github.com/tari01/caja-rename

Source: %name-%version.tar

Patch: %name-%version-%release.patch

BuildRequires(pre): rpm-macros-cmake

BuildRequires: cmake
BuildRequires: pkgconfig(gtk+-3.0)
BuildRequires: pkgconfig(libcaja-extension)
BuildRequires: pkgconfig(gmodule-export-2.0)
BuildRequires: ayatana-cmake-modules
BuildRequires: intltool

Requires: /usr/bin/caja

%description
An extension for the Caja file browser allowing users to rename multiple
files/folders in a single pass.

The application can change the case, insert, replace and delete strings,
as well as enumerate the selection. Any changes are instantly visible in
the preview list. The user interface strives to be as simple as
possible, without confusing advanced operations.

%prep
%setup
%patch -p1

%build
%cmake
%cmake_build

%install
%cmake_install

# this translation is ignored by %%find_lang
rm -fv %buildroot%_datadir/locale/zh_Hans/LC_MESSAGES/%name.mo

%find_lang %name

%files -f %name.lang
%doc *.md COPYING
%_libdir/caja/extensions-2.0/*.so
%_datadir/caja/extensions/*.caja-extension
%_iconsdir/*/*/apps/%name.*

%changelog
* Fri Feb 07 2025 Nikolay Strelkov <snk@altlinux.org> 25.1.1-alt1
- Initial build for Sisyphus
