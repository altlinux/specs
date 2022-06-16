%define _unpackaged_files_terminate_build 1
%define oname hglib

Name: python3-module-%oname
Version: 2.6.2
Release: alt1

Summary: Mercurial Python library

License: MIT
Group: Development/Python3
Url: https://pypi.python.org/pypi/python-hglib/
BuildArch: noarch

Source0: https://pypi.python.org/packages/80/9c/1618281fc1ef0df4436b1435de6276452fefb46b111b3b00d3e20fcf5e17/python-%{oname}-%{version}.tar.gz

BuildRequires(pre): rpm-build-python3

%py3_provides %oname


%description
python-hglib is a library with a fast, convenient interface to
Mercurial. It uses Mercurial's command server for communication with hg.

%prep
%setup -q -n python-%{oname}-%{version}

sed -i 's|#!/usr/bin/env python|#!/usr/bin/env python3|' \
    $(find ./ -name '*.py')

%build
%python3_build

%install
%python3_install

%files
%doc README examples
%python3_sitelibdir/*

%changelog
* Thu Jun 16 2022 Grigory Ustinov <grenka@altlinux.org> 2.6.2-alt1
- Build new version.

* Tue Nov 05 2019 Andrey Bychkov <mrdrew@altlinux.org> 2.6.1-alt1
- version updated to 2.6.1
- disable python2, enable python3

* Wed Jan 11 2017 Igor Vlasenko <viy@altlinux.ru> 2.3-alt1
- automated PyPI update

* Mon Jan 25 2016 Sergey Alembekov <rt@altlinux.ru> 1.5-alt3
- Rebuild with "def_disable check"
- Cleanup buildreq

* Tue Mar 03 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.5-alt2
- Fixed build

* Tue Dec 23 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.5-alt1
- Initial build for Sisyphus

