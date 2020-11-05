%define oname servicemanager

%def_without bootstrap

Name: python3-module-servicemanager
Version: 2.0.7
Release: alt1

Summary: A python tool to manage developing and testing with lots of microservices

License: ASL v2.0
Group: Development/Python3
Url: https://pypi.python.org/pypi/servicemanager/

BuildArch: noarch

# Source-url: %__pypi_url %oname
Source: %name-%version.tar

Obsoletes: python-module-servicemanager
Provides: python-module-servicemanager

BuildRequires(pre): rpm-build-intro >= 2.2.5
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python3-module-setuptools

%description
A set of utilities to run applications and micro services during the
development and testing phase... and make development easier in a micro
service environment.

%prep
%setup

%build
%python3_build_debug

%install
%python3_install
%python3_prune

%files
%doc *.md
%_bindir/*
%python3_sitelibdir/*

%changelog
* Thu Nov 05 2020 Vitaly Lipatov <lav@altlinux.ru> 2.0.7-alt1
- new version 2.0.7 (with rpmrb script)

* Thu Nov 05 2020 Vitaly Lipatov <lav@altlinux.ru> 0.0.16-alt3
- build python3 package separately

* Thu May 17 2018 Andrey Bychkov <mrdrew@altlinux.org> 0.0.16-alt2
- rebuild with python3.6

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.0.16-alt1.git20141007.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Fri Oct 10 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.0.16-alt1.git20141007
- Initial build for Sisyphus

