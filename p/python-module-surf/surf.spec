%define oname surf

%def_with python3
%def_disable check

Name: python-module-%oname
Version: 1.1.6
Release: alt2.git20140617.1.1
Summary: Python library for working with RDF data in an Object-Oriented way
License: BSD
Group: Development/Python
Url: https://github.com/cosminbasca/surfrdf
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/cosminbasca/surfrdf.git
Source: %name-%version.tar
BuildArch: noarch

#BuildPreReq: python-devel python-module-setuptools-tests
#BuildPreReq: python-module-rdflib python-module-simplejson
#BuildPreReq: python-module-rdfextras python-module-pyparsing
#BuildPreReq: python-module-SPARQLWrapper
#BuildPreReq: python-module-sphinx-devel
%if_with python3
BuildRequires(pre): rpm-build-python3
#BuildPreReq: python3-devel python3-module-setuptools-tests
#BuildPreReq: python3-module-rdflib python3-module-simplejson
#BuildPreReq: python3-module-rdfextras python3-module-pyparsing
#BuildPreReq: python3-module-SPARQLWrapper
%endif

%py_provides %oname

BuildRequires(pre): rpm-macros-sphinx
# Automatically added by buildreq on Thu Jan 28 2016 (-bi)
# optimized out: python-base python-devel python-module-PyStemmer python-module-Pygments python-module-babel python-module-cssselect python-module-genshi python-module-isodate python-module-jinja2 python-module-jinja2-tests python-module-markupsafe python-module-pyparsing python-module-pytz python-module-rdflib python-module-setuptools python-module-six python-module-snowballstemmer python-module-sphinx python-module-sphinx_rtd_theme python-modules python-modules-compiler python-modules-ctypes python-modules-email python-modules-encodings python-modules-json python-modules-logging python-modules-multiprocessing python-modules-unittest python-modules-xml python-tools-2to3 python3 python3-base python3-module-pyparsing python3-module-rdflib python3-module-setuptools
BuildRequires: python-module-alabaster python-module-docutils python-module-html5lib python-module-objects.inv python-module-pytest python-module-rdfextras python-module-rdflib_jsonld python3-module-pytest python3-module-rdfextras python3-module-rdflib_jsonld rpm-build-python3 time

%description
SuRF is a Python library for working with RDF data in an Object-Oriented
way. In SuRF, RDF nodes (subjects and objects) are represented as Python
objects and RDF arcs (predicates) as their attributes. SuRF is an Object
RDF Mapper (ORM), similar in concept to Object Relational Mappers like
SQLAlchemy. SuRF was inspired by ActiveRDF for Ruby.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR
Requires: %name-plugins = %EVR

%description tests
SuRF is a Python library for working with RDF data in an Object-Oriented
way. In SuRF, RDF nodes (subjects and objects) are represented as Python
objects and RDF arcs (predicates) as their attributes. SuRF is an Object
RDF Mapper (ORM), similar in concept to Object Relational Mappers like
SQLAlchemy. SuRF was inspired by ActiveRDF for Ruby.

This package contains tests for %oname.

%package plugins
Summary: Plugins for %oname
Group: Development/Python
Requires: %name = %EVR
%py_requires rdfextras

%description plugins
SuRF is a Python library for working with RDF data in an Object-Oriented
way. In SuRF, RDF nodes (subjects and objects) are represented as Python
objects and RDF arcs (predicates) as their attributes. SuRF is an Object
RDF Mapper (ORM), similar in concept to Object Relational Mappers like
SQLAlchemy. SuRF was inspired by ActiveRDF for Ruby.

This package contains plugins for %oname.

%package pickles
Summary: Pickles for %oname
Group: Development/Python

%description pickles
SuRF is a Python library for working with RDF data in an Object-Oriented
way. In SuRF, RDF nodes (subjects and objects) are represented as Python
objects and RDF arcs (predicates) as their attributes. SuRF is an Object
RDF Mapper (ORM), similar in concept to Object Relational Mappers like
SQLAlchemy. SuRF was inspired by ActiveRDF for Ruby.

This package contains pickles for %oname.

%package docs
Summary: Documentation for %oname
Group: Development/Documentation
BuildArch: noarch

%description docs
SuRF is a Python library for working with RDF data in an Object-Oriented
way. In SuRF, RDF nodes (subjects and objects) are represented as Python
objects and RDF arcs (predicates) as their attributes. SuRF is an Object
RDF Mapper (ORM), similar in concept to Object Relational Mappers like
SQLAlchemy. SuRF was inspired by ActiveRDF for Ruby.

This package contains documentation for %oname.

%package -n python3-module-%oname
Summary: Python library for working with RDF data in an Object-Oriented way
Group: Development/Python3
%py3_provides %oname

%description -n python3-module-%oname
SuRF is a Python library for working with RDF data in an Object-Oriented
way. In SuRF, RDF nodes (subjects and objects) are represented as Python
objects and RDF arcs (predicates) as their attributes. SuRF is an Object
RDF Mapper (ORM), similar in concept to Object Relational Mappers like
SQLAlchemy. SuRF was inspired by ActiveRDF for Ruby.

%package -n python3-module-%oname-plugins
Summary: Plugins for %oname
Group: Development/Python3
Requires: python3-module-%oname = %EVR
%py3_requires rdfextras

%description -n python3-module-%oname-plugins
SuRF is a Python library for working with RDF data in an Object-Oriented
way. In SuRF, RDF nodes (subjects and objects) are represented as Python
objects and RDF arcs (predicates) as their attributes. SuRF is an Object
RDF Mapper (ORM), similar in concept to Object Relational Mappers like
SQLAlchemy. SuRF was inspired by ActiveRDF for Ruby.

This package contains plugins for %oname.

%package -n python3-module-%oname-tests
Summary: Tests for %oname
Group: Development/Python3
Requires: python3-module-%oname = %EVR
Requires: python3-module-%oname-plugins = %EVR

%description -n python3-module-%oname-tests
SuRF is a Python library for working with RDF data in an Object-Oriented
way. In SuRF, RDF nodes (subjects and objects) are represented as Python
objects and RDF arcs (predicates) as their attributes. SuRF is an Object
RDF Mapper (ORM), similar in concept to Object Relational Mappers like
SQLAlchemy. SuRF was inspired by ActiveRDF for Ruby.

This package contains tests for %oname.

%prep
%setup

ln -s README.md README.txt

%if_with python3
cp -fR . ../python3
find ../python3 -type f -name '*.py' -exec 2to3 -w -n '{}' +
%endif

%prepare_sphinx docs
ln -s ../objects.inv docs/source/

%build
%python_build_debug
#for i in allegro_franz rdflib sesame2 sparql_protocol; do
for i in rdflib sesame2 sparql_protocol; do
	pushd plugins/%oname.$i
	%python_build_debug
	popd
done

%if_with python3
pushd ../python3
%python3_build_debug
#for i in allegro_franz rdflib sesame2 sparql_protocol; do
for i in rdflib sesame2 sparql_protocol; do
	pushd plugins/%oname.$i
	%python3_build_debug
	popd
done
popd
%endif

%install
%python_install
for i in plugin query resource test; do
	cp -fR %oname/$i \
		%buildroot%python_sitelibdir/%oname/
done
#for i in allegro_franz rdflib sesame2 sparql_protocol; do
for i in rdflib sesame2 sparql_protocol; do
	pushd plugins/%oname.$i
	%python_install
	popd
done

%if_with python3
pushd ../python3
%python3_install
for i in plugin query resource test; do
	cp -fR %oname/$i \
		%buildroot%python3_sitelibdir/%oname/
done
#for i in allegro_franz rdflib sesame2 sparql_protocol; do
for i in rdflib sesame2 sparql_protocol; do
	pushd plugins/%oname.$i
	%python3_install
	popd
done
popd
%endif

export PYTHONPATH=%buildroot%python_sitelibdir
%make -C docs pickle
%make -C docs html

cp -fR docs/build/pickle %buildroot%python_sitelibdir/%oname/

%check
export PYTHONPATH=%buildroot%python_sitelibdir
python setup.py test
#for i in allegro_franz rdflib sesame2 sparql_protocol; do
for i in rdflib sesame2 sparql_protocol; do
	pushd plugins/%oname.$i
	python setup.py test
	popd
done
%if_with python3
pushd ../python3
python3 setup.py test
#for i in allegro_franz rdflib sesame2 sparql_protocol; do
for i in rdflib sesame2 sparql_protocol; do
	pushd plugins/%oname.$i
	python3 setup.py test
	popd
done
popd
%endif

%files
%doc *.txt *.md examples
%python_sitelibdir/surf
%python_sitelibdir/SuRF-*.egg-info
%exclude %python_sitelibdir/surf/test
%exclude %python_sitelibdir/surf/pickle

%files pickles
%python_sitelibdir/surf/pickle

%files docs
%doc docs/build/html/*

%files plugins
%python_sitelibdir/*
%exclude %python_sitelibdir/surf
%exclude %python_sitelibdir/SuRF-*.egg-info

%files tests
%python_sitelibdir/surf/test

%if_with python3
%files -n python3-module-%oname
%doc *.txt *.md examples
%python3_sitelibdir/surf
%python3_sitelibdir/SuRF-*.egg-info
%exclude %python3_sitelibdir/surf/test

%files -n python3-module-%oname-tests
%python3_sitelibdir/surf/test

%files -n python3-module-%oname-plugins
%python3_sitelibdir/*
%exclude %python3_sitelibdir/surf
%exclude %python3_sitelibdir/SuRF-*.egg-info
%endif

%changelog
* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.1.6-alt2.git20140617.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 1.1.6-alt2.git20140617.1
- NMU: Use buildreq for BR.

* Wed Dec 17 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1.6-alt2.git20140617
- Added requirement on rdfextras for plugins

* Tue Dec 16 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1.6-alt1.git20140617
- Initial build for Sisyphus

