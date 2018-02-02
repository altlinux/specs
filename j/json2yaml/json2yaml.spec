Name: json2yaml
Version: 1.1.1
Release: alt2.1
Summary: Convert JSON to YAML or vice versa, while preserving the order of associative arrays
License: ASLv2.0
Group: File tools
BuildArch: noarch
Url: https://pypi.python.org/pypi/json2yaml/

# https://github.com/drbild/json2yaml.git
Source: %{name}-%{version}.tar.gz

BuildRequires: python-module-setuptools python-module-docopt
BuildRequires: python-module-yaml python-module-pyaml
BuildRequires: python-modules-json

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
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 1.1.1-alt2.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Thu Nov 02 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 1.1.1-alt2
- Rebuilt to fix file permissions (closes: #34045)

* Fri Jan 06 2017 Igor Vlasenko <viy@altlinux.ru> 1.1.1-alt1
- automated PyPI update

* Wed Jan 28 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.0-alt1.git20150127
- Initial build for Sisyphus

