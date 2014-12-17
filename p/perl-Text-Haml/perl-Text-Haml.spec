# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-perl
BuildRequires: perl(CPAN/Meta.pm) perl(CPAN/Meta/Prereqs.pm) perl(Digest/MD5.pm) perl(File/Path.pm) perl(Module/Build.pm) perl(Test/More.pm) perl-Module-Build perl-devel perl-podlators
# END SourceDeps(oneline)
%define upstream_name    Text-Haml
%define upstream_version 0.990116

Name:       perl-%{upstream_name}
Version:    %{upstream_version}
Release:    alt1_4

Summary:    Haml Perl implementation
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/Text/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(Carp.pm)
BuildRequires: perl(Data/Section/Simple.pm)
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
%{__perl} Build.PL --install_path bindoc=%_man1dir --installdirs=vendor
./Build

%check
./Build test

%install
./Build install --destdir=%buildroot
rm -f %{buildroot}/%{perl_vendor_privlib}/Text/README.pod

%files
%doc META.json META.yml 
%{perl_vendor_privlib}/*


%changelog
* Wed Dec 17 2014 Igor Vlasenko <viy@altlinux.ru> 0.990116-alt1_4
- update by mgaimport

* Tue Oct 07 2014 Igor Vlasenko <viy@altlinux.ru> 0.990116-alt1_2
- update by mgaimport

* Thu May 01 2014 Igor Vlasenko <viy@altlinux.ru> 0.990116-alt1_1
- update by mgaimport

* Thu Feb 20 2014 Igor Vlasenko <viy@altlinux.ru> 0.990115-alt1_1
- update by mgaimport

* Fri Oct 25 2013 Igor Vlasenko <viy@altlinux.ru> 0.990111-alt1
- automated CPAN update

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

