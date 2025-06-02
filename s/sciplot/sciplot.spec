Name:    sciplot
Version: 0.3.1
Release: alt2
Summary: A modern C++ scientific plotting library powered by gnuplot

License: MIT
Group:   Sciences/Mathematics
Url:     https://github.com/sciplot/sciplot

Source0: %name-%version.tar
Source1: %name-postsubmodules-%version.tar
Patch:   testing-sciplot-cpptests.patch

BuildRequires(pre): rpm-macros-cmake
BuildRequires: cmake gcc-c++
BuildRequires: ctest

%description
The goal of the sciplot project is to enable a C++ programmer to conveniently
plot beautiful graphs as easy as in other high-level programming languages.
sciplot is a header-only library that needs a C++17-capable compiler, but has
no external dependencies for compiling. The only external runtime dependencies
are gnuplot-palettes for providing color palettes and a gnuplot executable.

%package devel
Summary: %summary
Group: Development/C++
Provides: %name-static = %EVR

%description devel
The goal of the sciplot project is to enable a C++ programmer to conveniently
plot beautiful graphs as easy as in other high-level programming languages.
sciplot is a header-only library that needs a C++17-capable compiler, but has
no external dependencies for compiling. The only external runtime dependencies
are gnuplot-palettes for providing color palettes and a gnuplot executable.

%package examples
Summary: Various examples showcasing %name
Group: Development/Documentation
Requires: /usr/bin/gnuplot

%description examples
This package contains a number of examples using and showcasing %name.

%prep
%setup -a1
%patch -p1

# Fix permissions
chmod -x LICENSE README.md

%build
export CXXFLAGS+=-std=c++17

# Building docs requires mkdocs which isn't packaged
%cmake -DSCIPLOT_BUILD_DOCS=OFF
%cmake_build

%install
%cmake_install

# Install examples manually and rename them for clarity
for f in examples/example-* ; do
  install -Dpm0755 "$f" "%buildroot%_bindir/sciplot-$(basename "$f")"
done

%check
%ctest

%files devel
%doc LICENSE README.md
%_datadir/%name
%_includedir/%name

%files examples
%doc LICENSE
%_bindir/sciplot-example-*

%changelog
* Sun Jun 01 2025 Sergey Palcheh <minergenon@altlinux.org> 0.3.1-alt2
- added testing-sciplot-cpptests.patch

* Tue Jan 14 2025 Sergey Palcheh <minergenon@altlinux.org> 0.3.1-alt1
- initial build for ALT Sisyphus

