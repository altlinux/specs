%define oname pyaml
Name: python-module-%oname
Version: 14.05.7
Release: alt1.git20140528
Summary: pretty-yaml: Pretty YAML serialization
License: WTFPL
Group: Development/Python
Url: https://pypi.python.org/pypi/pyaml/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/mk-fg/pretty-yaml.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-module-setuptools-tests python-module-yaml
BuildPreReq: python-module-unidecode

%py_provides %oname

%description
PyYAML-based module to produce pretty and readable YAML-serialized data.

%prep
%setup

%build
%python_build_debug

%install
%python_install

%check
python setup.py test
export PYTHONPATH=$PWD
python pyaml/tests/dump.py

%files
%doc COPYING *.md
%python_sitelibdir/*

%changelog
* Thu Oct 30 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 14.05.7-alt1.git20140528
- Initial build for Sisyphus

