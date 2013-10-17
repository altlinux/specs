# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-perl
BuildRequires: perl(MIME/Base64.pm) perl(Storable.pm) perl(Test.pm) perl(URI.pm) perl-Module-Build perl-devel perl-podlators
# END SourceDeps(oneline)
%define upstream_name    HTTP-Headers-Fast
%define upstream_version 0.16

Name:       perl-%{upstream_name}
Version:    %{upstream_version}
Release:    alt3_2

Summary:    Faster implementation of HTTP::Headers
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/HTTP/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(HTTP/Date.pm)
BuildRequires: perl(Module/Build.pm)
BuildRequires: perl(Test/More.pm)
BuildRequires: perl(Test/Requires.pm)
BuildArch:  noarch
Source44: import.info

%description
HTTP::Headers::Fast is a perl class for parsing/writing HTTP headers.

The interface is the same as HTTP::Headers.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%__perl Build.PL --install_path bindoc=%_man1dir installdirs=vendor
./Build CFLAGS="%{optflags}"

%check
./Build test

%install
./Build install destdir=%{buildroot}

%files
%doc Changes LICENSE META.json META.yml  README
%perl_vendor_privlib/*

%changelog
* Thu Oct 17 2013 Igor Vlasenko <viy@altlinux.ru> 0.16-alt3_2
- build for Sisyphus

* Fri Sep 13 2013 Cronbuild Service <cronbuild@altlinux.org> 0.16-alt2_2
- rebuild to get rid of unmets

* Wed Aug 07 2013 Igor Vlasenko <viy@altlinux.ru> 0.16-alt1_2
- mgaimport update

* Thu Jul 25 2013 Igor Vlasenko <viy@altlinux.ru> 0.16-alt1_1
- converted for ALT Linux by srpmconvert tools

