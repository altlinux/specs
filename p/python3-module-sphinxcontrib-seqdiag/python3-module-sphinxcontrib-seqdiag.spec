%define  modulename sphinxcontrib-seqdiag

Name:    python3-module-%modulename
Version: 0.8.5
Release: alt2

Summary: A sphinx extension for embedding sequence diagram using seqdiag

License: BSD-2-Clause
Group:   Development/Python3
URL:     https://github.com/blockdiag/sphinxcontrib-seqdiag

Packager: Grigory Ustinov <grenka@altlinux.org>

BuildRequires(pre): rpm-build-python3

BuildArch: noarch

Source:  %modulename-%version.tar

%description
%summary

%prep
%setup -n %modulename-%version

%build
%python3_build

%install
%python3_install

%files
%python3_sitelibdir/sphinxcontrib*
%doc *.rst

%changelog
* Mon Jan 20 2020 Andrey Bychkov <mrdrew@altlinux.org> 0.8.5-alt2
- Porting on Python3.

* Sun Sep 22 2019 Grigory Ustinov <grenka@altlinux.org> 0.8.5-alt1
- Initial build for Sisyphus.
