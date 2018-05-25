%define oname facebook-scribe

%def_without bootstrap

Name: python-module-%oname
Version: 2.0
Release: alt2.1

Summary: A Python client for Facebook Scribe
License: ASL v2.0
Group: Development/Python
Url: https://pypi.python.org/pypi/facebook-scribe/
# https://github.com/tomprimozic/scribe-python.git
BuildArch: noarch

Source: %name-%version.tar

BuildRequires: python-devel python-module-setuptools

BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools


%description
This is a Python client for scribe.

%package -n python3-module-%oname
Summary: A Python client for Facebook Scribe
Group: Development/Python3
%if_with bootstrap
%add_python3_req_skip thrift
%endif

%description -n python3-module-%oname
This is a Python client for scribe.

%prep
%setup

cp -fR . ../python3

%build
%python_build_debug

pushd ../python3
%python3_build_debug
popd

%install
%python_install

pushd ../python3
%python3_install
popd

%files
%doc *.md
%python_sitelibdir/*

%files -n python3-module-%oname
%doc *.md
%python3_sitelibdir/*


%changelog
* Fri May 25 2018 Andrey Bychkov <mrdrew@altlinux.org> 2.0-alt2.1
- rebuild with all requires

* Sun May 20 2018 Andrey Bychkov <mrdrew@altlinux.org> 2.0-alt2
- rebuild with python3.6

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 2.0-alt1.git20130530.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Tue Sep 30 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0-alt1.git20130530
- Initial build for Sisyphus

