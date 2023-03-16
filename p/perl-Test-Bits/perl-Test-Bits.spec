# BEGIN SourceDeps(oneline):
BuildRequires: perl(List/AllUtils.pm) perl(Scalar/Util.pm) perl(Test/Fatal.pm) perl(Test/More.pm) perl(Test/Tester.pm) perl(parent.pm)
# END SourceDeps(oneline)
%define module_version 0.02
%define module_name Test-Bits
%define _unpackaged_files_terminate_build 1
BuildRequires: rpm-build-perl perl-devel perl-podlators
BuildRequires(pre): rpm-build-licenses

Name: perl-%module_name
Version: 0.02
Release: alt2
Summary: Provides a bits_is() subroutine for testing binary data
Group: Development/Perl
License: %artistic_license_v2
URL: http://metacpan.org/release/Test-Bits

Source0: http://cpan.org.ua/authors/id/D/DR/DROLSKY/%module_name-%module_version.tar.gz
BuildArch: noarch

%description
%summary

%prep
%setup -n %module_name-%module_version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc README Changes LICENSE
%perl_vendor_privlib/T*

%changelog
* Tue Mar 07 2023 L.A. Kostis <lakostis@altlinux.ru> 0.02-alt2
- Fix License.

* Tue Sep 03 2013 Igor Vlasenko <viy@altlinux.ru> 0.02-alt1
- initial import by package builder

