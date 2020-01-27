%define mname pyannote
%define oname %mname.server

Name: python3-module-%oname
Version: 0.7
Release: alt3

Summary: PyAnnote REST API
License: MIT
Group: Development/Python3
Url: https://pypi.python.org/pypi/pyannote.server/

# https://github.com/pyannote/pyannote-server.git
Source: %name-%version.tar
Patch0: fix-import.patch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-flask python3-module-flask-cors
BuildRequires: python3-module-pyannote.core

%py3_provides %oname


%description
PyAnnote is a Python module for collaborative annotation of multimodal
documents.

This package provides REST API on top of PyAnnote.

%prep
%setup
%patch0 -p1

sed -i 's|@VERSION@|%version|' %mname/server/_version.py

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
%doc *.md demo
%python3_sitelibdir/%mname/server
%python3_sitelibdir/*.egg-info


%changelog
* Mon Jan 27 2020 Andrey Bychkov <mrdrew@altlinux.org> 0.7-alt3
- Porting on Python3.

* Tue May 24 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.7-alt2.git20141031.1
- (AUTO) subst_x86_64.

* Tue Jan 26 2016 Sergey Alembekov <rt@altlinux.ru> 0.7-alt2.git20141031
- Rebuild with "def_disable check"
- Cleanup buildreq

* Wed Nov 19 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.7-alt1.git20141031
- Initial build for Sisyphus

