%define module_name Compress-Stream-Zstd
%define _unpackaged_files_terminate_build 1

Name: perl-%module_name
Version: 0.202
Release: alt4
Summary: Perl interface to the Zstd (Zstandard) (de)compressor
Group: Development/Perl
License: BSD
URL: https://github.com/pmqs/Compress-Stream-Zstd

Source0: http://mirror.yandex.ru/mirrors/cpan/authors/id/P/PM/PMQS/%{module_name}-%{version}.tar.gz

BuildRequires: gcc-c++ libcurl-devel libgtest-devel liblz4-devel liblzma-devel libsowing-devel libxxhash-devel libzstd-devel perl(Config.pm) perl(Exporter.pm) perl(ExtUtils/ParseXS.pm) perl(Module/Build.pm) perl(Test/More.pm) perl(XSLoader.pm) perl(parent.pm) zlib-devel
BuildRequires: rpm-build-perl perl-devel perl-podlators

%description
The Compress::Stream::Zstd module provides an interface to the Zstd
(de)compressor.

%prep
%setup -q -n %{module_name}-%{version}

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc LICENSE Changes README.md
%perl_vendor_archlib/C*
%perl_vendor_autolib/*

%changelog
* Fri Nov 26 2021 L.A. Kostis <lakostis@altlinux.ru> 0.202-alt4
- Rebuild by human.

* Wed Jun 16 2021 Igor Vlasenko <viy@altlinux.org> 0.202-alt3
- rebuild with perl 5.34.0

* Thu Oct 01 2020 Igor Vlasenko <viy@altlinux.ru> 0.202-alt2
- rebuild with perl 5.30

* Fri Aug 28 2020 Igor Vlasenko <viy@altlinux.ru> 0.202-alt1
- updated by package builder

* Tue Jul 21 2020 Igor Vlasenko <viy@altlinux.ru> 0.201-alt1
- initial import by package builder
