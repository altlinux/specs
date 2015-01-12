%define oname FlexGet

%def_disable check

Name: python-module-%oname
Version: 1.2.258
Release: alt1.git20150111
Summary: Downloading/processing content (torrents, podcasts...) from different sources
License: MIT
Group: Development/Python
Url: https://pypi.python.org/pypi/FlexGet/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/Flexget/Flexget.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-module-setuptools-tests python-module-feedparser
BuildPreReq: python-module-SQLAlchemy python-module-yaml
BuildPreReq: python-module-BeautifulSoup4 python-module-html5lib
BuildPreReq: python-module-PyRSS2Gen python-module-pynzb
BuildPreReq: python-module-progressbar python-module-rpyc
BuildPreReq: python-module-jinja2 python-module-requests
BuildPreReq: python-module-dateutil python-module-jsonschema
BuildPreReq: python-module-tvrage python-module-tmdb3
BuildPreReq: python-module-path python-module-guessit
BuildPreReq: python-module-apscheduler python-module-nose
BuildPreReq: python-module-guppy python-module-flask
BuildPreReq: python-module-cherrypy python-module-Paver
BuildPreReq: pylint python-module-coverage python-module-nosexcover
BuildPreReq: python-module-mock python-tools-pep8
BuildPreReq: python-module-httmock python-module-vcrpy
BuildPreReq: python-module-argparse python-module-pbr
BuildPreReq: python-module-pip
BuildPreReq: python-module-sphinx-devel

%py_provides flexget

%description
FlexGet is a multipurpose automation tool for content like torrents,
nzbs, podcasts, comics, series, movies, etc. It can use different kinds
of sources like RSS-feeds, html pages, csv files, search engines and
there are even plugins for sites that do not provide any kind of useful
feeds.

There are numerous plugins that allow utilizing FlexGet in interesting
ways and more are being added continuously.

FlexGet is extremely useful in conjunction with applications which have
watch directory support or provide interface for external utilities like
FlexGet.

%package pickles
Summary: Pickles for %oname
Group: Development/Python

%description pickles
FlexGet is a multipurpose automation tool for content like torrents,
nzbs, podcasts, comics, series, movies, etc. It can use different kinds
of sources like RSS-feeds, html pages, csv files, search engines and
there are even plugins for sites that do not provide any kind of useful
feeds.

This package contains pickles for %oname.

%package docs
Summary: Documentation for %oname
Group: Development/Documentation
BuildArch: noarch

%description docs
FlexGet is a multipurpose automation tool for content like torrents,
nzbs, podcasts, comics, series, movies, etc. It can use different kinds
of sources like RSS-feeds, html pages, csv files, search engines and
there are even plugins for sites that do not provide any kind of useful
feeds.

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
pushd docs
sphinx-build -b pickle -d build/doctrees . build/pickle
sphinx-build -b html -d build/doctrees . build/html
popd

install -d %buildroot%python_sitelibdir/%oname
cp -fR docs/build/pickle %buildroot%python_sitelibdir/%oname/

%check
py.test

%files
%doc *.rst
%_bindir/*
%python_sitelibdir/*
%exclude %python_sitelibdir/*/pickle

%files pickles
%python_sitelibdir/*/pickle

%files docs
%doc docs/build/html/*

%changelog
* Mon Jan 12 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2.258-alt1.git20150111
- Version 1.2.258

* Thu Jan 01 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2.246-alt1.git20150101
- Version 1.2.246

* Tue Dec 30 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2.244-alt1.git20141230
- Version 1.2.244

* Mon Dec 29 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2.243-alt1.git20141229
- Version 1.2.243

* Fri Dec 19 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2.238-alt1.git20141219
- Version 1.2.238

* Wed Dec 10 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2.234-alt1.git20141209
- Version 1.2.234

* Wed Nov 26 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2.227-alt1.git20141125
- Version 1.2.227

* Mon Nov 24 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2.226-alt1.git20141123
- Version 1.2.226

* Sun Nov 23 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2.225-alt1.git20141122
- Version 1.2.225

* Sat Nov 22 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2.223-alt1.git20141122
- Version 1.2.223

* Fri Nov 21 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2.222-alt1.git20141120
- Version 1.2.222

* Tue Nov 18 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2.221-alt1.git20141117
- Version 1.2.221

* Sun Nov 16 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2.220-alt1.git20141113
- Version 1.2.220

* Wed Nov 12 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2.219-alt1.git20141111
- Version 1.2.219

* Mon Nov 10 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2.218-alt1.git20141109
- Version 1.2.218

* Sat Nov 08 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2.215-alt1.git20141106
- Initial build for Sisyphus

