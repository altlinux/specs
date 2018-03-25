%define _unpackaged_files_terminate_build 1
%define oname pytest-virtualenv

%def_with check

Name: python-module-%oname
Version: 1.3.0
Release: alt1%ubt

Summary: Virtualenv fixture for py.test
License: MIT
Group: Development/Python
# Source-git: https://github.com/manahl/pytest-plugins.git
Url: https://pypi.python.org/pypi/pytest-virtualenv

Source: %oname-%version.tar

BuildRequires(pre): rpm-build-ubt
BuildRequires(pre): rpm-build-python3
BuildRequires: python-module-setuptools
BuildRequires: python3-module-setuptools

%if_with check
BuildRequires: python-module-pytest
BuildRequires: python-module-pytest-shutil
BuildRequires: python-module-pytest-fixture-config
BuildRequires: python-module-mock
BuildRequires: python-module-path
BuildRequires: python-module-contextlib2
BuildRequires: python-module-virtualenv
BuildRequires: python3-module-pytest
BuildRequires: python3-module-pytest-shutil
BuildRequires: python3-module-pytest-fixture-config
BuildRequires: python3-module-mock
BuildRequires: python3-module-path
BuildRequires: python3-module-contextlib2
BuildRequires: python3-module-virtualenv
%endif

BuildArch: noarch

%description
Create a Python virtual environment in your test that cleans up on teardown.
The fixture has utility methods to install packages and list what's installed.

%package -n python3-module-%oname
Summary: Virtualenv fixture for py.test
Group: Development/Python3

%description -n python3-module-%oname
Create a Python virtual environment in your test that cleans up on teardown.
The fixture has utility methods to install packages and list what's installed.

%prep
%setup -n %oname-%version

# fix dependency
sed -i -e 's:setuptools-git:setuptools:g' \
	common_setup.py
cp -fR . ../python3
# change the DEFAULT_VIRTUALENV_FIXTURE_EXECUTABLE to ALT virtualenv executable
# otherwise python3 pytest-virtualenv uses python2 virtualenv executable
sed -i '/DEFAULT_VIRTUALENV_FIXTURE_EXECUTABLE = (cmdline.which(\x27virtualenv\x27) + \[\x27virtualenv\x27\])\[0\]/{s//DEFAULT_VIRTUALENV_FIXTURE_EXECUTABLE = (cmdline.which(\x27virtualenv3\x27) + \[\x27virtualenv3\x27\])\[0\]/;h};${x;/./{x;q0};x;q1}' \
	../python3/pytest_virtualenv.py

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
%doc LICENSE *.md
%python_sitelibdir/*

%files -n python3-module-%oname
%doc LICENSE *.md
%python3_sitelibdir/*

%changelog
* Sun Mar 25 2018 Stanislav Levin <slev@altlinux.org> 1.3.0-alt1%ubt
- 1.2.11 -> 1.3.0
- Change Python3 DEFAULT_VIRTUALENV_FIXTURE_EXECUTABLE to ALT specific

* Tue Oct 10 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 1.2.11-alt1%ubt
- Initial build for ALT.
