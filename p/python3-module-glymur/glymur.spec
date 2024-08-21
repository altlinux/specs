%define  oname glymur
%def_with check

Name:    python3-module-%oname
Version: 0.13.6
Release: alt1

Summary: Python interface to OpenJPEG library for reading and writing JPEG 2000 images

License: MIT
Group:   Development/Python3
URL:     https://pypi.org/project/Glymur
VCS:     https://github.com/quintusdias/glymur

Packager: Grigory Ustinov <grenka@altlinux.org>

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-wheel

%if_with check
BuildRequires: python3-module-pytest
BuildRequires: python3-module-numpy
BuildRequires: python3-module-numpy-testing
BuildRequires: python3-module-lxml
BuildRequires: python3-module-scikit-image
%endif

BuildArch: noarch

Source:  %name-%version.tar

%description
%summary.

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest

%files
%doc README.md CHANGES.txt LICENSE.txt
%_bindir/jp2dump
%_bindir/tiff2jp2
%python3_sitelibdir/%oname
%python3_sitelibdir/Glymur-%version.dist-info

%changelog
* Wed Aug 21 2024 Grigory Ustinov <grenka@altlinux.org> 0.13.6-alt1
- Automatically updated to 0.13.6.

* Sun Jul 28 2024 Grigory Ustinov <grenka@altlinux.org> 0.13.5-alt1
- Automatically updated to 0.13.5.

* Mon Jul 08 2024 Grigory Ustinov <grenka@altlinux.org> 0.13.4-alt1
- Automatically updated to 0.13.4.

* Thu Jul 04 2024 Grigory Ustinov <grenka@altlinux.org> 0.13.3-alt1
- Automatically updated to 0.13.3.

* Wed May 08 2024 Grigory Ustinov <grenka@altlinux.org> 0.13.2-alt1
- Automatically updated to 0.13.2.

* Tue Apr 23 2024 Grigory Ustinov <grenka@altlinux.org> 0.13.1-alt1
- Automatically updated to 0.13.1.

* Mon Apr 22 2024 Grigory Ustinov <grenka@altlinux.org> 0.13.0-alt1
- Automatically updated to 0.13.0.

* Thu Dec 21 2023 Grigory Ustinov <grenka@altlinux.org> 0.12.9-alt1
- Automatically updated to 0.12.9.

* Fri Jul 14 2023 Grigory Ustinov <grenka@altlinux.org> 0.12.8-alt1
- Automatically updated to 0.12.8.

* Sun Jun 11 2023 Grigory Ustinov <grenka@altlinux.org> 0.12.7-alt1
- Automatically updated to 0.12.7.

* Fri May 05 2023 Grigory Ustinov <grenka@altlinux.org> 0.12.5-alt1
- Automatically updated to 0.12.5.

* Thu Apr 27 2023 Grigory Ustinov <grenka@altlinux.org> 0.12.4-alt1
- Automatically updated to 0.12.4.

* Mon Apr 24 2023 Grigory Ustinov <grenka@altlinux.org> 0.12.3-alt1
- Automatically updated to 0.12.3.

* Thu Jan 12 2023 Grigory Ustinov <grenka@altlinux.org> 0.12.2-alt1
- Automatically updated to 0.12.2.

* Tue Nov 29 2022 Grigory Ustinov <grenka@altlinux.org> 0.12.1-alt1
- Automatically updated to 0.12.1.

* Mon Oct 31 2022 Grigory Ustinov <grenka@altlinux.org> 0.12.0-alt1
- Automatically updated to 0.12.0.

* Tue Sep 20 2022 Grigory Ustinov <grenka@altlinux.org> 0.11.7-alt1
- Automatically updated to 0.11.7.

* Tue Sep 13 2022 Grigory Ustinov <grenka@altlinux.org> 0.11.6-alt1
- Automatically updated to 0.11.6.

* Mon Sep 12 2022 Grigory Ustinov <grenka@altlinux.org> 0.11.5-alt1
- Automatically updated to 0.11.5.

* Wed Jul 20 2022 Grigory Ustinov <grenka@altlinux.org> 0.10.2-alt2
- Built and installed by pyproject_* macros.

* Mon Jul 18 2022 Grigory Ustinov <grenka@altlinux.org> 0.10.2-alt1
- Automatically updated to 0.10.2.

* Thu Jun 30 2022 Grigory Ustinov <grenka@altlinux.org> 0.10.1-alt1
- Automatically updated to 0.10.1.

* Thu Jun 16 2022 Grigory Ustinov <grenka@altlinux.org> 0.10.0-alt1
- Automatically updated to 0.10.0.

* Fri Mar 25 2022 Grigory Ustinov <grenka@altlinux.org> 0.9.9-alt1
- Automatically updated to 0.9.9.

* Mon Mar 14 2022 Grigory Ustinov <grenka@altlinux.org> 0.9.8-alt1
- Automatically updated to 0.9.8.

* Sat Feb 05 2022 Grigory Ustinov <grenka@altlinux.org> 0.9.7-alt1
- Automatically updated to 0.9.7.

* Tue Nov 23 2021 Grigory Ustinov <grenka@altlinux.org> 0.9.6-alt1
- Automatically updated to 0.9.6.

* Tue Sep 07 2021 Grigory Ustinov <grenka@altlinux.org> 0.9.4-alt1
- Automatically updated to 0.9.4.

* Thu Jan 14 2021 Grigory Ustinov <grenka@altlinux.org> 0.9.3-alt1
- Automatically updated to 0.9.3.

* Wed Sep 09 2020 Grigory Ustinov <grenka@altlinux.org> 0.9.2-alt1
- Initial build for Sisyphus.
