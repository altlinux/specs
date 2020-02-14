%define oname tinkerer

%def_without docs

Name: python3-module-%oname
Version: 1.6.0
Release: alt2

Summary: Sphinx-based blogging engine
License: BSD
Group: Development/Python3
BuildArch: noarch
Url: https://pypi.python.org/pypi/Tinkerer

# https://github.com/vladris/tinkerer.git
Source: %name-%version.tar
Patch0: fix-sphinx-import.patch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-jinja2
BuildRequires: python3-module-mock
BuildRequires: python3-module-nose
BuildRequires: python3-module-pyquery
BuildRequires: python3-module-sphinx


%description
Tinkerer is a blogging engine/static website generator powered by
Sphinx.

It allows blogging in reStructuredText format, comes with out-of-the-box
support for post publishing dates, authors, categories, tags, post
archive, RSS feed generation, comments powered by Disqus and more.

Tinkerer is also highly customizable through Sphinx extensions.

%if_with docs
%package pickles
Summary: Pickles for %oname
Group: Development/Python3

%description pickles
Tinkerer is a blogging engine/static website generator powered by
Sphinx.

It allows blogging in reStructuredText format, comes with out-of-the-box
support for post publishing dates, authors, categories, tags, post
archive, RSS feed generation, comments powered by Disqus and more.

Tinkerer is also highly customizable through Sphinx extensions.

This package contains pickles for %oname.

%package docs
Summary: Documentation for %oname
Group: Development/Documentation
BuildArch: noarch

%description docs
Tinkerer is a blogging engine/static website generator powered by
Sphinx.

It allows blogging in reStructuredText format, comes with out-of-the-box
support for post publishing dates, authors, categories, tags, post
archive, RSS feed generation, comments powered by Disqus and more.

Tinkerer is also highly customizable through Sphinx extensions.

This package contains documentation for %oname.
%endif

%prep
%setup
%patch0 -p1

%build
%python3_build_debug

%install
%python3_install

%if_with docs
export PYTHONPATH=%buildroot%python3_sitelibdir
pushd blog
sphinx-build-3 -b pickle -d build/doctrees . build/pickle
sphinx-build-3 -b html -d build/doctrees . build/html
popd
cp -fR blog/build/pickle %buildroot%python3_sitelibdir/%oname/
%endif

%check
%if 0
%__python3 setup.py test -v
export PYTHONPATH=$PWD
nosetests3 -vv --with-cover --cover-package=tinkerer --cover-inclusive
%endif

%files
%doc CONTRIBUTORS *.rst
%_bindir/*
%python3_sitelibdir/*
%if_with docs
%exclude %python3_sitelibdir/*/pickle

%files pickles
%python3_sitelibdir/*/pickle

%files docs
%doc blog/build/html/*
%endif


%changelog
* Fri Feb 14 2020 Andrey Bychkov <mrdrew@altlinux.org> 1.6.0-alt2
- Build for python2 disabled
- fix sphinx import.

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 1.6.0-alt1.git20170528.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Thu Oct 26 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 1.6.0-alt1.git20170528
- Updated to upstream version 1.6.0.

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.5-alt1.git20150212.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 1.5-alt1.git20150212.1
- NMU: Use buildreq for BR.

* Mon Aug 31 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.5-alt1.git20150212
- Initial build for Sisyphus

