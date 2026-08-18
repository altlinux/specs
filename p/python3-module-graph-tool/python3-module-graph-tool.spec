%define _unpackaged_files_terminate_build 1
%define pypi_name graph-tool
%define mod_name graph_tool

Name: python3-module-%pypi_name
Version: 2.98
Release: alt1

Summary: Efficient tool for manipulation and statistical analysis of graphs
License: LGPL-3.0-or-later and BSL-1.0 and BSD-3-Clause and GPL-3.0-or-later and MIT and Apache-2.0
Group: Development/Python3
VCS: https://git.skewed.de/count0/graph-tool
URL: https://graph-tool.skewed.de
ExcludeArch: i586

Source: %name-%version.tar

# For render and display graphs
Requires: python3-module-matplotlib
Requires: python3-module-matplotlib-cairo
Requires: libgtk+3-gir
Requires: python3-module-pygobject3
Requires: python3-module-zstandard

BuildRequires(pre): rpm-macros-python3
BuildRequires: gcc-c++
BuildRequires: boost-coroutine-devel
BuildRequires: boost-python3-devel
BuildRequires: cgal-devel
BuildRequires: libcairomm-devel
BuildRequires: libexpat-devel
BuildRequires: libgomp-devel
BuildRequires: libnumpy-py3-devel
BuildRequires: sparsehash-devel
BuildRequires: python3-module-pycairo-devel
BuildRequires: gawk


%description
Graph-tool is an efficient Python module for manipulation and statistical
analysis of graphs (a.k.a. networks). Contrary to most other python modules
with similar functionality, the core data structures and algorithms are
implemented in C++, making extensive use of template metaprogramming, based
heavily on the Boost Graph Library. This confers it a level of performance that
is comparable (both in memory usage and computation time) to that of a pure
C/C++ library.


%package devel
License: LGPL-3.0+ and BSL-1.0
Summary: C++ headers for graph-tool
Group: Development/C++
Requires: libgomp-devel

%description devel
Graph-tool is an efficient Python module for manipulation and statistical
analysis of graphs (a.k.a. networks). Contrary to most other python modules
with similar functionality, the core data structures and algorithms are
implemented in C++, making extensive use of template metaprogramming, based
heavily on the Boost Graph Library. This confers it a level of performance that
is comparable (both in memory usage and computation time) to that of a pure
C/C++ library.

This package contains development files for graph-tool.

%package doc
License: GPL-3.0-or-later and LGPL-3.0+
Summary: Documentation for graph-tool
Group: Development/C++

%description doc
Graph-tool is an efficient Python module for manipulation and statistical
analysis of graphs (a.k.a. networks). Contrary to most other python modules
with similar functionality, the core data structures and algorithms are
implemented in C++, making extensive use of template metaprogramming, based
heavily on the Boost Graph Library. This confers it a level of performance that
is comparable (both in memory usage and computation time) to that of a pure
C/C++ library.

This package contains documentation for graph-tool.

%prep
%setup

%build
# debuginfo > 10G and build fail by default
%define optflags_debug -g0
./autogen.sh
%configure
%make_build

# Provide Python metadata
%global graph_tool_distinfo %pypi_name-%{version}.dist-info
mkdir %{graph_tool_distinfo}
cat > %{graph_tool_distinfo}/METADATA << EOF
Metadata-Version: 2.1
Name: %pypi_name
Version: %version
Requires-dist: numpy
Requires-dist: scipy
Requires-dist: matplotlib
Requires-dist: pygobject3
Requires-dist: zstandard
EOF
echo rpm > %graph_tool_distinfo/INSTALLER

%install
%makeinstall_std
mv %buildroot%_datadir/doc/%pypi_name %buildroot%_datadir/doc/%name-%version

# Remove static objects
find %buildroot -name '*.la' -print -delete

# Install Python metadata
install -D -m644 %graph_tool_distinfo/METADATA %buildroot%python3_sitelibdir/%graph_tool_distinfo/METADATA
install -D -m644 %graph_tool_distinfo/INSTALLER %buildroot%python3_sitelibdir/%graph_tool_distinfo/INSTALLER

%check
%make check

%files
%python3_sitelibdir/%mod_name
%python3_sitelibdir/%graph_tool_distinfo
%exclude %python3_sitelibdir/graph_tool/include

%files devel
%python3_sitelibdir/%mod_name/include
%_libdir/pkgconfig/graph-tool-py%{_python3_version}.pc
%_libdir/pkgconfig/graph-tool-py.pc

%files doc
%_datadir/doc/python3-module-%pypi_name-%version

%changelog
* Tue Mar 24 2026 Aleksandr Dovydenkov <asd@altlinux.org> 2.98-alt1
- Initial build for ALT Linux.
