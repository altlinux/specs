%define oname libxmp

%def_with python3

Name: python-module-%oname
Version: 2.0.1
Release: alt1.git20150205
Summary: Python support for the DjVu image format
License: GPLv2
Group: Development/Python
Url: https://github.com/python-xmp-toolkit/python-xmp-toolkit
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/python-xmp-toolkit/python-xmp-toolkit.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools-tests libexempi
BuildPreReq: python-module-mock python-module-pytz
BuildPreReq: python-module-sphinx-devel
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: python3-module-mock python3-module-pytz
%endif

%py_provides %oname
%py_requires pytz
%ifarch x86_64
Requires: libexempi.so.3()(64bit)
%else
Requires: libexempi
%endif

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
* Sun Aug 16 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0.1-alt1.git20150205
- Initial build for Sisyphus

