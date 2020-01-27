%define mname pyannote
%define oname %mname.metrics

Name: python3-module-%oname
Version: 2.2
Release: alt1

Summary: PyAnnote metrics
License: MIT
Group: Development/Python3
Url: https://pypi.python.org/pypi/pyannote.metrics/

# https://github.com/pyannote/pyannote-metrics.git
Source: %name-%version.tar
Patch0: fix-detect-version.patch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-notebook
BuildRequires: python3-module-scipy python3-module-pandas
BuildRequires: python3-module-scikit-learn
BuildRequires: python3-module-pyannote.core

Conflicts: python-module-%oname
%py3_provides %oname


%description
PyAnnote is a Python module for collaborative annotation of multimodal
documents.

This package provides evaluation metrics.

%prep
%setup
%patch0 -p1

touch version.py
echo '%version' >> version.py

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
%_bindir/*
%python3_sitelibdir/%mname/*
%python3_sitelibdir/*.egg-info


%changelog
* Mon Jan 27 2020 Andrey Bychkov <mrdrew@altlinux.org> 2.2-alt1
- Version updated to 2.2
- porting on python3.

* Tue May 24 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.4.1-alt3.git20141120.1
- (AUTO) subst_x86_64.

* Tue Jan 26 2016 Sergey Alembekov <rt@altlinux.ru> 0.4.1-alt3.git20141120
- Rebuild with "def_disable check"
- Cleanup buildreq

* Thu Mar 05 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4.1-alt2.git20141120
- Fixed build

* Fri Nov 21 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4.1-alt1.git20141120
- Version 0.4.1

* Sat Nov 15 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4-alt1.git20141031
- Initial build for Sisyphus

