Name: glaze-devel
Version: 7.3.3
Release: alt1
License: MIT

Summary: Extremely fast, in memory, JSON and interface library for modern C++

Group: Development/C++

Url: https://github.com/stephenberry/glaze
Vcs: https://github.com/stephenberry/glaze.git

Source: %name-%version.tar

Patch1: fix-path.patch

BuildArch: noarch

BuildRequires(pre): rpm-macros-cmake

BuildRequires: gcc-c++ cmake

%description
One of the fastest JSON libraries in the world.
Glaze reads and writes from object memory, simplifying
interfaces and offering incredible performance.

%prep
%setup
%autopatch -p1

%build
%cmake -DBUILD_TESTING=OFF
%cmake_build

%install
%cmake_install

%files
%_includedir/glaze/
%_datadir/cmake/glaze/*.cmake

%changelog
* Wed Apr 15 2026 Kirill Unitsaev <fiersik@altlinux.org> 7.3.3-alt1
- new version 7.3.3

* Fri Mar 20 2026 Kirill Unitsaev <fiersik@altlinux.org> 7.2.1-alt1
- new version 7.2.1 (with rpmrb script)

* Sat Feb 07 2026 Kirill Unitsaev <fiersik@altlinux.org> 7.0.2-alt1
- new version 7.0.2 (with rpmrb script)

* Sun Jan 25 2026 Kirill Unitsaev <fiersik@altlinux.org> 7.0.1-alt1
- new version 7.0.1 (with rpmrb script)
- fix cmake config path (fix-path.patch)

* Fri Dec 05 2025 Kirill Unitsaev <fiersik@altlinux.org> 6.1.0-alt1
- new version 6.1.0 (with rpmrb script)

* Sat Nov 15 2025 Kirill Unitsaev <fiersik@altlinux.org> 6.0.3-alt1
- new version 6.0.3 (with rpmrb script)

* Sat Nov 08 2025 Kirill Unitsaev <fiersik@altlinux.org> 6.0.2-alt1
- new version 6.0.2 (with rpmrb script)

* Thu Oct 16 2025 Kirill Unitsaev <fiersik@altlinux.org> 6.0.0-alt1
- new version 6.0.0 (with rpmrb script)

* Tue Sep 30 2025 Kirill Unitsaev <fiersik@altlinux.org> 5.7.2-alt1
- new version 5.7.2 (with rpmrb script)

* Sun Aug 31 2025 Kirill Unitsaev <fiersik@altlinux.org> 5.6.1-alt1
- new version 5.6.1 (with rpmrb script)

* Thu Jul 17 2025 Kirill Unitsaev <fiersik@altlinux.org> 5.5.4-alt1
- new version 5.5.4 (with rpmrb script)

* Sat Jun 14 2025 Kirill Unitsaev <fiersik@altlinux.org> 5.4.1-alt1
- new version 5.4.1 (with rpmrb script)

* Wed May 28 2025 Kirill Unitsaev <fiersik@altlinux.org> 5.3.0-alt1
- new version 5.3.0 (with rpmrb script)

* Thu May 08 2025 Kirill Unitsaev <fiersik@altlinux.org> 5.2.0-alt1
- new version 5.2.0 (with rpmrb script)

* Thu May 01 2025 Kirill Unitsaev <fiersik@altlinux.org> 5.1.1-alt1
- new version 5.1.1 (with rpmrb script)

* Mon Apr 28 2025 Kirill Unitsaev <fiersik@altlinux.org> 5.1.0-alt1
- new version 5.1.0 (with rpmrb script)

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
