%define pypi_name pypng

%def_with check
%def_with numpy

Name:    python3-module-%pypi_name
Version: 0.20231004.0
Release: alt1

Summary: Pure Python library for PNG image encoding/decoding
License: MIT
Group:   Development/Python3
URL:     https://gitlab.com/drj11/pypng

Packager: Grigory Ustinov <grenka@altlinux.org>

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools python3-module-wheel

%if_with check
BuildRequires: python3-module-pytest
%if_with numpy
BuildRequires: python3-module-numpy
%endif
%endif

BuildArch: noarch

Source: %name-%version.tar

%description
%summary

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

# needs prix.py, that isn't installed
rm -f %buildroot%_bindir/priplan9topng

%check
%pyproject_run_pytest -k 'not test_test_dir'

%files
%doc LICENCE *.md
%_bindir/prichunkpng
%_bindir/pricolpng
%_bindir/priditherpng
%_bindir/priforgepng
%_bindir/prigreypng
%_bindir/pripalpng
%_bindir/pripamtopng
%_bindir/pripnglsch
%_bindir/pripngtopam
%_bindir/prirowpng
%_bindir/priweavepng
%python3_sitelibdir/png.py
%python3_sitelibdir/__pycache__
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}

%changelog
* Tue Oct 24 2023 Grigory Ustinov <grenka@altlinux.org> 0.20231004.0-alt1
- Automatically updated to 0.20231004.0.

* Mon Feb 13 2023 Grigory Ustinov <grenka@altlinux.org> 0.20220715.0-alt1
- Initial build for Sisyphus.
