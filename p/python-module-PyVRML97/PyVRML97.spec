%define oname PyVRML97

%def_with python3

Name: python-module-%oname
Version: 2.3.0
Release: alt1.b1.1
Summary: VRML97 Scenegraph model for Python
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/PyVRML97
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python-tools-2to3
%endif

%description
This project provides a core semantic model for VRML97 objects which is
close to (but not identical to) that specified in the VRML97 spec. It is
primarily used for the OpenGLContext project's VRML97 rendering engine,
but can also be used for generating, parsing or processing VRML97
scenegraphs.

%package -n python3-module-%oname
Summary: VRML97 Scenegraph model for Python
Group: Development/Python3

%description -n python3-module-%oname
This project provides a core semantic model for VRML97 objects which is
close to (but not identical to) that specified in the VRML97 spec. It is
primarily used for the OpenGLContext project's VRML97 rendering engine,
but can also be used for generating, parsing or processing VRML97
scenegraphs.

%prep
%setup

%if_with python3
cp -fR . ../python3
find ../python3 -type f -name '*.py' -exec 2to3 -w -n '{}' +
%endif

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

%files
%doc *.txt
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc *.txt
%python3_sitelibdir/*
%endif

%changelog
* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 2.3.0-alt1.b1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Sun Aug 24 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.3.0-alt1.b1
- Initial build for Sisyphus

