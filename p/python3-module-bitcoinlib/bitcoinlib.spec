%define _unpackaged_files_terminate_build 1
%define pname bitcoin
%define oname python-bitcoinlib

%def_disable check

Name: python3-module-bitcoinlib
Version: 0.11.0
Release: alt1

Summary: Provides an easy interface to the Bitcoin data structures and protocol

License: LGPLv3+
Group: Development/Python3
Url: https://pypi.python.org/pypi/python-bitcoinlib/

# Source-url: %__pypi_url %oname
Source: %name-%version.tar

BuildArch: noarch

BuildRequires(pre): rpm-build-intro >= 2.2.5
BuildRequires(pre): rpm-build-python3

%if_with check
BuildRequires: python3-module-pytest
%endif

Provides: python3-module-%pname = %EVR

%py3_provides %pname
%py3_requires json


%description
This Python library provides an easy interface to the bitcoin data
structures and protocol. The approach is low-level and "ground up", with
a focus on providing tools to manipulate the internals of how Bitcoin
works.

%prep
%setup

sed -i 's|#!/usr/bin/env python|#!/usr/bin/env python3|' \
    $(find ./ -name '*.py')

%build
%python3_build

%install
%python3_install
%python3_prune

%check
python3 setup.py test

%files
%doc *.md PKG-INFO
%python3_sitelibdir/*


%changelog
* Sun Sep 12 2021 Vitaly Lipatov <lav@altlinux.ru> 0.11.0-alt1
- new version 0.11.0 (with rpmrb script)
- cleanup spec
- disable packing tests

* Tue Nov 05 2019 Andrey Bychkov <mrdrew@altlinux.org> 0.7.0-alt2
- disable python2

* Tue Jan 17 2017 Igor Vlasenko <viy@altlinux.ru> 0.7.0-alt1
- automated PyPI update

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.3.1-alt1.git20150110.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.3.1-alt1.git20150110.1
- NMU: Use buildreq for BR.

* Sat Jan 17 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3.1-alt1.git20150110
- Initial build for Sisyphus

