%define oname openid-selector

Name: python3-module-%oname
Version: 0.2
Release: alt2

Summary: Simple Javascript OpenID selector
License: BSD
Group: Development/Python3
Url: https://github.com/frgomes/openid-selector
BuildArch: noarch

# https://github.com/frgomes/openid-selector.git
Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3

%py3_provides openid_selector


%description
This is a simple Javascript OpenID selector. It has been designed so
that users do not even need to know what OpenID is to use it, they
simply select their account by a recognisable logo.

%prep
%setup

%build
%python3_build_debug

%install
%python3_install

%files
%doc *.txt *.html
%python3_sitelibdir/*


%changelog
* Wed Nov 27 2019 Andrey Bychkov <mrdrew@altlinux.org> 0.2-alt2
- python2 disabled

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.2-alt1.git20131126.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Sat Oct 11 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2-alt1.git20131126
- Initial build for Sisyphus

