%define oname jedi
%def_disable check

Name: python-module-%oname
Version: 0.12.1
Release: alt1.1
Summary: An autocompletion tool for Python that can be used for text editors
License: MIT
Group: Development/Python
Url: https://pypi.python.org/pypi/jedi/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/davidhalter/jedi.git
Source: jedi-%version.tar.gz
BuildArch: noarch

%py_provides %oname

# Automatically added by buildreq on Fri Aug 03 2018
# optimized out: python-base python-module-OpenSSL python-module-PyStemmer python-module-Pygments python-module-SQLAlchemy python-module-asn1crypto python-module-attrs python-module-babel python-module-cffi python-module-chardet python-module-cryptography python-module-docutils python-module-enum34 python-module-funcsigs python-module-idna python-module-imagesize python-module-ipaddress python-module-jinja2 python-module-lxml python-module-markupsafe python-module-ndg-httpsclient python-module-ntlm python-module-pkg_resources python-module-pluggy python-module-py python-module-pycparser python-module-pytest python-module-pytz python-module-requests python-module-simplejson python-module-six python-module-sphinx python-module-sphinxcontrib python-module-typing python-module-urllib3 python-module-webencodings python-module-whoosh python-modules python-modules-compiler python-modules-ctypes python-modules-distutils python-modules-email python-modules-encodings python-modules-json python-modules-logging python-modules-multiprocessing python-modules-unittest python-modules-xml python-sphinx-objects.inv python3 python3-base python3-module-OpenSSL python3-module-Pygments python3-module-babel python3-module-cffi python3-module-chardet python3-module-cryptography python3-module-docutils python3-module-idna python3-module-imagesize python3-module-jinja2 python3-module-markupsafe python3-module-pkg_resources python3-module-pytz python3-module-requests python3-module-six python3-module-sphinx python3-module-urllib3 sh3 xz
BuildRequires: ctags python-module-alabaster python-module-docopt python-module-html5lib python-module-setuptools python-module-sphinxcontrib-websupport python3-dev python3-module-alabaster python3-module-sphinxcontrib-websupport time
BuildRequires(pre): rpm-build-python3
BuildRequires(pre): rpm-macros-sphinx
BuildRequires(pre): rpm-macros-sphinx3
BuildRequires:	python3-module-parso python-module-parso

%description
Jedi is an autocompletion tool for Python that can be used in
IDEs/editors. Jedi works. Jedi is fast. It understands all of the basic
Python syntax elements including many builtin functions.

Additionaly, Jedi suports two different goto functions and has support
for renaming as well as Pydoc support and some other IDE features.

%package -n python3-module-%oname
Summary: An autocompletion tool for Python that can be used for text editors
Group: Development/Python3
%py3_provides %oname

%description -n python3-module-%oname
Jedi is an autocompletion tool for Python that can be used in
IDEs/editors. Jedi works. Jedi is fast. It understands all of the basic
Python syntax elements including many builtin functions.

Additionaly, Jedi suports two different goto functions and has support
for renaming as well as Pydoc support and some other IDE features.

%package pickles
Summary: Pickles for %oname
Group: Development/Python

%description pickles
Jedi is an autocompletion tool for Python that can be used in
IDEs/editors. Jedi works. Jedi is fast. It understands all of the basic
Python syntax elements including many builtin functions.

Additionaly, Jedi suports two different goto functions and has support
for renaming as well as Pydoc support and some other IDE features.

This package contains pickles for %oname.

%package docs
Summary: Documentation for %oname
Group: Development/Documentation
BuildArch: noarch

%description docs
Jedi is an autocompletion tool for Python that can be used in
IDEs/editors. Jedi works. Jedi is fast. It understands all of the basic
Python syntax elements including many builtin functions.

Additionaly, Jedi suports two different goto functions and has support
for renaming as well as Pydoc support and some other IDE features.

This package contains documentation for %oname.

%prep
%setup -n %oname-%version

sed 's|env python|env python3|' < sith.py > sith.py3
subst 's|^#!.*python$|#!%__python|' sith.py

ln -s ../objects.inv docs/

%build
%python_build_debug

%prepare_sphinx .
%make -C docs pickle
%make -C docs html
%prepare_sphinx3 .
%make -C docs SPHINXBUILD=py3_sphinx-build BUILDDIR=_build3 html

%install
install -D -m755 sith.py %buildroot%_bindir/sith.py
install -D -m755 sith.py3 %buildroot%_bindir/sith.py3

%python_install
%python3_install

cp -fR docs/_build/pickle %buildroot%python_sitelibdir/%oname/

%check
export LC_ALL=en_US.UTF-8
python setup.py test
rm -fR build
py.test -vv
python3 setup.py test
rm -fR build
py.test-%_python3_version -vv

%files
%doc *.txt *.rst
%_bindir/*
%exclude %_bindir/*.py3
%python_sitelibdir/*
%exclude %python_sitelibdir/*/pickle

%files pickles
%python_sitelibdir/*/pickle

%files docs
%doc docs/_build/html/*

%files -n python3-module-%oname
%doc *.txt *.rst
%doc docs/_build3/html/*
%_bindir/*.py3
%python3_sitelibdir/*

%changelog
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

