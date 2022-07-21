%define  oname HeapDict

%def_with check

Name:    python3-module-%oname
Version: 1.0.1
Release: alt1

Summary: A heap with decrease-key and increase-key operations

License: BSD-3-Clause
Group:   Development/Python3
URL:     https://pypi.org/project/HeapDict

Packager: Grigory Ustinov <grenka@altlinux.org>

BuildRequires(pre): rpm-build-python3

%if_with check
BuildRequires: python3-test
BuildRequires: python3-module-pytest
%endif

BuildArch: noarch

Source:  %name-%version.tar

%description
HeapDict is designed to be used as a priority queue, where items are added and
consumed by priority. Compared to an ordinary dict, a heapdict has the
following differences: popitem and peekitem returns the (key, priority) pair
with the lowest priority, instead of a random object.

%prep
%setup

%build
%python3_build

%install
%python3_install

%check
py.test-3

%files
%doc *.rst
%python3_sitelibdir/heapdict.py
%python3_sitelibdir/__pycache__
%python3_sitelibdir/%oname-%version-py%_python3_version.egg-info

%changelog
* Thu Jul 21 2022 Grigory Ustinov <grenka@altlinux.org> 1.0.1-alt1
- Initial build for Sisyphus.
