%define _unpackaged_files_terminate_build 1
%define mname configparser

%def_with check

Name: python-module-%mname
Version: 3.5.0
Release: alt4%ubt
Summary: This library brings the updated configparser from Python 3.5 to Python 2.6-3.5

Group: Development/Python
License: MIT
# Source: https://bitbucket.org/ambv/configparser
Url: https://pypi.python.org/pypi/configparser

Source: %name-%version.tar

BuildRequires(pre): rpm-build-ubt
BuildRequires(pre): rpm-build-python
BuildRequires(pre): rpm-build-python3

BuildRequires: python-module-setuptools
BuildRequires: python3-module-setuptools

%if_with check
BuildRequires: python-test
BuildRequires: python3-test
BuildRequires: python-module-tox
BuildRequires: python-module-virtualenv
BuildRequires: python3-module-tox
BuildRequires: python3-module-virtualenv
%endif

%py_provides %mname

%description
The ancient ConfigParser module available in the standard library 2.x has seen a
major update in Python 3.2. This is a backport of those changes so that they can
be used directly in Python 2.6 - 3.5.

%package -n python3-module-%mname
Summary: This library brings the updated configparser from Python 3.5 to Python 2.6-3.5
Group: Development/Python3
%py3_provides %mname

%description -n python3-module-%mname
The ancient ConfigParser module available in the standard library 2.x has seen a
major update in Python 3.2. This is a backport of those changes so that they can
be used directly in Python 2.6 - 3.5.

%prep
%setup
rm -rfv *.egg-info
rm -rfv ../python3
cp -a . ../python3

%build
%python_build_debug
pushd ../python3
%python3_build_debug
popd

%install
%python_install
pushd ../python3
%python3_install
popd

%if "%_libexecdir" != "%_libdir"
mv %buildroot%_libexecdir %buildroot%_libdir
%endif

%check
export PIP_INDEX_URL=http://host.invalid./
%define python_version_nodots() %(%1 -Esc "import sys; sys.stdout.write('{0.major}{0.minor}'.format(sys.version_info))")

tox --sitepackages -e py%{python_version_nodots python} -v

pushd ../python3
tox.py3 --sitepackages -e py%{python_version_nodots python3} -v
popd

%files
%python_sitelibdir/*

%files -n python3-module-%mname
%python3_sitelibdir/*

%changelog
* Mon Apr 02 2018 Stanislav Levin <slev@altlinux.org> 3.5.0-alt4%ubt
- Add python3-test to BuildRequires to fix tests

* Sat Mar 24 2018 Stanislav Levin <slev@altlinux.org> 3.5.0-alt3%ubt
- Rebuild with new setuptools to fix namespace package
- Enable tests

* Thu Oct 26 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 3.5.0-alt2%ubt
- Made package arch-specific for compatibility with python-2 backports setup.

* Wed Oct 25 2017 Stanislav Levin <slev@altlinux.org> 3.5.0-alt1%ubt
- Initial build

