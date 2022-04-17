%def_disable check

Name: python3-module-jedi
Version: 0.18.1
Release: alt1
Summary: An autocompletion tool for Python that can be used for text editors
License: MIT
Group: Development/Python
Url: https://pypi.python.org/pypi/jedi/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/davidhalter/jedi.git
Source: jedi-%version.tar.gz
BuildArch: noarch

BuildRequires(pre): rpm-build-python3
BuildRequires(pre): rpm-macros-sphinx3
# Automatically added by buildreq on Mon Feb 01 2021
# optimized out: ca-trust python-modules python-sphinx-objects.inv python2-base python3 python3-base python3-dev python3-module-Pygments python3-module-alabaster python3-module-babel python3-module-cffi python3-module-chardet python3-module-cryptography python3-module-docutils python3-module-idna python3-module-imagesize python3-module-jinja2 python3-module-markupsafe python3-module-openssl python3-module-packaging python3-module-pkg_resources python3-module-pytz python3-module-requests python3-module-sphinx python3-module-urllib3 sh4 xz
BuildRequires: ctags python3-module-setuptools python3-module-sphinx_rtd_theme python3-module-sphinxcontrib-applehelp python3-module-sphinxcontrib-devhelp python3-module-sphinxcontrib-htmlhelp python3-module-sphinxcontrib-jsmath python3-module-sphinxcontrib-qthelp python3-module-sphinxcontrib-serializinghtml

BuildRequires: python3-module-parso

%description
Jedi is an autocompletion tool for Python that can be used in
IDEs/editors. Jedi works. Jedi is fast. It understands all of the basic
Python syntax elements including many builtin functions.

Additionaly, Jedi suports two different goto functions and has support
for renaming as well as Pydoc support and some other IDE features.

%package pickles
Summary: Pickles for jedi
Group: Development/Python

%description pickles
Jedi is an autocompletion tool for Python that can be used in
IDEs/editors. Jedi works. Jedi is fast. It understands all of the basic
Python syntax elements including many builtin functions.

Additionaly, Jedi suports two different goto functions and has support
for renaming as well as Pydoc support and some other IDE features.

This package contains pickles for jedi.

%package docs
Summary: Documentation for jedi
Group: Development/Documentation
BuildArch: noarch

%description docs
Jedi is an autocompletion tool for Python that can be used in
IDEs/editors. Jedi works. Jedi is fast. It understands all of the basic
Python syntax elements including many builtin functions.

Additionaly, Jedi suports two different goto functions and has support
for renaming as well as Pydoc support and some other IDE features.

This package contains documentation for jedi.

%prep
%setup -n jedi-%version

sed -i 's|env python|env python3|' sith.py

ln -s ../objects.inv docs/

%build
%python3_build_debug

%prepare_sphinx3 .
%make -C docs pickle SPHINXBUILD=py3_sphinx-build BUILDDIR=_build3
%make -C docs html SPHINXBUILD=py3_sphinx-build BUILDDIR=_build3

%install
install -D -m755 sith.py %buildroot%_bindir/sith.py

%python3_install

cp -fR docs/_build3/pickle %buildroot%python3_sitelibdir/jedi/

%check
export LC_ALL=en_US.UTF-8
python3 setup.py test
rm -fR build
py.test-%_python3_version -vv

%files
%doc *.txt *.rst
%_bindir/*
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/pickle

%files pickles
%python3_sitelibdir/*/pickle

%files docs
%doc docs/_build3/html/*

%changelog
* Sun Apr 17 2022 Fr. Br. George <george@altlinux.org> 0.18.1-alt1
- Autobuild version bump to 0.18.1

* Mon Feb 01 2021 Fr. Br. George <george@altlinux.ru> 0.18.0-alt1
- Autobuild version bump to 0.18.0

* Tue Apr 28 2020 Andrey Cherepanov <cas@altlinux.org> 0.12.1-alt1.1
- Set versioned Python2 interpreter in shebang.

* Fri Aug 03 2018 Fr. Br. George <george@altlinux.ru> 0.12.1-alt1
- Autobuild version bump to 0.12.1

* Wed May 16 2018 Andrey Bychkov <mrdrew@altlinux.org> 0.9.0-alt1.git20150623.1.2
- (NMU) rebuild with python3.6

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.9.0-alt1.git20150623.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.9.0-alt1.git20150623.1
- NMU: Use buildreq for BR.

* Sat Aug 08 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9.0-alt1.git20150623
- Version 0.9.0

* Sun Jan 04 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.8.1-alt1.final0.git20150102
- Initial build for Sisyphus

