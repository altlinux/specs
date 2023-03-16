%define module_name Data-IEEE754
# BEGIN SourceDeps(oneline):
BuildRequires: perl(Exporter.pm) perl(ExtUtils/MakeMaker.pm) perl(File/Spec.pm) perl(Test/Bits.pm) perl(Test/More.pm) perl(strict.pm) perl(utf8.pm) perl(warnings.pm)
# END SourceDeps(oneline)
%define _unpackaged_files_terminate_build 1
BuildRequires(pre): rpm-build-licenses
BuildRequires: rpm-build-perl perl-devel perl-podlators

Name: perl-%module_name
Version: 0.02
Release: alt2
Summary: Pack and unpack big-endian IEEE754 floats and doubles
Group: Development/Perl
License: %artistic_license_v2
URL: http://metacpan.org/release/Data-IEEE754

Source0: http://mirror.yandex.ru/mirrors/cpan/authors/id/M/MA/MAXMIND/%{module_name}-%{version}.tar.gz
BuildArch: noarch

%description
%summary

%prep
%setup -q -n %{module_name}-%{version}

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc README.md Changes LICENSE CONTRIBUTING.md
%perl_vendor_privlib/D*

%changelog
* Tue Mar 07 2023 L.A. Kostis <lakostis@altlinux.ru> 0.02-alt2
- Fix License.

* Mon May 01 2017 Igor Vlasenko <viy@altlinux.ru> 0.02-alt1
- regenerated from template by package builder

* Fri Sep 06 2013 Igor Vlasenko <viy@altlinux.ru> 0.01-alt1
- initial import by package builder

