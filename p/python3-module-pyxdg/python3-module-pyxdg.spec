%def_enable snapshot
%define pypi_name pyxdg
%def_enable check

Name: python3-module-%pypi_name
Version: 0.28
Release: alt2

Summary: Implementations of freedesktop.org standards in Python 3
License: LGPL-2.0
Group: Development/Python3
Url: http://freedesktop.org/Software/pyxdg

Vcs: https://gitlab.freedesktop.org/xdg/pyxdg.git

%if_disabled snapshot
Source: https://github.com/takluyver/pyxdg/archive/rel-%version/%pypi_name-%version.tar.gz
%else
Source: %pypi_name-%version.tar
%endif
BuildArch: noarch

Requires: shared-mime-info
Provides: %pypi_name = %EVR

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python3-module-setuptools python3-module-wheel
%{?_enable_check:BuildRequires: python3(pytest) python3(imp) shared-mime-info icon-theme-hicolor}

%description
PyXDG contains implementations of freedesktop.org standards in Python 3.

%prep
%setup -n %pypi_name%{?_disable_snapshot:-rel}-%version

# since 2.5.1 text/x-cython separated from x-python and not executable
sed -i '/app_executable/s/^/#/' test/test_mime.py

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest

%files
%python3_sitelibdir/xdg/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}
%doc AUTHORS ChangeLog README TODO


%changelog
* Sat Jul 04 2026 Yuri N. Sedunov <aris@altlinux.org> 0.28-alt2
- updated to rel-0.28-3-g63033ac

* Mon Feb 19 2024 Yuri N. Sedunov <aris@altlinux.org> 0.28-alt1.2
- updated BR

* Thu May 04 2023 Yuri N. Sedunov <aris@altlinux.org> 0.28-alt1.1
- removed python3-module-nose from BR (ALT #46064)

* Thu Oct 06 2022 Yuri N. Sedunov <aris@altlinux.org> 0.28-alt1
- 0.28 (added $XDG_STATE_DIR support)
- ported to %%pyproject* macros

* Wed Dec 09 2020 Yuri N. Sedunov <aris@altlinux.org> 0.27-alt1
- 0.27 (python3-only)

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

