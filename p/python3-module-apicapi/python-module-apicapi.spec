%define oname apicapi

Name:       python3-module-%oname
Version:    1.6.4
Release:    alt1

Summary:    Library for APIC REST api

License:    ASL 2.0
URL:        http://github.com/noironetworks/apicapi
Group:      Development/Python3

Source:     %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-module-html5lib python3-module-oslo.db

BuildArch:  noarch

%add_python3_req_skip oslo.config oslo.db.sqlalchemy
%py3_requires oslo_config oslo_db.sqlalchemy

%description
There is a Python library provides an interface to the APIC REST api.

%prep
%setup

# Let RPM handle the dependencies
rm -f test-requirements.txt requirements.txt

%build
%python3_build

%install
%python3_install

# Delete tests
rm -fr %buildroot%python_sitelibdir/*/test
rm -fr %buildroot%python3_sitelibdir/*/test

%files
%_bindir/*
%python3_sitelibdir/*

%changelog
* Fri Oct 25 2019 Grigory Ustinov <grenka@altlinux.org> 1.6.4-alt1
- Updated version to 1.6.4.
- Build without python2.

* Thu May 24 2018 Andrey Bychkov <mrdrew@altlinux.org> 1.6.0-alt1
- Updated version to 1.6.0

* Sat May 19 2018 Andrey Bychkov <mrdrew@altlinux.org> 1.0.3-alt2
- rebuild with python3.6

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.0.3-alt1.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 1.0.3-alt1.1
- NMU: Use buildreq for BR.

* Fri Mar 13 2015 Alexey Shabalin <shaba@altlinux.ru> 1.0.3-alt1
- Initial release for Sisyphus

