%define oname whoosh
%define fname python-module-%oname
%define descr \
Whoosh is a fast, featureful full-text indexing and searching library \
implemented in pure Python. Programmers can use it to easily add search \
functionality to their applications and websites. Every part of how \
Whoosh works can be extended or replaced to meet your needs exactly.

Name: %fname
Version: 2.7.4
Release: alt2

Summary: Fast pure-Python indexing and search library
Group: Development/Python

License: BSD
URL: https://bitbucket.org/mchaput/whoosh/wiki/Home
# hg clone https://bitbucket.org/mchaput/whoosh
Source: %oname-%version.tar

BuildRequires(pre): rpm-build-python

BuildArch: noarch

%if ""=="3"
%add_python3_req_skip google
%add_python3_req_skip google.appengine.api
%add_python3_req_skip google.appengine.ext
%add_python3_req_skip whoosh.automata.fst
%filter_from_provides /^python(whoosh.automata.nfa)/d
# ImportError: No module named 'whoosh.automata.fst'
%filter_from_provides /^python(whoosh.filedb.gae)/d
# ImportError: No module named 'google'
%filter_from_provides /^python(whoosh.support.bench)/d
# ImportError: cannot import name 'find_object'
%endif

%description
%descr

%prep
%setup

%build
%python_build

%install
%python_install
cp -fR src/whoosh/query src/whoosh/matching %buildroot%python_sitelibdir/%oname/
# don't ship tests
rm %buildroot%python_sitelibdir/%oname/util/testing.py*

%files
%doc *.txt
%python_sitelibdir/*

%changelog
* Fri Jul 23 2021 Stanislav Levin <slev@altlinux.org> 2.7.4-alt2
- Dropped unused docs deps.

* Wed May 30 2018 Grigory Ustinov <grenka@altlinux.org> 2.7.4-alt1
- Build new version.

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

