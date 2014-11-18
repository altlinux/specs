%define mname pyannote
%define oname %mname.core
Name: python-module-%oname
Version: 0.2.4
Release: alt1.git20141118
Summary: PyAnnote core
License: MIT
Group: Development/Python
Url: https://pypi.python.org/pypi/pyannote.core/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/pyannote/pyannote-core.git
Source: %name-%version.tar

BuildPreReq: python-devel python-module-setuptools-tests
BuildPreReq: python-module-banyan python-module-numpy
BuildPreReq: python-module-pandas-tests python-module-networkx
BuildPreReq: python-module-simplejson python-module-matplotlib
BuildPreReq: python-module-pygraphviz ipython git
BuildPreReq: python-module-pytz

%py_provides %mname
%py_provides %mname.core
%py_requires pandas.util.testing

%description
PyAnnote is a Python module for collaborative annotation of multimodal
documents.

%prep
%setup

sed -i 's|@VERSION@|%version|' %mname/core/_version.py
git config --global user.email "real at altlinux.org"
git config --global user.name "REAL"
git init-db
git add . -A
git commit -a -m "%version"
git tag %version -m "%version"

%build
%python_build_debug

%install
%python_install

%ifarch x86_64
mv %buildroot%_libexecdir %buildroot%_libdir
%endif

install -p -m644 %mname/__init__.py \
	%buildroot%python_sitelibdir/%mname/

%check
python setup.py test

%files
%doc *.md doc
%python_sitelibdir/%mname
%python_sitelibdir/*.egg-info

%changelog
* Tue Nov 18 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2.4-alt1.git20141118
- Version 0.2.4

* Sun Nov 16 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2.3-alt1.git20141114
- Version 0.2.3

* Thu Nov 13 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2.2-alt1.git20141112
- Initial build for Sisyphus

