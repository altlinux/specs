%define _unpackaged_files_terminate_build 1

%define oname rql

%def_with check

Name: python3-module-%oname
Version: 0.42.0
Release: alt1

Summary: Relationship query language (RQL) utilities
License: LGPL-2.1+
Group: Development/Python3
Url: https://pypi.org/project/rql

Source0: %{oname}-%{version}.tar

Requires: python3-module-logilab-constraint

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-wheel
%if_with check
BuildRequires: python3-module-pytest
BuildRequires: python3-module-logilab-common
BuildRequires: python3-module-logilab-database
BuildRequires: python3-module-logilab-constraint
%endif

%description
A library providing the base utilities to handle RQL queries, such as a
parser, a type inferencer.

%prep
%setup -q -n %oname-%version

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest -v

%files
%doc README.* COPYING
%python3_sitelibdir/%oname
%python3_sitelibdir/%oname-%version.dist-info


%changelog
* Thu Dec 28 2023 Anton Vyatkin <toni@altlinux.org> 0.42.0-alt1
- new version 0.42.0

* Thu Feb 20 2020 Andrey Bychkov <mrdrew@altlinux.org> 0.36.0-alt1
- Version updated to 0.36.0
- porting to python3.

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.34.1-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Wed Jan 11 2017 Igor Vlasenko <viy@altlinux.ru> 0.34.1-alt1
- automated PyPI update

* Wed Nov 05 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.33.0-alt1
- Initial build for Sisyphus

