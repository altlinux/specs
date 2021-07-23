# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-python rpm-build-python3
# END SourceDeps(oneline)
%define oldname python-webob
%define fedora 27
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%{!?py3ver: %global py3ver %(%{__python3} -c "import sys ; print(sys.version[:3])")}


%global modname webob
%global desc WebOb provides wrappers around the WSGI request environment, and an object to \
help create WSGI responses. The objects map much of the specified behavior of \
HTTP, including header parsing and accessors for other standard parts of the \
environment.


Name:           python3-module-webob
Summary:        WSGI request and response object
Version:        1.8.6
Release:        alt2
License:        MIT
Group:          System/Libraries
URL:            http://pythonpaste.org/webob/
Source0:        https://files.pythonhosted.org/packages/source/W/WebOb/WebOb-%{version}.tar.gz
Source1:        README.Fedora

BuildArch:      noarch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools

%if 0%{?with_tests}
BuildRequires:  python3-module-nose
BuildRequires:  python3-module-pytest
%endif # with_tests
Source44: import.info


%description
%{desc}

%prep
%setup -q -n WebOb-%{version}
cp -p %{SOURCE1} .
# Disable performance_test, which requires repoze.profile, which isn't
# in Fedora.
rm -f tests/performance_test.py

# Remove an empty unneeded file that is there for scm purposes.
rm docs/_static/.empty

%build
%{__python3} setup.py build

%install
%{__python3} setup.py install --skip-build --root %{buildroot}

%check
%{__python3} setup.py test

%files
%doc --no-dereference docs/license.txt
%doc docs/* README.Fedora
%{python3_sitelibdir_noarch}/webob/
%{python3_sitelibdir_noarch}/WebOb-%{version}-py%{py3ver}.egg-info

%changelog
* Fri Jul 23 2021 Grigory Ustinov <grenka@altlinux.org> 1.8.6-alt2
- Drop python2 support.

* Tue Mar 31 2020 Igor Vlasenko <viy@altlinux.ru> 1.8.6-alt1
- new version

* Wed Jan 09 2019 Alexey Shabalin <shaba@altlinux.org> 1.8.5-alt1
- new version

* Wed Mar 14 2018 Igor Vlasenko <viy@altlinux.ru> 1.7.4-alt1_3
- new version

* Wed Jan 18 2017 Igor Vlasenko <viy@altlinux.ru> 1.7.1-alt1
- automated PyPI update

* Wed Jan 11 2017 Igor Vlasenko <viy@altlinux.ru> 1.7.0-alt1
- automated PyPI update

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.5.0-alt1.a0.git20150731.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 1.5.0-alt1.a0.git20150731.1
- NMU: Use buildreq for BR.

* Sat Aug 29 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.5.0-alt1.a0.git20150731
- Version 1.5.0a0

* Fri Feb 06 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.4.1-alt1.dev.git20150127
- Version 1.4.1dev

* Wed Jul 16 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.4-alt1
- Version 1.4

* Thu Jan 09 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.3.1-alt1
- Version 1.3.1

* Sun Mar 03 2013 Aleksey Avdeev <solo@altlinux.ru> 1.2.3-alt1
- Version 1.2.3

* Sat May 05 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2-alt1.b3.git20120504
- Version 1.2b3
- Added module for Python 3

* Mon Dec 12 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2-alt1.b2.git20111206
- Version 1.2b2

* Mon Dec 12 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1.1-alt1.hg20110917
- Version 1.1.1

* Mon Oct 24 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.0.7-alt1.hg20110430.1
- Rebuild with Python-2.7

* Tue May 10 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.7-alt1.hg20110430
- Version 1.0.7

* Fri Nov 19 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0-alt1.hg20101031
- Version 1.0

* Thu Jul 15 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9.8.post1-alt1.hg20100714
- Version 0.9.8.post1

* Thu Nov 19 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9.7-alt1.svn20090902.1
- Rebuilt with python 2.6

* Mon Sep 28 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9.7-alt1.svn20090902
- Initial build for Sisyphus

