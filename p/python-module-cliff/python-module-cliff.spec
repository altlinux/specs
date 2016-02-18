%global modname cliff

%def_with python3

Name:             python-module-%modname
Version:          1.15.0
Release:          alt2.1
Summary:          Command Line Interface Formulation Framework

Group:            Development/Python
License:          ASL 2.0
URL:              http://pypi.python.org/pypi/cliff
Source:          %name-%version.tar
Patch1: 0001-only-use-unicodecsv-for-python-2.x.patch

BuildArch:        noarch

Requires:    python-module-unicodecsv >= 0.8.0
Requires:    python-module-argparse
Requires:    python-module-prettytable >= 0.7
Requires:    python-module-yaml >= 3.1.0

BuildRequires(pre): rpm-macros-sphinx
# Automatically added by buildreq on Wed Jan 27 2016 (-bi)
# optimized out: pyflakes python-base python-devel python-module-PyStemmer python-module-Pygments python-module-babel python-module-cffi python-module-chardet python-module-cryptography python-module-cssselect python-module-docutils python-module-enum34 python-module-flake8 python-module-funcsigs python-module-genshi python-module-hacking python-module-jinja2 python-module-jinja2-tests python-module-markupsafe python-module-mccabe python-module-ndg-httpsclient python-module-ntlm python-module-pbr python-module-pyasn1 python-module-pyparsing python-module-pytz python-module-setuptools python-module-six python-module-snowballstemmer python-module-sphinx python-module-sphinx_rtd_theme python-module-unittest2 python-modules python-modules-compiler python-modules-ctypes python-modules-email python-modules-encodings python-modules-hotshot python-modules-json python-modules-logging python-modules-multiprocessing python-modules-unittest python-modules-xml python-tools-pep8 python3 python3-base python3-module-Pygments python3-module-babel python3-module-cffi python3-module-cryptography python3-module-cssselect python3-module-docutils python3-module-enum34 python3-module-genshi python3-module-jinja2 python3-module-markupsafe python3-module-ntlm python3-module-pbr python3-module-pip python3-module-pycparser python3-module-pyparsing python3-module-pytz python3-module-setuptools python3-module-six python3-module-snowballstemmer python3-module-sphinx python3-module-unittest2 xz
BuildRequires: python-module-alabaster python-module-cmd2 python-module-html5lib python-module-mock python-module-nose python-module-objects.inv python-module-oslosphinx python-module-prettytable python-module-stevedore python-module-unicodecsv python-module-yaml python3-module-cmd2 python3-module-html5lib python3-module-jinja2-tests python3-module-mock python3-module-nose python3-module-prettytable python3-module-stevedore python3-module-yaml rpm-build-python3 time

#BuildRequires:    python-devel
#BuildRequires:    python-module-setuptools
#BuildRequires:    python-module-pbr >= 1.6
#BuildRequires:    python-module-prettytable >= 0.7
#BuildRequires:    python-module-argparse
#BuildRequires:    python-module-cmd2 >= 0.6.7
#BuildRequires:    python-module-stevedore >= 1.5.0
#BuildRequires:    python-module-unicodecsv >= 0.8.0
#BuildRequires:    python-module-yaml >= 3.1.0
#BuildRequires:    python-module-six >= 1.9.0

# Required for the test suite
#BuildRequires:    python-module-nose
#BuildRequires:    python-module-mock

#BuildRequires:    bash
#BuildRequires:    bash-completion
#BuildRequires:    python-module-argparse

#BuildPreReq: python-module-sphinx-devel python-module-oslosphinx

%if_with python3
BuildRequires(pre): rpm-build-python3
#BuildRequires:    python3-devel
#BuildRequires:    python3-module-setuptools
#BuildRequires:    python3-module-pbr >= 1.6
#BuildRequires:    python3-module-prettytable >= 0.7
#BuildRequires:    python3-module-cmd2 >= 0.6.7
#BuildRequires:    python3-module-stevedore  >= 1.5.0
#BuildRequires:    python3-module-six  >= 1.9.0
#BuildRequires:    python3-module-yaml >= 3.1.0
#BuildRequires:    python3-module-nose
#BuildRequires:    python3-module-mock
#BuildRequires:    python3-module-argparse
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

%description -n python3-module-%modname
cliff is a framework for building command line programs. It uses setuptools
entry points to provide subcommands, output formatters, and other
extensions.

Documentation for cliff is hosted on readthedocs.org at
http://readthedocs.org/docs/cliff/en/latest/

%prep
%setup
%patch1 -p1

# Let RPM handle the dependencies
rm -f test-requirements.txt requirements.txt

#sed -i 's|^pbr.*||' requirements.txt
#sed -i 's|^argparse.*||' requirements.txt

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
sed -i 's/nosetests/nosetests3/' cliff/tests/test_help.py
PYTHONPATH=. nosetests3
popd
%endif

%files
%doc AUTHORS ChangeLog *.rst doc/build/html
%python_sitelibdir/*
%exclude %python_sitelibdir/*/tests

%if_with python3
%files -n python3-module-%modname
%doc AUTHORS ChangeLog *.rst doc/build/html
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/tests
%endif

%changelog
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
