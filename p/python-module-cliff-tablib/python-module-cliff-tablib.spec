%global modname cliff-tablib

%def_with python3

Name:             python-module-%modname
Version:          1.1
Release:          alt2.1
Summary:          tablib formatters for cliff

Group:            Development/Python
License:          ASL 2.0
URL:              https://pypi.python.org/pypi/cliff-tablib
Source0:          %name-%version.tar

BuildArch:        noarch

# Automatically added by buildreq on Wed Jan 27 2016 (-bi)
# optimized out: pyflakes python-base python-devel python-module-PyStemmer python-module-Pygments python-module-babel python-module-cffi python-module-cmd2 python-module-cryptography python-module-cssselect python-module-docutils python-module-enum34 python-module-flake8 python-module-genshi python-module-jinja2 python-module-mccabe python-module-pbr python-module-pyasn1 python-module-pyparsing python-module-pytz python-module-setuptools python-module-snowballstemmer python-module-sphinx python-module-stevedore python-module-yaml python-modules python-modules-compiler python-modules-ctypes python-modules-email python-modules-encodings python-modules-json python-modules-unittest python-tools-pep8 python3 python3-base python3-module-Pygments python3-module-babel python3-module-cffi python3-module-cryptography python3-module-cssselect python3-module-docutils python3-module-enum34 python3-module-genshi python3-module-jinja2 python3-module-ntlm python3-module-pip python3-module-pycparser python3-module-pyparsing python3-module-pytz python3-module-setuptools python3-module-snowballstemmer python3-module-sphinx python3-module-stevedore python3-module-yaml
BuildRequires: python-module-chardet python-module-cliff python-module-hacking python-module-html5lib python-module-ndg-httpsclient python-module-ntlm python3-module-cliff python3-module-html5lib python3-module-pbr rpm-build-python3

#BuildRequires:    python-devel
#BuildRequires:    python-module-setuptools
#BuildRequires:    python-module-pbr
#BuildRequires:    python-module-cliff
#BuildRequires:    python-module-tablib

#BuildPreReq: python-module-sphinx-devel python-module-oslosphinx

%if_with python3
BuildRequires(pre): rpm-build-python3
#BuildRequires:    python3-devel
#BuildRequires:    python3-module-setuptools
#BuildRequires:    python3-module-pbr
#BuildRequires:    python3-module-cliff
#BuildRequires:    python3-module-tablib

%endif

%description
The cliff framework is meant to be used to create multi-level commands
such as subversion and git, where the main program handles some basic
argument parsing and then invokes a sub-command to do the work. This
package adds JSON, YAML, and HTML output formatters to those commands.

%package -n python3-module-%modname
Summary:          tablib formatters for cliff
Group:            Development/Python3

%description -n python3-module-%modname
The cliff framework is meant to be used to create multi-level commands
such as subversion and git, where the main program handles some basic
argument parsing and then invokes a sub-command to do the work. This
package adds JSON, YAML, and HTML output formatters to those commands.

%prep
%setup

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

%install
%python_install

%if_with python3
pushd ../python3
%python3_install
popd
%endif

%files
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%modname
%python3_sitelibdir/*
%endif

%changelog
* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 1.1-alt2.1
- NMU: Use buildreq for BR.

* Tue Nov 03 2015 Alexey Shabalin <shaba@altlinux.ru> 1.1-alt2
- enable python3 package

* Wed Aug 26 2015 Alexey Shabalin <shaba@altlinux.ru> 1.1-alt1
- Initial release for Sisyphus
