%define version 0.2.3
%define release alt3
%setup_python_module pytils

Summary: Utils for easy processing string in russian.
Name: %packagename
Version: %version
Release: %release.1
Source: %modulename-%version.tar
License: GPL
Group: Development/Python
BuildArch: noarch
URL: http://www.pyobject.ru/projects/pytils/
Packager: Denis Klimov <zver@altlinux.org>

%description
Simple tools for processing string in russian (choose proper form for plurals,
in-words representation of numerals, dates in russian without locales,
transliteration, etc)

%prep
%setup -n %modulename-%version

%build
%__python setup.py build

%install
%__python setup.py install --root=%buildroot --optimize=2 --record=INSTALLED_FILES

%files -f INSTALLED_FILES
%doc doc/* Changelog LICENSE README TODO AUTHORS
%defattr(-,root,root)

%changelog
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

