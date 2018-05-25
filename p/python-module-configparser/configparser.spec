%define _unpackaged_files_terminate_build 1
%define mname configparser

%def_with check

Name: python-module-%mname
Version: 3.5.0
Release: alt5%ubt
Summary: This library brings the updated configparser from Python 3.5 to Python 2.6-3.5

Group: Development/Python
License: MIT
# Source: https://bitbucket.org/ambv/configparser
Url: https://pypi.python.org/pypi/configparser

Source: %name-%version.tar

BuildRequires(pre): rpm-build-ubt
BuildRequires(pre): rpm-build-python

BuildRequires: python-module-setuptools

%if_with check
BuildRequires: python-test
BuildRequires: python-module-tox
BuildRequires: python3-module-tox
%endif

%py_provides %mname

%description
The ancient ConfigParser module available in the standard library 2.x has seen a
major update in Python 3.2. This is a backport of those changes so that they can
be used directly in Python 2.6 - 3.5.

%prep
%setup
rm -rfv *.egg-info

%build
%python_build_debug

%install
%python_install

%if "%_libexecdir" != "%_libdir"
mv %buildroot%_libexecdir %buildroot%_libdir
%endif

%check
export PIP_INDEX_URL=http://host.invalid./

tox --sitepackages -e py%{python_version_nodots python} -v

%files
%python_sitelibdir/*

%changelog
* Fri May 25 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 3.5.0-alt5%ubt
- Rebuilt without python-3.

* Mon Apr 02 2018 Stanislav Levin <slev@altlinux.org> 3.5.0-alt4%ubt
- Add python3-test to BuildRequires to fix tests

* Sat Mar 24 2018 Stanislav Levin <slev@altlinux.org> 3.5.0-alt3%ubt
- Rebuild with new setuptools to fix namespace package
- Enable tests

* Thu Oct 26 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 3.5.0-alt2%ubt
- Made package arch-specific for compatibility with python-2 backports setup.

* Wed Oct 25 2017 Stanislav Levin <slev@altlinux.org> 3.5.0-alt1%ubt
- Initial build

