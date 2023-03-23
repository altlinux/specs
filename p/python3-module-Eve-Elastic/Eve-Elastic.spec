%define oname Eve-Elastic

Name: python3-module-%oname
Version: 7.3.0
Release: alt1

Summary: Elasticsearch data layer for eve rest framework
License: GPLv3
Group: Development/Python3
Url: https://pypi.org/project/Eve-Elastic
Vcs: https://github.com/petrjasek/eve-elastic.git

Source: %name-%version.tar

BuildArch: noarch

BuildRequires(pre): rpm-build-python3

%py3_provides eve_elastic

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

%build
%python3_build

%install
%python3_install

%files
%doc *.md *.rst
%python3_sitelibdir/eve_elastic
%python3_sitelibdir/Eve_Elastic-%version-*.egg-info


%changelog
* Thu Mar 23 2023 Anton Vyatkin <toni@altlinux.org> 7.3.0-alt1
- New version 7.3.0.

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

