%define _name Cython
%def_disable debugger

%def_with python3

Name: python-module-%_name
Version: 0.25.2
Release: alt1

Summary: C-extensions for Python
Group: Development/Python
License: Python
Url: http://www.cython.org

Source: http://cython.org/release/Cython-%version.tar.gz

Provides: %_name = %version-%release
Conflicts: python-module-Cython0.18

%if_with  python3
%add_python3_req_skip IPython
%endif

%add_python_req_skip IPython

BuildRequires: rpm-build-python
BuildRequires: python-devel python-module-setuptools python-module-json

%description
Cython is a language that makes writing C extensions for the Python
language as easy as Python itself. Cython is based on the well-known
Pyrex, but supports more cutting edge functionality and optimizations.

The Cython language is very close to the Python language, but Cython
additionally supports calling C functions and declaring C types on
variables and class attributes. This allows the compiler to generate
very efficient C code from Cython code.

This makes Cython the ideal language for wrapping for external C
libraries, and for fast C modules that speed up the execution of Python
code.

%package tests
Summary: Cython test suit
Group: Development/Python
Requires: %name = %version-%release
Conflicts: python-module-Cython0.18-tests

%description tests
Cython is a language that makes writing C extensions for the Python
language as easy as Python itself. Cython is based on the well-known
Pyrex, but supports more cutting edge functionality and optimizations.

The Cython language is very close to the Python3 language, but Cython
additionally supports calling C functions and declaring C types on
variables and class attributes. This allows the compiler to generate
very efficient C code from Cython code.

This makes Cython the ideal language for wrapping for external C
libraries, and for fast C modules that speed up the execution of Python
code.

This package provides modules for testing Cython using unittest.

%package debugger
Summary: Cython debugger
Group: Development/Python
Requires: %name = %version-%release
Requires: gdb

%description debugger
Cython is a language that makes writing C extensions for the Python
language as easy as Python itself. Cython is based on the well-known
Pyrex, but supports more cutting edge functionality and optimizations.

The Cython language is very close to the Python3 language, but Cython
additionally supports calling C functions and declaring C types on
variables and class attributes. This allows the compiler to generate
very efficient C code from Cython code.

This makes Cython the ideal language for wrapping for external C
libraries, and for fast C modules that speed up the execution of Python
code.

This package provides modules for debugging Cython programms.

%if_with python3
%package -n python3-module-%_name
Summary: C-extensions for Python3
Group: Development/Python3
# since 0.20.1
%py3_provides cython
Conflicts: python3-module-Cython0.18
BuildRequires: rpm-build-python3
BuildRequires: python3-devel python3-module-distribute

%description -n python3-module-%_name
Cython is a language that makes writing C extensions for the Python3
language as easy as Python3 itself. Cython is based on the well-known
Pyrex, but supports more cutting edge functionality and optimizations.

The Cython language is very close to the Python3 language, but Cython
additionally supports calling C functions and declaring C types on
variables and class attributes. This allows the compiler to generate
very efficient C code from Cython code.

This makes Cython the ideal language for wrapping for external C
libraries, and for fast C modules that speed up the execution of Python3
code.

%package -n python3-module-%_name-tests
Summary: Cython test suit for Python3
Group: Development/Python3
Conflicts: python3-module-Cython0.18-tests
Requires: python3-module-%_name = %version-%release

%description -n python3-module-%_name-tests
Cython is a language that makes writing C extensions for the Python3
language as easy as Python3 itself. Cython is based on the well-known
Pyrex, but supports more cutting edge functionality and optimizations.

The Cython language is very close to the Python3 language, but Cython
additionally supports calling C functions and declaring C types on
variables and class attributes. This allows the compiler to generate
very efficient C code from Cython code.

This makes Cython the ideal language for wrapping for external C
libraries, and for fast C modules that speed up the execution of Python3
code.

This package provides modules for testing Cython using unittest.

%package -n python3-module-%_name-debugger
Summary: Cython debugger for Python3
Group: Development/Python3
Requires: python3-module-%_name = %version-%release
Requires: gdb

%description -n python3-module-%_name-debugger
Cython is a language that makes writing C extensions for the Python3
language as easy as Python3 itself. Cython is based on the well-known
Pyrex, but supports more cutting edge functionality and optimizations.

The Cython language is very close to the Python3 language, but Cython
additionally supports calling C functions and declaring C types on
variables and class attributes. This allows the compiler to generate
very efficient C code from Cython code.

This makes Cython the ideal language for wrapping for external C
libraries, and for fast C modules that speed up the execution of Python3
code.

This package provides modules for debugging Cython programms.
%endif

%prep
%setup -n %_name-%version
%if_with python3
rm -rf ../python3
cp -a . ../python3
%endif

%build
%python_build
%if_with python3
pushd ../python3
%python3_build
popd
%endif

%install
%if_with python3
pushd ../python3
%python3_install
popd
mv %buildroot/%_bindir/cython %buildroot/%_bindir/cython3
mv %buildroot/%_bindir/cygdb %buildroot/%_bindir/cygdb3
%endif

%python_install

%files
%_bindir/cython
%_bindir/cythonize
%python_sitelibdir/pyximport/
%python_sitelibdir/%_name/
%python_sitelibdir/%_name-*egg-info
%python_sitelibdir/cython.py*
%doc *.txt Demos Doc Tools

%exclude %python_sitelibdir/%_name/Tests
%exclude %python_sitelibdir/%_name/Debugger

%files tests
%python_sitelibdir/%_name/Tests

%if_enabled debugger
%files debugger
%python_sitelibdir/%_name/Debugger
%_bindir/cygdb
%endif

%if_with python3
%files -n python3-module-%_name
%_bindir/cython3
%python3_sitelibdir/%_name/
%python3_sitelibdir/pyximport/
%python3_sitelibdir/cython.py
%python3_sitelibdir/__pycache__/cython.*
%python3_sitelibdir/*egg-info

%exclude %python3_sitelibdir/%_name/Tests
%exclude %python3_sitelibdir/%_name/Debugger

%files -n python3-module-%_name-tests
%python3_sitelibdir/%_name/Tests

%if_enabled debugger
%files -n python3-module-%_name-debugger
%python3_sitelibdir/%_name/Debugger
%_bindir/cygdb3
%endif
%endif

%changelog
* Sun Dec 11 2016 Yuri N. Sedunov <aris@altlinux.org> 0.25.2-alt1
- 0.25.2

* Thu Oct 27 2016 Yuri N. Sedunov <aris@altlinux.org> 0.25.1-alt1
- 0.25.1

* Sun Jul 17 2016 Yuri N. Sedunov <aris@altlinux.org> 0.24.1-alt1
- 0.24.1

* Fri Apr 08 2016 Yuri N. Sedunov <aris@altlinux.org> 0.24-alt1
- 0.24

* Fri Apr 08 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.23.4-alt3.1.1
- (NMU) Rebuild with python3-3.5.1-alt3 to get rid of the meaningless __pycache__/ dep
  (it is meaningless because arbitrary packages package that dir).

* Thu Mar 24 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.23.4-alt3.1
- (NMU) rebuild with python3-3.5 & rpm-build-python3-0.1.10
  (for ABI dependence and new python3(*) reqs)

* Thu Mar 24 2016 Denis Medvedev <nbr@altlinux.org> 0.23.4-alt3
- NMU - rebuild from srpm.

* Wed Mar 23 2016 Denis Medvedev <nbr@altlinux.org> 0.23.4-alt2
- NMU - making IPython not a requirement for Cython.

* Thu Nov 05 2015 Yuri N. Sedunov <aris@altlinux.org> 0.23.4-alt1
- 0.23.4

* Sat Aug 15 2015 Yuri N. Sedunov <aris@altlinux.org> 0.23-alt1
- 0.23

* Sun Feb 22 2015 Yuri N. Sedunov <aris@altlinux.org> 0.22-alt1
- 0.22

* Wed Oct 15 2014 Yuri N. Sedunov <aris@altlinux.org> 0.21-alt1
- 0.21

* Fri Feb 14 2014 Yuri N. Sedunov <aris@altlinux.org> 0.20.1-alt1
- 0.20.1 (ALT #28632)
- new *-tests subpackages
- prepared *-debugger subpackages

* Sun Mar 17 2013 Aleksey Avdeev <solo@altlinux.ru> 0.16-alt1.1
- Rebuild with Python-3.3

* Thu May 10 2012 Vitaly Kuznetsov <vitty@altlinux.ru> 0.16-alt1
- 0.16 (ALT #27317)

* Thu Apr 12 2012 Vitaly Kuznetsov <vitty@altlinux.ru> 0.15.1-alt2.1
- Rebuild to remove redundant libpython2.7 dependency

* Thu Feb 09 2012 Vitaly Kuznetsov <vitty@altlinux.ru> 0.15.1-alt2
- Build with Python3 (ALT #26914)

* Mon Dec 12 2011 Yuri N. Sedunov <aris@altlinux.org> 0.15.1-alt1
- 0.15.1

* Mon Oct 24 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.15-alt1.1
- Rebuild with Python-2.7

* Fri Aug 19 2011 Yuri N. Sedunov <aris@altlinux.org> 0.15-alt1
- 0.15

* Sat Mar 26 2011 Yuri N. Sedunov <aris@altlinux.org> 0.14.1-alt1
- 0.14.1 (ALT #25284)

* Tue Nov 16 2010 Yuri N. Sedunov <aris@altlinux.org> 0.13-alt1
- 0.13 (ALT #24574)

* Thu Mar 04 2010 Yuri N. Sedunov <aris@altlinux.org> 0.12.1-alt1
- updated to 0.12.1 (ALT #23072)

* Fri Nov 06 2009 Yuri N. Sedunov <aris@altlinux.org> 0.11.3-alt1
- 0.11.3 (ALT #22193)

* Fri Oct 17 2008 Yuri N. Sedunov <aris@altlinux.org> 0.9.8.1.1-alt1
- first build for Sisyphus
- TODO: -doc, -tools, -demos subpackages
