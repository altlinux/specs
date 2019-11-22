%define _unpackaged_files_terminate_build 1
%define oname json2xls

%def_disable check

Name: python3-module-%oname
Version: 1.0.0
Release: alt1

Summary: Generate excel by json
License: BSD
Group: Development/Python3
Url: https://pypi.python.org/pypi/json2xls/
# https://github.com/axiaoxin/json2xls.git
BuildArch: noarch

Source0: https://pypi.python.org/packages/b5/15/d42f0e21acd8b6d14ae40be08ca50b32c2b3d97b1b7207575c2629a2e5db/%{oname}-%{version}.tar.gz

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-click python3-module-pytest
BuildRequires: python3-module-requests python3-module-xlwt

%py3_provides %oname
%py3_requires json requests click xlwt


%description
json2xls: Generate Excel by JSON data.

%prep
%setup -q -n %{oname}-%{version}

sed -i 's|#!/usr/bin/env python|#!/usr/bin/env python3|' \
    $(find ./ -name '*.py')

%build
export LC_ALL=en_US.UTF-8
%python3_build_debug

%install
%python3_install

%check
%__python3 setup.py test

%files
%doc *.md docs/*.rst
%_bindir/*
%python3_sitelibdir/*


%changelog
* Fri Nov 22 2019 Andrey Bychkov <mrdrew@altlinux.org> 1.0.0-alt1
- Version updated to 1.0.0
- python2 disabled

* Wed Jan 11 2017 Igor Vlasenko <viy@altlinux.ru> 0.1.3c-alt1
- automated PyPI update

* Sat May 28 2016 Igor Vlasenko <viy@altlinux.ru> 0.1.2-alt2.git20150116
- NMU: rebuild with xlwt

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.1.2-alt1.git20150116.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.1.2-alt1.git20150116.1
- NMU: Use buildreq for BR.

* Sun Jan 18 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.2-alt1.git20150116
- Initial build for Sisyphus

