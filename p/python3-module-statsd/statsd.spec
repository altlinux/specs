%define oname statsd

Name: python3-module-%oname
Version: 4.0.1
Release: alt1

Summary: A simple statsd client

License: MIT
Group: Development/Python3
URL: https://pypi.org/project/statsd
VCS: https://github.com/jsocol/pystatsd

Source: %name-%version.tar

BuildArch: noarch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-wheel

%description
statsd is a friendly front-end to Graphite. This is a Python client for
the statsd daemon.

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

%files
%doc LICENSE AUTHORS *.rst *.md
%python3_sitelibdir/%oname
%python3_sitelibdir/%oname-%version.dist-info
%exclude %python3_sitelibdir/*/tests.*
%exclude %python3_sitelibdir/*/*/tests.*

%changelog
* Mon Jun 03 2024 Grigory Ustinov <grenka@altlinux.org> 4.0.1-alt1
- Build new version.

* Mon Sep 26 2022 Grigory Ustinov <grenka@altlinux.org> 3.3.0-alt1
- Build new version.

* Mon Oct 19 2020 Stanislav Levin <slev@altlinux.org> 3.2.1-alt2
- Stopped Python2 package build.

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 3.2.1-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Thu May 25 2017 Alexey Shabalin <shaba@altlinux.ru> 3.2.1-alt1
- 3.2.1

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 3.0.1-alt1.git20141105.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 3.0.1-alt1.git20141105.1
- NMU: Use buildreq for BR.

* Wed Mar 11 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.0.1-alt1.git20141105
- Initial build for Sisyphus

