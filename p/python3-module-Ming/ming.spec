%define oname Ming

%def_without check

Name: python3-module-%oname
Version: 0.17.1
Release: alt1

Summary: Bringing order to Mongo since 2009
License: MIT
Group: Development/Python3
Url: https://pypi.org/project/Ming/
Vcs: https://github.com/TurboGears/Ming

Source: %name-%version.tar

BuildArch: noarch
# mapping from PyPI name
# https://www.altlinux.org/Management_of_Python_dependencies_sources#Mapping_project_names_to_distro_names
Provides: python3-module-%{pep503_name %oname} = %EVR

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-wheel
%if_with check
BuildRequires: python3-module-pymongo
BuildRequires: python3-module-pytz
%endif

%description
Database mapping layer for MongoDB on Python. Includes schema
enforcement and some facilities for schema migration.

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_unittest

%files
%doc *.rst *.txt
%python3_sitelibdir/ming
%python3_sitelibdir/%{pyproject_distinfo %oname}/

%changelog
* Sat Jun 27 2026 Anton Vyatkin <toni@altlinux.org> 0.17.1-alt1
- New version 0.17.1.

* Tue Apr 14 2026 Anton Vyatkin <toni@altlinux.org> 0.17.0-alt1
- New version 0.17.0.

* Tue Sep 09 2025 Anton Vyatkin <toni@altlinux.org> 0.16.0-alt1
- New version 0.16.0.

* Wed Apr 02 2025 Stanislav Levin <slev@altlinux.org> 0.15.2-alt1.1
- NMU: fixed FTBFS (setuptools 75.8.1)

* Sat Dec 21 2024 Anton Vyatkin <toni@altlinux.org> 0.15.2-alt1
- New version 0.15.2.

* Thu Dec 12 2024 Anton Vyatkin <toni@altlinux.org> 0.15.1-alt1
- New version 0.15.1.

* Tue Feb 27 2024 Stanislav Levin <slev@altlinux.org> 0.13.0-alt1.1
- NMU: mapped PyPI name to distro's one.

* Mon Apr 24 2023 Anton Vyatkin <toni@altlinux.org> 0.13.0-alt1
- New version 0.13.0.

* Fri Dec 06 2019 Andrey Bychkov <mrdrew@altlinux.org> 0.5.0-alt3
- build for python2 disabled

* Wed May 16 2018 Andrey Bychkov <mrdrew@altlinux.org> 0.5.0-alt2.2
- (NMU) rebuild with python3.6

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.5.0-alt2.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Tue Jul 22 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.5.0-alt2
- Added module for Python 3

* Mon Jul 14 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.5.0-alt1
- Version 0.5.0

* Fri Nov 29 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4.2-alt1
- Version 0.4.2

* Mon Sep 16 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4.1-alt1
- Version 0.4.1

* Tue Feb 12 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3.2-alt1.dev.20121219
- Version 0.3.2dev-20121219

* Wed Sep 26 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3.2-alt1.dev.20120912
- Initial build for Sisyphus

