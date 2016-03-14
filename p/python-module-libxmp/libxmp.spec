%define oname libxmp

%def_with python3

Name: python-module-%oname
Version: 2.0.1
Release: alt1.git20150205.1.1
Summary: Python support for the DjVu image format
License: GPLv2
Group: Development/Python
Url: https://github.com/python-xmp-toolkit/python-xmp-toolkit
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/python-xmp-toolkit/python-xmp-toolkit.git
Source: %name-%version.tar
BuildArch: noarch

#BuildPreReq: python-devel python-module-setuptools-tests libexempi
#BuildPreReq: python-module-mock python-module-pytz
#BuildPreReq: python-module-sphinx-devel
%if_with python3
BuildRequires(pre): rpm-build-python3
#BuildPreReq: python3-devel python3-module-setuptools-tests
#BuildPreReq: python3-module-mock python3-module-pytz
%endif

%py_provides %oname
%py_requires pytz
%ifarch x86_64
Requires: libexempi.so.3()(64bit)
%else
Requires: libexempi
%endif

BuildRequires(pre): rpm-macros-sphinx
# Automatically added by buildreq on Thu Jan 28 2016 (-bi)
# optimized out: python-base python-devel python-module-PyStemmer python-module-Pygments python-module-babel python-module-cssselect python-module-funcsigs python-module-genshi python-module-jinja2 python-module-jinja2-tests python-module-markupsafe python-module-pbr python-module-pytest python-module-pytz python-module-setuptools python-module-six python-module-snowballstemmer python-module-sphinx python-module-sphinx_rtd_theme python-module-unittest2 python-modules python-modules-compiler python-modules-ctypes python-modules-email python-modules-encodings python-modules-json python-modules-logging python-modules-multiprocessing python-modules-unittest python3 python3-base python3-module-cffi python3-module-cryptography python3-module-cssselect python3-module-enum34 python3-module-genshi python3-module-ntlm python3-module-pip python3-module-pycparser python3-module-pytest python3-module-setuptools
BuildRequires: libexempi python-module-alabaster python-module-docutils python-module-html5lib python-module-mock python-module-objects.inv python-module-setuptools-tests python3-module-html5lib python3-module-pbr python3-module-pytz python3-module-setuptools-tests python3-module-unittest2 rpm-build-python3 time

%description
python-djvulibre is a set of Python bindings for the DjVuLibre library,
an open source implementation of DjVu.

%if_with python3
%package -n python3-module-%oname
Summary: Python support for the DjVu image format
Group: Development/Python3
%py3_provides %oname
%py3_requires pytz
%ifarch x86_64
Requires: libexempi.so.3()(64bit)
%else
Requires: libexempi
%endif

%description -n python3-module-%oname
python-djvulibre is a set of Python bindings for the DjVuLibre library,
an open source implementation of DjVu.
%endif

%package pickles
Summary: Pickles for %oname
Group: Development/Python

%description pickles
python-djvulibre is a set of Python bindings for the DjVuLibre library,
an open source implementation of DjVu.

This package contains pickles for %oname.

%prep
%setup

%if_with python3
cp -fR . ../python3
%endif

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

export PYTHONPATH=$PWD
%make -C docs pickle
%make -C docs html
cp -fR docs/.build/pickle %buildroot%python_sitelibdir/%oname/

%check
python setup.py test -v
%if_with python3
pushd ../python3
python3 setup.py test -v
popd
%endif

%files
%doc AUTHORS CHANGELOG *.rst docs/.build/html
%python_sitelibdir/*
%exclude %python_sitelibdir/*/pickle

%files pickles
%python_sitelibdir/*/pickle

%if_with python3
%files -n python3-module-%oname
%doc AUTHORS CHANGELOG *.rst docs/.build/html
%python3_sitelibdir/*
%endif

%changelog
* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 2.0.1-alt1.git20150205.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 2.0.1-alt1.git20150205.1
- NMU: Use buildreq for BR.

* Sun Aug 16 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0.1-alt1.git20150205
- Initial build for Sisyphus

