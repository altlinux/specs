%define oname google

Name: python3-module-google
Version: 3.0.0
Release: alt1

Summary: Python bindings to the Google search engine

License: BSD
Group: Development/Python3
Url: https://pypi.python.org/pypi/google/

# Source-url: %__pypi_url %oname
Source: %name-%version.tar

BuildArch: noarch

BuildRequires(pre): rpm-build-intro >= 2.1.3
BuildRequires(pre): rpm-build-python3

Obsoletes: python3-module-google.google
Provides: python3-module-google.google = %EVR

%description
Python bindings to the Google search engine.

%prep
%setup

%build
%python3_build

%install
%python3_install

%files
%doc *.md
%_bindir/*
%python3_sitelibdir/*


%changelog
* Sun Aug 01 2021 Vitaly Lipatov <lav@altlinux.ru> 3.0.0-alt1
- rename package to python3-module-google (as upstream named it)
- cleanup spec, new version 3.0.0 (with rpmrb script)

* Fri Dec 13 2019 Andrey Bychkov <mrdrew@altlinux.org> 1.05-alt2
- build for python2 disabled

* Wed May 16 2018 Andrey Bychkov <mrdrew@altlinux.org> 1.05-alt1.2
- (NMU) rebuild with python3.6

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.05-alt1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Fri Aug 29 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.05-alt1
- Initial build for Sisyphus

