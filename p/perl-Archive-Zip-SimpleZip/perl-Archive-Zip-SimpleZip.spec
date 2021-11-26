%define module_name Archive-Zip-SimpleZip
%define _unpackaged_files_terminate_build 1

Name: perl-%module_name
Version: 0.040
Release: alt2
Summary: Create Zip Archives
Group: Development/Perl
License: %perl_license
URL: https://github.com/pmqs/%module_name

Source0: http://mirror.yandex.ru/mirrors/cpan/authors/id/P/PM/PMQS/%{module_name}-%{version}.tar.gz
BuildArch: noarch

BuildRequires(pre): rpm-build-perl rpm-build-licenses perl-devel perl-podlators
BuildRequires: perl-Compress-Raw-Zlib perl-Term-Cap perl-Term-ANSIColor
BuildRequires: perl-Pod-Escapes perl-Filter perl-Encode perl-Pod-Simple perl-Pod-Usage
BuildRequires: perl-Devel-StackTrace perl-Compress-Stream-Zstd perl-Compress-Raw-Lzma
BuildRequires: perl-Compress-Raw-Bzip2 perl-IO-Compress perl-Test-NoWarnings
BuildRequires: perl-IO-Compress-Lzma perl-IO-Compress-Zstd perl-IO-Compress perl-Perl-OSType

%description
Archive::Zip::SimpleZip is a module that allows the creation of Zip.archives.

The module allows Zip archives to be written to a named file, a filehandle
or stored in-memory.

There are a small number methods available in Archive::Zip::SimpleZip, and
quite a few options, but for the most part all you need to know is how to
create a Zip archive and how to add a file to it.

%prep
%setup -q -n %{module_name}-%{version}

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README
%perl_vendor_privlib/A*

%changelog
* Tue Nov 23 2021 L.A. Kostis <lakostis@altlinux.ru> 0.040-alt2
- Rebuild by human.

* Sun Jul 18 2021 Igor Vlasenko <viy@altlinux.ru> 0.040-alt1
- updated by package builder

* Thu Sep 10 2020 Igor Vlasenko <viy@altlinux.ru> 0.039-alt1
- updated by package builder

* Tue Sep 08 2020 Igor Vlasenko <viy@altlinux.ru> 0.038-alt1
- updated by package builder

* Sat Jan 18 2020 Igor Vlasenko <viy@altlinux.ru> 0.035-alt1
- updated by package builder

* Fri Jun 21 2019 Igor Vlasenko <viy@altlinux.ru> 0.025-alt1
- updated by package builder

* Mon Jun 17 2019 Igor Vlasenko <viy@altlinux.ru> 0.024-alt1
- updated by package builder

* Wed Apr 11 2018 Igor Vlasenko <viy@altlinux.ru> 0.022-alt1
- regenerated from template by package builder

* Mon May 01 2017 Igor Vlasenko <viy@altlinux.ru> 0.010-alt1
- regenerated from template by package builder

* Mon Oct 07 2013 Igor Vlasenko <viy@altlinux.ru> 0.009-alt1
- initial import by package builder

