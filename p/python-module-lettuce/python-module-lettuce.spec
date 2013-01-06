%define modname lettuce

Name: python-module-%modname
Version: 0.2.11
Release: alt1
Summary: Behaviour Driven Development for Python
Group: Development/Python
License: GPLv3+
URL: http://lettuce.it/

BuildArch: noarch

%setup_python_module %modname

Source: %modname-%version.tar

BuildRequires: python-module-fuzzywuzzy
BuildRequires: python-module-lxml
BuildRequires: python-module-mock
BuildRequires: python-module-mox
BuildRequires: python-module-nose
BuildRequires: python-module-setuptools
BuildRequires: python-module-sure

%description
Lettuce is an extremely useful and charming tool for BDD (Behavior
Driven Development). It can execute plain-text functional descriptions
as automated tests for Python projects, just as Cucumber does for Ruby.

Lettuce makes the development and testing process really easy, scalable,
readable and - what is best - it allows someone who doesn't program to
describe the behavior of a certain system, without imagining those
descriptions will automatically test the system during its development.

%prep
%setup -n %modname-%version

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
* Sun Jan 06 2013 Ivan A. Melnikov <iv@altlinux.org> 0.2.11-alt1
- New version;
- Correct description.

* Sun Nov 04 2012 Ivan A. Melnikov <iv@altlinux.org> 0.2.10-alt1.git36ffa10
- Initial build for Sisyphus.

