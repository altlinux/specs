%define version 1.6.4
%define release alt2
%setup_python_module PyQuante

Summary: PyQuante: Quantum Chemistry in Python
Name: %packagename
Version: %version
Release: %release
License: BSD
Group: Development/Python
URL: http://pyquante.sourceforge.net

Source: %modulename-%version.tar.gz

Requires: python-module-gnuplot
BuildRequires: python-devel python-module-distribute

# Automatically added by buildreq on Mon May 15 2006
BuildRequires: python-modules python-modules-compiler python-modules-encodings

%description
PyQuante is an open-source suite of programs for developing quantum
chemistry methods. The program is written in the Python programming
language, and has many 'rate-determining' modules also written in C
for speed. The resulting code is not nearly as fast as Jaguar,
Gaussian, or GAMESS, but the resulting code is much easier to
understand and modify. The goal of this software is not necessarily to
provide a working quantum chemistry program (although it will
hopefully do that), but rather to provide a well-engineered set of
tools so that scientists can construct their own quantum chemistry
programs without going through the tedium of having to write every
low-level routine. More information, including links to the download
page, is available at http://pyquante.sourceforge.net.

%package tests
Summary: Tests for PyQuante
Group: Development/Python
Requires: %name = %version-%release

%description tests
PyQuante is an open-source suite of programs for developing quantum
chemistry methods. The program is written in the Python programming
language, and has many 'rate-determining' modules also written in C
for speed. The resulting code is not nearly as fast as Jaguar,
Gaussian, or GAMESS, but the resulting code is much easier to
understand and modify. The goal of this software is not necessarily to
provide a working quantum chemistry program (although it will
hopefully do that), but rather to provide a well-engineered set of
tools so that scientists can construct their own quantum chemistry
programs without going through the tedium of having to write every
low-level routine. More information, including links to the download
page, is available at http://pyquante.sourceforge.net.

This package contains tests for PyQuante.

%prep
%setup -n %modulename-%version

%build
%python_build_debug

%install
%python_install --optimize=2

%files
%doc Doc LICENSE README Tests
%python_sitelibdir/PyQuante
%python_sitelibdir/PyQuante-%version-py*.egg-info
%exclude %python_sitelibdir/PyQuante/test_*

%files tests
%python_sitelibdir/PyQuante/test_*

%changelog
* Thu Nov 30 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 1.6.4-alt2
- Fixed build.

* Fri Jan 27 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.6.4-alt1
- Version 1.6.4

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.6.3-alt2.1
- Rebuild with Python-2.7

* Sat Mar 26 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.6.3-alt2
- Rebuilt for debuginfo

* Tue Nov 23 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.6.3-alt1
- Version 1.6.3

* Fri Jan 08 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.5.0-alt3
- Rebuilt without python-module-Numeric

* Fri Nov 20 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.5.0-alt2.2
- Rebuilt with python 2.6

* Tue Nov 10 2009 Repocop Q. A. Robot <repocop@altlinux.org> 1.5.0-alt2.1.qa1
- NMU (by repocop): the following fixes applied:
  * vendor-tag for python-module-PyQuante
  * postclean-05-filetriggers for spec file

* Tue Jan 29 2008 Grigory Batalov <bga@altlinux.ru> 1.5.0-alt2.1
- Rebuilt with python-2.5.

* Tue Jan 22 2008 Grigory Batalov <bga@altlinux.ru> 1.5.0-alt2
- Remove python version from BuildPreReq.

* Mon May 15 2006 Andrey Khavryuchenko <akhavr@altlinux.ru> 1.5.0-alt1
  Initial build
