%define _unpackaged_files_terminate_build 1
%define oname svgwrite

Name: python3-module-%oname
Version: 1.4.2
Release: alt1

Summary: A Python library to create SVG drawings

License: MIT
Group: Development/Python3
Url: https://pypi.python.org/pypi/svgwrite

Source: %name-%version.tar

BuildArch: noarch

BuildRequires(pre): rpm-build-python3

%description
A Python library to create SVG drawings.

%prep
%setup

%build
%python3_build

%install
%python3_install

%files
%doc *.TXT
%python3_sitelibdir/%oname
%python3_sitelibdir/%oname-%version-py%_python3_version.egg-info

%changelog
* Wed Jun 29 2022 Grigory Ustinov <grenka@altlinux.org> 1.4.2-alt1
- Build new version.

* Fri Jul 23 2021 Grigory Ustinov <grenka@altlinux.org> 1.1.9-alt2
- Drop python2 support.

* Wed Jan 11 2017 Igor Vlasenko <viy@altlinux.ru> 1.1.9-alt1
- automated PyPI update

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.1.6-alt1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Mon Aug 25 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1.6-alt1
- Initial build for Sisyphus

