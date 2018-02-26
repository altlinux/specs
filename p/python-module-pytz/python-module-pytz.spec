%define oname pytz

%def_with python3

Name: python-module-%oname
Version: 2012c
Release: alt1

%setup_python_module %oname

Summary: World timezone definitions, modern and historical
Source0: %modulename-%version.tar
License: MIT
Group: Development/Python
BuildArch: noarch
Url: http://pytz.sourceforge.net

Packager: Python Development Team <python@packages.altlinux.org>

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
Requires: python3-module-%oname = %version-%release

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
Requires: %name = %version-%release

%description tests
pytz brings the Olson tz database into Python. This library allows
accurate and cross platform timezone calculations using Python 2.3
or higher. It also solves the issue of ambiguous times at the end
of daylight savings, which you can read more about in the Python
Library Reference (datetime.tzinfo).

This package contains tests for pytz.

%prep
%setup -n %modulename-%version
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

%files -f INSTALLED_FILES
%python_sitelibdir/%modulename
%exclude %python_sitelibdir/%modulename/tests
%doc *.txt

%files tests
%python_sitelibdir/%modulename/tests

%if_with python3
%files -n python3-module-%oname
%doc *.txt
%python3_sitelibdir/*
%exclude %python3_sitelibdir/%oname/tests

#files -n python3-module-%oname-tests
#python3_sitelibdir/%oname/tests
%endif

%changelog
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
