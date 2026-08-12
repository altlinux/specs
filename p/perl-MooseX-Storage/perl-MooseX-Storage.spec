%define real_name MooseX-Storage

Name: perl-%real_name
Version: 0.53
Release: alt1

Summary: A serialization framework for Moose classes

License: %perl_license
Group: Development/Perl

URL: https://metacpan.org/release/%real_name
# Source-url: https://cpan.metacpan.org/authors/id/E/ET/ETHER/%real_name-%version.tar.gz
Source: %real_name-%version.tar

BuildArch: noarch

BuildRequires(pre): rpm-build-perl rpm-build-licenses
BuildRequires: perl-devel perl-Module-Metadata
BuildRequires: perl-Moose perl-String-RewritePrefix perl-namespace-autoclean perl-JSON-PP perl-JSON-MaybeXS perl-IO-Stringy perl-YAML perl-Storable
BuildRequires: perl-Test-Deep perl-Test-Deep-Type perl-Test-Fatal perl-Test-Needs

%description
MooseX::Storage is a serialization framework for Moose classes. It lets you
store and retrieve Moose objects (with their type constraints and traits) to
and from JSON, YAML, Storable, and other formats via a small set of roles
applied to your classes.

%prep
%setup -q -n %real_name-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes LICENSE README
%perl_vendor_privlib/MooseX/Storage*

%changelog
* Tue Jul 28 2026 Vitaly Lipatov <lav@altlinux.ru> 0.53-alt1
- initial build for Sisyphus
