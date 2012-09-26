%define modulename turbokid

Name: python-module-%modulename
Version: 1.0.6
Release: alt1.svn20100918

Summary: provides a template engine plug-in for the Kid templating engine
License: MIT
Group: Development/Python

Url: http://docs.turbogears.org/TurboKid
BuildArch: noarch

Source: %name-%version.tar

# Automatically added by buildreq on Fri Apr 03 2009
BuildRequires: python-module-setuptools

%setup_python_module %modulename

%description
This package provides a template engine plugin, allowing you
to easily use Kid with TurboGears, Buffet or other systems
that support python.templating.engines.

There are plans to integrate this functionality into Kid,
so this package may eventually become superfluous.

Kid templates are assumed to have a "kid" extension.

For information on the Kid templating engine, go here:
http://kid-templating.org

%package tests
Summary: Tests for TurboKid
Group: Development/Python
Requires: %name = %version-%release

%description tests
This package contains tests for TurboKid.

%prep
%setup

%build
%python_build

%install
%python_install

%files
%python_sitelibdir/%modulename/
%exclude %python_sitelibdir/%modulename/tests
%python_sitelibdir/*.egg-info

%files tests
%python_sitelibdir/%modulename/tests

%changelog
* Wed Sep 26 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.6-alt1.svn20100918
- Version 1.0.6

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.0.4-alt1.1.1
- Rebuild with Python-2.7

* Thu Nov 19 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.4-alt1.1
- Rebuilt with python 2.6

* Fri Apr 03 2009 Vladimir V. Kamarzin <vvk@altlinux.org> 1.0.4-alt1
- Initial build for Sisyphus

