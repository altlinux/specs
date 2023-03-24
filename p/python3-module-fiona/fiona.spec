%define oname fiona

# check relies on a lot of network
%def_without check

Name: python3-module-%oname
Version: 1.9.2
Release: alt1

Summary: Fiona reads and writes spatial data files

License: BSD-3-Clause
Group: Development/Python3
Url: https://pypi.python.org/pypi/Fiona/

# https://github.com/Toblerity/Fiona.git
Source: %name-%version.tar

Patch: use_sphinx-apidoc-3.patch

BuildRequires(pre): rpm-build-python3
BuildRequires(pre): rpm-macros-sphinx3
BuildRequires: libgdal-devel gcc-c++
BuildRequires: python3-module-Cython
BuildRequires: python3-module-sphinx
BuildRequires: python3-module-attrs
BuildRequires: python3-module-click
BuildRequires: python3-module-cligj
BuildRequires: python3-module-munch

Conflicts: fio
Conflicts: python-module-fiona < %EVR
Obsoletes: python-module-fiona < %EVR
%py3_provides %oname

%description
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
Group: Development/Python3

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
%patch -p1

%prepare_sphinx3 .
ln -s ../objects.inv docs/

%build
%add_optflags -fno-strict-aliasing
%python3_build

python3 setup.py build_ext -i
export PYTHONPATH=$PWD
%make SPHINXBUILD="sphinx-build-3" -C docs pickle
%make SPHINXBUILD="sphinx-build-3" -C docs html

%install
%python3_install

cp -fR docs/_build/pickle %buildroot%python3_sitelibdir/%oname/

%check

%files
%doc CHANGES.txt CREDITS.txt *.rst examples
%_bindir/fio
%python3_sitelibdir/%oname
%python3_sitelibdir/Fiona-%version-py%_python3_version.egg-info
%exclude %python3_sitelibdir/*/pickle

%files pickles
%dir %python3_sitelibdir/%oname
%python3_sitelibdir/*/pickle

%files docs
%doc docs/_build/html docs/*.txt

%changelog
* Thu Mar 23 2023 Grigory Ustinov <grenka@altlinux.org> 1.9.2-alt1
- Automatically updated to 1.9.2.

* Wed Feb 15 2023 Grigory Ustinov <grenka@altlinux.org> 1.9.1-alt1
- Automatically updated to 1.9.1.

* Tue Feb 07 2023 Grigory Ustinov <grenka@altlinux.org> 1.9.0-alt1
- Automatically updated to 1.9.0.

* Sun Oct 16 2022 Grigory Ustinov <grenka@altlinux.org> 1.8.22-alt1
- Automatically updated to 1.8.22.

* Thu Mar 24 2022 Grigory Ustinov <grenka@altlinux.org> 1.8.21-alt1
- Automatically updated to 1.8.21.

* Sat Jun 05 2021 Grigory Ustinov <grenka@altlinux.org> 1.8.20-alt1
- Automatically updated to 1.8.20.

* Thu May 13 2021 Grigory Ustinov <grenka@altlinux.org> 1.8.19-alt1
- Automatically updated to 1.8.19.

* Sun Nov 01 2020 Vitaly Lipatov <lav@altlinux.ru> 1.8.17-alt2
- fix build

* Wed Sep 16 2020 Grigory Ustinov <grenka@altlinux.org> 1.8.17-alt1
- Automatically updated to 1.8.17.

* Thu Mar 19 2020 Grigory Ustinov <grenka@altlinux.org> 1.8.13-alt1
- Build new version.
- Add conflict on python-module-fiona (Closes: #37383).

* Thu Oct 24 2019 Grigory Ustinov <grenka@altlinux.org> 1.8.9-alt1
- Build new version.

* Mon Sep 30 2019 Grigory Ustinov <grenka@altlinux.org> 1.8.8-alt1
- Build new version.

* Tue Mar 19 2019 Grigory Ustinov <grenka@altlinux.org> 1.8.6-alt1
- Build new version.

* Tue Jan 15 2019 Grigory Ustinov <grenka@altlinux.org> 1.8.4-alt1
- Build new version.

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

