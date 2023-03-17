%define oname netkit

Name: python3-module-%oname
Version: 3.1.10
Release: alt1

Summary: Useful kit for network programming
License: MIT
Group: Development/Python3
Url: https://pypi.python.org/pypi/netkit/
BuildArch: noarch

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3

%description
Useful kit for network programming.

%prep
%setup

%build
%python3_build_debug

%install
%python3_install

%files
%doc PKG-INFO
%python3_sitelibdir/%oname
%python3_sitelibdir/%oname-%version-*.egg-info


%changelog
* Thu Mar 09 2023 Anton Vyatkin <toni@altlinux.org> 3.1.10-alt1
- new version 3.1.10

* Mon Feb 10 2020 Andrey Bychkov <mrdrew@altlinux.org> 0.2.116-alt2
- Build for python3 disabled.

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.2.116-alt1.git20141127.1.1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.2.116-alt1.git20141127.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.2.116-alt1.git20141127.1
- NMU: Use buildreq for BR.

* Thu Nov 27 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2.116-alt1.git20141127
- Version 0.2.116

* Tue Nov 25 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2.115-alt1.git20141125
- Initial build for Sisyphus

