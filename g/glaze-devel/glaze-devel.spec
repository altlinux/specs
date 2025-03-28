Name: glaze-devel
Version: 5.0.2
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
* Fri Mar 28 2025 Kirill Unitsaev <fiersik@altlinux.org> 5.0.2-alt1
- new version 5.0.2 (with rpmrb script)

* Tue Mar 25 2025 Kirill Unitsaev <fiersik@altlinux.org> 5.0.1-alt1
- new version 5.0.1 (with rpmrb script)

* Sun Mar 16 2025 Kirill Unitsaev <fiersik@altlinux.org> 5.0.0-alt1
- new version 5.0.0 (with rpmrb script)

* Mon Feb 17 2025 Kirill Unitsaev <fiersik@altlinux.org> 4.4.2-alt1
- new version 4.4.2 (with rpmrb script)

* Thu Jan 30 2025 Kirill Unitsaev <fiersik@altlinux.org> 4.3.1-alt1
- Initial build
