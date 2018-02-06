%define oname yuicompressor

%def_with python3

Name: python-module-%oname
Version: 2.4.8
Release: alt1.1.1.1
Summary: YUI Compressor packaged for Python
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/yuicompressor/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar
BuildArch: noarch

#BuildPreReq: python-devel python-module-setuptools jre /proc
%if_with python3
BuildRequires(pre): rpm-build-python3
#BuildPreReq: python3-devel python3-module-setuptools
%endif

%py_provides %oname
Requires: jre /proc

# Automatically added by buildreq on Thu Jan 28 2016 (-bi)
# optimized out: python-base python-devel python-module-pytest python-module-setuptools python-modules python-modules-compiler python-modules-ctypes python-modules-email python-modules-encodings python-modules-unittest python3 python3-base python3-module-pytest python3-module-setuptools
BuildRequires: python-module-setuptools python3-module-setuptools rpm-build-python3

%description
YUI Compressor is a JavaScript and CSS minifier written in Java. This
package bundles the YUI Compressor JAR file to ease its use in Python
projects.

%package -n python3-module-%oname
Summary: YUI Compressor packaged for Python
Group: Development/Python3
%py3_provides %oname
Requires: jre /proc

%description -n python3-module-%oname
YUI Compressor is a JavaScript and CSS minifier written in Java. This
package bundles the YUI Compressor JAR file to ease its use in Python
projects.

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

%check
python setup.py test
%if_with python3
pushd ../python3
python3 setup.py test
popd
%endif

%files
%doc CHANGES README
%_bindir/*
%if_with python3
%exclude %_bindir/*.py3
%endif
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc CHANGES README
%_bindir/*.py3
%python3_sitelibdir/*
%endif

%changelog
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 2.4.8-alt1.1.1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 2.4.8-alt1.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 2.4.8-alt1.1
- NMU: Use buildreq for BR.

* Fri Feb 13 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.4.8-alt1
- Initial build for Sisyphus

