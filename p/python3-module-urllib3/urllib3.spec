%define oname urllib3
%def_disable check
%def_without docs

Name: python3-module-%oname
Version: 1.26.14
Release: alt1

Epoch: 2

Summary: Library with thread-safe connection pooling, file post support, sanity friendly etc
License: MIT
Group: Development/Python3

Url: https://github.com/shazow/urllib3/

# make all imports of things in packages try system copies first
Patch: %name-%version.patch

# https://github.com/shazow/urllib3.git
Source: %oname-%version.tar
BuildArch: noarch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-six
BuildRequires: python3-module-mock
BuildRequires: python3-module-nose
#Requires: python3-module-ndg-httpsclient
Requires: python3-module-six ca-certificates
%if_with docs
BuildRequires(pre): rpm-macros-sphinx3
BuildRequires: python3-module-sphinx
%endif

%description
Python HTTP library with thread-safe connection pooling, file post
support, sanity friendly, and more.

%package tests
Summary: Tests for urllib3
Group: Development/Python3
Requires: %name = %EVR

%description tests
Python HTTP library with thread-safe connection pooling, file post
support, sanity friendly, and more.

This package contains tests for urllib3.

%if_with docs
%package pickles
Summary: Pickles for urllib3
Group: Development/Python3

%description pickles
Python HTTP library with thread-safe connection pooling, file post
support, sanity friendly, and more.

This package contains pickles for urllib3.

%package docs
Summary: Documentation for urllib3
Group: Development/Documentation

%description docs
Python HTTP library with thread-safe connection pooling, file post
support, sanity friendly, and more.

This package contains documentation for urllib3.
%endif

%prep
%setup -n %oname-%version
#rm -rf urllib3/packages/
%patch -p1

%if_with docs
%prepare_sphinx3 .
ln -s ../objects.inv docs/
%endif

%build
%python3_build

%install
%python3_install

# drop deprecated ntlm support
rm -fv %buildroot%python3_sitelibdir/%oname/contrib/ntlmpool.py

%if_with docs
export PYTHONPATH=%buildroot%python3_sitelibdir
pushd docs
%make SPHINXBUILD="sphinx-build-3" html
%make SPHINXBUILD="sphinx-build-3" pickle
popd

cp -fR docs/_build/pickle %buildroot%python3_sitelibdir/%oname/
%endif

%check
py.test-3

%files
%doc *.txt *.rst
%python3_sitelibdir/*
%if_with docs
%exclude %python3_sitelibdir/*/pickle

%files pickles
%python3_sitelibdir/*/pickle

%files docs
%doc docs/_build/html/*
%endif

%changelog
* Thu Jan 12 2023 Vladimir Didenko <cow@altlinux.org> 2:1.26.14-alt1
- 1.26.6 -> 1.26.14 (fixes compatibility with cryptography >= 39)

* Tue Aug 17 2021 Vitaly Lipatov <lav@altlinux.ru> 2:1.26.6-alt3
- drop deprecated ntlm support

* Sun Aug 01 2021 Vitaly Lipatov <lav@altlinux.ru> 2:1.26.6-alt2
- drop circle requires python3-module-ndg-httpsclient

* Thu Jul 01 2021 Grigory Ustinov <grenka@altlinux.org> 2:1.26.6-alt1
- 1.26.5 -> 1.26.6.

* Fri Jun 11 2021 Grigory Ustinov <grenka@altlinux.org> 2:1.26.5-alt1
- 1.25.10 -> 1.26.5 (Closes: #40197)
- Build without python2 support.
- Build without docs.

* Fri Jul 24 2020 Anton Farygin <rider@altlinux.ru> 2:1.25.10-alt1
- 1.25.6 -> 1.25.10

* Sat Oct 05 2019 Anton Farygin <rider@altlinux.ru> 2:1.25.6-alt1
- 1.24.3 -> 1.25.6

* Mon May 06 2019 Stanislav Levin <slev@altlinux.org> 2:1.24.3-alt1
- 1.24.2 -> 1.24.3 (fixes: CVE-2019-9740).

* Mon Apr 22 2019 Stanislav Levin <slev@altlinux.org> 2:1.24.2-alt1
- 1.24.1 -> 1.24.2 (fixes: CVE-2019-11324).

* Mon Dec 24 2018 Alexey Shabalin <shaba@altlinux.org> 2:1.24.1-alt2
- fixed import system six

* Mon Dec 24 2018 Alexey Shabalin <shaba@altlinux.org> 2:1.24.1-alt1
- 1.24.1

* Wed Sep 27 2017 Andrey Cherepanov <cas@altlinux.org> 2:1.21.1-alt1
- 1.21.1
- Add optional test check

* Wed Apr 20 2016 Alexey Shabalin <shaba@altlinux.ru> 2:1.15.1-alt1
- 1.15.1

* Mon Apr 11 2016 Ivan Zakharyaschev <imz@altlinux.org> 1:20150503-alt1.1.1.1
- (NMU) rebuild with rpm-build-python3-0.1.10 (for new-style python3(*) reqs)
  and with python3-3.5 (for byte-compilation).

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1:20150503-alt1.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 1:20150503-alt1.1
- NMU: Use buildreq for BR.

* Fri Sep 18 2015 Lenar Shakirov <snejok@altlinux.ru> 1:20150503-alt1
- Build old snapshot - 20150503 (1.10.4)
  * Problem between python-requests and urllib3
  * Epoch: 1

* Mon Aug 17 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 20150729-alt1
- New snapshot

* Thu Feb 26 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 20150222-alt1
- New snapshot

* Thu Feb 12 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 20150210-alt1
- New snapshot

* Tue Dec 23 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 20141214-alt1
- New snapshot

* Tue Aug 19 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 20140810-alt2
- New snapshot

* Tue Jul 22 2014 Lenar Shakirov <snejok@altlinux.ru> 20140708-alt2
- Unbundle ssl_match_hostname, ordereddict and six package
- Use system python-module-{six,backports.ssl_match_hostname,ordereddict}

* Tue Jul 15 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 20140708-alt1
- New snapshot
- Added module for Python 3

* Mon Dec 02 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 20131126-alt1
- New snapshot

* Thu Sep 19 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 20130915-alt1
- New snapshot

* Wed Apr 03 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 20130204-alt1
- Initial build for Sisyphus

