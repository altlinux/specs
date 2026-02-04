%define _unpackaged_files_terminate_build 1
%define oname pytest-datafiles

Name: python3-module-%oname
Version: 3.0.1
Release: alt1

Summary: py.test plugin to create a 'tmpdir' containing predefined files/directories
License: MIT
Group: Development/Python3
Url: https://pypi.python.org/pypi/pytest-datafiles/
BuildArch: noarch
VCS: https://github.com/omarkohl/pytest-datafiles.git
Source0: %name-%version.tar
Source1: %pyproject_deps_config_name

BuildRequires(pre): rpm-build-pyproject
%pyproject_runtimedeps_metadata
%pyproject_builddeps_build

%description
py.test plugin to create a tmpdir containing a preconfigured set of
files and/or directories.

%prep
%setup
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest -v

%files
%doc README.md
%python3_sitelibdir/*

%changelog
* Wed Feb 04 2026 Anton Farygin <rider@altlinux.org> 3.0.1-alt1
- 1.0 -> 3.0.1

* Thu Nov 28 2019 Andrey Bychkov <mrdrew@altlinux.org> 1.0-alt2
- python2 disabled

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 1.0-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Wed Jan 11 2017 Igor Vlasenko <viy@altlinux.ru> 1.0-alt1
- automated PyPI update

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.1-alt1.dev0.git20150728.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Wed Jul 29 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1-alt1.dev0.git20150728
- Initial build for Sisyphus

