%define _unpackaged_files_terminate_build 1
%define oname zipp

%def_without check

Name: python3-module-%oname
Version: 0.5.0
Release: alt2

Summary: A pathlib-compatible Zipfile object wrapper

License: MIT
Group: Development/Python3
Url: https://pypi.org/project/zipp/

BuildArch: noarch

# Source-url: %__pypi_url %oname
Source: %name-%version.tar

BuildRequires(pre): rpm-build-intro >= 2.2.5
BuildRequires(pre): rpm-build-python3

BuildRequires: python3(setuptools_scm)

%if_with check
BuildRequires: python3(contextlib2)
BuildRequires: python3(pytest)
BuildRequires: python3(unittest2)
%endif

%description
A pathlib-compatible Zipfile object wrapper.


%prep
%setup
# currently disable PEP517/518
rm -f pyproject.toml

%build
# SETUPTOOLS_SCM_PRETEND_VERSION: when defined and not empty,
# its used as the primary source for the version number in which
# case it will be a unparsed string
export SETUPTOOLS_SCM_PRETEND_VERSION=%version
%python3_build

%install
export SETUPTOOLS_SCM_PRETEND_VERSION=%version
%python3_install

%check
py.test3

%files
%doc LICENSE README.rst
%python3_sitelibdir/zipp.py
%python3_sitelibdir/__pycache__/zipp.cpython-*.py*
%python3_sitelibdir/zipp-*.egg-info/

%changelog
* Sun Apr 25 2021 Vitaly Lipatov <lav@altlinux.ru> 0.5.0-alt2
- NMU: build python3 module only, cleanup spec

* Tue May 14 2019 Stanislav Levin <slev@altlinux.org> 0.5.0-alt1
- 0.4.0 -> 0.5.0.

* Fri May 03 2019 Stanislav Levin <slev@altlinux.org> 0.4.0-alt1
- 0.3.3 -> 0.4.0.

* Mon Jan 28 2019 Stanislav Levin <slev@altlinux.org> 0.3.3-alt1
- Initial build.
