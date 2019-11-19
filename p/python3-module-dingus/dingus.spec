%define oname dingus

Name: python3-module-%oname
Version: 0.3.4
Release: alt2

Summary: A record-then-assert mocking library
License: MIT
Group: Development/Python3
Url: https://pypi.python.org/pypi/dingus/
BuildArch: noarch

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3


%description
A dingus is sort of like a mock object. The main difference is that you
don't set up expectations ahead of time. You just run your code, using a
dingus in place of another object or class, and it will record what
happens to it. Then, once your code has been exercised, you can make
assertions about what it did to the dingus.

%prep
%setup

%build
%python3_build_debug

%install
%python3_install

%files
%doc *.txt
%python3_sitelibdir/*


%changelog
* Tue Nov 19 2019 Andrey Bychkov <mrdrew@altlinux.org> 0.3.4-alt2
- python2 disabled

* Wed May 16 2018 Andrey Bychkov <mrdrew@altlinux.org> 0.3.4-alt1.2
- (NMU) rebuild with python3.6

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.3.4-alt1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Sat Jul 19 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3.4-alt1
- Initial build for Sisyphus

