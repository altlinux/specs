%define modname lettuce

Name: python-module-%modname

Version: 0.2.10
Release: alt1.git36ffa10

Summary: Behaviour Driven Development for Python

Group: Development/Python
License: GPLv3+
URL: http://lettuce.it/

BuildArch: noarch

%setup_python_module %modname

Source: %modname-%version-%release.tar

BuildRequires: python-module-fuzzywuzzy
BuildRequires: python-module-lxml
BuildRequires: python-module-mock
BuildRequires: python-module-mox
BuildRequires: python-module-nose
BuildRequires: python-module-setuptools
BuildRequires: python-module-sure

%description
Fuzzy string matching like a boss.

%prep
%setup -n %modname-%version-%release

%build
%python_build

%install
%python_install

%check
export PYTHONPATH=`pwd`
nosetests -s tests/unit
nosetests -s tests/functional

%files
%doc COPYING README.md
%python_sitelibdir/%modname/
%python_sitelibdir/*.egg-info
%_bindir/lettuce

%changelog
* Sun Nov 04 2012 Ivan A. Melnikov <iv@altlinux.org> 0.2.10-alt1.git36ffa10
- Initial build for Sisyphus.

