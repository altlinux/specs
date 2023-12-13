%define  oname certomancer-csc-dummy

Name:    python3-module-%oname
Version: 0.2.3
Release: alt1

Summary: A Certomancer-based demo CSC server for integration tests

License: MIT
Group:   Development/Python3
URL:     https://github.com/MatthiasValvekens/certomancer-csc-dummy

Packager: Grigory Ustinov <grenka@altlinux.org>

BuildRequires(pre): rpm-build-python3

BuildRequires: python3-module-wheel

BuildArch: noarch

Source:  %name-%version.tar

%description
This package contains a minimal implementation of the Cloud Signature Consortium
(CSC) API for remote signing. It's intended for use in integration tests
and demonstrations. Most of the heavy lifting is actually done by Certomancer.
This package merely wraps calls to Certomancer in an aiohttp-based web interface
that exposes (a subset of) the CSC API.

This is a testing tool, and it omits all sorts of essential security features:
* Requests are not authenticated
* No SAD replay prevention of any sort, other than the standard hash pinning
    supported by the CSC protocol
* All keys in the Certomancer config can be used to sign hashes in CSC calls


%prep
%setup

%build
%python3_build

%install
%python3_install

%files
%doc *.md
%_bindir/certomancer-csc
%python3_sitelibdir/csc_dummy
%python3_sitelibdir/certomancer_csc_dummy-%version-py%_python3_version.egg-info

%changelog
* Wed Dec 13 2023 Grigory Ustinov <grenka@altlinux.org> 0.2.3-alt1
- Automatically updated to 0.2.3.

* Mon May 15 2023 Grigory Ustinov <grenka@altlinux.org> 0.2.2-alt1
- Automatically updated to 0.2.2.

* Sun Aug 21 2022 Grigory Ustinov <grenka@altlinux.org> 0.2.1-alt1
- Automatically updated to 0.2.1.

* Fri Jul 29 2022 Grigory Ustinov <grenka@altlinux.org> 0.2.0-alt1
- Initial build for Sisyphus.
