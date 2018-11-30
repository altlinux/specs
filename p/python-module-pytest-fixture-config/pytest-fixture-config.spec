%define _unpackaged_files_terminate_build 1
%define oname pytest-fixture-config

Name: python-module-%oname
Version: 1.3.0
Release: alt1
Summary: Fixture configuration utils for py.test
License: MIT
Group: Development/Python
Url: https://pypi.python.org/pypi/pytest-fixture-config
BuildArch: noarch

Source: %oname-%version.tar

BuildRequires: python-dev python-module-pytest python2.7(six)
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-dev python3-module-pytest python3(six)

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

cp -fR . ../python3

%build
%python_build

pushd ../python3
%python3_build
popd

%install
pushd ../python3
%python3_install
popd

%python_install

%check
PYTHONPATH=$(pwd) py.test -v
pushd ../python3
PYTHONPATH=$(pwd) py.test3 -v
popd

%files
%doc CHANGES.md README.md
%python_sitelibdir/pytest_fixture_config-*.egg-info/
%python_sitelibdir/pytest_fixture_config.py*

%files -n python3-module-%oname
%doc CHANGES.md README.md
%python3_sitelibdir/__pycache__/pytest_fixture_config.*.py*
%python3_sitelibdir/pytest_fixture_config-*.egg-info/
%python3_sitelibdir/pytest_fixture_config.py

%changelog
* Fri Nov 30 2018 Stanislav Levin <slev@altlinux.org> 1.3.0-alt1
- 1.2.11 -> 1.3.0.
- Fixed build.

* Tue Oct 10 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 1.2.11-alt1
- Initial build for ALT.
