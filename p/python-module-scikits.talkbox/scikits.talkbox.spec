%define mname scikits
%define oname %mname.talkbox
Name: python-module-%oname
Epoch: 1
Version: 0.2.3
Release: alt2.git20091014.1
Summary: Talkbox, a set of python modules for speech/signal processing
License: MIT
Group: Development/Python
Url: https://pypi.python.org/pypi/scikits.talkbox/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# git://github.com/cournape/talkbox.git
Source: %name-%version.tar

BuildPreReq: python-module-setuptools libnumpy-devel
BuildPreReq: python-module-scipy python-module-Cython
BuildPreReq: python-module-lxml python-module-sphinx-devel
BuildPreReq: python-module-numpydoc python-module-Paver
BuildPreReq: texlive-latex-recommended texmf-latex-preview

%py_provides %oname
%py_requires %mname numpy scipy

%description
Talkbox, to make your numpy environment speech aware!

Talkbox is set of python modules for speech/signal processing. The goal
of this toolbox is to be a sandbox for features which may end up in
scipy at some point.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR

%description tests
Talkbox, to make your numpy environment speech aware!

Talkbox is set of python modules for speech/signal processing. The goal
of this toolbox is to be a sandbox for features which may end up in
scipy at some point.

This package contains tests for %oname.

%package pickles
Summary: Pickles for %oname
Group: Development/Python

%description pickles
Talkbox, to make your numpy environment speech aware!

Talkbox is set of python modules for speech/signal processing. The goal
of this toolbox is to be a sandbox for features which may end up in
scipy at some point.

This package contains pickles for %oname.

%package docs
Summary: Documentation for %oname
Group: Development/Documentation
BuildArch: noarch

%description docs
Talkbox, to make your numpy environment speech aware!

Talkbox is set of python modules for speech/signal processing. The goal
of this toolbox is to be a sandbox for features which may end up in
scipy at some point.

This package contains documentation for %oname.

%prep
%setup

rm -f scikits/talkbox/tools/src/*.c

%prepare_sphinx docs
ln -s ../objects.inv docs/src/
rm -f docs/ext/numpydoc.py

%build
export PYTHONPATH=$PWD:$PWD/docs/ext
paver build_version_files
cython scikits/talkbox/tools/src/cacorr.pyx
cython scikits/talkbox/tools/src/cffilter.pyx
%python_build_debug

%install
export PYTHONPATH=$PWD:$PWD/docs/ext
%python_install

python setup.py build_ext -i
%make -C docs pickle
%make -C docs html

install -d %buildroot%python_sitelibdir/%oname
cp -fR docs/build/pickle %buildroot%python_sitelibdir/%oname/

%check
python setup.py test

%files
%doc Changelog README TODO
%python_sitelibdir/%mname/talkbox
%python_sitelibdir/*.egg-info
%exclude %python_sitelibdir/%mname/talkbox/*/tests

%files tests
%python_sitelibdir/%mname/talkbox/*/tests

%files pickles
%python_sitelibdir/*/pickle

%files docs
%doc docs/build/html docs/src/examples

%changelog
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 1:0.2.3-alt2.git20091014.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Tue Apr 28 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1:0.2.3-alt2.git20091014
- Rebuilt with updated NumPy

* Sun Mar 01 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1:0.2.3-alt1.git20091014
- Initial build for Sisyphus

