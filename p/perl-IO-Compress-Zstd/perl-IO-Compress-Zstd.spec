%define _unpackaged_files_terminate_build 1
%define module_name IO-Compress-Zstd
Name: perl-%module_name
Version: 2.204
Release: alt1
Summary: Write zstd files/buffers
Group: Development/Perl
License: %perl_license
URL: https://github.com/pmqs/%module_name

Source0: http://www.cpan.org/authors/id/P/PM/PMQS/%{module_name}-%{version}.tar.gz
BuildArch: noarch

BuildRequires: rpm-build-perl perl-devel perl-Test-NoWarnings perl-IO-Compress perl-Compress-Stream-Zstd
BuildRequires(pre): rpm-build-licenses

%description
This module provides a Perl interface that allows writing zstd
compressed data to files or buffer.

For reading zstd files/buffers, see the companion module
IO::Uncompress::UnZstd.

%prep
%setup -q -n %{module_name}-%{version}

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README
%perl_vendor_privlib/I*

%changelog
* Sun Feb 12 2023 Igor Vlasenko <viy@altlinux.org> 2.204-alt1
- automated CPAN update

* Fri Jul 01 2022 Igor Vlasenko <viy@altlinux.org> 2.201-alt1
- new version

* Thu Apr 07 2022 Igor Vlasenko <viy@altlinux.org> 2.103-alt1
- new version

* Fri Nov 26 2021 L.A. Kostis <lakostis@altlinux.ru> 2.101-alt2
- Rebuild by human.

* Thu Feb 25 2021 Igor Vlasenko <viy@altlinux.ru> 2.101-alt1
- updated by package builder

* Fri Jan 15 2021 Igor Vlasenko <viy@altlinux.ru> 2.100-alt1
- updated by package builder

* Sun Nov 01 2020 Igor Vlasenko <viy@altlinux.ru> 2.099-alt1
- updated by package builder

* Mon Sep 07 2020 Igor Vlasenko <viy@altlinux.ru> 2.096-alt1
- initial import by package builder

