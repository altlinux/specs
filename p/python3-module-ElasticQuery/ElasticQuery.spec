%define oname ElasticQuery

Name: python3-module-%oname
Version: 3.1
Release: alt2

Summary: A simple query builder for Elasticsearch
License: MIT
Group: Development/Python3
Url: https://pypi.python.org/pypi/ElasticQuery/
# https://github.com/Fizzadar/ElasticQuery.git
BuildArch: noarch

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python-tools-2to3
BuildRequires: python3-module-pytest
BuildRequires: python3(jsontest)
BuildRequires: python3(dictdiffer)

%py3_provides elasticquery


%description
A simple query builder for Elasticsearch. Outputs json ready to be sent
to Elasticsearch via your favourite client.

%prep
%setup

## py2 -> py3
find ./ -type f -name '*.py' -exec 2to3 -w -n '{}' +

sed -i 's|#!/usr/bin/env python|#!/usr/bin/env python3|' \
    $(find ./ -name '*.py')
##

%build
%python3_build_debug

%install
%python3_install

%check
python3 setup.py test

%files
%doc *.md
%python3_sitelibdir/*


%changelog
* Thu Nov 14 2019 Andrey Bychkov <mrdrew@altlinux.org> 3.1-alt2
- python2 disabled

* Tue Mar 06 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 3.1-alt1
- Updated to upstream version 3.1.

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.2.0-alt1.git20141125.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Wed Jan 27 2016 Mikhail Efremov <sem@altlinux.org> 0.2.0-alt1.git20141125.1
- NMU: Use buildreq for BR.

* Wed Nov 26 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2.0-alt1.git20141125
- Version 0.2.0

* Thu Nov 06 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.18-alt1.git20141106
- Version 0.1.18

* Sun Nov 02 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.17-alt1.git20141030
- Initial build for Sisyphus

