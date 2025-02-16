%define oname Nuitka
%define _unpackaged_files_terminate_build 1

Name: nuitka
Version: 2.6.6
Release: alt1

Summary: Python compiler with full language support and CPython compatibility

License: ASLv2.0
Group: Development/Python3
Url: https://pypi.python.org/pypi/Nuitka/
Vcs: http://git.nuitka.net/Nuitka.git

# Source-url: %__pypi_url %oname
Source: %name-%version.tar

#BuildArch: noarch

BuildRequires(pre): rpm-build-intro
BuildRequires(pre): rpm-build-python3
#BuildRequires: gcc-c++
BuildRequires: python3-module-setuptools python3-module-wheel

AutoReq: yes, nopython3
AutoProv: no

Requires: pkgconfig(python3)
# fixes very slow fallback for ordered sets
Requires: python3(ordered_set)

%description
Nuitka is **the** Python compiler. It is a seamless replacement or
extension to the Python interpreter and compiles **every** construct
that CPython 2.6, 2.7, 3.2, 3.3, and 3.4 have. It then executed
uncompiled code, and compiled code together in an extremely compatible
manner.

You can use all Python library modules or and all extension modules
freely. It translates the Python into a C level program that then uses
"libpython" to execute in the same way as CPython does. All optimization
is aimed at avoiding overhead, where it's unnecessary. None is aimed at
removing compatibility, although there is an "improved" mode, where not
every bug of standard Python is emulated, e.g. more complete error
messages are given.

%prep
%setup


%build
%pyproject_build

%install
%pyproject_install

%files
%doc *.rst
%_bindir/nuitka
%_bindir/nuitka-run
%python3_sitelibdir/%name/
%python3_sitelibdir/%oname-%version.dist-info

%changelog
* Sun Feb 16 2025 Vitaly Lipatov <lav@altlinux.ru> 2.6.6-alt1
- build for Sisyphus again

* Mon Dec 16 2019 Andrey Bychkov <mrdrew@altlinux.org> 0.5.11-alt2
- build for python2 disabled

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.5.11-alt1.git20150318.1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.5.11-alt1.git20150318.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Wed Mar 18 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.5.11-alt1.git20150318
- Initial build for Sisyphus

