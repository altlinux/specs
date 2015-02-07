%global modname cliff

%def_with python3

Name:             python-module-%modname
Version:          1.9.0
Release:          alt1
Summary:          Command Line Interface Formulation Framework

Group:            Development/Python
License:          ASL 2.0
URL:              http://pypi.python.org/pypi/cliff
Source0:          %{name}-%{version}.tar

BuildArch:        noarch

BuildRequires:    python-devel
BuildRequires:    python-module-setuptools
BuildRequires:    python-module-pbr
BuildRequires:    python-module-prettytable
BuildRequires:    python-module-cmd2 >= 0.6.7
BuildRequires:    python-module-stevedore
BuildRequires:    python-module-six

# Required for the test suite
BuildRequires:    python-module-nose
BuildRequires:    python-module-mock
BuildRequires:    bash
BuildRequires:    bash-completion

Requires:         python-module-setuptools
Requires:         python-module-prettytable
Requires:         python-module-cmd2 >= 0.6.7
Requires:         python-module-stevedore
Requires:         python-module-six

BuildRequires:    python-module-argparse
Requires:         python-module-argparse

BuildPreReq: python-module-sphinx-devel python-module-oslosphinx

%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires:    python3-devel
BuildRequires:    python3-module-setuptools
BuildRequires:    python3-module-pbr
BuildRequires:    python3-module-prettytable
BuildRequires:    python3-module-cmd2 >= 0.6.7
BuildRequires:    python3-module-stevedore
BuildRequires:    python3-module-six
BuildRequires:    python3-module-nose
BuildRequires:    python3-module-mock
BuildRequires:    python3-module-argparse
%endif

%description
cliff is a framework for building command line programs. It uses setuptools
entry points to provide subcommands, output formatters, and other
extensions.

Documentation for cliff is hosted on readthedocs.org at
http://readthedocs.org/docs/cliff/en/latest/

%package -n python3-module-%modname
Summary:          Command Line Interface Formulation Framework
Group:            Development/Python3
Requires:         python3-module-setuptools
Requires:         python3-module-prettytable
Requires:         python3-module-cmd2 >= 0.6.7
Requires:         python3-module-stevedore
Requires:         python3-module-six
Requires:         python3-module-argparse

%description -n python3-module-%modname
cliff is a framework for building command line programs. It uses setuptools
entry points to provide subcommands, output formatters, and other
extensions.

Documentation for cliff is hosted on readthedocs.org at
http://readthedocs.org/docs/cliff/en/latest/

%prep
%setup

sed -i 's|^pbr.*||' requirements.txt

# Remove bundled egg info
rm -rf *.egg-info

%if_with python3
cp -fR . ../python3
%endif

%prepare_sphinx doc
ln -s ../objects.inv doc/source/

%build
%python_build

%if_with python3
pushd ../python3
%python3_build
popd
%endif

%install
%python_install

%if_with python3
pushd ../python3
%python3_install
popd
%endif

export PYTHONPATH=$PWD
%make -C doc html

%check
PYTHONPATH=. nosetests
%if_with python3
pushd ../python3
PYTHONPATH=. nosetests3
popd
%endif

%files
%doc AUTHORS ChangeLog *.rst doc/build/html
%{python_sitelibdir}/%{modname}
%{python_sitelibdir}/%{modname}-%{version}*

%if_with python3
%files -n python3-module-%modname
%doc AUTHORS ChangeLog *.rst doc/build/html
%{python3_sitelibdir}/%{modname}
%{python3_sitelibdir}/%{modname}-%{version}*
%endif

%changelog
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
