%define _unpackaged_files_terminate_build 1
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-perl
BuildRequires: perl(File/Path.pm) perl(Test/More.pm) perl-devel perl-podlators perl(Data/Section/Simple.pm)
# END SourceDeps(oneline)
%define upstream_name    Text-Haml
%define upstream_version 0.990110

Name:       perl-%{upstream_name}
Version:    0.990110
Release:    alt1

Summary:    Haml Perl implementation
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source:    http://www.cpan.org/authors/id/V/VT/VTI/Text-Haml-%{version}.tar.gz

BuildRequires: perl(Carp.pm)
BuildRequires: perl(Encode.pm)
BuildRequires: perl(ExtUtils/MakeMaker.pm)
BuildRequires: perl(File/Basename.pm)
BuildRequires: perl(File/Spec.pm)
BuildRequires: perl(IO/File.pm)
BuildRequires: perl(Scalar/Util.pm)
BuildRequires: perl(URI/Escape.pm)
BuildArch:  noarch
Source44: import.info

%description
the Text::Haml manpage implements Haml the
http://haml-lang.com/docs/yardoc/file.HAML_REFERENCE.html manpage
specification.

the Text::Haml manpage passes specification tests written by Norman Clarke
http://github.com/norman/haml-spec and supports only cross-language Haml
features. Do not expect Ruby specific things to work.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLMAN1DIR=%_man1dir INSTALLDIRS=vendor

%make

%check
%make test

%install
%makeinstall_std

%files
%doc META.json META.yml 
%perl_vendor_privlib/*

%changelog
* Tue Oct 22 2013 Igor Vlasenko <viy@altlinux.ru> 0.990110-alt1
- automated CPAN update

* Mon Oct 21 2013 Igor Vlasenko <viy@altlinux.ru> 0.990109-alt1_2
- update by mgaimport

* Wed Sep 11 2013 Igor Vlasenko <viy@altlinux.ru> 0.990109-alt1_1
- update by mgaimport

* Mon Aug 12 2013 Igor Vlasenko <viy@altlinux.ru> 0.990109-alt1
- automated CPAN update

* Tue Aug 06 2013 Igor Vlasenko <viy@altlinux.ru> 0.990108-alt1_1
- build for Sisyphus

* Thu Jul 25 2013 Igor Vlasenko <viy@altlinux.ru> 0.990107-alt1_1
- converted for ALT Linux by srpmconvert tools

