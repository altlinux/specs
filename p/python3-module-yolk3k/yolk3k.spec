%define _unpackaged_files_terminate_build 1
%define oldname yolk
%define oname yolk3k

Name: python3-module-%oname
Version: 0.9
Release: alt2
Summary: Command-line tool for querying PyPI and Python packages installed on your system
License: BSD
Group: Development/Python3
Url: https://pypi.python.org/pypi/yolk3k/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/myint/yolk.git
Source0: https://pypi.python.org/packages/b1/4d/8d00d5e7c07c7969f2134c5af082d338ebcc6027e2ea6c0d6a6bc149d0ec/%{oname}-%{version}.tar.gz
BuildArch: noarch

BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools

%py3_provides %oldname
Conflicts: python3-module-%oldname

Conflicts: python-module-%oname
Obsoletes: python-module-%oname

%description
Yolk is a Python tool for obtaining information about installed Python
packages and querying packages available on PyPI (Python Package Index).
yolk3k is a fork of the original yolk. yolk3k add Python 3 support
(while maintaining Python 2 support). It also adds additional features.

You can see which packages are active, non-active or in development mode
and show you which have newer versions available by querying PyPI.

%prep
%setup -n %oname-%version

%build
%python3_build

%install
%python3_install

%files
%doc CREDITS *.rst
%_bindir/*
%python3_sitelibdir/*

%changelog
* Wed Nov 25 2020 Grigory Ustinov <grenka@altlinux.org> 0.9-alt2
- Build without python2 support.

* Wed Jan 11 2017 Igor Vlasenko <viy@altlinux.ru> 0.9-alt1
- automated PyPI update

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.8.4-alt1.git20140628.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Tue Sep 02 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.8.4-alt1.git20140628
- Initial build for Sisyphus

