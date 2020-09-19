%define modname pyxdg
%def_with python2
%def_enable check

Name: python-module-%modname
Version: 0.26
Release: alt2

Summary: Implementations of freedesktop.org standards in Python
License: LGPLv2
Group: Development/Python
Url: http://freedesktop.org/Software/pyxdg
Packager: Python Development Team <python@packages.altlinux.org>

# https://gitlab.freedesktop.org/xdg/pyxdg.git
Vcs: https://github.com/takluyver/pyxdg.git
Source: %modname-%version.tar
Patch: %modname-0.26-alt-TryExec-test-py3.patch
Patch1: %modname-0.26-alt-TryExec-test-py2.patch
#https://github.com/takluyver/pyxdg/pull/12
#https://patch-diff.githubusercontent.com/raw/takluyver/pyxdg/pull/12.patch
Patch2: %modname-0.26-up-python-3.8.4-compatibility.patch

BuildArch: noarch

Provides: pyxdg = %version-%release

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel
%{?_enable_check:BuildRequires: python3-module-nose}

%{?_with_python2:
BuildRequires(pre): rpm-build-python
BuildRequires: python-devel python-modules-compiler
%{?_enable_check:BuildRequires: python-module-nose icon-theme-hicolor shared-mime-info %_bindir/python2}}

%description
PyXDG contains implementations of freedesktop.org standards in Python.

%package -n python3-module-%modname
Summary: Implementations of freedesktop.org standards in Python 3
Group: Development/Python3

%description -n python3-module-%modname
PyXDG contains implementations of freedesktop.org standards in Python 3.

%prep
%setup -n %modname-%version %{?_with_python2:-a0
cp -a %modname-%version py2build
pushd py2build
%patch1 -p1
popd}
%patch -p1
%patch2 -p1

%build
%python3_build
%{?_with_python2:
pushd py2build
%python_build}

%install
%python3_install
%{?_with_python2:
pushd py2build
%python_install
popd}

%check
pushd test
PYTHONPATH=%buildroot%python3_sitelibdir nosetests-3
popd
%{?_with_python2:
pushd py2build/test
PYTHONPATH=%buildroot%python_sitelibdir nosetests-2
popd}

%files -n python3-module-%modname
%doc AUTHORS ChangeLog README TODO
%python3_sitelibdir/*

%{?_with_python2:
%files
%doc AUTHORS ChangeLog README TODO
%python_sitelibdir/*}


%changelog
* Sat Sep 19 2020 Yuri N. Sedunov <aris@altlinux.org> 0.26-alt2
- fixed compatibility with python >= 3.8.4
  (see https://github.com/takluyver/pyxdg/pull/12)

* Thu Jul 23 2020 Yuri N. Sedunov <aris@altlinux.org> 0.26-alt1
- updated to rel-0.26-2-g7ad4b32
- made python2 build optional
- enabled %%check

* Mon Apr 11 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.25-alt1.1.1
- (NMU) rebuild with rpm-build-python3-0.1.10 (for new-style python3(*) reqs)
  and with python3-3.5 (for byte-compilation).

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.25-alt1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Apr 11 2013 Paul Wolneykien <manowar@altlinux.org> 0.25-alt1
- Dual build: python + python3.
- Use plain tar packaging.
- Fresh up to v0.25 with the help of cronbuild and update-source-functions.

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.19-alt1.1
- Rebuild with Python-2.7

* Sun Nov 28 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.19-alt1
- Version 0.19

* Tue Nov 17 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.17-alt1.1
- Rebuilt with python 2.6

* Tue Jun 02 2009 Fr. Br. George <george@altlinux.ru> 0.17-alt1
- Version up

* Thu Jan 24 2008 Grigory Batalov <bga@altlinux.ru> 0.15-alt1.1
- Rebuilt with python-2.5.

* Sat Sep 29 2007 Igor Zubkov <icesik@altlinux.org> 0.15-alt1
- build for Sisyphus

