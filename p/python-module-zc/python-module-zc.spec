%define oname zc
%define version 1.0.0
%define release alt6

%def_with python3

%setup_python_module %oname

Summary: The ``zc`` package is a pure namespace package
Name: %packagename
Version: %version
Release: %release
License: ZPL
Group: Development/Python
Packager: Python Development Team <python@packages.altlinux.org>

# need for links with some Zope modules
Requires: python-module-z3c
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel
%endif

### Don't set BuildArch to noarch - other zc packages arch-dependent.

%description
%summary

%if_with python3
%package -n python3-module-%oname
Summary: The ``zc`` package is a pure namespace package (Python 3)
Group: Development/Python3
Requires: python3-module-z3c

%description -n python3-module-%oname
%summary
%endif

%install
mkdir -p %buildroot/%python_sitelibdir/%modulename
cat <<EOF > %buildroot/%python_sitelibdir/%modulename/__init__.py
try:
    # Declare this a namespace package if pkg_resources is available.
    import pkg_resources
    pkg_resources.declare_namespace('zc')
except ImportError:
    pass
EOF

%if_with python3
install -d %buildroot/%python3_sitelibdir/%oname
install -m644 %buildroot/%python_sitelibdir/%modulename/__init__.py \
	%buildroot/%python3_sitelibdir/%oname/
%endif

%files
%dir %python_sitelibdir/%modulename
%python_sitelibdir/%modulename/__init__.py*

%if_with python3
%files -n python3-module-%oname
%dir %python3_sitelibdir/%oname
%python3_sitelibdir/%oname/__init__.py*
%dir %python3_sitelibdir/%oname/__pycache__
%python3_sitelibdir/%oname/__pycache__/__init__.*
%endif

%changelog
* Wed Apr 18 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.0-alt6
- Added requirement on python3-module-z3c

* Thu Apr 12 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.0-alt5
- Added module for Python 3 (bootstrap)

* Mon Oct 24 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.0.0-alt4.1
- Rebuild with Python-2.7

* Sat Jun 04 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.0-alt4
- Really added requirement on python-module-z3c

* Sat Jun 04 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.0-alt3
- Added requirement on python-module-z3c

* Mon Nov 23 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.0-alt2
- Rebuilt with python 2.6

* Tue Jan 29 2008 Grigory Batalov <bga@altlinux.ru> 1.0.0-alt1.1
- Rebuilt with python-2.5.

* Wed Feb 21 2007 Ivan Fedorov <ns@altlinux.ru> 1.0.0-alt1
- Initial build for ALT Linux.
