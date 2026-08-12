Name:           moin-uneex
Version:        1.0
Release:        alt1
License:        GPLv2+
Group:          Networking/Other
Source:         %name-%version.tar
BuildArch:      noarch
Summary: Set of MoinMoin plugins specific to uneex.org
BuildRequires:  python-devel
Requires:       moin

%description
%summary

%prep
%setup

%install
mkdir -p %buildroot%python_sitelibdir/MoinMoin/macro
install macro/*.py %buildroot%python_sitelibdir/MoinMoin/macro/

%files
%python_sitelibdir/MoinMoin/macro/*

%changelog
* Fri Aug 07 2026 Fr. Br. George <george@altlinux.org> 1.0-alt1
- Initilal build for ALT
