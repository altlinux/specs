%define pypi_name Cython
%def_disable debugger
%ifarch armh
%def_disable check
%else
%def_enable check
%endif

Name: python3-module-%pypi_name
Version: 0.29.33
Release: alt1

Summary: C-extensions for Python 3
Group: Development/Python3
License: Apache-2.0
Url: http://www.cython.org

Vcs: https://github.com/cython/cython.git
#Source: https://pypi.io/packages/source/C/%pypi_name/%pypi_name-%version.tar.gz
Source: https://github.com/cython/cython/archive/%version/%pypi_name-%version.tar.gz

%add_python3_req_skip IPython IPython.core IPython.core.magic IPython.utils IPython.utils.text

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python3-module-setuptools python3-module-wheel
%{?_enable_check:BuildRequires: python3-module-tox
BuildRequires: gcc-c++ libgomp-devel
BuildRequires: python3-module-coverage python3-module-pycodestyle
BuildRequires: python3-module-numpy libnumpy-py3-devel}

%description
Cython is a language that makes writing C extensions for the Python 3
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
Group: Development/Python3
Requires: %name = %EVR

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
Group: Development/Python3
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
libraries, and for fast C modules that speed up the execution of Python 3
code.

This package provides modules for debugging Cython programms.

%prep
%setup -n cython-%version

%build
%pyproject_build

%install
%pyproject_install
for f in cy{thon{,ize},gdb}; do
ln -s $f %buildroot/%_bindir/"$f"3;
done

%check
%tox_check

%files
%_bindir/cython
%_bindir/cythonize
%_bindir/cython3
%_bindir/cythonize3
%python3_sitelibdir/%pypi_name/
%python3_sitelibdir/pyximport/
%python3_sitelibdir/cython.py
%python3_sitelibdir/__pycache__/cython.*
%python3_sitelibdir/*.dist-info
%doc CHANGES* README* USAGE*

%exclude %python3_sitelibdir/%pypi_name/Tests
%exclude %python3_sitelibdir/%pypi_name/Debugger

%files tests
%python3_sitelibdir/%pypi_name/Tests

%if_enabled debugger
%files debugger
%python3_sitelibdir/%pypi_name/Debugger
%_bindir/cygdb
%_bindir/cygdb3
%endif

%changelog
* Mon Jan 09 2023 Yuri N. Sedunov <aris@altlinux.org> 0.29.33-alt1
- 0.29.33

* Fri Jul 29 2022 Yuri N. Sedunov <aris@altlinux.org> 0.29.32-alt1
- 0.29.32

* Wed Jul 27 2022 Yuri N. Sedunov <aris@altlinux.org> 0.29.31-alt1
- 0.29.31
- ported to %%pyproject macros, enabled %%check

* Tue May 17 2022 Yuri N. Sedunov <aris@altlinux.org> 0.29.30-alt1
- 0.29.30

* Mon May 16 2022 Yuri N. Sedunov <aris@altlinux.org> 0.29.29-alt1
- 0.29.29

* Wed Mar 02 2022 Yuri N. Sedunov <aris@altlinux.org> 0.29.28-alt1
- 0.29.28

* Thu Dec 16 2021 Yuri N. Sedunov <aris@altlinux.org> 0.29.26-alt1
- 0.29.26

* Mon Dec 06 2021 Yuri N. Sedunov <aris@altlinux.org> 0.29.25-alt1
- 0.29.25

* Fri Jul 16 2021 Yuri N. Sedunov <aris@altlinux.org> 0.29.24-alt1
- 0.29.24

* Wed May 26 2021 Yuri N. Sedunov <aris@altlinux.org> 0.29.23-alt2
- python3-only package

* Wed Apr 14 2021 Yuri N. Sedunov <aris@altlinux.org> 0.29.23-alt1
- 0.29.23

* Sat Feb 20 2021 Yuri N. Sedunov <aris@altlinux.org> 0.29.22-alt1
- 0.29.22

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
