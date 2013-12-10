Summary: Test certificates for pesign
Name: pesign-test-certs
Version: 0.1
Release: alt1
Group: Development/Other
License: GPLv2
BuildArch: noarch
ExclusiveArch: %ix86 x86_64
# http://pkgs.fedoraproject.org/repo/pkgs/pesign/rh-test-certs.tar.bz2/328db7cb27847cb610b7cf8f9c470455/rh-test-certs.tar.bz2
Source: rh-test-certs.tar

%description
This package contains test certificates for pesign.

%prep
%setup -c

%install
mkdir %buildroot
mv rh-test-certs/etc %buildroot/

%pre
getent group pesign >/dev/null || groupadd -r pesign

%files
%defattr(644,root,pesign,710)
/etc/pki/pesign/

%changelog
* Mon Dec 02 2013 Dmitry V. Levin <ldv@altlinux.org> 0.1-alt1
- Initial revision.
