%define oname pyprof2calltree

Name: python3-module-%oname
Version: 1.4.5
Release: alt1

Summary: Help visualize profiling data from cProfile with kcachegrind

License: MIT
Group: Development/Python3
Url: http://pypi.python.org/pypi/pyprof2calltree

Source0: %name-%version.tar
BuildArch: noarch

BuildRequires(pre): rpm-build-python3

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
%setup

%build
%python3_build

%install
%python3_install

%files
%doc *.txt
%_bindir/%oname
%python3_sitelibdir/%oname.py
%python3_sitelibdir/__pycache__
%python3_sitelibdir/%oname-%version-py%_python3_version.egg-info

%changelog
* Thu May 18 2023 Grigory Ustinov <grenka@altlinux.org> 1.4.5-alt1
- Automatically updated to 1.4.5.

* Thu Jun 02 2022 Grigory Ustinov <grenka@altlinux.org> 1.4.4-alt1
- Build new version.

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

