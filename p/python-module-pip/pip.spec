
%def_with python3

Summary: pip installs packages.  Python packages.  An easy_install replacement
Name: python-module-pip
Version: 9.0.1
Release: alt1.1
Source0: pip-%version.tar.gz
Patch: pip-1.5.6-alt-python3.patch
License: MIT
Group: Development/Python
BuildArch: noarch
Url: http://www.pip-installer.org
%setup_python_module pip

BuildRequires(pre): rpm-macros-sphinx
# Automatically added by buildreq on Thu Jan 28 2016 (-bi)
# optimized out: python-base python-devel python-module-PyStemmer python-module-Pygments python-module-SQLAlchemy python-module-babel python-module-cssselect python-module-genshi python-module-jinja2 python-module-jinja2-tests python-module-lxml python-module-markupsafe python-module-pluggy python-module-py python-module-pytest python-module-pytz python-module-setuptools python-module-simplejson python-module-six python-module-snowballstemmer python-module-sphinx python-module-sphinx_rtd_theme python-module-whoosh python-modules python-modules-compiler python-modules-ctypes python-modules-email python-modules-encodings python-modules-json python-modules-logging python-modules-multiprocessing python-modules-unittest python-modules-xml python3 python3-base python3-module-pytest python3-module-setuptools xz
BuildRequires: python-module-alabaster python-module-docutils python-module-html5lib python-module-objects.inv python-module-setuptools python3-module-setuptools rpm-build-python3 time

#BuildRequires: python-module-setuptools
#BuildPreReq: python-module-sphinx-devel
%if_with python3
BuildRequires(pre): rpm-build-python3
%add_python3_req_skip  UserDict
%endif

%description
%summary

%package pickles
Summary: Pickles for pip
Group: Development/Python

%description pickles
%summary

This package contains pickles for pip.

%package docs
Summary: Documentation for pip
Group: Development/Documentation

%description docs
%summary

This package contains documentation for pip.

%if_with python3
%package -n python3-module-%modulename
Summary: pip installs packages.  Python packages.  An easy_install replacement
Group: Development/Python3
%py3_provides %modulename pip._vendor.six.moves pip._vendor.six.moves.urllib

%description -n python3-module-%modulename
%summary
%endif

%prep
%setup -n %modulename-%version

%prepare_sphinx .
ln -s ../objects.inv docs/

%build
%python_build

%install
%python3_install
%python_install

export PYTHONPATH=%buildroot%python_sitelibdir
%make -C docs pickle
%make -C docs html

cp -fR docs/_build/pickle %buildroot%python_sitelibdir/%modulename/

%files
%doc *.txt *.rst
%_bindir/*
%if_with python3
%exclude %_bindir/pip3*
%endif
%python_sitelibdir/*
%exclude %python_sitelibdir/*/pickle

%files pickles
%python_sitelibdir/*/pickle

%files docs
%doc docs/_build/html/*

%if_with python3
%files -n python3-module-%modulename
%doc *.txt *.rst
%_bindir/pip3*
%python3_sitelibdir/*
%endif

%changelog
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 9.0.1-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Mon Mar 13 2017 Fr. Br. George <george@altlinux.ru> 9.0.1-alt1
- Autobuild version bump to 9.0.1

* Mon Oct 31 2016 Fr. Br. George <george@altlinux.ru> 8.1.2-alt1
- Autobuild version bump to 8.1.2
- Fix python3 version

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 8.0.2-alt1.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 8.0.2-alt1.1
- NMU: Use buildreq for BR.

* Tue Jan 26 2016 Fr. Br. George <george@altlinux.ru> 8.0.2-alt1
- Autobuild version bump to 8.0.2

* Tue Jan 26 2016 Fr. Br. George <george@altlinux.ru> 7.1.2-alt2
- New build scheme

* Sun Aug 23 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 7.1.2-alt1
- Version 7.1.2

* Wed Aug 12 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 7.1.0-alt1
- Version 7.1.0

* Mon Jan 19 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 6.0.6-alt1
- Version 6.0.6

* Wed Dec 24 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 6.0.3-alt1
- Version 6.0.3

* Tue Dec 23 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 6.0.1-alt1
- Version 6.0.1

* Sat Jul 19 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.5.6-alt1
- Version 1.5.6
- Added module for Python 3

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.0-alt1.1
- Rebuild with Python-2.7

* Fri Jun 10 2011 Sergey Alembekov <rt@altlinux.ru> 1.0-alt1
- new version
- spec fixes

* Sun Mar 20 2011 Sergey Alembekov <rt@altlinux.ru> 0.8.3-alt1
- initial build for ALTLinux
