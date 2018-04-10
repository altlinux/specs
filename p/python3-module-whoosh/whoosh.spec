%define oname whoosh
%define fname python3-module-%oname
%define descr \
Whoosh is a fast, featureful full-text indexing and searching library \
implemented in pure Python. Programmers can use it to easily add search \
functionality to their applications and websites. Every part of how \
Whoosh works can be extended or replaced to meet your needs exactly.

Name: %fname
Version: 2.7.0
Release: alt2.hg20150805

%if ""==""
Summary: Fast pure-Python indexing and search library
Group: Development/Python3
%else
Summary: Documentation for %oname
Group: Development/Documentation
%endif

License: BSD
URL: https://bitbucket.org/mchaput/whoosh/wiki/Home
# hg clone https://bitbucket.org/mchaput/whoosh
Source: %oname-%version.tar

BuildRequires(pre): rpm-build-python3 rpm-macros-sphinx
BuildRequires: python-module-alabaster python-module-docutils python-module-html5lib python-module-objects.inv
Buildrequires: python-module-sphinx-pickles python3-module-setuptools time

BuildArch: noarch

%if "3"=="3"
%add_python3_req_skip google
%add_python3_req_skip google.appengine.api
%add_python3_req_skip google.appengine.ext
%add_python3_req_skip whoosh.automata.fst
%filter_from_provides /^python3(whoosh.automata.nfa)/d
# ImportError: No module named 'whoosh.automata.fst'
%filter_from_provides /^python3(whoosh.filedb.gae)/d
# ImportError: No module named 'google'
%filter_from_provides /^python3(whoosh.support.bench)/d
# ImportError: cannot import name 'find_object'
%endif

%if ""!=""
Conflicts: %fname < %EVR
Conflicts: %fname > %EVR
%endif

%description
%descr

%if ""!=""
This package contains documentation for %oname.

%package -n %fname-pickles
Summary: Pickles for whoosh
Group: Development/Python3

%description -n %fname-pickles
%descr

This package contains pickles for %oname.

%else

%package tests
Summary: Tests for %oname
Group: Development/Python3
Requires: %fname = %version-%release
%if "3"=="3"
%py3_requires nose
%endif

%description tests
%descr

This package contains tests for whoosh.

%endif

%prep
%setup
%if ""!=""
%prepare_sphinx docs
ln -s ../objects.inv docs/source/
%endif

%build
%if ""==""
%python3_build
%else
mkdir docs/source/_static
%generate_pickles docs/source docs/source %oname
sphinx-build -E -a -b html -c docs/source -d doctrees docs/source html
%endif

%install
%if ""!=""
mkdir -p %buildroot%python3_sitelibdir/%oname/
cp -fR pickle %buildroot%python3_sitelibdir/%oname/
%else
%python3_install
cp -fR src/whoosh/query src/whoosh/matching %buildroot%python3_sitelibdir/%oname/
%endif

%if ""==""
%files
%doc *.txt
%python3_sitelibdir/*
%exclude %python3_sitelibdir/%oname/util/testing.py*

%files tests
%doc tests
%python3_sitelibdir/%oname/util/testing.py*

%else

%files
%doc html/*

%files -n %fname-pickles
%python3_sitelibdir/%oname/pickle
%endif

%changelog
* Fri Mar 30 2018 Grigory Ustinov <grenka@altlinux.org> 2.7.0-alt2.hg20150805
- Tranfer package to subst-packaging system.

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 2.7.0-alt1.hg20150805.1.1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 2.7.0-alt1.hg20150805.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 2.7.0-alt1.hg20150805.1
- NMU: Use buildreq for BR.

* Sat Aug 08 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.7.0-alt1.hg20150805
- Version 2.7.0

* Wed Jul 16 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.6.0-alt1.hg20140505
- New snapshot

* Mon Dec 02 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.6.0-alt1.hg20131128
- Version 2.6.0

* Mon Feb 18 2013 Aleksey Avdeev <solo@altlinux.ru> 2.4.1-alt1
- Version 2.4.1

* Mon Apr 16 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.3.2-alt1.hg20120406
- Version 2.3.2
- Added module for Python 3

* Sun Nov 27 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.3.1-alt1.hg20111114
- Initial build for Sisyphus

