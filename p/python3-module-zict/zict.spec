%define  oname zict

%def_with check

Name:    python3-module-%oname
Version: 3.0.0
Release: alt1

Summary: Mutable mapping tools

License: BSD-3-Clause
Group:   Development/Python3
URL:     https://pypi.org/project/zict

Packager: Grigory Ustinov <grenka@altlinux.org>

BuildRequires(pre): rpm-build-python3

%if_with check
BuildRequires: python3-module-pytest
BuildRequires: python3-module-HeapDict
BuildRequires: python3-module-lmdb
BuildRequires: python3-module-pytest-timeout
BuildRequires: python3-module-pytest-asyncio
BuildRequires: python3-module-pytest-repeat
%endif

BuildArch: noarch

Source:  %name-%version.tar

%description
Zict builds abstract MutableMapping classes that consume and build on other
MutableMappings. They can be composed with each other to form intuitive
interfaces over complex storage systems policies.

Data can be stored in-memory, on disk, in archive files, etc., managed with
different policies like LRU, and transformed when arriving or departing the
dictionary

%prep
%setup

%build
%python3_build

%install
%python3_install

%check
export PYTHONPATH=$PWD
py.test-3 -ra

%files
%doc *.md
%python3_sitelibdir/%oname
%python3_sitelibdir/%oname-%version-py%_python3_version.egg-info

%changelog
* Mon Apr 24 2023 Grigory Ustinov <grenka@altlinux.org> 3.0.0-alt1
- Automatically updated to 3.0.0.

* Thu Jul 21 2022 Grigory Ustinov <grenka@altlinux.org> 2.2.0-alt1
- Initial build for Sisyphus.
