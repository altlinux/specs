%define _unpackaged_files_terminate_build 1
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-perl
BuildRequires: perl(MIME/Base64.pm) perl(Storable.pm) perl(Test.pm) perl(URI.pm) perl-Module-Build perl-devel perl-podlators
# END SourceDeps(oneline)
%define upstream_name    HTTP-Headers-Fast

Name:       perl-%{upstream_name}
Version:    0.21
Release:    alt1

Summary:    Faster implementation of HTTP::Headers
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/authors/id/T/TO/TOKUHIROM/%{upstream_name}-%{version}.tar.gz

BuildRequires: perl(HTTP/Date.pm)
BuildRequires: perl(Module/Build/Tiny.pm)
BuildRequires: perl(Test/More.pm)
BuildRequires: perl(Test/Requires.pm)
BuildArch:  noarch
Source44: import.info

%description
HTTP::Headers::Fast is a perl class for parsing/writing HTTP headers.

The interface is the same as HTTP::Headers.

%prep
%setup -q -n %{upstream_name}-%{version}

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes LICENSE META.json META.yml README.md
%perl_vendor_privlib/*

%changelog
* Wed May 10 2017 Igor Vlasenko <viy@altlinux.ru> 0.21-alt1
- automated CPAN update

* Fri Nov 27 2015 Igor Vlasenko <viy@altlinux.ru> 0.20-alt1
- automated CPAN update

* Sun Oct 11 2015 Igor Vlasenko <viy@altlinux.ru> 0.19-alt1
- automated CPAN update

* Wed Mar 05 2014 Igor Vlasenko <viy@altlinux.ru> 0.17-alt1
- automated CPAN update

* Thu Oct 17 2013 Igor Vlasenko <viy@altlinux.ru> 0.16-alt3_2
- build for Sisyphus

* Fri Sep 13 2013 Cronbuild Service <cronbuild@altlinux.org> 0.16-alt2_2
- rebuild to get rid of unmets

* Wed Aug 07 2013 Igor Vlasenko <viy@altlinux.ru> 0.16-alt1_2
- mgaimport update

* Thu Jul 25 2013 Igor Vlasenko <viy@altlinux.ru> 0.16-alt1_1
- converted for ALT Linux by srpmconvert tools

