%define modname ExifRead
%define pypi_name exifread

# no test resources in tarball
%def_disable check

Name: python3-module-%pypi_name
Version: 3.5.1
Release: alt1

Summary: Python3 library to extract Exif metadata
Group: Development/Python3
License: BSD-3-Clause
Url: https://pypi.org/project/%modname

Vcs: https://github.com/ianare/exif-py

Source: https://pypi.io/packages/source/e/%pypi_name/%pypi_name-%version.tar.gz

BuildArch: noarch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3(wheel) python3(setuptools)
%{?_enable_check:BuildRequires: python3(pytest)}

%description
Easy to use Python3 module to extract Exif metadata from digital image files.
Supported formats: TIFF, JPEG, PNG, Webp, HEIC.

%prep
%setup -n %pypi_name-%version

%build
%pyproject_build

%install
%pyproject_install

%check
py.test3

%files
%_bindir/EXIF.py
%python3_sitelibdir_noarch/%pypi_name/
%python3_sitelibdir_noarch/%{pyproject_distinfo %pypi_name}
%doc README* ChangeLog*

%changelog
* Fri Aug 29 2025 Yuri N. Sedunov <aris@altlinux.org> 3.5.1-alt1
- 3.5.1

* Tue Aug 05 2025 Yuri N. Sedunov <aris@altlinux.org> 3.4.0-alt1
- 3.4.0

* Fri Jul 18 2025 Yuri N. Sedunov <aris@altlinux.org> 3.3.2-alt1
- 3.3.2

* Tue May 13 2025 Yuri N. Sedunov <aris@altlinux.org> 3.3.1-alt1
- 3.3.1

* Fri May 09 2025 Yuri N. Sedunov <aris@altlinux.org> 3.3.0-alt1.1
- fixed build with setuptools 75.8.1

* Thu May 01 2025 Yuri N. Sedunov <aris@altlinux.org> 3.3.0-alt1
- 3.3.0

* Mon Apr 28 2025 Yuri N. Sedunov <aris@altlinux.org> 3.2.0-alt1
- 3.2.0

* Sat Apr 26 2025 Yuri N. Sedunov <aris@altlinux.org> 3.1.0-alt1
- 3.1.0

* Wed May 11 2022 Yuri N. Sedunov <aris@altlinux.org> 3.0.0-alt1
- 3.0.0

* Wed Jan 05 2022 Yuri N. Sedunov <aris@altlinux.org> 2.3.2-alt1
- first build for Sisyphus




