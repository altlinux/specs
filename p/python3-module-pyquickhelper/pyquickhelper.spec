%define oname pyquickhelper
Name: python3-module-%oname
Version: 1.1.494
Release: alt1.git20150422
Summary: Folder synchronization, a logging function, helpers to generate documentation and more
License: BSD
Group: Development/Python3
Url: https://pypi.python.org/pypi/pyquickhelper/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/sdpython/pyquickhelper.git
Source: %name-%version.tar
#BuildArch: noarch

BuildRequires(pre): rpm-build-python3 rpm-macros-sphinx
BuildPreReq: python3-devel python3-module-setuptools-tests xset /proc
BuildPreReq: python3-module-numpy python3-module-pandas git pandoc
BuildPreReq: python3-module-six python3-module-dateutils
BuildPreReq: python3-module-requests python3-module-docutils
BuildPreReq: python3-module-matplotlib ipython3 graphviz
BuildPreReq: python3-module-flake8 python3-tools-pep8
BuildPreReq: python3-module-autopep8 python3-module-sphinx-devel
BuildPreReq: python3-module-zmq
BuildPreReq: python3-module-solar_theme python3-modules-tkinter
BuildPreReq: python3-module-sphinxcontrib-images
BuildPreReq: python3-module-matplotlib-sphinxext

%py3_provides %oname
Requires: git pandoc xset /proc
%py3_requires numpy pandas six dateutils requests docutils IPython pep8
%py3_requires matplotlib flake8 autopep8 sphinx zmq
%py3_requires sphinxcontrib.images matplotlib.sphinxext

%description
Various functionalities: folder synchronization, a logging function,
helpers to generate documentation with sphinx, generation of code for
Python 2.7 from Python 3.

Functionalities:

* simple forms in notebooks
* help generation including notebook conversion
* folder synchronization
* logging
* help running unit tests
* simple server to server sphinx documentation
* file compression, zip, gzip, 7z
* helpers for ipython notebooks (upgrade, offline run)
* parser to quickly add a magic command in a notebook
* Sphinx directives to integrate a blogpost in the documentation

%package docs
Summary: Documentation for %oname
Group: Development/Documentation
#BuildArch: noarch

%description docs
Various functionalities: folder synchronization, a logging function,
helpers to generate documentation with sphinx, generation of code for
Python 2.7 from Python 3.

This package contains documentation for %oname.

%prep
%setup

git config --global user.email "real at altlinux.org"
git config --global user.name "REAL"
git init-db
git remote add origin https://github.com/sdpython/pyquickhelper.git
git add . -A
git commit -a -m "%version"
git tag -m "%version" %version

%prepare_sphinx _doc/sphinxdoc
ln -s ../objects.inv _doc/sphinxdoc/source/

%build
%python3_build_debug --verbose

%install
%python3_install

%ifarch x86_64
mv %buildroot%_libexecdir %buildroot%_libdir
%endif

export LC_ALL=en_US.UTF-8
python3 setup.py build_sphinx
mv _doc/sphinxdoc/build docs

%check
export LC_ALL=en_US.UTF-8
python3 setup.py test
#python3 setup.py unittests

%files
%doc *.rst
%python3_sitelibdir/*

%files docs
%doc build/notebooks docs

%changelog
* Wed Apr 22 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1.494-alt1.git20150422
- Initial build for Sisyphus

