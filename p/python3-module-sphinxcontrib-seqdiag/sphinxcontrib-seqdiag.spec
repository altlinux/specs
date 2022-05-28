%define  modulename sphinxcontrib-seqdiag

%def_without check

Name:    python3-module-%modulename
Version: 3.0.0
Release: alt1

Summary: A sphinx extension for embedding sequence diagram using seqdiag

License: BSD-2-Clause
Group:   Development/Python3
URL:     https://github.com/blockdiag/sphinxcontrib-seqdiag

Packager: Grigory Ustinov <grenka@altlinux.org>

BuildRequires(pre): rpm-build-python3

%if_with check
BuildRequires: python3-module-pytest
BuildRequires: python3-module-sphinx-testing
BuildRequires: python3-module-mock
BuildRequires: python3-module-webcolors
%endif

BuildArch: noarch

Source:  %name-%version.tar

%description
%summary

%prep
%setup

%build
%python3_build

%install
%python3_install

%check
%{__python3} -m pytest

%files
%python3_sitelibdir/sphinxcontrib*
%doc *.rst

%changelog
* Sat May 28 2022 Grigory Ustinov <grenka@altlinux.org> 3.0.0-alt1
- Automatically updated to 3.0.0.

* Mon May 31 2021 Grigory Ustinov <grenka@altlinux.org> 2.0.0-alt1
- Automatically updated to 2.0.0.

* Mon Jan 20 2020 Andrey Bychkov <mrdrew@altlinux.org> 0.8.5-alt2
- Porting on Python3.

* Sun Sep 22 2019 Grigory Ustinov <grenka@altlinux.org> 0.8.5-alt1
- Initial build for Sisyphus.
