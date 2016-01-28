%define oname zest.pocompile

%def_with python3

Name: python-module-%oname
Version: 1.5
Release: alt1.dev0.git20130705.1
Summary: Compile po files when releasing a package
License: GPL
Group: Development/Python
Url: https://pypi.python.org/pypi/zest.pocompile/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/zestsoftware/zest.pocompile.git
Source: %name-%version.tar

#BuildPreReq: python-devel python-module-setuptools-tests
#BuildPreReq: python-module-zest.releaser
#BuildPreReq: python-module-gettext python-module-unittest2
%if_with python3
BuildRequires(pre): rpm-build-python3
#BuildPreReq: python3-devel python3-module-setuptools-tests
#BuildPreReq: python3-module-zest.releaser
#BuildPreReq: python3-module-gettext python3-module-unittest2
%endif

%py_provides %oname
%py_requires zest zest.releaser

# Automatically added by buildreq on Thu Jan 28 2016 (-bi)
# optimized out: python-base python-devel python-module-pytest python-module-setuptools python-module-traceback2 python-modules python-modules-compiler python-modules-ctypes python-modules-email python-modules-encodings python-modules-unittest python3 python3-base python3-module-pytest python3-module-setuptools
BuildRequires: python-module-gettext python-module-setuptools-tests python-module-unittest2 python-module-zest.releaser python3-module-setuptools-tests python3-module-unittest2 python3-module-zest.releaser rpm-build-python3

%description
This package compiles po files. It contains a zest.releaser entry point
and a stand-alone command line tool.

%package -n python3-module-%oname
Summary: Compile po files when releasing a package
Group: Development/Python3
%py3_provides %oname
%py3_requires zest zest.releaser

%description -n python3-module-%oname
This package compiles po files. It contains a zest.releaser entry point
and a stand-alone command line tool.

%prep
%setup

%if_with python3
cp -fR . ../python3
%endif

%build
%python_build_debug

%if_with python3
pushd ../python3
%python3_build_debug
popd
%endif

%install
%if_with python3
pushd ../python3
%python3_install
popd
pushd %buildroot%_bindir
for i in $(ls); do
	mv $i $i.py3
done
popd
%endif

%python_install

%ifarch x86_64
mv %buildroot%_libexecdir %buildroot%_libdir
%endif

%check
python setup.py test
%if_with python3
pushd ../python3
python3 setup.py test
popd
%endif

%files
%doc *.txt
%_bindir/*
%if_with python3
%exclude %_bindir/*.py3
%endif
%python_sitelibdir/zest/*
%python_sitelibdir/*.egg-info

%if_with python3
%files -n python3-module-%oname
%doc *.txt
%_bindir/*.py3
%python3_sitelibdir/zest/*
%python3_sitelibdir/*.egg-info
%endif

%changelog
* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 1.5-alt1.dev0.git20130705.1
- NMU: Use buildreq for BR.

* Thu Oct 23 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.5-alt1.dev0.git20130705
- Initial build for Sisyphus

