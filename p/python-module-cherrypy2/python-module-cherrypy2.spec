%define modulename cherrypy

Name: python-module-%{modulename}2
Version: 2.3.0
Release: alt2.1.1

%setup_python_module %modulename

Summary: CherryPy is a pythonic, object-oriented web development framework
License: BSD
Group: Development/Python

URL: http://www.cherrypy.org
Packager: Vladimir V. Kamarzin <vvk@altlinux.org>
BuildArch: noarch

Source0: %name-%version.tar

Provides: python-module-cherrypy = %version-%release
Obsoletes: python-module-cherrypy <= 2.1.0-alt1.1
Conflicts: python-module-cherrypy >= 3.1.1-alt1

BuildPreReq: %py_dependencies setuptools

%description
Your CherryPy powered web applications are in fact stand-alone Python applications embedding their own multi-threaded web server. You can deploy them anywhere you can run Python applications. Apache is not required, but it's possible to run a CherryPy application behind it.

%prep
%setup

%build
%python_build

%install
%python_install

%files
%python_sitelibdir/%modulename/
%python_sitelibdir/*.egg-info
%doc cherrypy/tutorial CHANGELOG.txt CHERRYPYTEAM.txt

%changelog
* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 2.3.0-alt2.1.1
- Rebuild with Python-2.7

* Thu Nov 19 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.3.0-alt2.1
- Rebuilt with python 2.6

* Mon Apr 06 2009 Vladimir V. Kamarzin <vvk@altlinux.org> 2.3.0-alt2
- Add provides/obsoletes/conflicts

* Sat Apr 04 2009 Vladimir V. Kamarzin <vvk@altlinux.org> 2.3.0-alt1
- 2.3.0
- Rename package to python-module-cherrypy2

* Thu Jan 24 2008 Grigory Batalov <bga@altlinux.ru> 2.1.0-alt1.1
- Rebuilt with python-2.5.

* Sun Oct 30 2005 Maxim Bodyansky <maximbo@altlinux.ru> 2.1.0-alt1
- Initial build for Sisyphus
