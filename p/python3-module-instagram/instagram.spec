%define oname instagram

Name: python3-module-%oname
Version: 1.3.2
Release: alt1

Summary: Instagram API client
License: MIT
Group: Development/Python3
Url: https://pypi.python.org/pypi/python-instagram/
BuildArch: noarch

# https://github.com/Instagram/python-instagram.git
Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3


%description
Python Client for Instagram API
http://instagram.com/developers/

%prep
%setup

%build
%python3_build_debug

%install
%python3_install

%files
%doc *.md
%python3_sitelibdir/*


%changelog
* Tue Jan 14 2020 Andrey Bychkov <mrdrew@altlinux.org> 1.3.2-alt1
- Version updated to 1.3.2

* Wed May 16 2018 Andrey Bychkov <mrdrew@altlinux.org> 1.1.1-alt1.git20140611.2
- (NMU) rebuild with python3.6

* Mon Mar 14 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.1.1-alt1.git20140611.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Tue Sep 23 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1.1-alt1.git20140611
- Initial build for Susyphus


