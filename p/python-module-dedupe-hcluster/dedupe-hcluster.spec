%define mname hcluster
%define oname dedupe-%mname

%def_with python3

Name: python-module-%oname
Version: 0.3.2
Release: alt1.git20150304.2.1
Summary: Hierarchical Clustering Algorithms (Information Theory)
License: SciPy License (BSD Style)
Group: Development/Python
Url: https://pypi.python.org/pypi/dedupe-hcluster

# https://github.com/datamade/hcluster.git
Source: %name-%version.tar

BuildRequires: python-devel python-module-setuptools
BuildRequires: python-module-future libnumpy-devel
BuildRequires: python-module-nose python-module-Cython
BuildRequires: python-module-html5lib python-module-ipyparallel python-module-numpy-testing
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python3-module-setuptools
BuildRequires: python3-module-future libnumpy-py3-devel
BuildRequires: python3-module-nose python3-module-Cython
BuildRequires: python3-module-html5lib python3-module-notebook python3-module-numpy-testing
%endif

%py_provides %mname
Provides: python-module-%mname = %EVR
Conflicts: python-module-%mname < %EVR
Obsoletes: python-module-%mname < %EVR
%py_requires numpy future

%description
This library provides Python functions for hierarchical clustering. Its
features include

* generating hierarchical clusters from distance matrices
* computing distance matrices from observation vectors
* computing statistics on clusters
* cutting linkages to generate flat clusters
* and visualizing clusters with dendrograms.

It is a fork of clustering and distance functions from the scipy that
removes all the dependencies on scipy. It preserves the API of hcluster
0.2.

%if_with python3
%package -n python3-module-%oname
Summary: Hierarchical Clustering Algorithms (Information Theory)
Group: Development/Python3
%py3_provides %mname
Provides: python3-module-%mname = %EVR
Conflicts: python3-module-%mname < %EVR
Obsoletes: python3-module-%mname < %EVR
%py3_requires numpy future

%description -n python3-module-%oname
This library provides Python functions for hierarchical clustering. Its
features include

* generating hierarchical clusters from distance matrices
* computing distance matrices from observation vectors
* computing statistics on clusters
* cutting linkages to generate flat clusters
* and visualizing clusters with dendrograms.

It is a fork of clustering and distance functions from the scipy that
removes all the dependencies on scipy. It preserves the API of hcluster
0.2.
%endif

%prep
%setup

%if_with python3
cp -fR . ../python3
%endif

%build
%add_optflags -fno-strict-aliasing
%python_build_debug

%if_with python3
pushd ../python3
%python3_build_debug
popd
%endif

%install
%python_install

%if_with python3
pushd ../python3
%python3_install
popd
%endif

%check
python setup.py test -v
python setup.py build_ext -i
nosetests -vv
%if_with python3
pushd ../python3
python3 setup.py test -v
python3 setup.py build_ext -i
nosetests3 -vv
popd
%endif

%files
%doc LICENSE.txt *.md
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc LICENSE.txt *.md
%python3_sitelibdir/*
%endif

%changelog
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.3.2-alt1.git20150304.2.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Fri Aug 18 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 0.3.2-alt1.git20150304.2
- Updated build dependencies.

* Thu Mar 17 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.3.2-alt1.git20150304.1.1
- (NMU) rebuild with python3-3.5 & rpm-build-python3-0.1.10
  (for ABI dependence and new python3(*) reqs)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.3.2-alt1.git20150304.1
- NMU: Use buildreq for BR.

* Wed Aug 26 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3.2-alt1.git20150304
- Initial build for Sisyphus

