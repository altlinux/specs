%def_with gui
%def_without jupiter

Name: cadabra2
Version: 2.6.0
Release: alt1

Summary: A field-theory motivated approach to computer algebra
License: GPL-3.0-or-later
Group: Sciences/Mathematics
Url: https://cadabra.science
VCS: https://github.com/kpeeters/cadabra2.git

Source0: %name-%version.tar
Source1: submodules.tar
Patch: %name-%version-%release.patch

BuildRequires(pre): rpm-macros-fedora-compat
BuildRequires(pre): rpm-macros-cmake
BuildRequires: rpm-build-cmake
BuildRequires: rpm-build-ninja

BuildRequires: gcc-c++
BuildRequires: python3-dev
BuildRequires: libglibmm2.68-devel
BuildRequires: libsqlite3-devel
BuildRequires: libffi-devel
BuildRequires: libgmpxx-devel
BuildRequires: libpcrecpp-devel
BuildRequires: boost-beast-devel
BuildRequires: boost-program_options-devel
BuildRequires: boost-filesystem-devel
BuildRequires: boost-signals-devel
BuildRequires: boost-asio-devel
BuildRequires: libssl-devel
BuildRequires: python3-module-setuptools

%if_with gui
BuildRequires: icon-theme-hicolor
BuildRequires: libgtkmm3-devel
BuildRequires: libgtksourceview3-devel
BuildRequires: libgtksourceviewmm3-devel
BuildRequires: libgtkmm4-devel
BuildRequires: tbb-devel
BuildRequires: libtinyxml2-devel
BuildRequires: libblkid-devel
BuildRequires: libfribidi-devel
BuildRequires: libuuid-devel
BuildRequires: libpixman-devel
BuildRequires: libXdamage-devel
BuildRequires: libxkbcommon-devel
BuildRequires: libwayland-cursor-devel
BuildRequires: libwayland-egl-devel
BuildRequires: libepoxy-devel
BuildRequires: at-spi2-atk-devel
%endif

# Optional addon (see tutorials/README.md)
%filter_from_requires /python3(obswebsocket)/d

%description
Cadabra is a symbolic computer algebra system, designed
specifically for the solution of problems encountered in quantum and
classical field theory. It has extensive functionality for tensor
computer algebra, tensor polynomial simplification including multi-term
symmetries, fermions and anti-commuting variables, Clifford algebras and
Fierz transformations, implicit coordinate dependence, multiple index
types and many more. The input format is a subset of TeX. Both a
command-line and a graphical interface are available, and there is a
kernel for Jupyter

%prep
%setup -a1
%autopatch -p1

%build
%cmake -G Ninja \
	-DCMAKE_BUILD_TYPE=Debug \
	-DPACKAGING_MODE=ON \
	-DPYTHON_SITE_PATH="%python3_sitelibdir" \
	-DDESTDIR="%buildroot" \
	-DCMAKE_SKIP_INSTALL_RPATH:BOOL=NO \
	-DENABLE_FRONTEND=%{with gui} \
	-DENABLE_JUPYTER=%{with jupiter} \
	-DENABLE_PY_JUPYTER=%{with jupiter} \
%nil
%cmake_build

%install
%cmake_install

%add_findprov_lib_path %python3_sitelibdir

%files
%doc CITATION.cff JUPYTER.rst README.rst tutorials/README.md
%_bindir/cadabra*
%_bindir/cdb-nbtool
%_datadir/cadabra2
%_man1dir/cadabra*
%python3_sitelibdir/__pycache__/*
%python3_sitelibdir/cadabra2*
%python3_sitelibdir/cdb_appdirs.py
%python3_sitelibdir/cdb

%if_with jupiter
	%python3_sitelibdir/cadabra2_jupyter
	%python3_sitelibdir/notebook/static/components/codemirror/mode/cadabra
	%_datadir/jupyter
%endif

%if_with gui
	%_desktopdir/science.cadabra.cadabra2-gtk.desktop
	%_iconsdir/hicolor/128x128/apps/cadabra2-gtk.png
	%_iconsdir/hicolor/256x256/apps/cadabra2-gtk.png
	%_iconsdir/hicolor/64x64/apps/cadabra2-gtk.png
	%_iconsdir/hicolor/scalable/apps/cadabra2-gtk.svg
	%_metainfodir/science.cadabra.cadabra2-gtk.appdata.xml
%endif

%changelog
* Fri Oct 30 2026 Ulysses Apokin <ulysses@altlinux.org> 2.6.0-alt1
- New version.
- Fix FTBFS.

* Sun Apr 28 2024 Vladislav Zavjalov <slazav@altlinux.org> 2.4.5.4-alt2
- add BuildRequires: python3-module-setuptools

* Mon Jan 29 2024 Vladislav Zavjalov <slazav@altlinux.org> 2.4.5.4-alt1
- v.2.4.5.4

* Mon Sep 25 2023 Vladislav Zavjalov <slazav@altlinux.org> 2.4.4.1-alt1
- v.2.4.4.1

* Mon Dec 12 2022 Vladislav Zavjalov <slazav@altlinux.org> 2.4.2.4-alt1
- v.2.4.2.4

* Fri Oct 07 2022 Vladislav Zavjalov <slazav@altlinux.org> 2.4.0.2-alt1
- v.2.4.0.2

* Sat Feb 26 2022 Vladislav Zavjalov <slazav@altlinux.org> 2.3.8-alt2
- current upstream snapshot (ce5bc98) with a few important fixes
- add RPATH to binaries to fix "cadabra2.cpython-310.so not found" error

* Thu Jan 13 2022 Vladislav Zavjalov <slazav@altlinux.org> 2.3.8-alt1
- First build for Altlinux
