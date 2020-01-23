%define oname Flask-Bootstrap

Name: python3-module-%oname
Version: 3.3.0.2
Release: alt3

Summary: Ready-to-use Twitter-bootstrap for use in Flask
License: BSD
Group: Development/Python3
Url: https://pypi.python.org/pypi/Flask-Bootstrap/
BuildArch: noarch

# https://github.com/mbr/flask-bootstrap.git
Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-flask
BuildRequires: python3-module-flask-appconfig
BuildRequires: python3-module-flask-wtf
BuildRequires: python3-module-sphinx-devel
BuildRequires: python3-module-sphinx_readable_theme

%py3_requires flask
%py3_provides flask_bootstrap


%description
Flask-Bootstrap packages Bootstrap into an extension that mostly
consists of a blueprint named 'bootstrap'. It can also create links to
serve Bootstrap from a CDN and works with no boilerplate code in your
application.

%package pickles
Summary: Pickles for %oname
Group: Development/Python3

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

sed -i 's|sphinx-build|sphinx-build-3|' docs/Makefile

%build
%python3_build_debug

%install
%python3_install

export PYTHONPATH=$PWD
%make -C docs pickle
%make -C docs html

install -d %buildroot%python3_sitelibdir/%oname
cp -fR docs/_build/pickle %buildroot%python3_sitelibdir/%oname/

%check
%__python3 setup.py test

%files
%doc CHANGES DEVELOPMENT *.rst
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/pickle

%files pickles
%python3_sitelibdir/*/pickle

%files docs
%doc run_sample_app.py sample_application docs/_build/html


%changelog
* Thu Jan 23 2020 Andrey Bychkov <mrdrew@altlinux.org> 3.3.0.2-alt3
- Porting on Python3.

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 3.3.0.2-alt2.dev1.git20141109.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Sat May 28 2016 Igor Vlasenko <viy@altlinux.ru> 3.3.0.2-alt2.dev1.git20141109
- NMU: rebuild with python-module-sphinx_readable_theme

* Mon Jan 05 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.3.0.2-alt1.dev1.git20141109
- Initial build for Sisyphus

