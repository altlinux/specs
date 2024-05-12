%define mname dogpile
%define oname %mname.cache

%def_with check

Name: python3-module-%oname
Version: 1.3.3
Release: alt1

Summary: A caching front-end based on the Dogpile lock

License: MIT
Group: Development/Python3
URL: https://pypi.org/project/dogpile.cache
VCS: https://github.com/sqlalchemy/dogpile.cache

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-wheel

%if_with check
BuildRequires: python3-module-pbr
BuildRequires: python3-module-tox
BuildRequires: python3-module-pytest
BuildRequires: python3-module-mako
BuildRequires: python3-module-decorator
BuildRequires: python3-module-stevedore
%endif

Provides: python3-module-dogpile-cache = %EVR
Obsoletes: python3-module-dogpile-cache < %EVR
Provides: python3-module-dogpile-core = %EVR
Obsoletes: python3-module-dogpile-core < %EVR

%py3_provides %oname
%py3_provides %mname.core

%description
A caching API built around the concept of a "dogpile lock", which allows
continued access to an expiring data value while a single thread
generates a new value.

dogpile.cache builds on the dogpile.core locking system, which
implements the idea of "allow one creator to write while others read" in
the abstract. Overall, dogpile.cache is intended as a replacement to the
Beaker caching system, the internals of which are written by the same
author. All the ideas of Beaker which "work" are re-implemented in
dogpile.cache in a more efficient and succinct manner, and all the cruft
(Beaker's internals were first written in 2005) relegated to the trash
heap.

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

%if "%_libexecdir" != "%_libdir"
mv %buildroot%_libexecdir %buildroot%_libdir
%endif

%check
%tox_check_pyproject

%files
%doc LICENSE *.rst
%python3_sitelibdir/%mname
%python3_sitelibdir/%oname-%version.dist-info

%changelog
* Sun May 12 2024 Grigory Ustinov <grenka@altlinux.org> 1.3.3-alt1
- Automatically updated to 1.3.3.

* Fri Mar 01 2024 Grigory Ustinov <grenka@altlinux.org> 1.3.2-alt1
- Automatically updated to 1.3.2.

* Sat Feb 10 2024 Grigory Ustinov <grenka@altlinux.org> 1.3.1-alt1
- Automatically updated to 1.3.1.

* Mon Dec 25 2023 Grigory Ustinov <grenka@altlinux.org> 1.3.0-alt1
- Automatically updated to 1.3.0.

* Tue Jul 11 2023 Grigory Ustinov <grenka@altlinux.org> 1.2.2-alt1
- Automatically updated to 1.2.2.

* Sun Jun 11 2023 Grigory Ustinov <grenka@altlinux.org> 1.2.1-alt1
- Automatically updated to 1.2.1.
- Fixed license.

* Thu Apr 27 2023 Grigory Ustinov <grenka@altlinux.org> 1.2.0-alt1
- Automatically updated to 1.2.0.

* Fri Jul 15 2022 Grigory Ustinov <grenka@altlinux.org> 1.1.8-alt1
- Automatically updated to 1.1.8.

* Mon Jun 13 2022 Grigory Ustinov <grenka@altlinux.org> 1.1.6-alt1
- Automatically updated to 1.1.6.

* Tue Apr 26 2022 Grigory Ustinov <grenka@altlinux.org> 1.1.5-alt1
- Automatically updated to 1.1.5.

* Tue Feb 11 2020 Andrey Bychkov <mrdrew@altlinux.org> 0.7.1-alt2
- Build for python2 disabled.

* Mon Apr 22 2019 Alexey Shabalin <shaba@altlinux.org> 0.7.1-alt1
- 0.7.1

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.6.2-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Tue Oct 18 2016 Alexey Shabalin <shaba@altlinux.ru> 0.6.2-alt1
- 0.6.2
- The dogpile.core package has been rolled into dogpile.cache directly

* Tue May 24 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.5.7-alt1.1
- (AUTO) subst_x86_64.

* Tue Apr 12 2016 Alexey Shabalin <shaba@altlinux.ru> 0.5.7-alt1
- 0.5.7

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.5.6-alt2.git20150202.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.5.6-alt2.git20150202.1
- NMU: Use buildreq for BR.

* Wed Feb 18 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.5.6-alt2.git20150202
- Provides: python-module-dogpile-cache

* Fri Feb 06 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.5.6-alt1.git20150202
- Initial build for Sisyphus

