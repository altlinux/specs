%define version 0.3
%define release alt1
%setup_python_module pytils

%def_with python3

Summary: Utils for easy processing string in russian.
Name: %packagename
Version: %version
Release: alt1.1
Source: %modulename-%version.tar
License: GPL
Group: Development/Python
BuildArch: noarch
URL: http://www.pyobject.ru/projects/pytils/

%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel
%endif

%description
Simple tools for processing string in russian (choose proper form for plurals,
in-words representation of numerals, dates in russian without locales,
transliteration, etc)

%package -n python3-module-%modulename
Summary: Utils for easy processing string in russian
Group: Development/Python3

%description -n python3-module-%modulename
Simple tools for processing string in russian (choose proper form for plurals,
in-words representation of numerals, dates in russian without locales,
transliteration, etc)

%prep
%setup -n %modulename-%version

%if_with python3
cp -fR . ../python3
%endif

%build
%python_build

%if_with python3
pushd ../python3
%python3_build
popd
%endif

%install
%python_install --record=INSTALLED_FILES

%if_with python3
pushd ../python3
%python3_install
popd
%endif

%files -f INSTALLED_FILES
%doc doc/* Changelog LICENSE TODO AUTHORS

%if_with python3
%files -n python3-module-%modulename
%doc doc/* Changelog LICENSE TODO AUTHORS
%python3_sitelibdir/*
%endif

%changelog
* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.3-alt1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Mon Aug 25 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3-alt1
- Version 0.3
- Added module for Python 3

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.2.3-alt3.1
- Rebuild with Python-2.7

* Thu Nov 19 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2.3-alt3
- Rebuilt with python 2.6

* Tue Nov 10 2009 Denis Klimov <zver@altlinux.org> 0.2.3-alt2
- new version from e4c8b0 hg snapshot
- Remove Vendor tag

* Fri Jan 30 2009 Denis Klimov <zver@altlinux.org> 0.2.3-alt1
- new version
- use tar source archive type
- remove needless -q option in setup macros

* Thu Jan 24 2008 Grigory Batalov <bga@altlinux.ru> 0.2.2-alt1.1
- Rebuilt with python-2.5.

* Mon Aug 13 2007 Andrew Kornilov <hiddenman@altlinux.ru> 0.2.2-alt1
- First build for Sisyphus

