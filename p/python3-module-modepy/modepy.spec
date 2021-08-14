%define _unpackaged_files_terminate_build 1
%define oname modepy

%def_without docs

Name: python3-module-%oname
Version: 2016.1.2
Release: alt3

Summary: Modes and nodes for high-order discretizations
License: MIT
Group: Development/Python3
Url: https://documen.tician.de/modepy/
# https://github.com/inducer/modepy.git
BuildArch: noarch

Source: %name-%version.tar
Patch1: %oname-alt-docs.patch

BuildRequires(pre): rpm-build-python3


%description
modepy helps you create well-behaved high-order discretizations on
simplices (i.e. triangles and tetrahedra). These are a key building
block for high-order unstructured discretizations, as often used in a
finite element context.

The basic objects that modepy manipulates are functions on a simplex.
For example, it supplies an orthonormal basis on triangles (shown here)
and tetrahedra.

%package pickles
Summary: Pickles for modepy
Group: Development/Python3

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

%if_with docs
sed -i 's|sphinx-build|sphinx-build-3|' doc/Makefile
%endif

%build
%python3_build_debug

%install
%python3_install

%if_with docs
export PYTHONPATH=%buildroot%python3_sitelibdir
%make -C doc pickle
%make -C doc html

cp -fR doc/_build/pickle %buildroot%python3_sitelibdir/%oname/
%endif

%files
%doc LICENSE
%doc README.rst
%python3_sitelibdir/*
%if_with docs
%exclude %python_sitelibdir/%oname/pickle
%endif

%if_with docs
%files pickles
%python3_sitelibdir/%oname/pickle

%files doc
%doc doc/_build/html/*
%endif


%changelog
* Sat Aug 14 2021 Vitaly Lipatov <lav@altlinux.ru> 2016.1.2-alt3
- drop unused BR: rpm-macros-sphinx

* Wed Nov 13 2019 Andrey Bychkov <mrdrew@altlinux.org> 2016.1.2-alt2
- disable python2

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

