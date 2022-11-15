%define mname pyannote
%define oname %mname.parser

Name: python3-module-%oname
Version: 0.8
Release: alt1.1

Summary: PyAnnote parsers
License: MIT
Group: Development/Python3
Url: https://pypi.python.org/pypi/pyannote.parser/

# https://github.com/pyannote/pyannote-parser.git
Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-six python3-module-%mname.core

%py3_provides %oname
%py3_requires %mname

%add_python3_self_prov_path %buildroot%python3_sitelibdir/%mname/parser/base.py

%description
PyAnnote is a Python module for collaborative annotation of multimodal
documents.

This package provides annotation file parsers.

%prep
%setup

%build
%python3_build_debug

%install
%python3_install

%if "%_libexecdir" != "%_libdir"
mv %buildroot%_libexecdir %buildroot%_libdir
%endif

%check
%if 0
%__python3 setup.py test
%endif

%files
%doc *.md
%python3_sitelibdir/%mname/*
%python3_sitelibdir/*.egg-info


%changelog
* Sun Nov 13 2022 Daniel Zagaynov <kotopesutility@altlinux.org> 0.8-alt1.1
- NMU: used %%add_python3_self_prov_path macro to skip self-provides from dependencies.

* Mon Jan 27 2020 Andrey Bychkov <mrdrew@altlinux.org> 0.8-alt1
- Version updated to 0.8
- porting on python3.

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.3-alt1.git20141209.1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Tue May 24 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.3-alt1.git20141209.1
- (AUTO) subst_x86_64.

* Wed Dec 10 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3-alt1.git20141209
- Version 0.3

* Tue Nov 18 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2.4-alt1.git20141117
- Version 0.2.4

* Sun Nov 16 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2.3-alt1.git20141114
- Version 0.2.3

* Fri Nov 14 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2.2-alt1.git20141113
- Initial build for Sisyphus

