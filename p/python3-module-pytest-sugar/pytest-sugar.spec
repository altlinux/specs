%define _unpackaged_files_terminate_build 1
%define oname pytest-sugar

%def_with check

Name: python3-module-%oname
Version: 0.9.4
Release: alt1
Summary: Plugin for py.test that shows failures and errors instantly and shows a progress bar
License: BSD
Group: Development/Python3
BuildArch: noarch
Url: https://pypi.org/project/pytest-sugar/

# https://github.com/Frozenball/pytest-sugar.git
Source: %name-%version.tar
Patch0: %name-%version-alt.patch

BuildRequires(pre): rpm-build-python3

%if_with check
BuildRequires: python3-module-packaging >= 14.1
BuildRequires: python3-module-pytest >= 2.9
BuildRequires: python3-module-termcolor >= 1.1.0
BuildRequires: python3-module-pytest-xdist
BuildRequires: python3(tox)
%endif

%py3_provides pytest_sugar

%description
pytest-sugar is a plugin for py.test that changes the default look and
feel of py.test (e.g. progressbar, show tests that fail instantly).

%prep
%setup
%autopatch -p1

%build
%python3_build_debug

%install
%python3_install

%check
export PIP_NO_BUILD_ISOLATION=no
export PIP_NO_INDEX=YES
export TOXENV=py3
tox.py3 --sitepackages -vvr

%files
%doc *.rst
%python3_sitelibdir/*

%changelog
* Thu Oct 15 2020 Stanislav Levin <slev@altlinux.org> 0.9.4-alt1
- 0.9.2 -> 0.9.4.
- Stopped Python2 package build(Python2 EOL).

* Fri Dec 07 2018 Alexey Shabalin <shaba@altlinux.org> 0.9.2-alt1
- 0.9.2

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.3.5-alt1.git20141126.2.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Thu Nov 09 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 0.3.5-alt1.git20141126.2
- Fixed build.

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.3.5-alt1.git20141126.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Nov 27 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3.5-alt1.git20141126
- Initial build for Sisyphus

