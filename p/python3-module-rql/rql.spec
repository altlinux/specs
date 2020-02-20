%define _unpackaged_files_terminate_build 1

%define oname rql

Name: python3-module-%oname
Version: 0.36.0
Release: alt1

Summary: Relationship query language (RQL) utilities
License: LGPL
Group: Development/Python3
Url: https://pypi.python.org/pypi/rql/

Source0: %{oname}-%{version}.tar
Patch0: fix-import-of-pygments.patch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-logilab-common
BuildRequires: python3-module-logilab-database
BuildRequires: python3-module-Pygments
BuildRequires: python3-module-logilab-constraint

Requires: python3-module-logilab-constraint


%description
A library providing the base utilities to handle RQL queries, such as a
parser, a type inferencer.

%prep
%setup -q -n %oname-%version
%patch0 -p2

%build
%python3_build_debug

%install
%python3_install

%check
%__python3 setup.py test

%files
%doc README COPYING
%python3_sitelibdir/*


%changelog
* Thu Feb 20 2020 Andrey Bychkov <mrdrew@altlinux.org> 0.36.0-alt1
- Version updated to 0.36.0
- porting to python3.

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.34.1-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Wed Jan 11 2017 Igor Vlasenko <viy@altlinux.ru> 0.34.1-alt1
- automated PyPI update

* Wed Nov 05 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.33.0-alt1
- Initial build for Sisyphus

