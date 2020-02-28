%define oname httreplay

Name: python3-module-%oname
Version: 0.2.0
Release: alt2

Summary: A HTTP replay library for testing
License: MIT
Group: Development/Python3
Url: https://pypi.python.org/pypi/httreplay/

BuildArch: noarch

# https://github.com/davepeck/httreplay.git
Source: %name-%version.tar
Patch0: fix-creation-of-https-connection.patch

BuildRequires(pre): rpm-build-python3


%description
A Python HTTP replay library for testing. Supports [httplib, requests,
urllib3] and HTTP/S requests.

%prep
%setup
%patch0 -p1

%build
%python3_build_debug

%install
%python3_install

%files
%doc *.md
%python3_sitelibdir/*


%changelog
* Fri Feb 28 2020 Andrey Bychkov <mrdrew@altlinux.org> 0.2.0-alt2
- Build for python2 disabled.

* Wed May 16 2018 Andrey Bychkov <mrdrew@altlinux.org> 0.2.0-alt1.git20150126.1.2
- (NMU) rebuild with python3.6

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.2.0-alt1.git20150126.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.2.0-alt1.git20150126.1
- NMU: Use buildreq for BR.

* Tue Jan 27 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2.0-alt1.git20150126
- Initial build for Sisyphus

