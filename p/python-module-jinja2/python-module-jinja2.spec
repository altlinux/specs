%define oname jinja2

%def_with doc
%def_with python3
%def_disable check

Name: python-module-%oname
Version: 2.9
Release: alt1.dev.git20150726.1.1.1.1

Summary: The new and improved version of a small but fast template engine
License: BSD
Group: Development/Python
Url: http://jinja.pocoo.org/2/

Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/mitsuhiko/jinja2.git
Source0: %name-%version.tar
#Patch: %name-%version-%release.patch

BuildArch: noarch

#BuildPreReq: python-devel python-module-setuptools-tests
# for docs
#BuildPreReq: python-module-sphinx python-module-Pygments
#BuildPreReq: python-module-jinja2-tests python-module-markupsafe
%if_with python3
BuildRequires(pre): rpm-build-python3
# Automatically added by buildreq on Thu Jan 28 2016 (-bi)
# optimized out: python-base python-devel python-module-PyStemmer python-module-Pygments python-module-babel python-module-cssselect python-module-genshi python-module-jinja2 python-module-jinja2-tests python-module-markupsafe python-module-pytz python-module-setuptools python-module-six python-module-snowballstemmer python-module-sphinx python-module-sphinx_rtd_theme python-modules python-modules-compiler python-modules-ctypes python-modules-email python-modules-encodings python-modules-json python-modules-logging python-modules-multiprocessing python-modules-unittest python3 python3-base python3-module-setuptools
BuildRequires: python-module-alabaster python-module-docutils python-module-html5lib python-module-pytest python3-module-pytest rpm-build-python3 time

#BuildRequires: python3-devel python3-module-setuptools-tests
#BuildPreReq: python-tools-2to3
%endif

Requires: %name-tests = %version-%release

%description
Jinja2 is a template engine written in pure Python. It provides a Django
inspired non-XML syntax but supports inline expressions and an optional
sandboxed environment.

%if_with python3
%package -n python3-module-%oname
Summary: The new and improved version of a small but fast template engine (Python 3)
Group: Development/Python3
Requires: python3-module-%oname-tests = %version-%release

%description -n python3-module-%oname
Jinja2 is a template engine written in pure Python. It provides a Django
inspired non-XML syntax but supports inline expressions and an optional
sandboxed environment.

%package -n python3-module-%oname-tests
Summary: Tests for Jinja2 (Python 3)
Group: Development/Python3
Requires: python3-module-%oname = %version-%release

%description -n python3-module-%oname-tests
Jinja2 is a template engine written in pure Python. It provides a Django
inspired non-XML syntax but supports inline expressions and an optional
sandboxed environment.

This package contains tests for Jinja2.
%endif

%package tests
Summary: Tests for Jinja2
Group: Development/Python
Requires: %name = %version-%release

%description tests
Jinja2 is a template engine written in pure Python. It provides a Django
inspired non-XML syntax but supports inline expressions and an optional
sandboxed environment.

This package contains tests for Jinja2.

%package doc
Summary: Documentation for Jinja2
Group: Development/Documentation

%description doc
Jinja2 is a template engine written in pure Python. It provides a Django
inspired non-XML syntax but supports inline expressions and an optional
sandboxed environment.

This package contains HTML documentation for Jinja2.

%package pickles
Summary: Pickles for Jinja2
Group: Development/Python

%description pickles
Jinja2 is a template engine written in pure Python. It provides a Django
inspired non-XML syntax but supports inline expressions and an optional
sandboxed environment.

This package contains pickles for Jinja2.


%prep
%setup
%if_with python3
rm -rf ../python3
cp -a . ../python3
%endif

%build
%python_build
%if_with python3
pushd ../python3
%python3_build
popd
%endif

%if_with doc
%make_build -C docs html
%make_build -C docs pickle
%endif

%install
%python_install
# IronPython support
rm -f %buildroot%python_sitelibdir_noarch/jinja2/_ipysupport.py

%if_with python3
pushd ../python3
%python3_install
popd
rm -f %buildroot%python3_sitelibdir_noarch/jinja2/_ipysupport.py
%endif

%if_with doc
cp -fR docs/_build/pickle %buildroot%python_sitelibdir_noarch/jinja2/
%endif

%check
make test

%files
%python_sitelibdir_noarch/jinja2/
%python_sitelibdir_noarch/*.egg-info
%exclude %python_sitelibdir_noarch/jinja2/tests.py*
#exclude %python_sitelibdir_noarch/jinja2/testsuite
%if_with doc
%exclude %python_sitelibdir_noarch/jinja2/pickle
%doc ext/
%endif
%doc AUTHORS CHANGES

%files tests
%python_sitelibdir_noarch/jinja2/tests.py*
#python_sitelibdir_noarch/jinja2/testsuite

%if_with doc
%files doc
%doc docs/_build/html/*

%files pickles
%dir %python_sitelibdir_noarch/jinja2
%python_sitelibdir_noarch/jinja2/pickle
%endif

%if_with python3
%files -n python3-module-%oname
%doc AUTHORS CHANGES
%python3_sitelibdir_noarch/jinja2/
%python3_sitelibdir_noarch/*.egg-info
%exclude %python3_sitelibdir_noarch/jinja2/tests.py*
%exclude %python3_sitelibdir_noarch/jinja2/*/tests.*
#exclude %python3_sitelibdir_noarch/jinja2/testsuite

%files -n python3-module-%oname-tests
%python3_sitelibdir_noarch/jinja2/tests.py*
%python3_sitelibdir_noarch/jinja2/*/tests.*
#python3_sitelibdir_noarch/jinja2/testsuite
%endif

%changelog
* Sat Jan 14 2017 Michael Shigorin <mike@altlinux.org> 2.9-alt1.dev.git20150726.1.1.1.1
- BOOTSTRAP: introduced doc knob (avoid sphinx)

* Mon Apr 11 2016 Ivan Zakharyaschev <imz@altlinux.org> 2.9-alt1.dev.git20150726.1.1.1
- (NMU) rebuild with rpm-build-python3-0.1.10 (for new-style python3(*) reqs)
  and with python3-3.5 (for byte-compilation).

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 2.9-alt1.dev.git20150726.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 2.9-alt1.dev.git20150726.1
- NMU: Use buildreq for BR.

* Thu Jul 30 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.9-alt1.dev.git20150726
- Version 2.9.dev

* Fri Jul 11 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.8-alt2.git20140610
- New snapshot

* Tue Jan 14 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.8-alt2.git20140110
- New snapshot

* Fri Nov 29 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.8-alt2.git20130807
- Added requirement on tests for python3-module-%oname

* Tue Sep 17 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.8-alt1.git20130807
- Version 2.8

* Wed Mar 27 2013 Aleksey Avdeev <solo@altlinux.ru> 2.7-alt1.git20120916
- New snapshot

* Fri Apr 13 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.7-alt1.git20120313
- New snapshot
- Added module for Python 3

* Fri Dec 23 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.7-alt1.git20111215
- Version 2.7

* Fri Dec 09 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.6-alt1
- Version 2.6

* Fri Nov 25 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.5.5-alt2
- Enabled docs

* Fri Oct 21 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 2.5.5-alt1.1
- Rebuild with Python-2.7 (bootstraping without docs)

* Tue Nov 23 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.5.5-alt1
- Version 2.5.5

* Mon Aug 02 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.5-alt2
- Added requirement on tests package

* Mon Aug 02 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.5-alt1
- Version 2.5
- Extracted tests into separate package
- Added pickles

* Thu Nov 12 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.2.1-alt1.2
- Enable building of documentation

* Thu Nov 12 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.2.1-alt1.1
- Rebuilt with python 2.6 (bootstrap)

* Thu Sep 17 2009 Andrey Rahmatullin <wrar@altlinux.ru> 2.2.1-alt1
- 2.2.1
- enable building of documentation
- build as noarch

* Mon May 04 2009 Andrey Rahmatullin <wrar@altlinux.ru> 2.1.1-alt1
- initial build
