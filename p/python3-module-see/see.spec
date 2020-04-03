%define oname see

Name: python3-module-%oname
Version: 1.1.1
Release: alt2

Summary: A human-readable alternative to dir
License: BSD
Group: Development/Python3
Url: https://pypi.python.org/pypi/see

BuildArch: noarch

# https://github.com/inky/see.git
Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel

%py3_provides %oname

%description
An alternative to Python's dir function. Easy to type; easy to read! For
humans only.

%prep
%setup

%build
%python3_build_debug

%install
%python3_install

%files
%doc *.md *.rst
%python3_sitelibdir/*

%changelog
* Fri Apr 03 2020 Andrey Bychkov <mrdrew@altlinux.org> 1.1.1-alt2
- Build for python2 disabled.

* Tue Apr 30 2019 Grigory Ustinov <grenka@altlinux.org> 1.1.1-alt1.git20150417.2
- Rebuild with python3.7.

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.1.1-alt1.git20150417.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Sat Jul 25 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1.1-alt1.git20150417
- Initial build for Sisyphus

