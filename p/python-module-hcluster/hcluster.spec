%define oname hcluster
Name: python-module-%oname
Version: 0.2.0
Release: alt1.svn20100205
Summary: A hierarchical clustering package for Scipy
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/hcluster/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# http://scipy-cluster.googlecode.com/svn/trunk/
Source: %name-%version.tar

BuildPreReq: python-module-setuptools-tests libnumpy-devel
BuildPreReq: python-module-scipy python-module-nose

%py_provides %oname
%py_requires scipy

%description
This library provides Python functions for hierarchical clustering. Its
features include

* generating hierarchical clusters from distance matrices
* computing distance matrices from observation vectors
* computing statistics on clusters
* cutting linkages to generate flat clusters
* and visualizing clusters with dendrograms.

%prep
%setup

%build
%python_build_debug

%install
%python_install

%check
python setup.py build_ext -i
nosetests -v

%files
%doc THANKS TODO
%python_sitelibdir/*

%changelog
* Tue Feb 10 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2.0-alt1.svn20100205
- Initial build for Sisyphus

