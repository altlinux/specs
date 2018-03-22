%define oname fiona

%def_with python3
%def_disable check

Name: python-module-%oname
Version: 1.7.9
Release: alt1.1
Summary: Fiona reads and writes spatial data files
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/Fiona/

# https://github.com/Toblerity/Fiona.git
Source: %name-%version.tar
Patch1: %oname-%version-alt-docs.patch

BuildRequires(pre): rpm-macros-sphinx
BuildRequires: libgdal-devel gcc-c++
BuildRequires: python-devel
BuildRequires: python-module-alabaster python-module-objects.inv
BuildRequires: python-module-Cython python-module-html5lib python-module-nose python-module-notebook python-module-pytest
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel
BuildRequires: python3-module-Cython python3-module-html5lib python3-module-nose python3-module-notebook python3-module-pytest
%endif

Conflicts: fio
%py_provides %oname
%py_requires logging json cligj six click click_plugins

%description
Fiona is OGR's neat, nimble, no-nonsense API for Python programmers.

Fiona is designed to be simple and dependable. It focuses on reading and
writing data in standard Python IO style and relies upon familiar Python
types and protocols such as files, dictionaries, mappings, and iterators
instead of classes specific to OGR. Fiona can read and write real-world
data using multi-layered GIS formats and zipped virtual file systems and
integrates readily with other Python GIS packages such as pyproj, Rtree,
and Shapely.

%package -n python3-module-%oname
Summary: Fiona reads and writes spatial data files
Group: Development/Python3
%py3_provides %oname
%py3_requires logging json cligj six click click_plugins

%description -n python3-module-%oname
Fiona is OGR's neat, nimble, no-nonsense API for Python programmers.

Fiona is designed to be simple and dependable. It focuses on reading and
writing data in standard Python IO style and relies upon familiar Python
types and protocols such as files, dictionaries, mappings, and iterators
instead of classes specific to OGR. Fiona can read and write real-world
data using multi-layered GIS formats and zipped virtual file systems and
integrates readily with other Python GIS packages such as pyproj, Rtree,
and Shapely.

%package pickles
Summary: Pickles for %oname
Group: Development/Python

%description pickles
Fiona is OGR's neat, nimble, no-nonsense API for Python programmers.

Fiona is designed to be simple and dependable. It focuses on reading and
writing data in standard Python IO style and relies upon familiar Python
types and protocols such as files, dictionaries, mappings, and iterators
instead of classes specific to OGR. Fiona can read and write real-world
data using multi-layered GIS formats and zipped virtual file systems and
integrates readily with other Python GIS packages such as pyproj, Rtree,
and Shapely.

This package contains pickles for %oname.

%package docs
Summary: Documentation for %oname
Group: Development/Documentation
BuildArch: noarch

%description docs
Fiona is OGR's neat, nimble, no-nonsense API for Python programmers.

Fiona is designed to be simple and dependable. It focuses on reading and
writing data in standard Python IO style and relies upon familiar Python
types and protocols such as files, dictionaries, mappings, and iterators
instead of classes specific to OGR. Fiona can read and write real-world
data using multi-layered GIS formats and zipped virtual file systems and
integrates readily with other Python GIS packages such as pyproj, Rtree,
and Shapely.

This package contains documentation for %oname.

%prep
%setup
%patch1 -p1

%if_with python3
cp -fR . ../python3
%endif

%prepare_sphinx .
ln -s ../objects.inv docs/

%build
%add_optflags -fno-strict-aliasing
%python_build_debug

%if_with python3
pushd ../python3
%python3_build_debug
popd
%endif

%install
%if_with python3
pushd ../python3
%python3_install
popd
pushd %buildroot%_bindir
for i in $(ls); do
	mv $i $i.py3
done
popd
%endif

%python_install

python setup.py build_ext -i
export PYTHONPATH=$PWD
%make -C docs pickle
%make -C docs html

cp -fR docs/_build/pickle %buildroot%python_sitelibdir/%oname/

%check
export LC_ALL=en_US.UTF-8
python setup.py test
%if_with python3
pushd ../python3
python3 setup.py test
popd
%endif

%files
%doc CHANGES.txt CREDITS.txt *.rst examples
%_bindir/*
%if_with python3
%exclude %_bindir/*.py3
%endif
%python_sitelibdir/*
%exclude %python_sitelibdir/*/pickle

%files pickles
%python_sitelibdir/*/pickle

%files docs
%doc docs/_build/html docs/*.txt

%if_with python3
%files -n python3-module-%oname
%doc CHANGES.txt CREDITS.txt *.rst examples
%_bindir/*.py3
%python3_sitelibdir/*
%endif

%changelog
* Thu Mar 22 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 1.7.9-alt1.1
- (NMU) Rebuilt with python-3.6.4.

* Fri Aug 18 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 1.7.9-alt1
- Updated to upstream version 1.7.9.

* Thu Mar 17 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.6.0-alt1.git20150810.1.1
- (NMU) rebuild with python3-3.5 & rpm-build-python3-0.1.10
  (for ABI dependence and new python3(*) reqs)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 1.6.0-alt1.git20150810.1
- NMU: Use buildreq for BR.

* Wed Aug 12 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.6.0-alt1.git20150810
- Version 1.6.0

* Mon Mar 02 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.5.0-alt1.git20150301
- New snapshot

* Thu Feb 19 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.5.0-alt1.git20150204
- Initial build for Sisyphus

