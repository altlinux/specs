%define _unpackaged_files_terminate_build 1

%define oname prettytable

%def_disable check

Name: python3-module-%oname
Version: 2.1.0
Release: alt1
Summary: Python3 library for easily displaying tabular data in a visually appealing ASCII table format

Group: Development/Python3
License: BSD
Source: %name-%version.tar
Patch: %name-%version-%release.patch
Url: https://github.com/jazzband/prettytable
BuildArch: noarch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel
BuildRequires: python3-module-setuptools python3-module-setuptools_scm
%if_enabled check
BuildRequires: python3-module-pytest-cov python3-module-tox python3-module-wcwidth python3-module-coverage
%endif

%py3_provides %oname

%description
PrettyTable is a simple Python library designed to make it quick and
easy to represent tabular data in visually appealing ASCII tables. It
was inspired by the ASCII tables used in the PostgreSQL shell psql.
PrettyTable allows for selection of which columns are to be printed,
independent alignment of columns (left or right justified or centred)
and printing of "sub-tables" by specifying a row range.

%prep
%setup
%patch -p1

%build
export SETUPTOOLS_SCM_PRETEND_VERSION=%version
%python3_build

%install
export SETUPTOOLS_SCM_PRETEND_VERSION=%version
%python3_install

%check
export SETUPTOOLS_SCM_PRETEND_VERSION=%version
export PIP_NO_INDEX=YES
export TOXENV=py%{python_version_nodots python3}
#tox.py3 --sitepackages -r -vv
tox.py3 -e py%{python_version_nodots python3} -v

%files
%doc README.md COPYING CHANGELOG.md
%python3_sitelibdir/*

%changelog
* Wed Apr 07 2021 Alexey Shabalin <shaba@altlinux.org> 2.1.0-alt1
- 2.1.0

* Fri May 25 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 0.10-alt2.g4676e41
- NMU: packaged egg-info files.

* Mon May 14 2018 L.A. Kostis <lakostis@altlinux.ru> 0.10-alt1.g4676e41
- GIT 4676e41.
- Added boxchar changes from https://github.com/platomav/PTable (need MCExtractor to work).
- Disable tests (as they rely on coverage %% rather than exit code).

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.7.2-alt2.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Sat Feb 07 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.7.2-alt2
- Added provides: prettytable

* Sat Feb 07 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.7.2-alt1
- Version 0.7.2
- Added module for Python 3

* Mon Sep 17 2012 Pavel Shilovsky <piastry@altlinux.org> 0.6.1-alt1
- Initial release for Sisyphus (based on Fedora)
