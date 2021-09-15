## SPEC file for Perl module Sort-Key-OID

%define real_name Sort-Key-OID

Name: perl-%real_name
Version: 0.05
Release: alt1

Summary: Sort::Key::OID - sort OIDs very fast

License: %perl_license
Group: Development/Perl

URL: https://metacpan.org/pod/Sort::Key::OID

Source: %real_name-%version.tar

BuildRequires(pre): perl-devel rpm-build-licenses perl(Module/Build.pm)
BuildRequires: perl-Sort-Key

%description
This module extends the Sort::Key family of modules to support sorting of OID
values. Also, once this module is loaded, the new type oid will be available
from Sort::Key::Maker.

%prep
%setup -q -n %real_name-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc README Changes
%perl_vendor_archlib/Sort/Key/OID*
%perl_vendor_autolib/Sort/Key/OID*

%changelog
* Wed Sep 15 2021 L.A. Kostis <lakostis@altlinux.ru> 0.05-alt1
- Initial build for ALTLinux.


