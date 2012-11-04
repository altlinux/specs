%define modname sure

Name: python-module-%modname

Version: 1.0.6
Release: alt1

Summary: Assertion toolbox for python

Group: Development/Python
License: GPLv3+
URL: https://github.com/gabrielfalcao/sure

BuildArch: noarch

%setup_python_module %modname

Source: %modname-%version.tar

BuildRequires: python-module-setuptools python-module-nose

%description
A Python assertion toolbox that works fine with nose.

%prep
%setup -n %modname-%version

%build
%python_build

%install
%python_install

%check
nosetests

%files
%doc README.md COPYING
%python_sitelibdir/%modname/
%python_sitelibdir/*.egg-info

%changelog
* Sun Nov 04 2012 Ivan A. Melnikov <iv@altlinux.org> 1.0.6-alt1
- Initial build for Sisyphus.

