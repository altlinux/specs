%define oname yams

%def_with check

Name: python3-module-%oname
Version: 0.51.0
Release: alt1

Summary: Entity / relation schema
License: LGPL-2.1
Group: Development/Python3
Url: https://pypi.org/project/yams

Source: %name-%version.tar

BuildArch: noarch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-wheel
%if_with check
BuildRequires: python3-module-logilab-common
BuildRequires: python3-module-dateutil
BuildRequires: python3-module-importlib-metadata
BuildRequires: python3-module-pytest
%endif

%py_provides %oname

%description
Yet Another Magic Schema ! A simple/generic but powerful entities /
relations schema, suitable to represent RDF like data. The schema is
readable/writable from/to various formats.

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest -v

%files
%doc README.rst COPYING
%_bindir/*
%python3_sitelibdir/%oname
%python3_sitelibdir/%{pyproject_distinfo %oname}


%changelog
* Tue Nov 28 2023 Anton Vyatkin <toni@altlinux.org> 0.51.0-alt1
- new version 0.51.0

* Mon Aug 07 2023 Anton Vyatkin <toni@altlinux.org> 0.50.2-alt1
- new version 0.50.2

* Fri Aug 04 2023 Anton Vyatkin <toni@altlinux.org> 0.50.1-alt1
- new version 0.50.1

* Wed Jul 19 2023 Anton Vyatkin <toni@altlinux.org> 0.50.0-alt1
- new version 0.50.0

* Wed Mar 22 2023 Anton Vyatkin <toni@altlinux.org> 0.49.3-alt1
- new version 0.49.3

* Wed Mar 08 2023 Anton Vyatkin <toni@altlinux.org> 0.49.1-alt1
- new version 0.49.1

* Tue Oct 29 2019 Andrey Bychkov <mrdrew@altlinux.org> 0.45.1-alt2
- python2 -> python3

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.45.1-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Mon Oct 16 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 0.45.1-alt1
- Updated to upstream version 0.45.1.

* Tue Dec 23 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.40.2-alt1
- Version 0.40.2

* Wed Nov 05 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.40.0-alt1
- Version 0.40.0

* Wed Nov 05 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.39.1-alt1
- Initial build for Sisyphus

