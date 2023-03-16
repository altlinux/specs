%define module_name MaxMind-DB-Reader-XS
%define _unpackaged_files_terminate_build 1

Name: perl-%module_name
Version: 1.000009
Release: alt1
Summary: Fast XS implementation of MaxMind DB reader
Group: Development/Perl
License: %artistic_license_v2
URL: https://metacpan.org/release/MaxMind-DB-Reader-XS

# https://github.com/maxmind/%{module_name}/archive/refs/tags/v%{version}.tar.gz
Source0: %{name}-%{version}.tar
Source1: maxmind-db.tar

BuildRequires(pre): rpm-build-licenses
BuildRequires: rpm-build-perl perl-devel perl-podlators libmaxminddb-devel perl-Math-Int128 perl-Math-Int64
BuildRequires: perl-MaxMind-DB-Common perl-MaxMind-DB-Reader perl-Moo perl-Module-Build perl-Net-Works
# for tests
BuildRequires: perl-Net-Works perl-Path-Class perl-Test-Number-Delta perl-Test-Requires

# 64-bit only
ExcludeArch: %ix86 armh

%description
Simply installing this module causes MaxMind::DB::Reader to use the XS
implementation, which is much faster than the Perl implementation.

The XS implementation links against the libmaxminddb library.

See MaxMind::DB::Reader for API details.

%prep
%setup -q -a1

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc LICENSE Changes README.md CONTRIBUTING.md
%perl_vendor_archlib/M*
%perl_vendor_autolib/*

%changelog
* Fri Mar 10 2023 L.A. Kostis <lakostis@altlinux.ru> 1.000009-alt1
- initial build for ALTLinux.
