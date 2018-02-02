Name: DoThings
Version: 0.2
Release: alt1.git20150320.1
Summary: Simple To-Do-List in Termial
License: BSD
Group: Toys
Url: https://pypi.python.org/pypi/DoThings/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/MarzinZ/things.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-module-setuptools python-module-docopt

%py_provides things
%py_requires docopt

%description
An easy to-do-list in Terminal.

%prep
%setup

%build
%python_build_debug

%install
%python_install

%check
python setup.py test
export PATH=$PATH:%buildroot%_bindir
export PYTHONPATH=%buildroot%python_sitelibdir
things "test"
things all
things done 1
things all

%files
%doc *.md example.png
%_bindir/*
%python_sitelibdir/*

%changelog
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.2-alt1.git20150320.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Fri Mar 20 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2-alt1.git20150320
- Initial build for Sisyphus

