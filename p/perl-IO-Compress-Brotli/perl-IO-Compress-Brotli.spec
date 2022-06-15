%define module_name IO-Compress-Brotli
Epoch: 2
# BEGIN SourceDeps(oneline):
BuildRequires: libbrotli-devel libsowing-devel perl(ExtUtils/MakeMaker.pm) perl(File/Slurper.pm) perl(Getopt/Long.pm) perl(Time/HiRes.pm) perl(parent.pm)
# END SourceDeps(oneline)
%define _unpackaged_files_terminate_build 1
BuildRequires: rpm-build-perl perl-devel perl-podlators

Name: perl-%module_name
Version: 0.004001
Release: alt3
Summary: Read Brotli buffers/streams
Group: Development/Perl
License: perl
Url: %CPAN %module_name

Source0: http://mirror.yandex.ru/mirrors/cpan/authors/id/M/MG/MGV/%{module_name}-%{version}.tar.gz

%description
IO::Compress::Brotli currently does nothing.

%package scripts
Summary: %module_name scripts
Group: Development/Perl
Requires: %name = %{?epoch:%epoch:}%version-%release
BuildArch: noarch

%description scripts
scripts for %module_name
%prep
%setup -q -n %{module_name}-%{version}

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README
%perl_vendor_archlib/I*
%perl_vendor_autolib/*

%files scripts
%_bindir/*

%changelog
* Wed Jun 16 2021 Igor Vlasenko <viy@altlinux.org> 2:0.004001-alt3
- rebuild with perl 5.34.0

* Thu Oct 01 2020 Igor Vlasenko <viy@altlinux.ru> 2:0.004001-alt2.1
- rebuild with perl 5.30

* Fri Feb 01 2019 Cronbuild Service <cronbuild@altlinux.org> 2:0.004001-alt1.1
- rebuild with perl 5.28.1

* Mon May 21 2018 Igor Vlasenko <viy@altlinux.ru> 2:0.004001-alt1
- regenerated from template by package builder

* Mon Dec 18 2017 Igor Vlasenko <viy@altlinux.ru> 2:0.004-alt4
- rebuild with perl 5.26

* Sun Oct 29 2017 Igor Vlasenko <viy@altlinux.ru> 2:0.004-alt3
- regenerated from template by package builder

* Wed Feb 15 2017 Cronbuild Service <cronbuild@altlinux.org> 1:0.002001-alt2
- rebuild to get rid of unmets

* Sun Sep 18 2016 Igor Vlasenko <viy@altlinux.ru> 1:0.002001-alt1
- regenerated from template by package builder

* Thu Sep 01 2016 Igor Vlasenko <viy@altlinux.ru> 1:0.002-alt2
- regenerated from template by package builder

* Tue Mar 22 2016 Igor Vlasenko <viy@altlinux.ru> 0.001001-alt1
- initial import by package builder

