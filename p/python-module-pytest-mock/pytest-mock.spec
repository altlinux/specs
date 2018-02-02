%define oname pytest-mock

%def_with python3

Name: python-module-%oname
Version: 1.6.2
Release: alt1.1
Summary: Thin-wrapper around the mock package for easier use with py.test
License: MIT
Group: Development/Python
Url: https://pypi.python.org/pypi/pytest-mock
BuildArch: noarch

# https://github.com/pytest-dev/pytest-mock.git
Source: %name-%version.tar.gz

BuildRequires(pre): rpm-build-python
BuildRequires: git-core
BuildRequires: python-module-setuptools python-module-setuptools_scm
BuildRequires: python-module-mock
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools python3-module-setuptools_scm
BuildRequires: python3-module-mock
%endif

%description
Thin-wrapper around the mock package for easier use with py.test

This plugin installs a mocker fixture which is a thin-wrapper around the
patching API provided by the mock package, but with the benefit of not having
to worry about undoing patches at the end of a test

%package -n python3-module-%oname
Summary: Thin-wrapper around the mock package for easier use with py.test
Group: Development/Python3

%description -n python3-module-%oname
Thin-wrapper around the mock package for easier use with py.test

This plugin installs a mocker fixture which is a thin-wrapper around the
patching API provided by the mock package, but with the benefit of not having
to worry about undoing patches at the end of a test

%prep
%setup

# setup version info
git config --global user.email "darktemplar at altlinux.org"
git config --global user.name "darktemplar"
git init-db
git add . -A
git commit -a -m "%version"
git tag %version -m "%version"

%if_with python3
cp -a . ../python3
%endif

%build
%python_build

%if_with python3
pushd ../python3
%python3_build
popd
%endif

%install
%if_with python3
pushd ../python3
%python3_install
popd
%endif

%python_install

%check
PYTHONPATH=$(pwd) py.test ||:

%if_with python3
pushd ../python3
PYTHONPATH=$(pwd) py.test3 ||:
popd
%endif

%files
%doc LICENSE *.rst
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc LICENSE *.rst
%python3_sitelibdir/*
%endif

%changelog
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 1.6.2-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Mon Aug 14 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 1.6.2-alt1
- Updated to upstream version 1.6.2.

* Sat Jan 21 2017 Anton Midyukov <antohami@altlinux.org> 1.5.0-alt1
- Initial build for ALT Linux Sisyphus.
