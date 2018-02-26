%define modulename turbocheetah

Name: python-module-%modulename
Version: 1.0
Release: alt1.1.1

Summary: TurboGears support package which provides a template engine plug-in for the Cheetah templating engine
License: MIT
Group: Development/Python

Url: http://docs.turbogears.org/TurboCheetah
Packager: Vladimir V. Kamarzin <vvk@altlinux.org>
BuildArch: noarch

Source: %name-%version.tar

BuildRequires: python-module-setuptools

%setup_python_module %modulename

%description
TurboCheetah is a TurboGears support package which provides a template engine
plug-in for the Cheetah templating engine, allowing you to use Cheetah templates
with TurboGears, Buffet or other systems that support the
python.templating.engines entry point.

%prep
%setup

%build
%python_build

%install
%python_install

%files
%python_sitelibdir/%modulename/
%python_sitelibdir/*.egg-info

%changelog
* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.0-alt1.1.1
- Rebuild with Python-2.7

* Thu Nov 19 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0-alt1.1
- Rebuilt with python 2.6

* Sat Apr 04 2009 Vladimir V. Kamarzin <vvk@altlinux.org> 1.0-alt1
- Initial build for Sisyphus

