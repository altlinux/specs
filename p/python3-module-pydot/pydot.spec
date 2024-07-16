%define oname pydot

%def_without check

Name: python3-module-%oname
Version: 3.0.0
Release: alt1

Summary: Python interface to Graphiz's Dot

License: MIT
Group: Development/Python3
URL: https://pypi.org/project/pydot
VCS: https://github.com/pydot/pydot

Source: %name-%version.tar

BuildArch: noarch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-wheel

%if_with check
BuildRequires: python3-module-parameterized
BuildRequires: python3-module-pyparsing
BuildRequires: python3-module-chardet
BuildRequires: graphviz
%endif

Requires: %_bindir/dot

%description
An interface for creating both directed and non directed graphs from
Python. Currently all attributes implemented in the Dot language are
supported (up to Graphviz 1.16).

Output can be inlined in Postscript into interactive scientific
environments like TeXmacs, or output in any of the format's supported
by the Graphviz tools dot, neato, twopi.

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

%check
export PYTHONPATH=%buildroot%python3_sitelibdir
python3 test/test_pydot.py

%files
%doc ChangeLog
%python3_sitelibdir/%oname
%python3_sitelibdir/%oname-%version.dist-info

%changelog
* Tue Jul 16 2024 Grigory Ustinov <grenka@altlinux.org> 3.0.0-alt1
- Automatically updated to 3.0.0.

* Sun Jun 02 2024 Grigory Ustinov <grenka@altlinux.org> 2.0.0-alt1
- Automatically updated to 2.0.0.

* Fri Jul 09 2021 Grigory Ustinov <grenka@altlinux.org> 1.4.2-alt1
- Build new version.
- Drop python2 support.

* Wed Dec 26 2018 Grigory Ustinov <grenka@altlinux.org> 1.4.1-alt1
- Build new version.

* Wed May 16 2018 Andrey Bychkov <mrdrew@altlinux.org> 1.0.29-alt1.git20140730.1.2
- (NMU) rebuild with python3.6

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.0.29-alt1.git20140730.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 1.0.29-alt1.git20140730.1
- NMU: Use buildreq for BR.

* Mon Feb 09 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.29-alt1.git20140730
- Version 1.0.29

* Thu May 10 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.28-alt1
- Version 1.0.28

* Wed Oct 26 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.0.2-alt1.1.1
- Rebuild with Python-2.7

* Tue Nov 17 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.2-alt1.1
- Rebuilt with python 2.6

* Thu Jun 19 2008 Vitaly Lipatov <lav@altlinux.ru> 1.0.2-alt1
- new version 1.0.2 (with rpmrb script)

* Sun Sep 16 2007 Vitaly Lipatov <lav@altlinux.ru> 0.9.10-alt1
- initial build for ALT Linux Sisyphus
