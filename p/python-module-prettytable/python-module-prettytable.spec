%define _unpackaged_files_terminate_build 1

%define oname prettytable
%define git 4676e41

%def_with python3
%def_disable tests

Name:		python-module-%oname
Version:	0.10
Release:	alt2.g%git
Summary:	Python library to display tabular data in tables

Group:		Development/Python
License:	BSD
Source0:	%{name}-%{version}.tar.gz
# boxchar changes from https://github.com/platomav/PTable
Patch1:         0001-add-line-drawing-mode.patch
Patch2:         0002-Fix-hrules-ALL-Line-Drawing-Mode.patch
Patch3:         0003-Fix-vrules-ALL-w-o-Header-Line-Drawing-Mode.patch
Patch4:         0004-Fix-Line-Drawing-Mode-w-o-Title-Header.patch
Patch5:         alt-encoding.patch

URL:		http://pypi.python.org/pypi/PrettyTable

BuildArch:	noarch
BuildRequires:	python-devel
%if_enabled tests
BuildRequires:  python-module-nose python-module-coverage
%endif
BuildRequires:	python-module-setuptools
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires:	python3-devel
%if_enabled tests
BuildRequires:  python3-module-nose python3-module-coverage
%endif
BuildRequires:	python3-module-setuptools
%endif

%py_provides %oname

%description
PrettyTable is a simple Python library designed to make it quick and
easy to represent tabular data in visually appealing ASCII tables. It
was inspired by the ASCII tables used in the PostgreSQL shell psql.
PrettyTable allows for selection of which columns are to be printed,
independent alignment of columns (left or right justified or centred)
and printing of "sub-tables" by specifying a row range.

%package -n python3-module-%oname
Summary:	Python library to display tabular data in tables
Group:		Development/Python3
%py3_provides %oname

%description -n python3-module-%oname
PrettyTable is a simple Python library designed to make it quick and
easy to represent tabular data in visually appealing ASCII tables. It
was inspired by the ASCII tables used in the PostgreSQL shell psql.
PrettyTable allows for selection of which columns are to be printed,
independent alignment of columns (left or right justified or centred)
and printing of "sub-tables" by specifying a row range.

%prep
%setup
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p2

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

%if_enabled tests
%check
export LC_ALL=en_US.UTF-8
make test
%if_with python3
pushd ../python3
make test
popd
%endif
%endif #tests

%install
%python_install

%if_with python3
pushd ../python3
%python3_install
popd
%endif
rm -rf %buildroot%_bindir

%files
%doc README.rst COPYING CHANGELOG.md
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc README.rst COPYING CHANGELOG.md
%python3_sitelibdir/*
%endif

%changelog
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
- Added provides: %oname

* Sat Feb 07 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.7.2-alt1
- Version 0.7.2
- Added module for Python 3

* Mon Sep 17 2012 Pavel Shilovsky <piastry@altlinux.org> 0.6.1-alt1
- Initial release for Sisyphus (based on Fedora)
