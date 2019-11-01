%define oname binstr

Name: python3-module-%oname
Version: 1.3
Release: alt2

Summary: Utility functions for strings of binary digits
License: GPLv3
Group: Development/Python3
Url: https://pypi.python.org/pypi/binstr/
# https://github.com/DavidMcEwan/binstr.git
BuildArch: noarch

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3

%py3_provides %oname


%description
A collection of utility functions for creating and operating on strings
of binary digits. It is compatible with Python versions >2.6 including
3.x.

It is useful to use these functions to make small bugs in your code
easier to find since all inputs are checked thoroughly for errors using
assertions.

%prep
%setup

%build
%python3_build_debug

%install
%python3_install

%check
python3 binstr_test.py -v

%files
%doc *.txt
%python3_sitelibdir/*


%changelog
* Fri Nov 01 2019 Andrey Bychkov <mrdrew@altlinux.org> 1.3-alt2
- disable python2

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.3-alt1.git20110927.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 1.3-alt1.git20110927.1
- NMU: Use buildreq for BR.

* Sat Jan 10 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.3-alt1.git20110927
- Initial build for Sisyphus

