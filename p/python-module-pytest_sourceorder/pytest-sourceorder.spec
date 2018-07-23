%define _unpackaged_files_terminate_build 1

%define mname pytest_sourceorder
%def_with check

Name: python-module-%mname
Version: 0.5.1
Release: alt1

Summary: A pytest plugin for ensuring tests within a class are run in source order
License: %gpl3plus
Group: Development/Python
# Source-git: https://github.com/encukou/pytest-sourceorder
Url: https://pypi.org/project/pytest-sourceorder

Source: %name-%version.tar

BuildRequires(pre): rpm-build-licenses
BuildRequires(pre): rpm-build-python3

BuildArch: noarch

BuildRequires: python-module-setuptools
BuildRequires: python3-module-setuptools

%if_with check
BuildRequires: python-module-pytest
BuildRequires: python3-module-pytest
%endif

%description
Allows tests within a specially marked class to be run in source order,
instead of the "almost alphabetical" order Pytest normally uses.

%package -n python3-module-%mname
Summary: A pytest plugin for ensuring tests within a class are run in source order
Group: Development/Python3

%description -n python3-module-%mname
Allows tests within a specially marked class to be run in source order,
instead of the "almost alphabetical" order Pytest normally uses.
This is a Python3 module.

%prep
%setup

cp -a . ../python3

%build
%python_build

pushd ../python3
%python3_build
popd

%check
python -m pytest -v

pushd ../python3
python3 -m pytest -v
popd

%install
%python_install

pushd ../python3
%python3_install
popd

%files
%doc README.rst COPYING
%python_sitelibdir/%mname-*.egg-info
%python_sitelibdir/%mname.py*

%files -n python3-module-%mname
%doc README.rst COPYING
%python3_sitelibdir/%mname-*.egg-info
%python3_sitelibdir/%mname.py
%python3_sitelibdir/__pycache__/%mname.*.py*

%changelog
* Mon Jul 23 2018 Stanislav Levin <slev@altlinux.org> 0.5.1-alt1
- 0.4 -> 0.5.1
- Build package for Python3

* Tue Dec 29 2015 Mikhail Efremov <sem@altlinux.org> 0.4-alt1
- Initial build.

