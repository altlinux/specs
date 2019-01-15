%define  modulename contextvars

Name:    python3-module-%modulename
Version: 2.3
Release: alt1

Summary: PEP 567 Backport
License: Apache-2.0
Group:   Development/Python3
URL:     https://github.com/MagicStack/contextvars

Packager: Evgeny Sinelnikov <sin@altlinux.org>

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-dev python3-module-setuptools

BuildArch: noarch

Source:  %modulename-%version.tar

%description
This module provides APIs to manage, store, and access context-local state.
The ContextVar class is used to declare and work with Context Variables.

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
* Tue Jan 15 2019 Evgeny Sinelnikov <sin@altlinux.org> 2.3-alt1
- Initial build for Sisyphus
