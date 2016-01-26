%define mname pyannote
%define oname %mname.server
%def_disable check

Name: python-module-%oname
Version: 0.7
Release: alt2.git20141031
Summary: PyAnnote REST API
License: MIT
Group: Development/Python
Url: https://pypi.python.org/pypi/pyannote.server/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/pyannote/pyannote-server.git
Source: %name-%version.tar
BuildRequires: python-module-notebook python-module-pyannote.metrics

#BuildPreReq: python-module-setuptools-tests python-module-%mname.parser
#BuildPreReq: python-module-%mname.metrics python-module-flask
#BuildPreReq: python-module-flask-cors

%py_provides %oname
#%py_requires %mname.metrics %mname.parser flask_cors

%description
PyAnnote is a Python module for collaborative annotation of multimodal
documents.

This package provides REST API on top of PyAnnote.

%prep
%setup

sed -i 's|@VERSION@|%version|' %mname/server/_version.py

%build
%python_build_debug

%install
%python_install

%ifarch x86_64
mv %buildroot%_libexecdir %buildroot%_libdir
%endif

%check
python setup.py test

%files
%doc *.md demo
%python_sitelibdir/%mname/server
%python_sitelibdir/*.egg-info

%changelog
* Tue Jan 26 2016 Sergey Alembekov <rt@altlinux.ru> 0.7-alt2.git20141031
- Rebuild with "def_disable check"
- Cleanup buildreq

* Wed Nov 19 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.7-alt1.git20141031
- Initial build for Sisyphus

