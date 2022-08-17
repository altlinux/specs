%define _unpackaged_files_terminate_build 1
%define oname jsonrpcserver

%def_with check

Name: python3-module-%oname
Version: 5.0.8
Release: alt1

Summary: JSON-RPC 2.0 server library

License: MIT
Group: Development/Python3
Url: https://pypi.python.org/pypi/jsonrpcserver

BuildArch: noarch

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3

%if_with check
BuildRequires: python3-module-pytest
BuildRequires: python3-module-OSlash
BuildRequires: python3-module-jsonschema
%endif

%description
A JSON-RPC 2.0 server library for Python 3.

%prep
%setup

%build
%python3_build

%install
%python3_install

%check
rm -fR build
export PYTHONPATH=%buildroot%python3_sitelibdir
py.test3

%files
%doc *.md
%python3_sitelibdir/%oname
%python3_sitelibdir/%oname-%version-py%_python3_version.egg-info

%changelog
* Wed Aug 17 2022 Grigory Ustinov <grenka@altlinux.org> 5.0.8-alt1
- Automatically updated to 5.0.8.
- Build with check.

* Thu Apr 07 2022 Grigory Ustinov <grenka@altlinux.org> 5.0.7-alt1
- Build new version.

* Mon Apr 13 2020 Andrey Bychkov <mrdrew@altlinux.org> 3.5.3-alt2
- Build for python2 removed.

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 3.5.3-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Tue Dec 19 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 3.5.3-alt1
- Updated to upstream version 3.5.3.

* Wed Jan 11 2017 Igor Vlasenko <viy@altlinux.ru> 3.4.1-alt1
- automated PyPI update

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.0.11-alt1.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 1.0.11-alt1.1
- NMU: Use buildreq for BR.

* Thu Feb 12 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.11-alt1
- Version 1.0.11

* Tue Dec 30 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.8-alt1
- Version 1.0.8

* Thu Dec 11 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.6-alt1
- Version 1.0.6

* Thu Dec 11 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.5-alt1
- Version 1.0.5

* Sat Nov 22 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.4-alt1
- Version 1.0.4

* Fri Nov 21 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.3-alt1
- Version 1.0.3

* Tue Nov 11 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.2-alt1
- Initial build for Sisyphus

