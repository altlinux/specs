# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-perl
BuildRequires: perl-podlators
# END SourceDeps(oneline)
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%define upstream_name    Alien-Build-Plugin-Download-GitLab
%define upstream_version 0.01

%{?perl_default_filter}

Name:       perl-%{upstream_name}
Version:    %{upstream_version}
Release:    alt1_2

Summary:    Alien::Build plugin to download from GitLab
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        https://metacpan.org/release/%{upstream_name}
Source0:    https://cpan.metacpan.org/authors/id/P/PL/PLICEASE/%{upstream_name}-%{upstream_version}.tar.gz
BuildArch:  noarch

BuildRequires:  perl(Alien/Build/Plugin.pm)
BuildRequires:	perl(ExtUtils/MakeMaker.pm)
BuildRequires:	perl(ExtUtils/MakeMaker.pm)
BuildRequires:  perl(JSON/PP.pm)
BuildRequires:  perl(Path/Tiny.pm)
BuildRequires:	perl(Test2/V0.pm)
BuildRequires:  perl(URI.pm)
BuildRequires:  perl(URI/Escape.pm)

BuildRequires:  perl(Test2/V0.pm)
Source44: import.info

%description
This plugin is designed for downloading assets from a GitLab instance.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}


%build
/usr/bin/perl Makefile.PL INSTALLDIRS=vendor

%make_build

%check
%__make test

%install
%makeinstall_std

%files
%doc Changes META.json META.yml README
%doc --no-dereference LICENSE
%{perl_vendor_privlib}/*


%changelog
* Fri Sep 30 2022 Igor Vlasenko <viy@altlinux.org> 0.01-alt1_2
- update by mgaimport

* Thu Sep 29 2022 Igor Vlasenko <viy@altlinux.org> 0.01-alt1_1
- new version

