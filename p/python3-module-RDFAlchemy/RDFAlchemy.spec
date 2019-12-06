%define oname RDFAlchemy

Name: python3-module-%oname
Version: 0.2.9
Release: alt3
Epoch: 1

Summary: rdflib wrapper for Python
License: BSD
Group: Development/Python3
Url: http://pypi.python.org/pypi/RDFAlchemy/
BuildArch: noarch

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-sphinx python-tools-2to3 python3-module-setuptools

%py3_provides %oname
%py3_requires paste.script


%description
RDFAlchemy is an abstraction layer, allowing python developers to use
familiar dot notation to access and update an rdf triplestore.

%prep
%setup

sed -i 's|@VERSION@|%version|' rdfalchemy/__init__.py

for i in $(find . -name '.*'); do
    if [ "$i" != "." ]; then
        rm -fR $i
    fi
done

%build
find -type f -name '*.py' -exec sed -i 's|%_bindir/env python|%_bindir/python3|' -- '{}' +
find -type f -name '*.py' -exec 2to3 -w '{}' +

for i in rdfalchemy/sparql/sesame2.py \
    rdfalchemy/sparql/parsers.py
do
    sed -i 's|import simplejson|import json as simplejson|' $i
done

%python3_build

%install
%python3_install

%files
%doc LICENSE README
%_bindir/sparql
%python3_sitelibdir/*


%changelog
* Fri Dec 06 2019 Andrey Bychkov <mrdrew@altlinux.org> 1:0.2.9-alt3
- python2 disabled

* Wed May 16 2018 Andrey Bychkov <mrdrew@altlinux.org> 1:0.2.9-alt2.1.2
- (NMU) rebuild with python3.6

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1:0.2.9-alt2.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Wed Jan 27 2016 Mikhail Efremov <sem@altlinux.org> 1:0.2.9-alt2.1
- NMU: Use buildreq for BR.

* Mon Apr 15 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1:0.2.9-alt2
- Use 'find... -exec...' instead of 'for ... $(find...'

* Fri Mar 22 2013 Aleksey Avdeev <solo@altlinux.ru> 1:0.2.9-alt1.1
- Rebuild with Python-3.3

* Tue May 08 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1:0.2.9-alt1
- Version 0.2.9
- Added module for Python 3

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.2b2-alt1.1
- Rebuild with Python-2.7

* Tue Jul 05 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2b2-alt1
- Initial build for Sisyphus

