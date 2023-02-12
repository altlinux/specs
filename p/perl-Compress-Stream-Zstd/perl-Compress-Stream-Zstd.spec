%define _unpackaged_files_terminate_build 1
%define module_name Compress-Stream-Zstd

Name: perl-%module_name
Version: 0.205
Release: alt1

Summary: Perl interface to the Zstd (Zstandard) (de)compressor
License: BSD
Group: Development/Perl

Url: https://github.com/pmqs/Compress-Stream-Zstd
Source0: http://www.cpan.org/authors/id/P/PM/PMQS/%{module_name}-%{version}.tar.gz
Patch: zstd-1.4.5-alt-e2k.patch

BuildRequires: gcc-c++ libcurl-devel libgtest-devel liblz4-devel liblzma-devel libsowing-devel libxxhash-devel libzstd-devel perl(Config.pm) perl(Exporter.pm) perl(ExtUtils/ParseXS.pm) perl(Module/Build.pm) perl(Test/More.pm) perl(XSLoader.pm) perl(parent.pm) zlib-devel
BuildRequires: rpm-build-perl perl-devel perl-podlators

%description
The Compress::Stream::Zstd module provides an interface to the Zstd
(de)compressor.

%prep
%setup -q -n %{module_name}-%{version}
%ifarch %e2k
pushd ext/zstd
%patch -p1
popd
%endif

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README.md
%perl_vendor_archlib/C*
%perl_vendor_autolib/*

%changelog
* Sun Feb 12 2023 Igor Vlasenko <viy@altlinux.org> 0.205-alt1
- automated CPAN update

* Thu Apr 28 2022 Igor Vlasenko <viy@altlinux.org> 0.203-alt1
- new version

* Sat Jan 15 2022 Michael Shigorin <mike@altlinux.org> 0.202-alt5
- E2K: apply zstd arch support patch (ALT version)
- minor spec cleanup

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
