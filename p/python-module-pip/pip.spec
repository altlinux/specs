Summary: pip installs packages.  Python packages.  An easy_install replacement
Name: python-module-pip
Version: 10.0.1
Release: alt2
Source0: pip-%version.tar.gz
Patch: pip-1.5.6-alt-python3.patch
License: MIT
Group: Development/Python
BuildArch: noarch
Url: http://www.pip-installer.org
%setup_python_module pip

BuildRequires(pre): rpm-macros-sphinx
# Automatically added by buildreq on Wed Jun 13 2018 (-bi)
# optimized out: python-base python-devel python-module-OpenSSL python-module-PyStemmer python-module-Pygments python-module-SQLAlchemy python-module-asn1crypto python-module-attrs python-module-babel python-module-backports python-module-backports.ssl_match_hostname python-module-cffi python-module-chardet python-module-cryptography python-module-docutils python-module-enum34 python-module-funcsigs python-module-idna python-module-imagesize python-module-ipaddress python-module-jinja2 python-module-lxml python-module-markupsafe python-module-ndg-httpsclient python-module-ntlm python-module-pluggy python-module-py python-module-pycparser python-module-pytest python-module-pytz python-module-requests python-module-setuptools python-module-simplejson python-module-six python-module-sphinx python-module-sphinxcontrib python-module-typing python-module-urllib3 python-module-webencodings python-module-whoosh python-modules python-modules-compiler python-modules-ctypes python-modules-email python-modules-encodings python-modules-json python-modules-logging python-modules-multiprocessing python-modules-unittest python-modules-xml python-sphinx-objects.inv python3 python3-base python3-module-OpenSSL python3-module-Pygments python3-module-asn1crypto python3-module-babel python3-module-cffi python3-module-chardet python3-module-cryptography python3-module-docutils python3-module-idna python3-module-imagesize python3-module-jinja2 python3-module-markupsafe python3-module-pytz python3-module-requests python3-module-setuptools python3-module-six python3-module-sphinx python3-module-urllib3 rpm-build-python3 xz
BuildRequires: ctags python-module-alabaster python-module-html5lib python-module-sphinxcontrib-websupport python3-module-alabaster python3-module-sphinxcontrib-websupport time

#BuildRequires: python-module-setuptools
#BuildPreReq: python-module-sphinx-devel
BuildRequires(pre): rpm-build-python3
##add_python3_req_skip  UserDict

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

%package -n python3-module-%modulename
Summary: pip installs packages.  Python packages.  An easy_install replacement
Group: Development/Python3
%py3_provides %modulename pip._vendor.six.moves pip._vendor.six.moves.urllib pip._vendor.six.moves.urllib.parse

%description -n python3-module-%modulename
%summary

%package -n python3-module-%modulename-pickles
Summary: Pickles for pip3
Group: Development/Python3

%description -n python3-module-%modulename-pickles
%summary

This package contains pickles for pip.

%package -n python3-module-%modulename-docs
Summary: Documentation for pip3
Group: Development/Documentation

%description -n python3-module-%modulename-docs
%summary

This package contains documentation for pip.

%prep
%setup -n %modulename-%version

# XXX wait for packaging pypa_theme
sed -i '
s/pypa_theme/default/
/.navigation_depth.: 3,/s/^/#/
/.issues_url.:/s/^/#/
' docs/conf.py


%prepare_sphinx .
ln -s ../objects.inv docs/

%build
# py2 and py3 builds are identical
%python_build

PYTHONPATH=`pwd`/build/lib %make -C docs pickle BUILDDIR=build2
PYTHONPATH=`pwd`/build/lib %make -C docs html BUILDDIR=build2

PYTHONPATH=`pwd`/build/lib %make -C docs pickle BUILDDIR=build3 SPHINXBUILD=py3_sphinx-build
PYTHONPATH=`pwd`/build/lib %make -C docs html BUILDDIR=build3 SPHINXBUILD=py3_sphinx-build

%install
%python3_install
%python_install

cp -fR docs/build2/pickle %buildroot%python_sitelibdir/%modulename/
cp -fR docs/build2/pickle %buildroot%python3_sitelibdir/%modulename/

%files
%doc *.txt *.rst
%_bindir/*
%exclude %_bindir/pip3*
%python_sitelibdir/*
%exclude %python_sitelibdir/*/pickle

%files pickles
%python_sitelibdir/*/pickle

%files docs
%doc docs/build2/html/*

%files -n python3-module-%modulename
%doc *.txt *.rst
%_bindir/pip3*
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/pickle

%files -n python3-module-%modulename-pickles
%python3_sitelibdir/*/pickle

%files -n python3-module-%modulename-docs
%doc docs/build3/html/*

%changelog
* Tue Jun 12 2018 Fr. Br. George <george@altlinux.ru> 10.0.1-alt2
- Autobuild version bump to 10.0.1
- Introduce python3 generated documentation

* Tue Jun 05 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 10.0.1-alt1%ubt
- Updated to upstream version 10.0.1.

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
