%define _unpackaged_files_terminate_build 1

Name: python3-module-pydicom
Version: 2.1.2
Release: alt1
Summary: Read, modify and write DICOM files with python code
License: BSD-3-Clause and MIT
Group: Sciences/Medicine
Url: https://pydicom.github.io/pydicom/dev

BuildArch: noarch

# https://github.com/pydicom/pydicom.git
Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel

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
%python3_build

%install
%python3_install

%files
%doc LICENSE
%doc README.md CONTRIBUTING.md
%doc examples
%python3_sitelibdir/dicom.py
%python3_sitelibdir/__pycache__/*
%python3_sitelibdir/pydicom
%exclude %python3_sitelibdir/pydicom/tests
%python3_sitelibdir/pydicom-%version-py*.egg-info

%files tests
%python3_sitelibdir/pydicom/tests

%changelog
* Mon May 31 2021 Aleksei Nikiforov <darktemplar@altlinux.org> 2.1.2-alt1
- Initial build for ALT.
