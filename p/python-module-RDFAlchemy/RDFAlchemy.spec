%define oname RDFAlchemy

%def_with python3

Name: python-module-%oname
Version: 0.2.9
Release: alt2.1
Epoch: 1
Summary: rdflib wrapper for Python
License: BSD
Group: Development/Python
Url: http://pypi.python.org/pypi/RDFAlchemy/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar
BuildArch: noarch

#BuildPreReq: python-devel python-module-distribute
%if_with python3
BuildRequires(pre): rpm-build-python3
# Automatically added by buildreq on Wed Jan 27 2016 (-bi)
# optimized out: python-base python-devel python-modules python-modules-compiler python-modules-ctypes python-modules-email python-modules-encodings python-modules-logging python-modules-unittest python-tools-2to3 python3 python3-base
BuildRequires: python-module-setuptools python3-module-setuptools rpm-build-python3 time

#BuildRequires: python3-devel python3-module-distribute
#BuildPreReq: python-tools-2to3
%endif

%py_provides %oname

%description
RDFAlchemy is an abstraction layer, allowing python developers to use
familiar dot notation to access and update an rdf triplestore.

%if_with python3
%package -n python3-module-%oname
Summary: rdflib wrapper for Python 3
Group: Development/Python3
%py3_provides %oname
%py3_requires paste.script

%description -n python3-module-%oname
RDFAlchemy is an abstraction layer, allowing python developers to use
familiar dot notation to access and update an rdf triplestore.
%endif

%prep
%setup
sed -i 's|@VERSION@|%version|' rdfalchemy/__init__.py

for i in $(find . -name '.*'); do
	if [ "$i" != "." ]; then
		rm -fR $i
	fi
done

%if_with python3
rm -rf ../python3
cp -a . ../python3
%endif

%build
%python_build
%if_with python3
pushd ../python3
find -type f -name '*.py' -exec sed -i 's|%_bindir/env python|%_bindir/python3|' -- '{}' +
find -type f -name '*.py' -exec 2to3 -w '{}' +
for i in rdfalchemy/sparql/sesame2.py \
	rdfalchemy/sparql/parsers.py
do
	sed -i 's|import simplejson|import json as simplejson|' $i
done
%python3_build
popd
%endif

%install
%if_with python3
pushd ../python3
%python3_install
popd
mv %buildroot%_bindir/sparql %buildroot%_bindir/sparql3
%endif

%python_install

%files
%doc LICENSE README
%_bindir/sparql
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc LICENSE README
%_bindir/sparql3
%python3_sitelibdir/*
%endif

%changelog
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

