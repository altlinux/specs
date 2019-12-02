%define oname blist

Name: python3-module-%oname
Version: 1.3.6
Release: alt3

Summary: A list-like type with better asymptotic performance and similar performance on small lists
License: BSD
Group: Development/Python3
Url: https://pypi.python.org/pypi/blist/

Source: blist-%version.tar.gz
Patch: 0001-Fix-compatibility-for-Python-3.7.patch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-pytest


%description
The blist is a drop-in replacement for the Python list that provides
better performance when modifying large lists. The blist package also
provides sortedlist, sortedset, weaksortedlist, weaksortedset,
sorteddict, and btuple types.

%prep
%setup -n %oname-%version
%patch -p1

sed -i '/ez_setup/d' setup.py

%build
%python3_build

%install
%python3_install

%check
%__python3 setup.py test

%files
%doc README.rst
%python3_sitelibdir/*%{oname}*


%changelog
* Mon Dec 02 2019 Andrey Bychkov <mrdrew@altlinux.org> 1.3.6-alt3
- python2 disabled

* Tue Apr 02 2019 Grigory Ustinov <grenka@altlinux.org> 1.3.6-alt2
- Rebuild with python3.7.

* Thu Mar 22 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 1.3.6-alt1.1.1.1
- (NMU) Rebuilt with python-3.6.4.

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 1.3.6-alt1.1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Thu Mar 17 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.3.6-alt1.1
- (NMU) rebuild with python3-3.5 & rpm-build-python3-0.1.10
  (for ABI dependence and new python3(*) reqs)

* Sun May 03 2015 Fr. Br. George <george@altlinux.ru> 1.3.6-alt1
- Autobuild version bump to 1.3.6

* Sun May 03 2015 Fr. Br. George <george@altlinux.ru> 1.3.5-alt1
- Initial build for ALT

