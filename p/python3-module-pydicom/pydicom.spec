%def_without check

Name: python3-module-pydicom
Version: 2.4.4
Release: alt1

Summary: Read, modify and write DICOM files with python code

License: BSD-3-Clause and MIT
Group: Sciences/Medicine
URL: https://pypi.org/project/pydicom
VCS: https://github.com/pydicom/pydicom

BuildArch: noarch

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-flit

%if_with check
BuildRequires: python3-module-pytest
%endif

%description
pydicom is a pure Python package for working with DICOM files.
It lets you read, modify and write DICOM data in an easy "pythonic" way.

As a pure Python package, pydicom can run anywhere Python runs
without any other requirements, although if you're working
with Pixel Data then we recommend you also install NumPy.

If you're looking for a Python library for DICOM networking
then you might be interested in another of our projects: pynetdicom.

%package tests
Summary: Read, modify and write DICOM files with python code
Group: Development/Python3
Requires: %name = %EVR

%description tests
pydicom is a pure Python package for working with DICOM files.
It lets you read, modify and write DICOM data in an easy "pythonic" way.

As a pure Python package, pydicom can run anywhere Python runs
without any other requirements, although if you're working
with Pixel Data then we recommend you also install NumPy.

If you're looking for a Python library for DICOM networking
then you might be interested in another of our projects: pynetdicom.

This package contains tests for pydicom.

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest

%files
%doc LICENSE README.md CONTRIBUTING.md examples
%_bindir/pydicom
%python3_sitelibdir/pydicom
%python3_sitelibdir/pydicom-%version.dist-info
%exclude %python3_sitelibdir/pydicom/tests

%files tests
%python3_sitelibdir/pydicom/tests

%changelog
* Sun May 19 2024 Grigory Ustinov <grenka@altlinux.org> 2.4.4-alt1
- Automatically updated to 2.4.4.

* Mon May 31 2021 Aleksei Nikiforov <darktemplar@altlinux.org> 2.1.2-alt1
- Initial build for ALT.
