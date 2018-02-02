%define oname Flask-Bootstrap
Name: python-module-%oname
Version: 3.3.0.2
Release: alt2.dev1.git20141109.1
Summary: Ready-to-use Twitter-bootstrap for use in Flask
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/Flask-Bootstrap/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/mbr/flask-bootstrap.git
Source: %name-%version.tar
BuildArch: noarch

BuildRequires: python-module-setuptools python-module-flask
BuildRequires: python-module-sphinx-devel
BuildRequires: python-module-sphinx_readable_theme

%py_provides flask_bootstrap
%py_requires flask

%description
Flask-Bootstrap packages Bootstrap into an extension that mostly
consists of a blueprint named 'bootstrap'. It can also create links to
serve Bootstrap from a CDN and works with no boilerplate code in your
application.

%package pickles
Summary: Pickles for %oname
Group: Development/Python

%description pickles
Flask-Bootstrap packages Bootstrap into an extension that mostly
consists of a blueprint named 'bootstrap'. It can also create links to
serve Bootstrap from a CDN and works with no boilerplate code in your
application.

This package contains pickles for %oname.

%package docs
Summary: Documentation for %oname
Group: Development/Documentation
BuildArch: noarch

%description docs
Flask-Bootstrap packages Bootstrap into an extension that mostly
consists of a blueprint named 'bootstrap'. It can also create links to
serve Bootstrap from a CDN and works with no boilerplate code in your
application.

This package contains documentation for %oname.

%prep
%setup

%prepare_sphinx .
ln -s ../objects.inv docs/

%build
%python_build_debug

%install
%python_install

export PYTHONPATH=$PWD
%make -C docs pickle
%make -C docs html

install -d %buildroot%python_sitelibdir/%oname
cp -fR docs/_build/pickle %buildroot%python_sitelibdir/%oname/

%check
python setup.py test

%files
%doc CHANGES DEVELOPMENT *.rst
%python_sitelibdir/*
%exclude %python_sitelibdir/*/pickle

%files pickles
%python_sitelibdir/*/pickle

%files docs
%doc run_sample_app.py sample_application docs/_build/html

%changelog
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 3.3.0.2-alt2.dev1.git20141109.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Sat May 28 2016 Igor Vlasenko <viy@altlinux.ru> 3.3.0.2-alt2.dev1.git20141109
- NMU: rebuild with python-module-sphinx_readable_theme

* Mon Jan 05 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.3.0.2-alt1.dev1.git20141109
- Initial build for Sisyphus

