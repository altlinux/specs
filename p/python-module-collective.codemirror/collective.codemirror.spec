%define mname collective
%define oname %mname.codemirror
Name: python-module-%oname
Version: 0.3
Release: alt1.dev.git20140619
Summary: Monkey patch Zope to enable CodeMirror in the ZMI 
License: GPLv2+
Group: Development/Python
Url: https://pypi.python.org/pypi/collective.codemirror/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/collective/collective.codemirror.git
Source: %name-%version.tar

BuildPreReq: python-module-setuptools-tests python-modules-json
BuildPreReq: python-module-Zope2-tests
BuildPreReq: python-module-Products.PythonScripts
BuildPreReq: python-module-zope.pagetemplate

%py_provides %oname
Requires: python-module-Zope2
%py_requires %mname json Products.PythonScripts zope.pagetemplate

%description
CodeMirror is a JavaScript library that provides features commonly found
in IDEs (like syntax highlighting and smart indent) to browser-based
editors. This product monkey patches Zope PythonScript ZMI edit form to
use CodeMirror. It was tested in Chrome, Firefox and IE 9.

%prep
%setup

%build
%python_build_debug

%install
%python_install

%ifarch x86_64
mv %buildroot%_libexecdir %buildroot%_libdir
%endif

cp -fR src/%mname/codemirror/* \
	%buildroot%python_sitelibdir/%mname/codemirror/

%check
python setup.py test

%files
%doc *.rst *.txt docs/*
%python_sitelibdir/%mname/*
%python_sitelibdir/*.egg-info

%changelog
* Wed Jan 07 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3-alt1.dev.git20140619
- Initial build for Sisyphus

