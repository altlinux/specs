%define oname Eve-Elastic

%def_disable check

Name: python3-module-%oname
Version: 0.2.5
Release: alt2

Summary: Elasticsearch data layer for eve rest framework
License: GPLv3
Group: Development/Python3
Url: https://pypi.python.org/pypi/Eve-Elastic/
# https://github.com/petrjasek/eve-elastic.git
BuildArch: noarch

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3

%py3_provides eve_elastic

BuildRequires: python3-module-nose python3-module-pytest python3-module-urllib3


%description
Eve-Elastic is elasticsearch data layer for eve REST framework.

Features:

* fulltext search
* filtering via elasticsearch filter dsl
* facets support
* aggragations support
* elasticsearch mapping generator for schema

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
%doc *.md *.rst
%python3_sitelibdir/*


%changelog
* Thu Nov 14 2019 Andrey Bychkov <mrdrew@altlinux.org> 0.2.5-alt2
- python2 disabled

* Wed May 16 2018 Andrey Bychkov <mrdrew@altlinux.org> 0.2.5-alt1.git20150209.1.2
- (NMU) rebuild with python3.6

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.2.5-alt1.git20150209.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Wed Jan 27 2016 Mikhail Efremov <sem@altlinux.org> 0.2.5-alt1.git20150209.1
- NMU: Use buildreq for BR.

* Tue Feb 10 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2.5-alt1.git20150209
- Version 0.2.5

* Fri Nov 28 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2.0-alt1.git20141124
- Initial build for Sisyphus

