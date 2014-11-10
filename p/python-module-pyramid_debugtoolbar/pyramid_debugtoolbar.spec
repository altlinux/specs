%define oname pyramid_debugtoolbar

%def_with python3

Name: python-module-%oname
Version: 2.2.1
Release: alt1.git20141109
Summary: A package which provides an interactive HTML debugger for Pyramid application development
License: RPL
Group: Development/Python
Url: https://pypi.python.org/pypi/pyramid_debugtoolbar/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/Pylons/pyramid_debugtoolbar.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools
BuildPreReq: python-module-sphinx-devel pylons_sphinx_theme
BuildPreReq: python-module-pyramid-tests python-module-zope.deprecation
BuildPreReq: python-module-zope.component python-module-repoze.lru
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
%endif

%description
pyramid_debugtoolbar provides a debug toolbar useful while you're
developing your Pyramid application.

Note that pyramid_debugtoolbar is a blatant rip-off of Michael van
Tellingen's flask-debugtoolbar (which itself was derived from Rob
Hudson's django-debugtoolbar). It also includes a lightly sanded down
version of the Werkzeug debugger code by Armin Ronacher and team.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR

%description tests
pyramid_debugtoolbar provides a debug toolbar useful while you're
developing your Pyramid application.

Note that pyramid_debugtoolbar is a blatant rip-off of Michael van
Tellingen's flask-debugtoolbar (which itself was derived from Rob
Hudson's django-debugtoolbar). It also includes a lightly sanded down
version of the Werkzeug debugger code by Armin Ronacher and team.

This package contains tests for %oname.

%package -n python3-module-%oname
Summary: A package which provides an interactive HTML debugger for Pyramid application development
Group: Development/Python3

%description -n python3-module-%oname
pyramid_debugtoolbar provides a debug toolbar useful while you're
developing your Pyramid application.

Note that pyramid_debugtoolbar is a blatant rip-off of Michael van
Tellingen's flask-debugtoolbar (which itself was derived from Rob
Hudson's django-debugtoolbar). It also includes a lightly sanded down
version of the Werkzeug debugger code by Armin Ronacher and team.

%package -n python3-module-%oname-tests
Summary: Tests for %oname
Group: Development/Python3
Requires: python3-module-%oname = %EVR

%description -n python3-module-%oname-tests
pyramid_debugtoolbar provides a debug toolbar useful while you're
developing your Pyramid application.

Note that pyramid_debugtoolbar is a blatant rip-off of Michael van
Tellingen's flask-debugtoolbar (which itself was derived from Rob
Hudson's django-debugtoolbar). It also includes a lightly sanded down
version of the Werkzeug debugger code by Armin Ronacher and team.

This package contains tests for %oname.

%package pickles
Summary: Pickles for %oname
Group: Development/Python

%description pickles
pyramid_debugtoolbar provides a debug toolbar useful while you're
developing your Pyramid application.

Note that pyramid_debugtoolbar is a blatant rip-off of Michael van
Tellingen's flask-debugtoolbar (which itself was derived from Rob
Hudson's django-debugtoolbar). It also includes a lightly sanded down
version of the Werkzeug debugger code by Armin Ronacher and team.

This package contains pickles for %oname.

%package docs
Summary: Documentation for %oname
Group: Development/Documentation
BuildArch: noarch

%description docs
pyramid_debugtoolbar provides a debug toolbar useful while you're
developing your Pyramid application.

Note that pyramid_debugtoolbar is a blatant rip-off of Michael van
Tellingen's flask-debugtoolbar (which itself was derived from Rob
Hudson's django-debugtoolbar). It also includes a lightly sanded down
version of the Werkzeug debugger code by Armin Ronacher and team.

This package contains documentation for %oname.

%prep
%setup

%if_with python3
cp -fR . ../python3
%endif

cp -fR %_datadir/pylons_sphinx_theme/* docs/_themes/
%prepare_sphinx .
ln -s ../objects.inv docs/

%build
%python_build_debug

%if_with python3
pushd ../python3
%python3_build_debug
popd
%endif

%install
%python_install

%if_with python3
pushd ../python3
%python3_install
popd
%endif

export PYTHONPATH=%buildroot%python_sitelibdir
%make -C docs pickle
%make -C docs html

cp -fR docs/_build/pickle %buildroot%python_sitelibdir/%oname/

%files
%doc *.txt *.rst
%python_sitelibdir/*
%exclude %python_sitelibdir/*/tests
%exclude %python_sitelibdir/*/pickle

%files pickles
%python_sitelibdir/*/pickle

%files tests
%python_sitelibdir/*/tests

%files docs
%doc demo docs/_build/html

%if_with python3
%files -n python3-module-%oname
%doc *.txt *.rst
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/tests

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/tests
%endif

%changelog
* Mon Nov 10 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.2.1-alt1.git20141109
- Version 2.2.1

* Fri Oct 03 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.2-alt1.git20140828
- Initial build for Sisyphus

