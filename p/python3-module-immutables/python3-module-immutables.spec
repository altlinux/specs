%define  modulename immutables

Name:    python3-module-%modulename
Version: 0.20
Release: alt1

Summary: A high-performance immutable mapping type for Python.
License: Apache-2.0
Group:   Development/Python3
URL:     https://github.com/MagicStack/immutables

Packager: Evgeny Sinelnikov <sin@altlinux.org>

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-dev python3-module-setuptools

Source:  %modulename-%version.tar

%description
An immutable mapping type for Python.

The underlying datastructure is a Hash Array Mapped Trie (HAMT) used in Clojure,
Scala, Haskell, and other functional languages. This implementation is used in
CPython 3.7 in the contextvars module (see PEP 550 and PEP 567 for more details)

%prep
%setup -n %modulename-%version

%build
%python3_build

%install
%python3_install

%files
%python3_sitelibdir/%modulename/
%python3_sitelibdir/*.egg-info
%doc README.*

%changelog
* Mon Dec 18 2023 Grigory Ustinov <grenka@altlinux.org> 0.20-alt1
- Automatically updated to 0.20.

* Wed Dec 14 2022 Grigory Ustinov <grenka@altlinux.org> 0.19-alt1
- Automatically updated to 0.19.

* Tue Feb 25 2020 Grigory Ustinov <grenka@altlinux.org> 0.11-alt1
- Build new version for python3.8.

* Tue Jan 15 2019 Evgeny Sinelnikov <sin@altlinux.org> 0.9-alt1
- Initial build for Sisyphus
