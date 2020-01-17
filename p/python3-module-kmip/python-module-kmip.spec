%define  oname kmip

Name:    python3-module-%oname
Version: 0.9.1
Release: alt2

Summary: Open source Python implementation of the KMIP specification.

License: ASL 2.0
Group:   Development/Python3
URL:     https://github.com/OpenKMIP/PyKMIP
BuildArch: noarch

Packager: Grigory Ustinov <grenka@altlinux.org>

BuildRequires(pre): rpm-build-python3

Conflicts: python-module-%oname

Source:  %oname-%version.tar

%description
PyKMIP is a Python implementation of the Key Management Interoperability
Protocol (KMIP), an OASIS communication standard for the management of objects
stored and maintained by key management systems. KMIP defines how key management
operations and operation data should be encoded and communicated between client
and server applications. Supported operations include the full CRUD key
management lifecycle, including operations for managing object metadata and
for conducting cryptographic operations. Supported object types include:
- symmetric/asymmetric encryption keys
- passwords/passphrases
- certificates
- opaque data blobs, and more

%prep
%setup -n %oname-%version

%build
%python3_build

%install
%python3_install

%files
%doc *.rst
%_bindir/pykmip-server
%python3_sitelibdir/%oname
%python3_sitelibdir/*.egg-info


%changelog
* Fri Jan 17 2020 Andrey Bychkov <mrdrew@altlinux.org> 0.9.1-alt2
- Porting on Python3.

* Thu Aug 08 2019 Grigory Ustinov <grenka@altlinux.org> 0.9.1-alt1
- Build new version.

* Wed Jun 19 2019 Grigory Ustinov <grenka@altlinux.org> 0.9.0-alt1
- Initial build for Sisyphus.
