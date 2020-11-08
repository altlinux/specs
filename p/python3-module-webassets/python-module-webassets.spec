%define oname webassets

%def_without docs
%def_without check

Name:       python3-module-%oname
Version:    2.0
Release:    alt1

Summary:    Media asset management for Python, with glue code for various web frameworks

License:    BSD
Group:      Development/Python3
Url:        https://pypi.python.org/pypi/webassets/

BuildArch:  noarch

# Source-url: https://pypi.io/packages/source/w/%oname/%oname-%version.tar.gz
Source: %name-%version.tar

BuildRequires(pre): rpm-build-intro >= 2.2.5
BuildRequires(pre): rpm-build-python3
%if_with docs
BuildRequires: python3-module-sphinx
%endif

# due the same /usr/bin/webassets
Conflicts: python-module-webassets
Obsoletes: python-module-webassets

%add_python3_req_skip webassets.six.moves

%description
Merges, minifies and compresses Javascript and CSS files, supporting a
variety of different filters, including YUI, jsmin, jspacker or CSS
tidy. Also supports URL rewriting in CSS files.


%if_with docs
%package pickles
Summary: Pickles for %oname
Group: Development/Python3

%description pickles
Merges, minifies and compresses Javascript and CSS files, supporting a
variety of different filters, including YUI, jsmin, jspacker or CSS
tidy. Also supports URL rewriting in CSS files.

This package contains pickles for %oname.

%package docs
Summary: Documentation for %oname
Group: Development/Documentation
BuildArch: noarch

%description docs
Merges, minifies and compresses Javascript and CSS files, supporting a
variety of different filters, including YUI, jsmin, jspacker or CSS
tidy. Also supports URL rewriting in CSS files.

This package contains documentation for %oname.
%endif

%prep
%setup

%build
%python3_build_debug

%install
%python3_install
%python3_prune

%if_with docs
%make -C docs pickle
%make -C docs html SPHINXBUILD=sphinx-build-3

cp -fR docs/_build/pickle %buildroot%python3_sitelibdir/%oname/
%endif

%check
%__python3 setup.py test

%files
%doc AUTHORS CHANGES *.rst
%_bindir/webassets
%python3_sitelibdir/*
%if_with docs
%exclude %python3_sitelibdir/*/pickle

%files pickles
%python3_sitelibdir/*/pickle

%files docs
%doc docs/_build/html examples
%endif

%changelog
* Fri Nov 06 2020 Vitaly Lipatov <lav@altlinux.ru> 2.0-alt1
- new version 2.0 (with rpmrb script)
- return to build from tarball
- don't pack tests

* Sun Feb 09 2020 Vitaly Lipatov <lav@altlinux.ru> 0.12.1-alt3
- add conflicts/obsoletes to python-module-webassets

* Thu Feb 06 2020 Andrey Bychkov <mrdrew@altlinux.org> 0.12.1-alt2
- Porting on python3.

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.12.1-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Wed Oct 04 2017 Vitaly Lipatov <lav@altlinux.ru> 0.12.1-alt1
- switch to build from tarball
- new version (0.12.1) with rpmgs script

* Thu Feb 19 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.11-alt1.dev.git20150202
- Initial build for Sisyphus

