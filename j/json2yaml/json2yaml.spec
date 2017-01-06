Name: json2yaml
Version: 1.1.1
Release: alt1
Summary: Convert JSON to YAML or vice versa, while preserving the order of associative arrays
License: ASLv2.0
Group: File tools
Url: https://pypi.python.org/pypi/json2yaml/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/drbild/json2yaml.git
Source0: https://pypi.python.org/packages/24/34/7aa5272ac1468e2e0fe0c5d1c8bf704ed0ee3701d24ee6fdbd7e13e55419/%{name}-%{version}.tar.gz
BuildArch: noarch

BuildPreReq: python-module-setuptools-tests python-module-docopt
BuildPreReq: python-module-yaml python-module-pyaml
BuildPreReq: python-modules-json

%py_requires yaml pyaml docopt json

%description
Convert JSON to YAML or vice versa, while preserving the order of
associative arrays.

%prep
%setup -q 

%build
%python_build_debug

%install
%python_install

%check
python setup.py test

%files
#doc NOTICE *.md
%_bindir/*
%python_sitelibdir/*

%changelog
* Fri Jan 06 2017 Igor Vlasenko <viy@altlinux.ru> 1.1.1-alt1
- automated PyPI update

* Wed Jan 28 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.0-alt1.git20150127
- Initial build for Sisyphus

