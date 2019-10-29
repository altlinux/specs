%define oname yams

Name: python3-module-%oname
Version: 0.45.1
Release: alt2

Summary: Entity / relation schema
License: LGPL
Group: Development/Python3
Url: https://pypi.python.org/pypi/yams/
BuildArch: noarch

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-logilab-common python-tools-2to3
BuildRequires: python3-module-logilab-database python3-module-six

%py_provides %oname


%description
Yet Another Magic Schema ! A simple/generic but powerful entities /
relations schema, suitable to represent RDF like data. The schema is
readable/writable from/to various formats.

%prep
%setup

find -type f \( -name '*.py' -o -name 'owl2yams' -o -name 'yams-check' \
             -o -name 'yams-view' \) -exec 2to3 -w -n '{}' +

sed -i 's|#!/usr/bin/env python|#!/usr/bin/env python3|' \
    $(find ./ \( -name '*.py' -o -name 'owl2yams' -o -name 'yams-check' \
              -o -name 'yams-view' \))
sed -i 's|#!/usr/bin/python|#!/usr/bin/python3|' \
    $(find ./ \( -name '*.py' -o -name 'owl2yams' -o -name 'yams-check' \
              -o -name 'yams-view' \))

%build
%python3_build_debug

%install
%python3_install

%check
python3 setup.py test

%files
%doc ChangeLog README
%_bindir/*
%python3_sitelibdir/*


%changelog
* Tue Oct 29 2019 Andrey Bychkov <mrdrew@altlinux.org> 0.45.1-alt2
- python2 -> python3

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.45.1-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Mon Oct 16 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 0.45.1-alt1
- Updated to upstream version 0.45.1.

* Tue Dec 23 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.40.2-alt1
- Version 0.40.2

* Wed Nov 05 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.40.0-alt1
- Version 0.40.0

* Wed Nov 05 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.39.1-alt1
- Initial build for Sisyphus

