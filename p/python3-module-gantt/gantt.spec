%define oname gantt

Name: python3-module-%oname
Version: 0.6.0
Release: alt3

Summary: This is a python class to create gantt chart using SVG

License: GPLv3+
Group: Development/Python3
Url: https://pypi.python.org/pypi/python-gantt/

BuildArch: noarch

Source: %name-%version.tar
Patch1: %oname-%version-alt.patch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-svgwrite python3-module-clize
BuildRequires: python3-module-nose python3(dateutil)
BuildRequires: python-tools-2to3

%py3_provides %oname org2gantt
%py3_requires svgwrite clize

Conflicts: python-module-%oname
Obsoletes: python-module-%oname

%description
Python-Gantt make possible to easily draw gantt charts from Python.
Output format is SVG.

%package tests
Summary: Tests for %oname
Group: Development/Python3
Requires: %name = %EVR

%description tests
Python-Gantt make possible to easily draw gantt charts from Python.
Output format is SVG.

This package contains tests for %oname.

%prep
%setup
%patch1 -p1

# hack to fix new clize bug: ValueError: Parameters --start-date and --svg use a duplicate alias '-s'
subst "s|'S'|'b'|" org2gantt/org2gantt.py

touch org2gantt/__init__.py

find %oname -type f -name '*.py' -exec 2to3 -w -n '{}' +

%build
%python3_build

%install
install -d %buildroot%_bindir
%python3_install
cp -fR org2gantt %buildroot%python3_sitelibdir/
ln -s %python3_sitelibdir/org2gantt/org2gantt.py \
	%buildroot%_bindir/org2gantt

%make doc

%check
export PYTHONPATH=$PWD
python3 setup.py build_ext -i
%make test PYTHON=python3 NOSETESTS=nosetests3

%files
%doc CHANGELOG *.txt org2gantt/*.org
%_bindir/org2gantt
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/test*
%exclude %python3_sitelibdir/*/*/test*
%exclude %python3_sitelibdir/*/example.org

%files tests
%python3_sitelibdir/*/test*
%python3_sitelibdir/*/*/test*
%python3_sitelibdir/*/example.org

%changelog
* Fri Jul 23 2021 Grigory Ustinov <grenka@altlinux.org> 0.6.0-alt3
- Drop python2 support.

* Sat Jun 01 2019 Vitaly Lipatov <lav@altlinux.ru> 0.6.0-alt2
- NMU: disable python2 module

* Mon Mar 05 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 0.6.0-alt1
- Updated to upstream version 0.6.0.

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.3.10-alt1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Wed Feb 25 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3.10-alt1
- Version 0.3.10

* Tue Jan 27 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3.8-alt1
- Version 0.3.8

* Wed Jan 14 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3.7-alt1
- Initial build for Sisyphus

