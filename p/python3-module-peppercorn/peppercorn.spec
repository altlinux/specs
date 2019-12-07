%define oname peppercorn

%def_without docs

Name: python3-module-%oname
Version: 0.6
Release: alt1

Summary: A library for converting a token stream into a data structure for use in web form posts
License: BSD
Group: Development/Python3
Url: https://pypi.python.org/pypi/peppercorn/
BuildArch: noarch

# https://github.com/Pylons/peppercorn.git
Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
%if_with docs
BuildRequires: pylons_sphinx_theme python3-module-sphinx
%endif

%py3_provides %oname


%description
A library for converting a token stream into a data structure comprised
of sequences, mappings, and scalars, developed primarily for converting
HTTP form post data into a richer data structure.

%package tests
Summary: Tests for %oname
Group: Development/Python3
Requires: %name = %EVR

%description tests
A library for converting a token stream into a data structure comprised
of sequences, mappings, and scalars, developed primarily for converting
HTTP form post data into a richer data structure.

This package contains tests for %oname.

%if_with docs
%package pickles
Summary: Pickles for %oname
Group: Development/Python3

%description pickles
A library for converting a token stream into a data structure comprised
of sequences, mappings, and scalars, developed primarily for converting
HTTP form post data into a richer data structure.

This package contains pickles for %oname.

%package docs
Summary: Documentation for %oname
Group: Development/Documentation
BuildArch: noarch

%description docs
A library for converting a token stream into a data structure comprised
of sequences, mappings, and scalars, developed primarily for converting
HTTP form post data into a richer data structure.

This package contains documentation for %oname.
%endif

%prep
%setup

%if_with docs
sed -i 's|sphinx-build|sphinx-build-3|' docs/Makefile
%endif

%build
%python3_build_debug

%install
%python3_install

%if_with docs
export PYTHONPATH=%buildroot%python3_sitelibdir
%make -C docs pickle
%make -C docs html

cp -fR docs/_build/pickle %buildroot%python3_sitelibdir/%oname/
%endif

%files
%doc *.txt
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/tests.*
%if_with docs
%exclude %python3_sitelibdir/*/pickle
%endif

%if_with docs
%files pickles
%python3_sitelibdir/*/pickle

%files docs
%doc docs/_build/html/*
%endif

%files tests
%python3_sitelibdir/*/tests.*


%changelog
* Sat Dec 07 2019 Andrey Bychkov <mrdrew@altlinux.org> 0.6-alt1
- Version updated to 0.6
- build for python2 disabled

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.5-alt1.git20140929.1.1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.5-alt1.git20140929.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.5-alt1.git20140929.1
- NMU: Use buildreq for BR.

* Thu Oct 09 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.5-alt1.git20140929
- Initial build for Sisyphus

