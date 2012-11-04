%define modname fuzzywuzzy

Name: python-module-%modname

Version: 0.1
Release: alt1.git775dfb

Summary: Fuzzy string matching in Python

Group: Development/Python
License: MIT
URL: https://github.com/seatgeek/fuzzywuzzy/

BuildArch: noarch

%setup_python_module %modname

Source: %modname-%version-%release.tar

BuildRequires: python-module-setuptools python-module-nose

%description
Fuzzy string matching like a boss.

%prep
%setup -n %modname-%version-%release
rm fuzzywuzzy/StringMatcher.py

%build
%python_build

%install
%python_install

%check
nosetests

%files
%doc LICENSE README.textile
%python_sitelibdir/%modname/
%python_sitelibdir/*.egg-info

%changelog
* Sun Nov 04 2012 Ivan A. Melnikov <iv@altlinux.org> 0.1-alt1.git775dfb
- Initial build for Sisyphus.

