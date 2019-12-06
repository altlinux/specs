%define _unpackaged_files_terminate_build 1
%define oname intervals

Name: python3-module-%oname
Version: 0.8.0
Release: alt2

Summary: Python tools for handling intervals (ranges of comparable objects)
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/intervals/
BuildArch: noarch

# https://github.com/kvesteri/intervals.git
Source0: https://pypi.python.org/packages/30/7a/7364356d073426b73014bc6f7aab36914fd9fc53e8d99150a0de69d7846a/%{oname}-%{version}.tar.gz

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-html5lib python3-module-infinity
BuildRequires: python3-module-pytest python3-module-sphinx

%py3_provides %oname


%description
Python tools for handling intervals (ranges of comparable objects).

%prep
%setup -q -n %{oname}-%{version}

%build
%python3_build_debug

%install
%python3_install

%check
%__python3 setup.py test

%files
%doc *.rst
%python3_sitelibdir/*


%changelog
* Fri Dec 06 2019 Andrey Bychkov <mrdrew@altlinux.org> 0.8.0-alt2
- python2 disabled

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.8.0-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Wed Jan 11 2017 Igor Vlasenko <viy@altlinux.ru> 0.8.0-alt1
- automated PyPI update

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.3.2-alt1.git20141209.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.3.2-alt1.git20141209.1
- NMU: Use buildreq for BR.

* Tue Dec 23 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3.2-alt1.git20141209
- New snapshot

* Sat Nov 01 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3.2-alt1.git20141021
- Initial build for Sisyphus

