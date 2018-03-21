%define modname daemon

Name: python-module-%modname
Version: 2.1.2
Release: alt1

Summary: Library to implement a well-behaved Unix daemon process
License: Apache-2.0 / GPLv3
Group: Development/Python
Url: http://pypi.python.org/pypi/python-daemon/
Packager: Python Development Team <python@packages.altlinux.org>
BuildArch: noarch

Source: daemon-%version.tar

# Automatically added by buildreq on Wed Jan 27 2016 (-bi)
# optimized out: python-base python-devel python-module-PyStemmer python-module-Pygments python-module-babel python-module-cssselect python-module-genshi python-module-jinja2 python-module-pytz python-module-snowballstemmer python-module-sphinx python-modules python-modules-compiler python-modules-ctypes python-modules-email python-modules-encodings python-modules-unittest python3 python3-base python3-module-Pygments python3-module-babel python3-module-cssselect python3-module-docutils python3-module-genshi python3-module-jinja2 python3-module-pytz python3-module-setuptools python3-module-snowballstemmer

BuildRequires: python-module-setuptools
BuildRequires: python-module-docutils
BuildRequires: python-module-html5lib
BuildRequires: python-modules-json

BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-module-html5lib
BuildPreReq: python3-module-sphinx
BuildPreReq: python3-module-setuptools
#BuildPreReq: python-module-docutils
#BuildPreReq: python-module-html5lib
#BuildPreReq: python-modules-json
#BuildRequires: python-module-setuptools
#BuildPreReq: python-module-lockfile > 0.10 python-module-docutils

#BuildRequires: python3-devel python3-module-setuptools
#BuildRequires: python3-module-lockfile > 0.10 python3-module-simplejson python3-module-docutils
#BuildPreReq: python-tools-2to3


%description
A well-behaved Unix daemon process is tricky to get right, but the required steps are much the same for every daemon program. A DaemonContext instance holds the behaviour and configured process environment for the program; use the instance as a context manager to enter a daemon state.

%package -n python3-module-%modname
Summary: Library to implement a well-behaved Unix daemon process
Group: Development/Python3
%py3_provides %modname

%description -n python3-module-%modname
A well-behaved Unix daemon process is tricky to get right, but the required steps are much the same for every daemon program. A DaemonContext instance holds the behaviour and configured process environment for the program; use the instance as a context manager to enter a daemon state.

%prep
%setup -n daemon-%version

rm -rf ../python3
cp -fR . ../python3

%build
%python_build

export LANG=en_GB.utf8
echo $LANG

pushd ../python3
%python3_build
popd

%install
%python_install

export LANG=en_GB.utf8
echo $LANG

pushd ../python3
%python3_install
popd

%files
%doc ChangeLog LICENSE.* README doc/*
%python_sitelibdir/%modname
%python_sitelibdir/python_daemon*

%files -n python3-module-%modname
%doc ChangeLog LICENSE.* README doc/*
%python3_sitelibdir/%modname
%python3_sitelibdir/python_daemon*


%changelog
* Wed Mar 21 2018 Andrey Bychkov <mrdrew@altlinux.org> 2.1.2-alt1
- Version 2.1.2

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 2.0.5-alt2.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Mon Mar 07 2016 Dmitry V. Levin (QA) <qa_ldv@altlinux.org> 2.0.5-alt2
- NMU: added python-modules-json and python-module-setuptools to BRs.

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 2.0.5-alt1.1
- NMU: Use buildreq for BR.

* Wed Aug 19 2015 Terechkov Evgenii <evg@altlinux.org> 2.0.5-alt1
- Update to 2.0.5

* Thu Jul 31 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.5.5-alt3
- Added module for Python 3

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.5.5-alt2.1
- Rebuild with Python-2.7

* Fri Aug 13 2010 Vladimir V. Kamarzin <vvk@altlinux.org> 1.5.5-alt2
- pidlockfile.py: add checking for stale {pid,lock}file

* Sun Apr 04 2010 Denis Klimov <zver@altlinux.org> 1.5.5-alt1
- Initial build for ALT Linux
