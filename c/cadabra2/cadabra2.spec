Name: cadabra2
Version: 2.4.2.4
Release: alt1

%def_with gui
%def_without jupiter

Summary: A field-theory motivated approach to computer algebra
License: GPL
Group: Sciences/Mathematics
Url: https://cadabra.science
# https://github.com/kpeeters/cadabra2

Source: %{name}-%{version}.tar
Patch0: 0001-PYTHON_SITE_PATH_1.patch
Patch1: 0002-PYTHON_SITE_PATH_2.patch
Patch2: 0003-PYTHON_SITE_PATH_3.patch
Patch3: 0004-nogit.patch

BuildPreReq: rpm-macros-cmake
BuildRequires: cmake python3-dev gcc-c++
BuildRequires: libglibmm-devel libsqlite3-devel libffi-devel
BuildRequires: libgmpxx-devel libpcrecpp-devel
BuildRequires: boost-program_options-devel boost-filesystem-devel
BuildRequires: boost-signals-devel boost-asio-devel
BuildRequires: libssl-devel
# python3-module-mpl_to
%if_with gui
BuildRequires: icon-theme-hicolor libgtkmm3-devel tbb-devel
# this only needed if I use cmake_build instead of make_build(?):
BuildRequires: libblkid-devel libfribidi-devel libuuid-devel libpixman-devel
BuildRequires: libXdamage-devel libxkbcommon-devel libwayland-cursor-devel
BuildRequires: libwayland-egl-devel libepoxy-devel at-spi2-atk-devel
%endif

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
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1

%build
%cmake_insource\
  -DCMAKE_BUILD_TYPE=Debug\
  -DPACKAGING_MODE=ON\
  -DPYTHON_SITE_PATH="%python3_sitelibdir"\
  -DDESTDIR="%buildroot"\
  -DCMAKE_SKIP_INSTALL_RPATH:BOOL=no\
%if_without gui
  -DENABLE_FRONTEND=OFF\
%endif
%if_without jupiter
  -DENABLE_JUPYTER=OFF\
  -DENABLE_PY_JUPYTER=OFF
%endif

%define _cmake__builddir .
%cmake_build

%install
%cmake_install

%add_findprov_lib_path %python3_sitelibdir

%files
%_bindir/cadabra*
%_bindir/cdb-nbtool
%_datadir/cadabra2
%_man1dir/cadabra*
%python3_sitelibdir/__pycache__/*
%python3_sitelibdir/cadabra2*
%python3_sitelibdir/cdb_appdirs.py
%dir %python3_sitelibdir/cdb
%python3_sitelibdir/cdb/*

%if_with jupiter
  %dir %python3_sitelibdir/cadabra2_jupyter
  %python3_sitelibdir/cadabra2_jupyter/*
  %dir %python3_sitelibdir/notebook/static/components/codemirror/mode/cadabra/
  %python3_sitelibdir/notebook/static/components/codemirror/mode/cadabra/*
  %_datadir/jupyter
%endif

%if_with gui
  %_desktopdir/cadabra2-gtk.desktop
  %_iconsdir/hicolor/128x128/apps/cadabra2-gtk.png
  %_iconsdir/hicolor/256x256/apps/cadabra2-gtk.png
  %_iconsdir/hicolor/64x64/apps/cadabra2-gtk.png
  %_iconsdir/hicolor/scalable/apps/cadabra2-gtk.svg
%endif

%changelog
* Mon Dec 12 2022 Vladislav Zavjalov <slazav@altlinux.org> 2.4.2.4-alt1
- v.2.4.2.4

* Fri Oct 07 2022 Vladislav Zavjalov <slazav@altlinux.org> 2.4.0.2-alt1
- v.2.4.0.2

* Sat Feb 26 2022 Vladislav Zavjalov <slazav@altlinux.org> 2.3.8-alt2
- current upstream snapshot (ce5bc98) with a few important fixes
- add RPATH to binaries to fix "cadabra2.cpython-310.so not found" error

* Thu Jan 13 2022 Vladislav Zavjalov <slazav@altlinux.org> 2.3.8-alt1
- First build for Altlinux

