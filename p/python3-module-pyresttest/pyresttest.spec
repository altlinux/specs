%define oname pyresttest

%def_with check

Name: python3-module-%oname
Version: 1.7.1
Release: alt3

Summary: Python RESTful API Testing & Microbenchmarking Tool
License: ASLv2.0
Group: Development/Python3
Url: https://pypi.python.org/pypi/pyresttest/
VCS: https://github.com/svanoort/pyresttest.git

Source: %name-%version.tar
Patch: use-system-six-alt-fix.patch

BuildArch: noarch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-wheel
%if_with check
BuildRequires: python3-module-pyaml
BuildRequires: python3-module-pycurl
BuildRequires: python3-module-future
BuildRequires: python3-module-six
%endif

Requires: python3-module-future

%py3_provides %oname

%description
* A simple but powerful REST testing and benchmarking framework
* Minimal dependencies, designed to slot into automated configuration
  management/orchestration tools
* Tests are defined in basic YAML or JSON config files, no code needed
* Logic is written and extensible in Python

%prep
%setup
%patch -p1

sed -i 's|#!/usr/bin/env python|#!/usr/bin/env python3|' \
    $(find ./ -name '*.py')

%build
%pyproject_build

%install
%pyproject_install

%check
export PYTHONPATH=%buildroot%python3_sitelibdir
%__python3 -m unittest discover -v

%files
%doc *.md
%_bindir/*
%python3_sitelibdir/%oname
%python3_sitelibdir/%oname-%version.dist-info


%changelog
* Thu Jan 25 2024 Anton Vyatkin <toni@altlinux.org> 1.7.1-alt3
- Fixed FTBFS.

* Thu Aug 17 2023 Daniel Zagaynov <kotopesutility@altlinux.org> 1.7.1-alt2.1
- NMU: ignored unmet dependency.

* Mon Feb 27 2023 Anton Vyatkin <toni@altlinux.org> 1.7.1-alt2
- Fix BuildRequires.

* Thu Nov 07 2019 Andrey Bychkov <mrdrew@altlinux.org> 1.7.1-alt1
- Version updated to 1.7.1
- disable python2

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 1.3.1-alt1.git20150213.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Fri Mar 06 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.3.1-alt1.git20150213
- Version 1.3.1

* Thu Jan 01 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2.1-alt1.git20141231
- Version 1.2.1

* Tue Dec 30 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1.1-alt1.git20141228
- Version 1.1.1

* Wed Nov 26 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.2-alt1.git20141125
- Initial build for Sisyphus

