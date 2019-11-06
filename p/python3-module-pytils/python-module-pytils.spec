%define oname pytils

Name: python3-module-%oname
Version: 0.3
Release: alt2

Summary: Utils for easy processing string in russian.
Source: %oname-%version.tar
License: GPL
Group: Development/Python3
URL: http://www.pyobject.ru/projects/pytils/
BuildArch: noarch

BuildRequires(pre): rpm-build-python3


%description
Simple tools for processing string in russian (choose proper form for plurals,
in-words representation of numerals, dates in russian without locales,
transliteration, etc)

%prep
%setup -n %oname-%version

%build
%python3_build

%install
%python3_install

%files
%doc doc/* Changelog LICENSE TODO AUTHORS
%python3_sitelibdir/*


%changelog
* Wed Nov 06 2019 Andrey Bychkov <mrdrew@altlinux.org> 0.3-alt2
- disable python2

* Wed May 16 2018 Andrey Bychkov <mrdrew@altlinux.org> 0.3-alt1.2
- (NMU) rebuild with python3.6

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

