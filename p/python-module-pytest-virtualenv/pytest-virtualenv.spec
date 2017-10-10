%define oname pytest-virtualenv

%def_with python3

Name: python-module-%oname
Version: 1.2.11
Release: alt1%ubt
Summary: Virtualenv fixture for py.test
License: MIT
Group: Development/Python
Url: https://pypi.python.org/pypi/pytest-virtualenv
BuildArch: noarch

Source: %oname-%version.tar

BuildRequires(pre): rpm-build-ubt
BuildRequires: python-dev python-module-pytest python2.7(mock) python2.7(path) python2.7(pytest_shutil)
BuildRequires: python2.7(contextlib2) python2.7(pytest_fixture_config) python-module-virtualenv
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-dev python3-module-pytest python3(mock) python3(path) python3(pytest_shutil)
BuildRequires: python3(contextlib2) python3(pytest_fixture_config) python3-module-virtualenv
%endif

%description
Create a Python virtual environment in your test that cleans up on teardown.
The fixture has utility methods to install packages and list what's installed.

%package -n python3-module-%oname
Summary: Virtualenv fixture for py.test
Group: Development/Python3
%py3_provides %oname

%description -n python3-module-%oname
Create a Python virtual environment in your test that cleans up on teardown.
The fixture has utility methods to install packages and list what's installed.

%prep
%setup -n %oname-%version

# fix dependency
sed -i -e 's:setuptools-git:setuptools:g' \
	common_setup.py

%if_with python3
cp -fR . ../python3
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
PYTHONPATH=$(pwd) py.test -v
%if_with python3
pushd ../python3
PYTHONPATH=$(pwd) py.test3 -v
popd
%endif

%files
%doc CHANGES.md README.md
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc CHANGES.md README.md
%python3_sitelibdir/*
%endif

%changelog
* Tue Oct 10 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 1.2.11-alt1%ubt
- Initial build for ALT.
