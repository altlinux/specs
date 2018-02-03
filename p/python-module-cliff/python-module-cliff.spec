%global oname cliff

%def_with python3

Name: python-module-%oname
Version: 2.4.0
Release: alt1.1
Summary: Command Line Interface Formulation Framework

Group: Development/Python
License: ASL 2.0
Url: http://docs.openstack.org/developer/%oname
Source: https://tarballs.openstack.org/%oname/%oname-%version.tar.gz

BuildArch: noarch

Requires: python-module-unicodecsv >= 0.8.0
Requires: python-module-argparse
Requires: python-module-prettytable >= 0.7.1
Requires: python-module-yaml >= 3.10.0

BuildRequires: python-devel
BuildRequires: python-module-setuptools
BuildRequires: python-module-pbr >= 1.8
BuildRequires: python-module-prettytable >= 0.7.1
BuildRequires: python-module-pyparsing >= 2.0.7
BuildRequires: python-module-argparse
BuildRequires: python-module-cmd2 >= 0.6.7
BuildRequires: python-module-stevedore >= 1.17.1
BuildRequires: python-module-unicodecsv >= 0.8.0
BuildRequires: python-module-yaml >= 3.10.0
BuildRequires: python-module-six >= 1.9.0
BuildRequires: python-module-sphinx >= 1.1.2
BuildRequires: python-module-oslosphinx >= 2.5.0

# Required for the test suite
BuildRequires: python-module-nose
BuildRequires: python-module-mock

%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-pbr >= 1.8
BuildRequires: python3-module-prettytable >= 0.7.1
BuildRequires: python3-module-pyparsing >= 2.0.7
BuildRequires: python3-module-argparse
BuildRequires: python3-module-cmd2 >= 0.6.7
BuildRequires: python3-module-stevedore  >= 1.17.1
BuildRequires: python3-module-six >= 1.9.0
BuildRequires: python3-module-yaml >= 3.10.0
BuildRequires: python3-module-nose
BuildRequires: python3-module-mock
%endif

%description
cliff is a framework for building command line programs. It uses setuptools
entry points to provide subcommands, output formatters, and other
extensions.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR

%description tests
This package contains tests for %oname.

%package -n python3-module-%oname
Summary: Command Line Interface Formulation Framework
Group: Development/Python3

%description -n python3-module-%oname
cliff is a framework for building command line programs. It uses setuptools
entry points to provide subcommands, output formatters, and other
extensions.

%package -n python3-module-%oname-tests
Summary: Tests for %oname
Group: Development/Python3
Requires: python3-module-%oname = %EVR

%description -n python3-module-%oname-tests
This package contains tests for %oname.

%package doc
Summary: Documentation for the Command Line Interface Formulation Framework
Group: Development/Documentation

%description doc
Documentation for the Command Line Interface Formulation Framework.


%prep
%setup -n %oname-%version

# Let RPM handle the dependencies
rm -f test-requirements.txt requirements.txt

#sed -i 's|^pbr.*||' requirements.txt
#sed -i 's|^argparse.*||' requirements.txt

# Remove bundled egg info
rm -rf *.egg-info

%if_with python3
cp -fR . ../python3
%endif

%build
%python_build

%if_with python3
pushd ../python3
%python3_build
popd
%endif

# generate html docs
sphinx-build doc/source html
# remove the sphinx-build leftovers
rm -rf html/.{doctrees,buildinfo}

%install
%python_install

%if_with python3
pushd ../python3
%python3_install
popd
%endif

%check
PYTHONPATH=. nosetests
#%if_with python3
#pushd ../python3
#sed -i 's/nosetests/nosetests3/' cliff/tests/test_help.py
#PYTHONPATH=. nosetests3
#popd
#%endif

%files
%doc AUTHORS ChangeLog *.rst
%python_sitelibdir/*
%exclude %python_sitelibdir/*/tests

%files tests
%python_sitelibdir/*/tests

%if_with python3
%files -n python3-module-%oname
%doc AUTHORS ChangeLog *.rst
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/tests

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/tests
%endif

%files doc
%doc html

%changelog
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 2.4.0-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Mon May 29 2017 Alexey Shabalin <shaba@altlinux.ru> 2.4.0-alt1
- 2.4.0
- add test packages
- add doc package

* Tue Oct 18 2016 Alexey Shabalin <shaba@altlinux.ru> 2.2.0-alt1
- 2.2.0

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.15.0-alt2.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 1.15.0-alt2.1
- NMU: Use buildreq for BR.

* Tue Nov 10 2015 Alexey Shabalin <shaba@altlinux.ru> 1.15.0-alt2
- update R:

* Thu Oct 29 2015 Alexey Shabalin <shaba@altlinux.ru> 1.15.0-alt1
- 1.15.0

* Tue Apr 28 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.12.0-alt1
- Version 1.12.0

* Tue Mar 31 2015 Alexey Shabalin <shaba@altlinux.ru> 1.10.1-alt1
- 1.10.1

* Sat Feb 07 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.9.0-alt1
- Version 1.9.0
- Added module for Python 3

* Tue Aug 05 2014 Lenar Shakirov <snejok@altlinux.ru> 1.6.1-alt1
- New version

* Mon Sep 30 2013 Pavel Shilovsky <piastry@altlinux.org> 1.0-alt2
- Remove distribute bootstrap
- Fix check section in spec

* Thu Sep 27 2012 Pavel Shilovsky <piastry@altlinux.org> 1.0-alt1
- Initial release for Sisyphus (based on Fedora)
