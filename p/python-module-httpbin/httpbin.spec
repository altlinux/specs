%define oname httpbin

Name: python-module-%oname
Version: 0.6.2
Release: alt1.1
Summary: HTTP Request and Response Service
License: MIT
Group: Development/Python
Url: https://pypi.python.org/pypi/httpbin/
# https://github.com/kennethreitz/httpbin.git
BuildArch: noarch

Source: %oname-%version.tar

%py_provides %oname

BuildRequires: python-module-gunicorn
BuildRequires: python-module-flask-common
BuildRequires: python-module-pytest
BuildRequires: python-module-flask
BuildRequires: python-module-six
BuildRequires: python-module-werkzeug

BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-module-pytest
BuildPreReq: python3-module-flask-common
BuildPreReq: python3-module-flask
BuildPreReq: python3-module-six
BuildPreReq: python3-module-werkzeug

%description
Testing an HTTP Library can become difficult sometimes. PostBin.org is
fantastic for testing POST requests, but not much else. This exists to
cover all kinds of HTTP scenarios. Additional endpoints are being
considered.

All endpoint responses are JSON-encoded.

%package -n python3-module-%oname
Summary: HTTP Request and Response Service
Group: Development/Python3
%py3_provides %oname

%description -n python3-module-%oname
Testing an HTTP Library can become difficult sometimes. PostBin.org is
fantastic for testing POST requests, but not much else. This exists to
cover all kinds of HTTP scenarios. Additional endpoints are being
considered.

All endpoint responses are JSON-encoded.

%prep
%setup -n %oname-%version

rm -rf ../python3
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
%doc AUTHORS *.md LICENSE
%python_sitelibdir/*

%files -n python3-module-%oname
%doc AUTHORS *.md LICENSE
%python3_sitelibdir/*


%changelog
* Fri Mar 30 2018 Andrey Bychkov <mrdrew@altlinux.org> 0.6.2-alt1.1
- Fixed requires

* Wed Mar 28 2018 Andrey Bychkov <mrdrew@altlinux.org> 0.6.2-alt1
- Updated version to 0.6.2

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.2.0-alt1.git20140826.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.2.0-alt1.git20140826.1
- NMU: Use buildreq for BR.

* Mon Nov 10 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2.0-alt1.git20140826
- Initial build for Sisyphus
