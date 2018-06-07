%define _unpackaged_files_terminate_build 1

%define oname pip

%def_with python3
%def_without doc

Summary: pip installs packages.  Python packages.  An easy_install replacement
Name: python-module-%oname
Version: 10.0.1
Release: alt1%ubt
License: MIT
Group: Development/Python
BuildArch: noarch
Url: http://www.pip-installer.org

# https://github.com/pypa/pip.git
Source: %name-%version.tar

BuildRequires(pre): rpm-build-ubt
BuildRequires: python-module-setuptools

%if_with doc
BuildRequires(pre): rpm-macros-sphinx
BuildRequires: python-module-alabaster python-module-docutils python-module-html5lib python-module-objects.inv
%endif

%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools
%add_python3_req_skip  UserDict
%endif

%description
%summary

%if_with doc
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
%endif

%if_with python3
%package -n python3-module-%oname
Summary: pip installs packages.  Python packages.  An easy_install replacement
Group: Development/Python3
%py3_provides %oname pip._vendor.six.moves pip._vendor.six.moves.urllib pip._vendor.six.moves.urllib.parse

%description -n python3-module-%oname
%summary
%endif

%prep
%setup

%if_with python3
cp -a . ../python3
%endif

%if_with doc
%prepare_sphinx .
ln -s ../objects.inv docs/
%endif

%build
%python_build

%if_with python3
pushd ../python3
%python3_build
popd
%endif

%install
%if_with python3
pushd ../python3
%python3_install
popd
%endif

%python_install

%if_with doc
export PYTHONPATH=%buildroot%python_sitelibdir
%make -C docs pickle
%make -C docs html

cp -fR docs/_build/pickle %buildroot%python_sitelibdir/%oname/
%endif

%files
%doc *.txt *.rst
%_bindir/*
%if_with python3
%exclude %_bindir/pip3*
%endif
%python_sitelibdir/*
%if_with doc
%exclude %python_sitelibdir/*/pickle

%files pickles
%python_sitelibdir/*/pickle

%files docs
%doc docs/_build/html/*
%endif

%if_with python3
%files -n python3-module-%oname
%doc *.txt *.rst
%_bindir/pip3*
%python3_sitelibdir/*
%endif

%changelog
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
