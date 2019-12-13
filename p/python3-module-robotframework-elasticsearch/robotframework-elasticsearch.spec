%define oname robotframework-elasticsearch

Name: python3-module-%oname
Version: 1.1
Release: alt3

Summary: ElasticSearch library for Robot Framework
License: GPLv2
Group: Development/Python3
Url: https://pypi.python.org/pypi/robotframework-elasticsearch/
BuildArch: noarch

# https://github.com/pagesjaunes/robotframework-elasticsearch.git
Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-robotframework
BuildRequires: python3-module-elasticsearch
BuildRequires: python-tools-2to3

%py3_provides ElasticSearchLib
%py3_requires robotframework elasticsearch


%description
This lib provides basic keywords to interact with elasticsearch in a
RobotFramework testsuite. It allows to query, count, create or delete an
index.

%prep
%setup

sed -i 's|#!/usr/bin/env python|#!/usr/bin/env python3|' \
    $(find ./ -name '*.py')

find ./ -type f -name '*.py' -exec 2to3 -w -n '{}' +

%build
%python3_build_debug

%install
%python3_install

%check
%__python3 setup.py build_ext -i

%files
%doc *.md doc/*
%python3_sitelibdir/*


%changelog
* Fri Dec 13 2019 Andrey Bychkov <mrdrew@altlinux.org> 1.1-alt3
- build for python2 disabled

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 1.1-alt2.git20150114.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Wed Dec 27 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 1.1-alt2.git20150114
- Fixed build.

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.1-alt1.git20150114.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Fri Mar 06 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1-alt1.git20150114
- Version 1.1
- Added module for Python 3

* Tue Dec 23 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0-alt1.git20141223
- Initial build for Sisyphus

