%define _name Cython

%def_with python3

Name: python-module-%_name
Version: 0.16
Release: alt1

Summary: C-extensions for Python
Group: Development/Python
License: Python
Url: http://www.cython.org

Source: http://www.cython.org/release/Cython-%version.tar.gz

Provides: %_name = %version-%release

BuildPreReq: rpm-build-python
BuildPreReq: python-devel python-module-setuptools

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

%if_with python3
%package -n python3-module-%_name
Summary: C-extensions for Python3
Group: Development/Python3
BuildRequires(pre): rpm-build-python3
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
%endif

%prep
%setup -q -n %_name-%version
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
%python_sitelibdir/pyximport/
%python_sitelibdir/%_name/
%python_sitelibdir/%_name-*egg-info
%python_sitelibdir/cython.py*
%doc *.txt Demos Doc Tools

# don't package tests files and debugger
%exclude %python_sitelibdir/%_name/Tests
%exclude %python_sitelibdir/%_name/*/Tests
%exclude %python_sitelibdir/%_name/Debugger
%exclude %_bindir/cygdb

%if_with python3
%files -n python3-module-%_name
%_bindir/cython3
%python3_sitelibdir/%_name/
%python3_sitelibdir/pyximport/
%python3_sitelibdir/cython.py
%python3_sitelibdir/__pycache__/cython.*
%python3_sitelibdir/*egg-info

# don't package tests files and debugger
%exclude %python3_sitelibdir/%_name/Tests
%exclude %python3_sitelibdir/%_name/*/Tests
%exclude %python3_sitelibdir/%_name/Debugger
%exclude %_bindir/cygdb3
%endif

%changelog
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
