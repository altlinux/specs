%define oname whoosh

%def_with python3

Name: python-module-%oname
Version: 2.3.2
Release: alt1.hg20120406
Summary: Fast pure-Python indexing and search library

Group: Development/Python
License: BSD
URL: https://bitbucket.org/mchaput/whoosh/wiki/Home
# hg clone https://bitbucket.org/mchaput/whoosh
Source: %oname-%version.tar
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

BuildPreReq: python-module-distribute python-devel
BuildPreReq: python-module-sphinx-devel
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python3-module-distribute
%endif
BuildArch: noarch

%description
Whoosh is a fast, featureful full-text indexing and searching library
implemented in pure Python. Programmers can use it to easily add search
functionality to their applications and websites. Every part of how
Whoosh works can be extended or replaced to meet your needs exactly.

%if_with python3
%package -n python3-module-%oname
Summary: Fast pure-Python3 indexing and search library
Group: Development/Python3
%add_python3_req_skip google

%description -n python3-module-%oname
Whoosh is a fast, featureful full-text indexing and searching library
implemented in pure Python. Programmers can use it to easily add search
functionality to their applications and websites. Every part of how
Whoosh works can be extended or replaced to meet your needs exactly.

%package -n python3-module-%oname-tests
Summary: Tests for whoosh (Python 3)
Group: Development/Python3
Requires: python3-module-%oname = %version-%release
%py3_requires nose

%description -n python3-module-%oname-tests
Whoosh is a fast, featureful full-text indexing and searching library
implemented in pure Python. Programmers can use it to easily add search
functionality to their applications and websites. Every part of how
Whoosh works can be extended or replaced to meet your needs exactly.

This package contains tests for whoosh.
%endif

%package tests
Summary: Tests for whoosh
Group: Development/Python
Requires: %name = %version-%release

%description tests
Whoosh is a fast, featureful full-text indexing and searching library
implemented in pure Python. Programmers can use it to easily add search
functionality to their applications and websites. Every part of how
Whoosh works can be extended or replaced to meet your needs exactly.

This package contains tests for whoosh.

%package docs
Summary: Documentation for whoosh
Group: Development/Documentation

%description docs
Whoosh is a fast, featureful full-text indexing and searching library
implemented in pure Python. Programmers can use it to easily add search
functionality to their applications and websites. Every part of how
Whoosh works can be extended or replaced to meet your needs exactly.

This package contains documentation for whoosh.

%package pickles
Summary: Pickles for whoosh
Group: Development/Python

%description pickles
Whoosh is a fast, featureful full-text indexing and searching library
implemented in pure Python. Programmers can use it to easily add search
functionality to their applications and websites. Every part of how
Whoosh works can be extended or replaced to meet your needs exactly.

This package contains pickles for whoosh.

%prep
%setup
%if_with python3
rm -rf ../python3
cp -a . ../python3
%endif

%prepare_sphinx docs
ln -s ../objects.inv docs/source/

%build
%python_build_debug
%if_with python3
pushd ../python3
%python3_build
popd
%endif

mkdir docs/source/_static
%generate_pickles docs/source docs/source %oname
sphinx-build -E -a -b html -c docs/source -d doctrees docs/source html

%install
%python_install
%if_with python3
pushd ../python3
%python3_install
cp -fR src/whoosh/query src/whoosh/matching \
	%buildroot%python3_sitelibdir/%oname/
popd
%endif

# pickles
cp -fR pickle %buildroot%python_sitelibdir/%oname/

%files
%doc *.txt
%python_sitelibdir/*
%exclude %python_sitelibdir/%oname/pickle
%exclude %python_sitelibdir/%oname/support/testing.py*

%files tests
%doc tests
%python_sitelibdir/%oname/support/testing.py*

%files docs
%doc html/*

%files pickles
%python_sitelibdir/%oname/pickle

%if_with python3
%files -n python3-module-%oname
%doc *.txt
%python3_sitelibdir/*
%exclude %python3_sitelibdir/%oname/support/testing.py*

%files -n python3-module-%oname-tests
%doc tests
%python3_sitelibdir/%oname/support/testing.py*
%endif

%changelog
* Mon Apr 16 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.3.2-alt1.hg20120406
- Version 2.3.2
- Added module for Python 3

* Sun Nov 27 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.3.1-alt1.hg20111114
- Initial build for Sisyphus

