Group: Development/Perl
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-perl
BuildRequires: perl(ExtUtils/MakeMaker.pm) perl-Module-Build perl-devel perl-podlators
# END SourceDeps(oneline)
%global pkgname HTML-Entities-Interpolate

Name:           perl-HTML-Entities-Interpolate
Version:        1.05
Release:        alt1_2
Summary:        Call HTML::Entities::encode_entities via a hash within a string
License:        Artistic 2.0
URL:            http://search.cpan.org/dist/HTML-Entities-Interpolate/
Source0:        http://www.cpan.org/authors/id/R/RS/RSAVAGE/%{pkgname}-%{version}.tgz
BuildArch:      noarch
BuildRequires:  perl(HTML/Entities.pm)
BuildRequires:  perl(Module/Build.pm)
BuildRequires:  perl(Test/More.pm)
BuildRequires:  perl(Test/Pod.pm)
BuildRequires:  perl(Tie/Function.pm)
Source44: import.info

%description
This is a pure perl module which calls HTML::Entities::encode_entities 
via a hash within a string.

%prep
%setup -qn %{pkgname}-%{version}

%build
%{__perl} Build.PL --install_path bindoc=%_man1dir installdirs=vendor
./Build

%install
./Build install destdir=%{buildroot} create_packlist=0
# %{_fixperms} %{buildroot}/*

%check
./Build test

%files
%doc Changes README
%{perl_vendor_privlib}/*

%changelog
* Wed Feb 19 2014 Igor Vlasenko <viy@altlinux.ru> 1.05-alt1_2
- moved to Sisyphus for Slic3r (by dd@ request)

* Mon Sep 23 2013 Igor Vlasenko <viy@altlinux.ru> 1.05-alt1
- initial import by package builder

