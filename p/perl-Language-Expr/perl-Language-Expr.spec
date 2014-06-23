# BEGIN SourceDeps(oneline):
BuildRequires: perl(Data/Clone.pm) perl(Data/Rmap.pm) perl(Exporter.pm) perl(ExtUtils/MakeMaker.pm) perl(List/MoreUtils.pm) perl(List/Util.pm) perl(Moo.pm) perl(Moo/Role.pm) perl(Pod/Coverage/TrustPod.pm) perl(Regexp/Grammars.pm) perl(Test/Exception.pm) perl(Test/More.pm) perl(Test/Pod.pm) perl(Test/Pod/Coverage.pm) perl(UUID/Tiny.pm) perl(boolean.pm) perl(experimental.pm)
# END SourceDeps(oneline)
%define module_version 0.23
%define module_name Language-Expr
%define _unpackaged_files_terminate_build 1
BuildRequires: rpm-build-perl perl-devel perl-podlators

Name: perl-%module_name
Version: 0.23
Release: alt1
Summary: Simple minilanguage for use in expression
Group: Development/Perl
License: perl
URL: https://metacpan.org/release/Language-Expr

Source0: http://cpan.org.ua/authors/id/S/SH/SHARYANTO/%{module_name}-%{module_version}.tar.gz
BuildArch: noarch

%description
From summary: %summary

%prep
%setup -n %{module_name}-%{module_version}

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README LICENSE
%perl_vendor_privlib/L*

%changelog
* Mon Jun 23 2014 Igor Vlasenko <viy@altlinux.ru> 0.23-alt1
- regenerated from template by package builder

* Thu Feb 20 2014 Igor Vlasenko <viy@altlinux.ru> 0.19-alt2_4
- moved to Sisyphus for Slic3r (by dd@ request)

* Wed May 01 2013 Igor Vlasenko <viy@altlinux.ru> 0.19-alt1_4
- initial fc import

