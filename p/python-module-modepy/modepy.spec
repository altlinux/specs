%define _unpackaged_files_terminate_build 1

%define oname modepy

%def_with python3
%def_without docs

Name: python-module-%oname
Version: 2016.1.2
Release: alt1
Summary: Modes and nodes for high-order discretizations
License: MIT
Group: Development/Python
Url: https://documen.tician.de/modepy/

BuildArch: noarch

# https://github.com/inducer/modepy.git
Source: %name-%version.tar

Patch1: %oname-alt-docs.patch

BuildRequires: python-devel python-module-setuptools

%if_with docs
BuildRequires(pre): rpm-macros-sphinx
BuildRequires: python-module-alabaster python-module-docutils python-module-html5lib
BuildRequires: python-module-matplotlib python-module-numpy-testing python-module-objects.inv
BuildRequires: python-module-pytools python-module-sphinx-bootstrap-theme
%endif

%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python3-module-setuptools
%endif


%description
modepy helps you create well-behaved high-order discretizations on
simplices (i.e. triangles and tetrahedra). These are a key building
block for high-order unstructured discretizations, as often used in a
finite element context.

The basic objects that modepy manipulates are functions on a simplex.
For example, it supplies an orthonormal basis on triangles (shown here)
and tetrahedra.

%package -n python3-module-%oname
Summary: Modes and nodes for high-order discretizations
Group: Development/Python3

%description -n python3-module-%oname
modepy helps you create well-behaved high-order discretizations on
simplices (i.e. triangles and tetrahedra). These are a key building
block for high-order unstructured discretizations, as often used in a
finite element context.

The basic objects that modepy manipulates are functions on a simplex.
For example, it supplies an orthonormal basis on triangles (shown here)
and tetrahedra.

%package pickles
Summary: Pickles for modepy
Group: Development/Python

%description pickles
modepy helps you create well-behaved high-order discretizations on
simplices (i.e. triangles and tetrahedra). These are a key building
block for high-order unstructured discretizations, as often used in a
finite element context.

The basic objects that modepy manipulates are functions on a simplex.
For example, it supplies an orthonormal basis on triangles (shown here)
and tetrahedra.

This package contains pickles for modepy.

%package doc
Summary: Documentation for modepy
Group: Development/Documentation

%description doc
modepy helps you create well-behaved high-order discretizations on
simplices (i.e. triangles and tetrahedra). These are a key building
block for high-order unstructured discretizations, as often used in a
finite element context.

The basic objects that modepy manipulates are functions on a simplex.
For example, it supplies an orthonormal basis on triangles (shown here)
and tetrahedra.

This package contains documentation for modepy.

%prep
%setup
%patch1 -p1

%if_with python3
cp -fR . ../python3
%endif

%if_with docs
%prepare_sphinx .
ln -s ../objects.inv doc/
%endif

%build
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

%if_with docs
export PYTHONPATH=%buildroot%python_sitelibdir
%make -C doc pickle
%make -C doc html

cp -fR doc/_build/pickle %buildroot%python_sitelibdir/%oname/
%endif

%files
%doc LICENSE
%doc README.rst
%python_sitelibdir/*
%if_with docs
%exclude %python_sitelibdir/%oname/pickle
%endif

%if_with docs
%files pickles
%python_sitelibdir/%oname/pickle

%files doc
%doc doc/_build/html/*
%endif

%if_with python3
%files -n python3-module-%oname
%doc LICENSE
%doc README.rst
%python3_sitelibdir/*
%endif

%changelog
* Tue Jul 23 2019 Aleksei Nikiforov <darktemplar@altlinux.org> 2016.1.2-alt1
- Updated to upstream version 2016.1.2.

* Wed May 16 2018 Andrey Bychkov <mrdrew@altlinux.org> 2013.3-alt1.git20140704.1.2
- (NMU) rebuild with python3.6

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 2013.3-alt1.git20140704.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 2013.3-alt1.git20140704.1
- NMU: Use buildreq for BR.

* Sat Aug 09 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2013.3-alt1.git20140704
- New snapshot
- Added module for Python 3

* Thu Jun 26 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2013.3-alt1.git20140621
- Initial build for Sisyphus

