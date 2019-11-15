%define oname jsondatabase

Name: python3-module-%oname
Version: 0.0.3
Release: alt2

Summary: A flat file database for json objects
License: BSD
Group: Development/Python3
Url: https://pypi.python.org/pypi/jsondatabase/
# https://github.com/gunthercox/jsondb.git
BuildArch: noarch

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3

%py3_provides %oname jsondb
%py3_requires json


%description
This is a utility for managing content in a database which stores
content in JSON format.

%prep
%setup

sed -i 's|#!/usr/bin/env python|#!/usr/bin/env python3|' \
    $(find ./ -name '*.py')

%build
%python3_build_debug

%install
%python3_install

%check
python3 setup.py test

%files
%doc *.rst *.md
%python3_sitelibdir/*


%changelog
* Fri Nov 15 2019 Andrey Bychkov <mrdrew@altlinux.org> 0.0.3-alt2
- python2 disabled

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.0.3-alt1.git20150214.1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.0.3-alt1.git20150214.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Mon Feb 16 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.0.3-alt1.git20150214
- Initial build for Sisyphus

