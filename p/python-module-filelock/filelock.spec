%define _unpackaged_files_terminate_build 1
%define oname filelock

%def_with check

Name: python-module-%oname
Version: 3.0.10
Release: alt1

Summary: A platform independent file lock for Python
License: Unlicense
Group: Development/Python
# Source-git: https://github.com/benediktschmitt/py-filelock.git
Url: https://pypi.python.org/pypi/filelock

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3

%if_with check
BuildRequires: pytest
BuildRequires: pytest3
%endif

BuildArch: noarch

%description
This package contains a single module, which implements a platform independent
file locking mechanism for Python.

The lock includes a lock counter and is thread safe. This means, when locking
the same lock object twice, it will not block.

%package -n python3-module-%oname
Summary: A platform independent file lock for Python3
Group: Development/Python3

%description -n python3-module-%oname
This package contains a single module, which implements a platform independent
file locking mechanism for Python3.

The lock includes a lock counter and is thread safe. This means, when locking
the same lock object twice, it will not block.

%prep
%setup
rm -rf ../python3
cp -a . ../python3

%build
%python_build

pushd ../python3
%python3_build
popd

%install
%python_install

pushd ../python3
%python3_install
popd

%check
pytest -xvv test.py

pushd ../python3
pytest3 -xvv test.py
popd

%files
%doc LICENSE.rst README.rst
%python_sitelibdir/filelock.py*
%python_sitelibdir/filelock-*.egg-info/

%files -n python3-module-%oname
%doc LICENSE.rst README.rst
%python3_sitelibdir/filelock.py
%python3_sitelibdir/__pycache__/filelock.*.py*
%python3_sitelibdir/filelock-*.egg-info/

%changelog
* Mon Jan 14 2019 Stanislav Levin <slev@altlinux.org> 3.0.10-alt1
- 3.0.9 -> 3.0.10.

* Wed Oct 10 2018 Stanislav Levin <slev@altlinux.org> 3.0.9-alt1
- Initial build.

