%define oname urllib3

%def_with python3

Name: python-module-%oname
Version: 20150503
Release: alt1.1.1

Epoch: 1

Summary: Library with thread-safe connection pooling, file post support, sanity friendly etc
License: MIT
Group: Development/Python

Url: https://github.com/shazow/urllib3/

# make all imports of things in packages try system copies first
Patch0:         python-urllib3-unbundle.patch

# https://github.com/shazow/urllib3.git
Source: %name-%version.tar
BuildArch: noarch

BuildRequires(pre): rpm-build-python
BuildRequires(pre): rpm-macros-sphinx
# Automatically added by buildreq on Thu Jan 28 2016 (-bi)
# optimized out: python-base python-devel python-module-OpenSSL python-module-PyStemmer python-module-Pygments python-module-babel python-module-cffi python-module-cryptography python-module-cssselect python-module-enum34 python-module-genshi python-module-jinja2 python-module-jinja2-tests python-module-markupsafe python-module-ndg python-module-pyasn1 python-module-pytz python-module-setuptools python-module-six python-module-snowballstemmer python-module-sphinx python-module-sphinx_rtd_theme python-modules python-modules-compiler python-modules-ctypes python-modules-email python-modules-encodings python-modules-json python-modules-logging python-modules-multiprocessing python-modules-unittest python3 python3-base
BuildRequires: python-module-alabaster python-module-docutils python-module-html5lib python-module-ndg-httpsclient python-module-objects.inv rpm-build-python3 time

#BuildRequires:  python-module-six python-module-backports.ssl_match_hostname
#BuildRequires: python-module-ndg-httpsclient
#BuildPreReq: python-module-sphinx-devel
%if_with python3
BuildRequires(pre): rpm-build-python3
#BuildPreReq: python3-devel
%endif

%setup_python_module %oname

Requires: python-module-ndg-httpsclient
Requires: python-module-six python-module-backports.ssl_match_hostname ca-certificates
%py_requires ndg.httpsclient

%description
Python HTTP library with thread-safe connection pooling, file post
support, sanity friendly, and more.

%package -n python3-module-%oname
Summary: Library with thread-safe connection pooling, file post support, sanity friendly etc
Group: Development/Python3
Requires: python3-module-ndg-httpsclient
Requires: python3-module-six ca-certificates

%description -n python3-module-%oname
Python HTTP library with thread-safe connection pooling, file post
support, sanity friendly, and more.

%package -n python3-module-%oname-tests
Summary: Tests for urllib3
Group: Development/Python3
Requires: python3-module-%oname = %EVR

%description -n python3-module-%oname-tests
Python HTTP library with thread-safe connection pooling, file post
support, sanity friendly, and more.

This package contains tests for urllib3.

%package tests
Summary: Tests for urllib3
Group: Development/Python
Requires: %name = %EVR

%description tests
Python HTTP library with thread-safe connection pooling, file post
support, sanity friendly, and more.

This package contains tests for urllib3.

%package pickles
Summary: Pickles for urllib3
Group: Development/Python

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

%prep
%setup

#rm -rf urllib3/packages/

#patch0 -p1

%if_with python3
cp -fR . ../python3
%endif

%prepare_sphinx .
ln -s ../objects.inv docs/

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

export PYTHONPATH=%buildroot%python_sitelibdir
pushd docs
%make html
%make pickle
popd

cp -fR docs/_build/pickle %buildroot%python_sitelibdir/%oname/

%files
%doc *.txt *.rst
%python_sitelibdir/*
#exclude %python_sitelibdir/*/test*
%exclude %python_sitelibdir/*/pickle

#files tests
#python_sitelibdir/*/test*

%files pickles
%python_sitelibdir/*/pickle

%files docs
%doc docs/_build/html/*

%if_with python3
%files -n python3-module-%oname
%doc *.txt *.rst
%python3_sitelibdir/*
#exclude %python3_sitelibdir/*/test*

#files -n python3-module-%oname-tests
#python3_sitelibdir/*/test*
%endif

%changelog
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

