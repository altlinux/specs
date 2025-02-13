Name: glaze-devel
Version: 4.3.1
Release: alt1
License: MIT

Summary: Extremely fast, in memory, JSON and interface library for modern C++

Group: Development/C++

Url: https://github.com/stephenberry/glaze
Vcs: https://github.com/stephenberry/glaze.git

Source: %name-%version.tar

BuildArch: noarch

BuildRequires(pre): rpm-macros-cmake

BuildRequires: gcc-c++ cmake

%description
One of the fastest JSON libraries in the world.
Glaze reads and writes from object memory, simplifying
interfaces and offering incredible performance.

%prep
%setup

%build
%cmake -DBUILD_TESTING=OFF
%cmake_build

%install
%cmake_install

%files
%_includedir/glaze/
%_datadir/glaze/*.cmake

%changelog
* Thu Jan 30 2025 Kirill Unitsaev <fiersik@altlinux.org> 4.3.1-alt1
- Initial build
