%define oname yuicompressor

%def_with python3

Name: python-module-%oname
Version: 2.4.8
Release: alt1
Summary: YUI Compressor packaged for Python
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/yuicompressor/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools-tests jre /proc
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
%endif

%py_provides %oname
Requires: jre /proc

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
* Fri Feb 13 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.4.8-alt1
- Initial build for Sisyphus

