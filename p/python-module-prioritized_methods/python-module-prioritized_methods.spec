%define modulename prioritized_methods

Name: python-module-%modulename
Version: 0.2.1
Release: alt1.1.1

Summary: An extension to PEAK-Rules to prioritize methods in order to to avoid AmbiguousMethods situations
License: MIT
Group: Development/Python

Url: http://toscawidgets.org/download
Packager: Vladimir V. Kamarzin <vvk@altlinux.org>
BuildArch: noarch

Source: %name-%version.tar

# Automatically added by buildreq on Wed Apr 01 2009
BuildRequires: python-module-setuptools

%setup_python_module %modulename

%description
%summary

%prep
%setup

%build
%python_build

%install
%python_install

%files
%python_sitelibdir/%{modulename}*
%python_sitelibdir/*.egg-info

%changelog
* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.2.1-alt1.1.1
- Rebuild with Python-2.7

* Thu Nov 19 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2.1-alt1.1
- Rebuilt with python 2.6

* Wed Apr 01 2009 Vladimir V. Kamarzin <vvk@altlinux.org> 0.2.1-alt1
- Initial build for Sisyphus

