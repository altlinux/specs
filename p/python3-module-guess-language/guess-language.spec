%define oname guess-language

%def_without check

Name: python3-module-%oname
Version: 0.2
Release: alt1.svn20100801.2
Summary: Guess the natural language of a text
License: LGPLv2.1
Group: Development/Python3
Url: https://pypi.python.org/pypi/guess-language/

# http://guess-language.googlecode.com/svn/trunk/
Source: %name-%version.tar
BuildArch: noarch

BuildRequires(pre): rpm-build-python3

%py3_provides guess_language

BuildRequires: python3-module-pytest /usr/bin/2to3

%description
Attempts to determine the natural language of a selection of Unicode
(utf-8) text.

Detects over 60 languages - all languages listed in the trigrams
directory plus Japanese, Chinese, Korean and Greek.

%package tests
Summary: Tests for %oname
Group: Development/Python3
Requires: %name = %EVR

%description tests
Attempts to determine the natural language of a selection of Unicode
(utf-8) text.

Detects over 60 languages - all languages listed in the trigrams
directory plus Japanese, Chinese, Korean and Greek.

%prep
%setup

find . -type f -name '*.py' -exec 2to3 -w -n '{}' +

%build
%python3_build

%install
%python3_install

%check
rm -fR build
py.test-3

%files
%doc README
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/*test.*
%exclude %python3_sitelibdir/*/*/*test.*

%files tests
%python3_sitelibdir/*/*test.*
%python3_sitelibdir/*/*/*test.*

%changelog
* Sun Jul 25 2021 Grigory Ustinov <grenka@altlinux.org> 0.2-alt1.svn20100801.2
- Drop python2 support.
- Build without check.

* Wed May 16 2018 Andrey Bychkov <mrdrew@altlinux.org> 0.2-alt1.svn20100801.1.2
- (NMU) rebuild with python3.6

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.2-alt1.svn20100801.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.2-alt1.svn20100801.1
- NMU: Use buildreq for BR.

* Sat Nov 08 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2-alt1.svn20100801
- Initial build for Sisyphus

