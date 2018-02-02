%define oname libxmp

%def_with python3

Name: python-module-%oname
Version: 2.0.1
Release: alt1.git20150205.2.1
Summary: Python support for the DjVu image format
License: GPLv2
Group: Development/Python
Url: https://github.com/python-xmp-toolkit/python-xmp-toolkit

# https://github.com/python-xmp-toolkit/python-xmp-toolkit.git
Source: %name-%version.tar
Patch1: %oname-%version-upstream-test.patch
BuildArch: noarch

BuildRequires: libexempi python-module-alabaster python-module-docutils python-module-html5lib python-module-mock python-module-objects.inv python-module-setuptools
BuildRequires(pre): rpm-macros-sphinx
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-html5lib python3-module-pbr python3-module-pytz python3-module-setuptools python3-module-unittest2
%endif

%py_provides %oname
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
%patch1 -p1

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
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 2.0.1-alt1.git20150205.2.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Mon Aug 14 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 2.0.1-alt1.git20150205.2
- Fixed build.

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 2.0.1-alt1.git20150205.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 2.0.1-alt1.git20150205.1
- NMU: Use buildreq for BR.

* Sun Aug 16 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0.1-alt1.git20150205
- Initial build for Sisyphus

