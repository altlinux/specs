%define modname Cython
%def_disable debugger

%def_with python2

Name: python-module-%modname
Version: 0.29.21
Release: alt1

Summary: C-extensions for Python
Group: Development/Python
License: Apache-2.0
Url: http://www.cython.org

#VCS: https://github.com/cython/cython.git
Source: https://pypi.io/packages/source/C/%modname/%modname-%version.tar.gz
#Source: https://github.com/cython/cython/archive/%version/%modname-%version.tar.gz

Provides: %modname = %EVR
Conflicts: python-module-Cython0.18

%add_python3_req_skip IPython IPython.core IPython.core.magic IPython.utils IPython.utils.text

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python3-module-distribute

%{?_with_python2:BuildRequires(pre): rpm-build-python
BuildRequires: python-devel python-module-setuptools python-module-json
%add_python_req_skip IPython}

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
Requires: %name = %EVR
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
Requires: %name = %EVR
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

%package -n python3-module-%modname
Summary: C-extensions for Python3
Group: Development/Python3
# since 0.20.1
%py3_provides cython
Conflicts: python3-module-Cython0.18

%description -n python3-module-%modname
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

%package -n python3-module-%modname-tests
Summary: Cython test suit for Python3
Group: Development/Python3
Conflicts: python3-module-Cython0.18-tests
Requires: python3-module-%modname = %EVR

%description -n python3-module-%modname-tests
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

%package -n python3-module-%modname-debugger
Summary: Cython debugger for Python3
Group: Development/Python3
Requires: python3-module-%modname = %EVR
Requires: gdb

%description -n python3-module-%modname-debugger
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

%prep
%setup -n %modname-%version
%if_with python2
rm -rf ../python2
cp -a . ../python2
%endif

%build
%python3_build
%if_with python2
pushd ../python2
%python_build
popd
%endif

%install
%if_with python2
pushd ../python2
%python_install
popd
for f in cy{thon{,ize},gdb}; do
mv %buildroot/%_bindir/$f %buildroot/%_bindir/"$f"2;
done
%endif

%python3_install
for f in cy{thon{,ize},gdb}; do
ln -s $f %buildroot/%_bindir/"$f"3;
done

%files
%if_with python2
%_bindir/cython2
%_bindir/cythonize2
%python_sitelibdir/pyximport/
%python_sitelibdir/%modname/
%python_sitelibdir/%modname-*egg-info
%python_sitelibdir/cython.py*
%doc *.txt Demos Tools docs

%exclude %python_sitelibdir/%modname/Tests
%exclude %python_sitelibdir/%modname/Debugger

%files tests
%python_sitelibdir/%modname/Tests

%if_enabled debugger
%files debugger
%python_sitelibdir/%modname/Debugger
%_bindir/cygdb2
%endif
%endif

%files -n python3-module-%modname
%_bindir/cython
%_bindir/cythonize
%_bindir/cython3
%_bindir/cythonize3
%python3_sitelibdir/%modname/
%python3_sitelibdir/pyximport/
%python3_sitelibdir/cython.py
%python3_sitelibdir/__pycache__/cython.*
%python3_sitelibdir/*egg-info

%exclude %python3_sitelibdir/%modname/Tests
%exclude %python3_sitelibdir/%modname/Debugger

%files -n python3-module-%modname-tests
%python3_sitelibdir/%modname/Tests

%if_enabled debugger
%files -n python3-module-%modname-debugger
%python3_sitelibdir/%modname/Debugger
%_bindir/cygdb
%_bindir/cygdb3
%endif

%changelog
* Thu Jul 09 2020 Yuri N. Sedunov <aris@altlinux.org> 0.29.21-alt1
- 0.29.21

* Wed Jun 10 2020 Yuri N. Sedunov <aris@altlinux.org> 0.29.20-alt1
- 0.29.20

* Fri May 29 2020 Yuri N. Sedunov <aris@altlinux.org> 0.29.19-alt1
- 0.29.19

* Mon Apr 27 2020 Yuri N. Sedunov <aris@altlinux.org> 0.29.17-alt1
- 0.29.17

* Tue Mar 24 2020 Yuri N. Sedunov <aris@altlinux.org> 0.29.16-alt1
- 0.29.16

* Thu Feb 06 2020 Yuri N. Sedunov <aris@altlinux.org> 0.29.15-alt1
- 0.29.15
- fixed License tag

* Sat Nov 02 2019 Yuri N. Sedunov <aris@altlinux.org> 0.29.14-alt1
- 0.29.14
- made python2 build optional

* Fri Aug 02 2019 Yuri N. Sedunov <aris@altlinux.org> 0.29.13-alt1
- 0.29.13

* Sun Jul 07 2019 Yuri N. Sedunov <aris@altlinux.org> 0.29.12-alt1
- 0.29.12

* Sun Jun 30 2019 Yuri N. Sedunov <aris@altlinux.org> 0.29.11-alt1
- 0.29.11

* Sun Jun 02 2019 Yuri N. Sedunov <aris@altlinux.org> 0.29.10-alt1
- 0.29.10

* Fri May 31 2019 Yuri N. Sedunov <aris@altlinux.org> 0.29.9-alt1
- 0.29.9

* Tue May 28 2019 Yuri N. Sedunov <aris@altlinux.org> 0.29.8-alt1
- 0.29.8

* Mon Apr 15 2019 Yuri N. Sedunov <aris@altlinux.org> 0.29.7-alt1
- 0.29.7

* Thu Feb 28 2019 Yuri N. Sedunov <aris@altlinux.org> 0.29.6-alt1
- 0.29.6

* Sat Feb 09 2019 Yuri N. Sedunov <aris@altlinux.org> 0.29.5-alt1
- 0.29.5

* Sat Feb 02 2019 Yuri N. Sedunov <aris@altlinux.org> 0.29.4-alt1
- 0.29.4

* Sat Jan 19 2019 Yuri N. Sedunov <aris@altlinux.org> 0.29.3-alt1
- 0.29.3

* Fri Dec 21 2018 Yuri N. Sedunov <aris@altlinux.org> 0.29.2-alt1
- 0.29.2

* Mon Nov 26 2018 Yuri N. Sedunov <aris@altlinux.org> 0.29.1-alt1
- 0.29.1

* Wed Aug 08 2018 Yuri N. Sedunov <aris@altlinux.org> 0.28.5-alt1
- 0.28.5

* Tue Jul 10 2018 Yuri N. Sedunov <aris@altlinux.org> 0.28.4-alt1
- 0.28.4

* Mon Jun 04 2018 Yuri N. Sedunov <aris@altlinux.org> 0.28.3-alt1
- 0.28.3

* Sat Apr 21 2018 Yuri N. Sedunov <aris@altlinux.org> 0.28.2-alt1
- 0.28.2

* Mon Mar 26 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 0.28.1-alt1.1
- (NMU) Rebuilt with python-3.6.4.

* Mon Mar 19 2018 Yuri N. Sedunov <aris@altlinux.org> 0.28.1-alt1
- 0.28.1

* Fri Mar 16 2018 Yuri N. Sedunov <aris@altlinux.org> 0.28-alt1
- 0.28

* Sun Nov 05 2017 Yuri N. Sedunov <aris@altlinux.org> 0.27.3-alt1
- 0.27.3

* Tue Oct 24 2017 Yuri N. Sedunov <aris@altlinux.org> 0.27.2-alt1
- 0.27.2

* Mon Oct 02 2017 Yuri N. Sedunov <aris@altlinux.org> 0.27.1-alt1
- 0.27.1

* Thu Sep 07 2017 Yuri N. Sedunov <aris@altlinux.org> 0.26.1-alt1
- 0.26.1

* Thu Jul 27 2017 Yuri N. Sedunov <aris@altlinux.org> 0.26-alt1
- 0.26

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
