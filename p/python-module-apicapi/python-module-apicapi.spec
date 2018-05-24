%define oname apicapi

Name:       python-module-%oname
Version:    1.6.0
Release:    alt1

Summary:    Library for APIC REST api
License:    ASL 2.0
URL:       http://github.com/noironetworks/%oname
Group:      Development/Python
BuildArch:  noarch

Source:    %name-%version.tar

BuildRequires: python-module-html5lib python-module-oslo.db
%add_python_req_skip oslo.config oslo.db.sqlalchemy
%py_requires oslo_config oslo_db.sqlalchemy

BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-module-html5lib python3-module-oslo.db


%description
There is a Python library provides an interface to the APIC REST api.

%package -n python3-module-%oname
Summary: Library for APIC REST api
Group: Development/Python3
%add_python3_req_skip oslo.config oslo.db.sqlalchemy
%py3_requires oslo_config oslo_db.sqlalchemy

%description -n python3-module-%oname
There is a Python library provides an interface to the APIC REST api.

%prep
%setup

# Let RPM handle the dependencies
rm -f test-requirements.txt requirements.txt

rm -rf ../python3
cp -a . ../python3

%build
%python_build

pushd ../python3
%python3_build
popd

%install
pushd ../python3
%python3_install
popd
mv %buildroot%_bindir/apic-cleanup %buildroot%_bindir/python3-apic-cleanup
mv %buildroot%_bindir/apic-route-reflector %buildroot%_bindir/python3-apic-route-reflector

%python_install

# Delete tests
rm -fr %buildroot%python_sitelibdir/*/test
rm -fr %buildroot%python3_sitelibdir/*/test

%files
%doc AUTHORS README.rst
%_bindir/*
%exclude %_bindir/python3-*
%python_sitelibdir/*

%files -n python3-module-%oname
%_bindir/python3-*
%python3_sitelibdir/*


%changelog
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

