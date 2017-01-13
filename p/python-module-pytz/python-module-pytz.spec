%define _unpackaged_files_terminate_build 1
%define oname pytz

%def_with python3

Name: python-module-%oname
Epoch: 1
Version: 2016.10
Release: alt1

%setup_python_module %oname

Summary: World timezone definitions, modern and historical
Source0: https://pypi.python.org/packages/d0/e1/aca6ef73a7bd322a7fc73fd99631ee3454d4fc67dc2bee463e2adf6bb3d3/%{oname}-%{version}.tar.bz2
License: MIT
Group: Development/Python
BuildArch: noarch
Url: http://pytz.sourceforge.net

%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel
%endif

%description
pytz brings the Olson tz database into Python. This library allows
accurate and cross platform timezone calculations using Python 2.3
or higher. It also solves the issue of ambiguous times at the end
of daylight savings, which you can read more about in the Python
Library Reference (datetime.tzinfo).

%if_with python3
%package -n python3-module-%oname
Summary: World timezone definitions, modern and historical (Python 3)
Group: Development/Python3

%description -n python3-module-%oname
pytz brings the Olson tz database into Python. This library allows
accurate and cross platform timezone calculations using Python 2.3
or higher. It also solves the issue of ambiguous times at the end
of daylight savings, which you can read more about in the Python
Library Reference (datetime.tzinfo).

%package -n python3-module-%oname-tests
Summary: Tests for pytz (Python 3)
Group: Development/Python3
Requires: python3-module-%oname = %EVR

%description -n python3-module-%oname-tests
pytz brings the Olson tz database into Python. This library allows
accurate and cross platform timezone calculations using Python 2.3
or higher. It also solves the issue of ambiguous times at the end
of daylight savings, which you can read more about in the Python
Library Reference (datetime.tzinfo).

This package contains tests for pytz.
%endif

%package tests
Summary: Tests for pytz
Group: Development/Python
Requires: %name = %EVR

%description tests
pytz brings the Olson tz database into Python. This library allows
accurate and cross platform timezone calculations using Python 2.3
or higher. It also solves the issue of ambiguous times at the end
of daylight savings, which you can read more about in the Python
Library Reference (datetime.tzinfo).

This package contains tests for pytz.

%package -n %oname-zoneinfo
Summary: Archive with zoneinfo
Group: Development/Python

%description -n %oname-zoneinfo
Archive with zoneinfo.

%prep
%setup -q -n %{oname}-%{version}
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

%install
%python_install --optimize=2 --record=INSTALLED_FILES
install -d %buildroot%python_sitelibdir/%modulename/tests
install -p -m644 %modulename/tests/* \
	%buildroot%python_sitelibdir/%modulename/tests
touch %buildroot%python_sitelibdir/%modulename/tests/__init__.py

%if_with python3
pushd ../python3
%python3_install
install -d %buildroot%python3_sitelibdir/%oname/tests
install -p -m644 %oname/tests/* \
	%buildroot%python3_sitelibdir/%oname/tests
touch %buildroot%python3_sitelibdir/%oname/tests/__init__.py
popd
%endif

install -d %buildroot%_datadir/%modulename
pushd %buildroot%python_sitelibdir/%modulename/zoneinfo
tar -czf %buildroot%_datadir/%modulename/zoneinfo.tar.gz *
popd

%files -f INSTALLED_FILES
%python_sitelibdir/%modulename
%exclude %python_sitelibdir/%modulename/tests
%doc *.txt

%files tests
%python_sitelibdir/%modulename/tests

%files -n %oname-zoneinfo
%_datadir/%modulename

%if_with python3
%files -n python3-module-%oname
%doc *.txt
%python3_sitelibdir/*
%exclude %python3_sitelibdir/%oname/tests

%files -n python3-module-%oname-tests
%python3_sitelibdir/%oname/tests
%endif

%changelog
* Wed Jan 11 2017 Igor Vlasenko <viy@altlinux.ru> 1:2016.10-alt1
- automated PyPI update

* Mon Apr 11 2016 Ivan Zakharyaschev <imz@altlinux.org> 1:2015.4-alt1.1.1
- (NMU) rebuild with rpm-build-python3-0.1.10 (for new-style python3(*) reqs)
  and with python3-3.5 (for byte-compilation).

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1:2015.4-alt1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Fri Jul 31 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1:2015.4-alt1
- Version 2015.4

* Thu Dec 04 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1:2014.10-alt2
- Added %oname-zoneinfo

* Thu Nov 27 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1:2014.10-alt1
- Version 2014.10

* Mon Nov 03 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1:2014.9-alt1
- Version 2014.9

* Fri Sep 19 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1:2014.7-alt1
- Version 2014.7

* Mon Aug 25 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1:2014.4-alt1
- Version 2014.4

* Thu Jan 09 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1:2013.9-alt1
- Version 2013.9

* Mon Sep 23 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2013d-alt1
- Version 2013d

* Thu Feb 21 2013 Aleksey Avdeev <solo@altlinux.ru> 2012j-alt1
- Version 2012j

* Mon Apr 16 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2012c-alt1
- Version 2012c
- Added module for Python 3

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 2010o-alt1.1
- Rebuild with Python-2.7

* Sun Nov 28 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2010o-alt1
- Version 2010o

* Tue Aug 03 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2010k-alt1
- Version 2010k
- Added tests

* Fri Nov 13 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2009j-alt4.1
- Rebuilt with python 2.6

* Tue Jul 14 2009 Ivan Fedorov <ns@altlinux.org> 2009j-alt4
- fix unowned directories

* Tue Jul 14 2009 Ivan Fedorov <ns@altlinux.org> 2009j-alt3
- fix building

* Tue Jul 14 2009 Ivan Fedorov <ns@altlinux.org> 2009j-alt2
- fix building

* Mon Jul 13 2009 Ivan Fedorov <ns@altlinux.org> 2009j-alt1
- 2009j

* Thu Jan 24 2008 Grigory Batalov <bga@altlinux.ru> 2006p-alt1.1
- Rebuilt with python-2.5.

* Sun Feb 18 2007 Ivan Fedorov <ns@altlinux.ru> 2006p-alt1
- 2006p

* Thu Feb 02 2006 Ivan Fedorov <ns@altlinux.ru> 2005r-alt1
- 2005r

* Tue Oct 04 2005 Ivan Fedorov <ns@altlinux.ru> 2005m-alt1
- Initial build for ALT Linux.
