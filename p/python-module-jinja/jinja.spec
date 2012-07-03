Name: python-module-jinja
Version: 1.2
Release: alt1.2.1.1
Summary: A small but fast template engine written in pure python
Summary(ru_RU.utf8): Небольшой, но быстрый движок шаблонов, написанный на python
License: BSD
Group: Development/Python
Url: http://jinja.pocoo.org/
Packager: Gennady Kovalev <gik@altlinux.ru>
Source0: jinja-%version.tar
#Patch0: jinja-%version-alt-allinone.patch

BuildPreReq: python python-module-setuptools

%description
A small but fast and easy to use stand-alone template engine written in pure python.

%description -l ru_RU.utf8
Небольшой, но очень быстрый, простой в использовании движок шаблонов, написанный на чистом python.

%prep
%setup -n jinja-%version
#patch0 -p1

%install
mkdir -p %buildroot
%python_build_debug
%python_install --install-data=%_datadir --optimize=2 \
	--record=INSTALLED_FILES
sed -i 's|%buildroot||g' INSTALLED_FILES

%files -f INSTALLED_FILES

%changelog
* Thu Apr 12 2012 Vitaly Kuznetsov <vitty@altlinux.ru> 1.2-alt1.2.1.1
- Rebuild to remove redundant libpython2.7 dependency

* Tue Nov 01 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.2-alt1.2.1
- Rebuild with Python-2.7

* Fri Mar 25 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2-alt1.2
- Rebuilt for debuginfo

* Thu Nov 19 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2-alt1.1
- Rebuilt with python 2.6

* Fri Feb 20 2009 Gennady Kovalev <gik@altlinux.ru> 1.2-alt1
- Initial build for sisyphus


