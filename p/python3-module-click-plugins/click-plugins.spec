%define oname click-plugins

Name: python3-module-%oname
Version: 1.0.2
Release: alt4

Summary: Register CLI commands via setuptools entry-points
License: BSD
Group: Development/Python3
Url: https://pypi.python.org/pypi/click-plugins

BuildArch: noarch

# https://github.com/click-contrib/click-plugins.git
Source: %name-%version.tar
Patch0: click-plugins-1.0.2-Click-7-changes-how-command-names-are-generated.patch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-click
BuildRequires: python3-module-pytest-cov

%description
An extension module for click to enable registering CLI commands via
setuptools entry-points.

%package examples
Summary: Examples for %oname
Group: Development/Documentation
BuildArch: noarch

%description examples
An extension module for click to enable registering CLI commands via
setuptools entry-points.

This package contains examples for %oname.

%prep
%setup
%patch -p1

%build
%python3_build_debug

%install
%python3_install

%check
%__python3 setup.py test -v
py.test3 -vv tests --cov click_plugins --cov-report term-missing

%files
%doc *.txt *.rst
%python3_sitelibdir/*

%files examples
%doc example/*

%changelog
* Thu Nov 05 2020 Vitaly Lipatov <lav@altlinux.ru> 1.0.2-alt4
- replace BR python3-module-click-tests with python3-module-click

* Tue Apr 14 2020 Andrey Bychkov <mrdrew@altlinux.org> 1.0.2-alt3
- Build for python2 disabled.

* Thu Aug 08 2019 Stanislav Levin <slev@altlinux.org> 1.0.2-alt2
- Fixed testing against Click 7.

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 1.0.2-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Wed Aug 16 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 1.0.2-alt1
- Updated to upstream version 1.0.2.

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.0-alt1.git20150720.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Wed Aug 12 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0-alt1.git20150720
- Initial build for Sisyphus

