%define oname html5lib

%def_without doc

Name: python3-module-html5lib
Epoch: 1
Version: 1.1
Release: alt1

Summary: Library for working with HTML5 documents

License: MIT
Group: Development/Python3
Url: https://github.com/html5lib/html5lib-python

# Source-url: %__pypi_url %oname
Source: %name-%version.tar

BuildRequires(pre): rpm-build-intro
BuildRequires(pre): rpm-build-python3

BuildArch: noarch

%{?_with_doc:BuildRequires(pre): rpm-macros-sphinx3}

#BuildRequires: python3-dev
BuildRequires: python3-module-setuptools >= 18.5
BuildRequires: python3(webencodings)
BuildRequires: python3(pytest) python3(six) python3(mock)

%description
A ruby/python based HTML parser/tokenizer based on the WHATWG
HTML5 specification for maximum compatibility with major
desktop web browsers.

%package doc
Summary: Documentation for html5lib
Group: Development/Documentation

%description doc
A ruby/python based HTML parser/tokenizer based on the WHATWG
HTML5 specification for maximum compatibility with major
desktop web browsers.

This package contains documentation for html5lib.

%prep
%setup
rm -f html5lib/tests/conftest.py
# https://github.com/html5lib/html5lib-python/issues/433
rm -f html5lib/tests/test_encoding.py
#sed -i "s|import chardet|raise ImportError('Skipping chardet test: file is missing')|g" html5lib/tests/test_encoding.py

%if_with doc
%prepare_sphinx3 .
ln -s ../objects.inv doc/
%endif

%build
%python3_build

%if_with doc
%make -C doc html
%endif

%install
%python3_install
%python3_prune

%check
py.test3

%files
%doc README.rst
%python3_sitelibdir/*

%if_with doc

%files doc
%doc doc/_build/html/*
%endif

%changelog
* Sun Jul 11 2021 Vitaly Lipatov <lav@altlinux.ru> 1:1.1-alt1
- build python3 module separately
- new version 1.1 (with rpmrb script)

* Mon Oct 07 2019 Vitaly Lipatov <lav@altlinux.ru> 1:1.0.1-alt1
- new version 1.0.1 (with rpmrb script)

* Thu May 30 2019 Stanislav Levin <slev@altlinux.org> 1:0.999999999-alt5
- Fixed Pytest4.x compatibility error.

* Sun Oct 14 2018 Igor Vlasenko <viy@altlinux.ru> 1:0.999999999-alt4.qa1
- NMU: applied repocop patch

* Fri Feb 16 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 1:0.999999999-alt4
- Updated build dependencies.

* Fri Oct 13 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 1:0.999999999-alt3
- Fixed python3 modules. Got rid of 2to3 conversion since it seems no longer necessary.
- Enabled tests.

* Thu Sep 07 2017 Vitaly Lipatov <lav@altlinux.ru> 1:0.999999999-alt2
- restore unichr after 2to3 (ALT bug 33854)

* Wed Jun 14 2017 Vitaly Lipatov <lav@altlinux.ru> 1:0.999999999-alt1
- new version (0.999999999) with rpmgs script

* Mon Jan 02 2017 Michael Shigorin <mike@altlinux.org> 1:0.999999-alt1.1.1.2
- BOOTSTRAP:
  + renamed docs knob to doc for consistency; see http://altlinux.org/bootstrap
  + made it avoid BR: rpm-macros-sphinx when disabled

* Mon Apr 11 2016 Ivan Zakharyaschev <imz@altlinux.org> 1:0.999999-alt1.1.1.1
- (NMU) rebuild with rpm-build-python3-0.1.10 (for new-style python3(*) reqs)
  and with python3-3.5 (for byte-compilation).

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1:0.999999-alt1.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 1:0.999999-alt1.1
- NMU: Use buildreq for BR.

* Wed Aug 12 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1:0.999999-alt1
- Version 0.999999

* Thu Aug 21 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1:0.999-alt1
- Version 0.999

* Tue Sep 17 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0-alt1.b3
- Version 1.0b3

* Mon Apr 15 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.95-alt4
- Use 'find... -exec...' instead of 'for ... $(find...'

* Fri Mar 22 2013 Aleksey Avdeev <solo@altlinux.ru> 0.95-alt3.1
- Rebuild with Python-3.3

* Tue Apr 10 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.95-alt3
- Added modules for Python 3

* Tue Apr 10 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.95-alt2
- Extracted tests into separate package

* Mon Apr 09 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.95-alt1
- Version 0.95

* Mon Oct 24 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.11.1-alt2.1.1
- Rebuild with Python-2.7

* Fri Nov 20 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.11.1-alt2.1
- Rebuilt with python 2.6

* Fri Jan 30 2009 Denis Klimov <zver@altlinux.org> 0.11.1-alt2
- install over --record option
- add README file

* Fri Jan 30 2009 Denis Klimov <zver@altlinux.org> 0.11.1-alt1
- Initial build for ALT Linux

