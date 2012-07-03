%define version 1.1.1
%define release alt1.2
%setup_python_module Extremes

Name: %packagename
Version:%version
Release: %release.1

Summary: Production-quality 'Min' and 'Max' objects

License: PSF or ZPL
Group: Development/Python
BuildArch: noarch
Url:  http://pypi.python.org/pypi/Extremes
Packager: Denis Klimov <zver@altlinux.org>

Source: %modulename-%version.tar

BuildPreReq: python-module-distribute

%description
The ``peak.util.extremes`` module provides a production-quality implementation
of the ``Min`` and ``Max`` objects from PEP 326.  While PEP 326 was rejected
for inclusion in the language or standard library, the objects described in it
are useful in a variety of applications.  In PEAK, they have been used to
implement generic functions (in RuleDispatch and PEAK-Rules), as well as to
handle scheduling and time operations in the Trellis.  Because this has led to
each project copying the same code, we've now split the module out so it can
be used independently.

%prep
%setup -n %modulename-%version

%build
%python_build

%install
%python_install

%files
%python_sitelibdir/peak/util/extremes*
%python_sitelibdir/Extremes*
%changelog
* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.1.1-alt1.2.1
- Rebuild with Python-2.7

* Mon Jul 04 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1.1-alt1.2
- Fixed build

* Thu Nov 19 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1.1-alt1.1
- Rebuilt with python 2.6

* Sun Apr 05 2009 Denis Klimov <zver@altlinux.org> 1.1.1-alt1
- Initial build for ALT Linux

