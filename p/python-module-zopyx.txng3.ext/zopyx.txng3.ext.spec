%define mname zopyx.txng3
%define oname %mname.ext
Name: python-module-%oname
Version: 3.3.7
Release: alt1.git20141102
Summary: TextIndexNG3 extension modules
License: ZPLv2.1
Group: Development/Python
Url: https://pypi.python.org/pypi/zopyx.txng3.ext/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/zopyx/zopyx.txng3.ext.git
Source: %name-%version.tar

BuildPreReq: python-module-setuptools-tests python-module-nose

%py_provides %oname
%py_requires %mname

%description
Helper modules for TextIndexNG3 (Snowball stemmer, normalizer, splitter,
etc.)

%prep
%setup

%build
%python_build_debug

%install
%python_install

install -p -m644 zopyx/txng3/ext/__init__.py \
	%buildroot%python_sitelibdir/zopyx/txng3/ext/

%check
python setup.py test

%files
%doc *.txt
%python_sitelibdir/zopyx/txng3/*
%python_sitelibdir/*.egg-info

%changelog
* Mon Nov 24 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.3.7-alt1.git20141102
- Initial build for Sisyphus

