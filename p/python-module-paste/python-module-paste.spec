%define modulename paste

%def_with python3

Name: python-module-%modulename
Version: 1.7.5.1
Release: alt1.hg20120305

Summary: Tools for using a Web Server Gateway Interface stack
License: MIT
Group: Development/Python

Url: http://pythonpaste.org
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>
BuildArch: noarch

Source: %name-%version.tar

BuildPreReq: python-module-setuptools
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python3-module-distribute
BuildPreReq: python-tools-2to3
%endif

%setup_python_module %modulename
%py_provides Paste

%add_python_req_skip flup openid scgi

%description
These provide several pieces of "middleware" (or filters) that can be
nested to build web applications. Each piece of middleware uses the
WSGI (PEP 333) interface, and should be compatible with other
middleware based on those interfaces.

%if_with python3
%package -n python3-module-%modulename
Summary: Tools for using a Web Server Gateway Interface stack (Python 3)
Group: Development/Python3
%py3_provides Paste
%add_python3_req_skip flup openid scgi hotshot

%description -n python3-module-%modulename
These provide several pieces of "middleware" (or filters) that can be
nested to build web applications. Each piece of middleware uses the
WSGI (PEP 333) interface, and should be compatible with other
middleware based on those interfaces.
%endif

%prep
%setup
#rm -f paste/util/subprocess24.py
sed -i -e '/^#!.*/,1 d' \
	paste/util/scgiserver.py \
	paste/debug/doctest_webapp.py

%if_with python3
rm -rf ../python3
cp -a . ../python3
%endif

%build
%python_build
%if_with python3
pushd ../python3
for i in $(find ./ -name '*.py'); do
	2to3 -w $i
done
sed -i 's|/usr/bin/env python|/usr/bin/env python3|' \
	tests/cgiapp_data/*
%python3_build
popd
%endif

%install
%python_install
# hack for autocreate "provides python2.5(paste)"
touch %buildroot%python_sitelibdir/%modulename/__init__.py

%if_with python3
pushd ../python3
%python3_install
touch %buildroot%python3_sitelibdir/%modulename/__init__.py
popd
%endif

%files
%python_sitelibdir/%modulename/
%python_sitelibdir/*.egg-info

%if_with python3
%files -n python3-module-%modulename
%python3_sitelibdir/%modulename/
%python3_sitelibdir/*.egg-info
%endif

%changelog
* Fri Apr 13 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.7.5.1-alt1.hg20120305
- New snapshot
- Added module for Python 3

* Fri Jan 27 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.7.5.1-alt1.hg20110817
- Version 1.7.5.1

* Mon Oct 24 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.7.3.1-alt2.1
- Rebuild with Python-2.7

* Sun Jun 26 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.7.3.1-alt2
- Added %%py_provides Paste

* Wed May 05 2010 Andrey Rahmatullin <wrar@altlinux.ru> 1.7.3.1-alt1
- 1.7.3.1
- remove some optional dependencies (closes: #23442)

* Wed Nov 18 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.7.2-alt1.1
- Rebuilt with python 2.6

* Mon Mar 30 2009 Vladimir V. Kamarzin <vvk@altlinux.org> 1.7.2-alt1
- Initial build for Sisyphus

