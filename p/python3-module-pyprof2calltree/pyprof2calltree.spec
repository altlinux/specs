%define _unpackaged_files_terminate_build 1
%define oname pyprof2calltree

Name: python3-module-%oname
Version: 1.4.0
Release: alt2
Summary: Help visualize profiling data from cProfile with kcachegrind
License: BSD
Group: Development/Python3
Url: http://pypi.python.org/pypi/pyprof2calltree/

Source0: https://pypi.python.org/packages/ad/d9/2e3380728d3c8709574d81b749020fdc047073576cecba38fe14d6672ce3/%{oname}-%{version}.tar.gz
BuildArch: noarch

BuildRequires(pre): rpm-build-python3
BuildPreReq: python-tools-2to3

%py3_provides %oname

Conflicts: python-module-%oname
Obsoletes: python-module-%oname

%description
Script to help visualize profiling data collected with the cProfile
python module with the kcachegrind (screenshots) graphical calltree
analyser.

This is a rebranding of the venerable
http://www.gnome.org/~johan/lsprofcalltree.py script by David Allouche
et Al. It aims at making it easier to distribute (e.g. through pypi) and
behave more like the scripts of the debian kcachegrind-converters
package. The final goal is to make it part of the official upstream
kdesdk package.

%prep
%setup -n %{oname}-%{version}

find . -type f -name '*.py' -exec 2to3 -w -n '{}' +

%build
%python3_build

%install
%python3_install

%files
%doc *.txt
%_bindir/*
%python3_sitelibdir/*

%changelog
* Mon Jul 26 2021 Grigory Ustinov <grenka@altlinux.org> 1.4.0-alt2
- Drop python2 support.

* Wed Jan 11 2017 Igor Vlasenko <viy@altlinux.ru> 1.4.0-alt1
- automated PyPI update

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.3.2-alt2.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Wed Jul 30 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.3.2-alt2
- Added provides %oname for Python 3

* Tue Jul 15 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.3.2-alt1
- Version 1.3.2
- Added module for Python 3

* Fri Nov 29 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.3.1-alt1
- Version 1.3.1

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.1.0-alt1.1
- Rebuild with Python-2.7

* Thu Jun 30 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1.0-alt1
- Initial build for Sisyphus

