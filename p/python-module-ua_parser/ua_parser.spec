%define oname ua_parser
Name: python-module-%oname
Version: 0.3.4
Release: alt1.git20141025
Summary: Python port of Browserscope's user agent parser
License: ASLv2.0
Group: Development/Python
Url: https://pypi.python.org/pypi/ua-parser/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/tobie/ua-parser.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-module-setuptools-tests python-module-yaml
BuildPreReq: python-modules-json

%py_provides %oname

%description
The crux of the original parser--the data collected by Steve Souders
over the years--has been extracted into a separate YAML file so as to be
reusable as is by implementations in other programming languages.

ua-parser is just a small wrapper around this data.

%prep
%setup

%build
%python_build_debug
python setup.py sdist

%install
%python_install

install -m644 py/%oname/regexes.* %buildroot%python_sitelibdir/%oname/

%check
python setup.py test
rm -fR build
export PYTHONPATH=%buildroot%python_sitelibdir
py.test

%files
%doc *.md *.txt *.markdown
%python_sitelibdir/*

%changelog
* Sun Oct 26 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3.4-alt1.git20141025
- Initial build for Sisyphus

