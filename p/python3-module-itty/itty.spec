%define oname itty
Name: python3-module-%oname
Version: 0.8.2
Release: alt1.git20140129.1
Summary: The itty-bitty Python web framework
License: BSD
Group: Development/Python3
Url: https://pypi.python.org/pypi/itty/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/toastdriven/itty.git
Source: %name-%version.tar
BuildArch: noarch

BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests

%py3_provides %oname

%description
itty.py is a little experiment, an attempt at a Sinatra influenced
micro-framework that does just enough to be useful and nothing more.

%prep
%setup

%build
%python3_build_debug

%install
%python3_install

%check
python3 setup.py test

%files
%doc AUTHORS *.rst
%python3_sitelibdir/*

%changelog
* Mon Mar 14 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.8.2-alt1.git20140129.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Fri Nov 21 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.8.2-alt1.git20140129
- Initial build for Sisyphus

