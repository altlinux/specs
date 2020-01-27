%define mname pyannote
%define oname %mname.core

Name: python3-module-%oname
Version: 3.5
Release: alt1

Summary: PyAnnote core
License: MIT
Group: Development/Python3
Url: https://pypi.python.org/pypi/pyannote.core/

# https://github.com/pyannote/pyannote-core.git
Source: %name-%version.tar
Patch0: fix-detect-version.patch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-typing_extensions
BuildRequires: python3-module-numpy python3-module-pandas
BuildRequires: python3-module-sortedcontainers
BuildRequires: python3-module-simplejson git

%py3_provides %mname
%py3_provides %mname.core


%description
PyAnnote is a Python module for collaborative annotation of multimodal
documents.

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

install -p -m644 %mname/__init__.py \
	%buildroot%python3_sitelibdir/%mname/

%check
%if 0
%__python3 setup.py test
%endif

%files
%doc *.md doc
%python3_sitelibdir/%mname
%python3_sitelibdir/*.egg-info


%changelog
* Mon Jan 27 2020 Andrey Bychkov <mrdrew@altlinux.org> 3.5-alt1
- Version updated to 3.5
- porting on python3.

* Wed Jun 12 2019 Stanislav Levin <slev@altlinux.org> 0.3.4-alt1.git20150304.1.1.1
- Added missing dep on `numpy.testing`.

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.3.4-alt1.git20150304.1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Tue May 24 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.3.4-alt1.git20150304.1
- (AUTO) subst_x86_64.

* Thu Mar 05 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3.4-alt1.git20150304
- Version 0.3.4

* Fri Nov 21 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2.5-alt1.git20141121
- Version 0.2.5

* Tue Nov 18 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2.4-alt1.git20141118
- Version 0.2.4

* Sun Nov 16 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2.3-alt1.git20141114
- Version 0.2.3

* Thu Nov 13 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2.2-alt1.git20141112
- Initial build for Sisyphus

