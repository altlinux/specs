Name: json2yaml
Version: 1.0.0
Release: alt1.git20150127
Summary: Convert JSON to YAML or vice versa, while preserving the order of associative arrays
License: ASLv2.0
Group: File tools
Url: https://pypi.python.org/pypi/json2yaml/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/drbild/json2yaml.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-module-setuptools-tests python-module-docopt
BuildPreReq: python-module-yaml python-module-pyaml
BuildPreReq: python-modules-json

%py_requires yaml pyaml docopt json

%description
Convert JSON to YAML or vice versa, while preserving the order of
associative arrays.

%prep
%setup

%build
%python_build_debug

%install
%python_install

%check
python setup.py test

%files
%doc NOTICE *.md
%_bindir/*
%python_sitelibdir/*

%changelog
* Wed Jan 28 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.0-alt1.git20150127
- Initial build for Sisyphus

