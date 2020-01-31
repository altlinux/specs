%define _unpackaged_files_terminate_build 1

%define oname requests-facebook

Name: python3-module-%oname
Version: 0.4.0
Release: alt2

Summary: A Python Library to interface with Facebook Graph API
License: BSD
Group: Development/Python3
Url: https://pypi.python.org/pypi/requests-facebook/
BuildArch: noarch

# https://github.com/michaelhelmick/requests-facebook.git
Source0: https://pypi.python.org/packages/fd/8a/b47e074ab4c8b06dfb63155af1fe1e3ac7a384c06352d98749eb9c9c124c/%{oname}-%{version}.tar.gz

BuildRequires(pre): rpm-build-python3


%description
Requests-Facebook is a Python library to help interface with Facebook
Graph API using the awesome requests library by @kennethreitz.

%prep
%setup -q -n %{oname}-%{version}

%build
%python3_build_debug

%install
%python3_install

%files
%doc *.rst
%python3_sitelibdir/*


%changelog
* Fri Jan 31 2020 Andrey Bychkov <mrdrew@altlinux.org> 0.4.0-alt2
- Build for python2 disabled.

* Wed Jan 11 2017 Igor Vlasenko <viy@altlinux.ru> 0.4.0-alt1
- automated PyPI update

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.2.1-alt1.git20140225.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Fri Sep 26 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2.1-alt1.git20140225
- Initial build for Sisyphus

