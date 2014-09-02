%define oname defusedxml

%def_with python3

Name: python-module-%oname
Version: 0.4.1
Release: alt1.hg20130328
Summary: XML bomb protection for Python stdlib modules
License: Python
Group: Development/Python
Url: https://pypi.python.org/pypi/defusedxml/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# hg clone https://bitbucket.org/tiran/defusedxml
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-module-setuptools
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
%endif

%description
defusedxml -- defusing XML bombs and other exploits.

%package -n python3-module-%oname
Summary: XML bomb protection for Python stdlib modules
Group: Development/Python3

%description -n python3-module-%oname
defusedxml -- defusing XML bombs and other exploits.

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
* Tue Sep 02 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4.1-alt1.hg20130328
- Initial build for Sisyphus

