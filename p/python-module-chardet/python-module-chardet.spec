%define oname	chardet

Name: python-module-%oname
Summary: Character encoding auto-detection in Python
License: LGPL
Group: Development/Python
Version: 2.0.1
Release: alt1.1
Source0: %oname-%version.tar
Packager: Evgenii Terechkov <evg@altlinux.ru>

Url: http://chardet.feedparser.org/
BuildArch: noarch

BuildRequires: python-devel

%description
Character encoding auto-detection in Python.

%prep
%setup -n %oname-%version

%build
python setup.py build

%install
python setup.py install --root=%buildroot --prefix=%prefix --optimize=2 --record=INSTALLED_FILES

%files -f INSTALLED_FILES
%python_sitelibdir/%oname
%doc docs

%changelog
* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 2.0.1-alt1.1
- Rebuild with Python-2.7

* Mon Mar 22 2010 Terechkov Evgenii <evg@altlinux.ru> 2.0.1-alt1
- 2.0.1

* Wed Nov 11 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.1-alt1.3.1
- Rebuilt with python 2.6

* Fri Feb 20 2009 Terechkov Evgenii <evg@altlinux.ru> 1.0.1-alt1.3
- Site-packages removed from packages (Closes #18909)
- Packager tag added

* Wed Dec 31 2008 Terechkov Evgenii <evg@altlinux.ru> 1.0.1-alt1.2
- Really fix build on x86_64

* Wed Dec 31 2008 Terechkov Evgenii <evg@altlinux.ru> 1.0.1-alt1.1
- Egg dropped to build on x86_64

* Sun Dec 28 2008 Terechkov Evgenii <evg@altlinux.ru> 1.0.1-alt1
- Initial build for ALT Linux Sisyphus (thanks Mandriva for initial spec)
