%define _unpackaged_files_terminate_build 1

%def_with docs

Summary: The PyPA recommended tool for installing Python packages
Name: python-module-pip
Version: 19.0.1
Release: alt1
Source0: pip-%version.tar.gz
License: MIT
Group: Development/Python
BuildArch: noarch
Url: http://www.pip-installer.org
Obsoletes: python-module-pip-pickles
%setup_python_module pip

%if_with docs
BuildRequires(pre): rpm-macros-sphinx
BuildRequires: python-module-sphinx
BuildRequires: python3-module-sphinx
%endif

BuildRequires(pre): rpm-build-python3

%description
%summary
%add_findprov_skiplist %python_sitelibdir/pip/_vendor/*

%if_with docs
%package docs
Summary: Documentation for pip
Group: Development/Documentation

%description docs
%summary

This package contains documentation for pip.
%endif

%package -n python3-module-%modulename
Summary: The PyPA recommended tool for installing Python packages
Group: Development/Python3
Obsoletes: python3-module-pip-pickles

%description -n python3-module-%modulename
%summary
%add_findprov_skiplist %python3_sitelibdir/pip/_vendor/*
%filter_from_requires /python3\(\.[[:digit:]]\)\?(pip\._vendor\..*)/d

%if_with docs
%package -n python3-module-%modulename-docs
Summary: Documentation for pip3
Group: Development/Documentation

%description -n python3-module-%modulename-docs
%summary

This package contains documentation for pip.
%endif

%prep
%setup -n %modulename-%version

%if_with docs
# XXX wait for packaging pypa_theme
sed -i '
s/pypa_theme/default/
/.navigation_depth.: 3,/s/^/#/
/.issues_url.:/s/^/#/
' docs/html/conf.py

%prepare_sphinx .
ln -s ../objects.inv docs/
%endif

%build
# py2 and py3 builds are identical
%python_build

%if_with docs
PYTHONPATH=`pwd`/build/lib sphinx-build-3 -c docs/html docs/html html3

PYTHONPATH=`pwd`/build/lib sphinx-build -c docs/html docs/html html2
%endif

%install
%python3_install
%python_install

%files
%doc *.txt *.rst
%_bindir/pip
%_bindir/pip2
%_bindir/pip2.7
%python_sitelibdir/pip/
%python_sitelibdir/pip-*.egg-info/

%if_with docs
%files docs
%doc html2

%files -n python3-module-%modulename-docs
%doc html3
%endif

%files -n python3-module-%modulename
%doc *.txt *.rst
%_bindir/pip3
%_bindir/pip3.6
%python3_sitelibdir/pip/
%python3_sitelibdir/pip-*.egg-info/

%changelog
* Sun Jan 27 2019 Stanislav Levin <slev@altlinux.org> 19.0.1-alt1
- 18.1 -> 19.0.1.

* Thu Oct 18 2018 Fr. Br. George <george@altlinux.ru> 18.1-alt1
- Autobuild version bump to 18.1
- Pickle modules removed

* Thu Aug 02 2018 Fr. Br. George <george@altlinux.ru> 18.0-alt1
- Autobuild version bump to 18.0

* Tue Jun 12 2018 Fr. Br. George <george@altlinux.ru> 10.0.1-alt2
- Autobuild version bump to 10.0.1
- Introduce python3 generated documentation

* Tue Jun 05 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 10.0.1-alt1
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
