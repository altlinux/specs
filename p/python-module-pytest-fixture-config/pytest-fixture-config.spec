%define oname pytest-fixture-config

%def_with python3

Name: python-module-%oname
Version: 1.2.11
Release: alt1%ubt
Summary: Fixture configuration utils for py.test
License: MIT
Group: Development/Python
Url: https://pypi.python.org/pypi/pytest-fixture-config
BuildArch: noarch

Source: %oname-%version.tar

BuildRequires(pre): rpm-build-ubt
BuildRequires: python-dev python-module-pytest python2.7(six)
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-dev python3-module-pytest python3(six)
%endif

%description
Simple configuration objects for Py.test fixtures.
Allows you to skip tests when their required config variables aren't set.

%package -n python3-module-%oname
Summary: Fixture configuration utils for py.test
Group: Development/Python3
%py3_provides %oname

%description -n python3-module-%oname
Simple configuration objects for Py.test fixtures.
Allows you to skip tests when their required config variables aren't set.

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
