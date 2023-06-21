#%%def_disable check

%define  modulename treq
Name:    python3-module-%modulename
Version: 22.2.0
Release: alt2

Summary: Python requests like API built on top of Twisted's HTTP client
License: MIT
Group:   Development/Python3
URL:     https://github.com/twisted/treq

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-dev
BuildRequires: python3-module-wheel
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-incremental
%if_disabled check
%else
#BuildRequires: pytest3
BuildRequires: python3(twisted)
BuildRequires: python3(twisted.trial)
BuildRequires: python3(twisted.web)
BuildRequires: python3(twisted.words)
BuildRequires: python3(requests)
BuildRequires: python3(service_identity)
BuildRequires: python3(httpbin)
BuildRequires: python3-module-twisted-core-tests
%endif

BuildArch: noarch

Source:  %modulename-%version.tar

%description
treq is an HTTP library inspired by requests but written on top of Twisted's
Agents.

It provides a simple, higher level API for making HTTP requests when using
Twisted.

%prep
%setup -n %modulename-%version

%build
%pyproject_build

%install
%pyproject_install
# cleanup tests
rm -rf %buildroot%python3_sitelibdir/%modulename/test
rm -rf %buildroot%python3_sitelibdir/%modulename/testing.py

%check
export PYTHONDONTWRITEBYTECODE=1
export PYTHONPATH=%buildroot/%python3_sitelibdir/
trial treq || exit 1
#pytest3 -v

%files
%python3_sitelibdir/%modulename/
%python3_sitelibdir/%modulename-%version.dist-info

%changelog
* Wed Jun 21 2023 Grigory Ustinov <grenka@altlinux.org> 22.2.0-alt2
- Fixed dependencies for building without check.

* Tue Jun 13 2023 Anton Midyukov <antohami@altlinux.org> 22.2.0-alt1
- new version

* Wed May 19 2021 Anton Midyukov <antohami@altlinux.org> 21.1.0-alt1
- new version

* Sun Nov 08 2020 Vitaly Lipatov <lav@altlinux.ru> 18.6.0-alt4
- NMU: drop testing.py in additional to removed tests

* Tue Oct 01 2019 Anton Farygin <rider@altlinux.ru> 18.6.0-alt3
- removed python2 support
- removed tests from python3-module-treq package

* Mon Jan 21 2019 Anton Midyukov <antohami@altlinux.org> 18.6.0-alt2
- Added python_req_hier (Closes: 35940)

* Wed Aug 22 2018 Anton Midyukov <antohami@altlinux.org> 18.6.0-alt1
- Initial build for Sisyphus
