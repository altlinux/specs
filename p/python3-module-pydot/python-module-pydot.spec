%define oname pydot

Name: python3-module-%oname
Version: 1.4.2
Release: alt1

Summary: Python interface to Graphiz's Dot

License: MIT
Group: Development/Python3
Url: https://pypi.org/project/pydot

Source: %oname-%version.tar.bz2

BuildArch: noarch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-pyparsing

Requires: %_bindir/dot

%description
An interface for creating both directed and non directed graphs from
Python. Currently all attributes implemented in the Dot language are
supported (up to Graphviz 1.16).

Output can be inlined in Postscript into interactive scientific
environments like TeXmacs, or output in any of the format's supported
by the Graphviz tools dot, neato, twopi.

%prep
%setup -n %oname-%version

%build
%python3_build

%install
%python3_install

%files
%doc ChangeLog
%python3_sitelibdir/*

%changelog
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
