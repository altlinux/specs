%define _unpackaged_files_terminate_build 1
%define module_name HTTP-Entity-Parser
# BEGIN SourceDeps(oneline):
BuildRequires: perl(Cwd.pm) perl(Encode.pm) perl(Encode/CN.pm) perl(Encode/JP.pm) perl(Encode/KR.pm) perl(Encode/TW.pm) perl(File/Spec/Functions.pm) perl(File/Temp.pm) perl(HTTP/Body.pm) perl(HTTP/Message.pm) perl(HTTP/MultiPartParser.pm) perl(Hash/MultiValue.pm) perl(JSON/MaybeXS.pm) perl(Module/Build/Tiny.pm) perl(Module/Load.pm) perl(Stream/Buffered.pm) perl(Test/More.pm) perl(WWW/Form/UrlEncoded.pm)
# END SourceDeps(oneline)
BuildRequires: rpm-build-perl perl-devel perl-podlators

Name: perl-%module_name
Version: 0.19
Release: alt1
Summary: PSGI compliant HTTP Entity Parser
Group: Development/Perl
License: perl
URL: https://github.com/kazeburo/HTTP-Entity-Parser

Source0: http://www.cpan.org/authors/id/K/KA/KAZEBURO/%{module_name}-%{version}.tar.gz
BuildArch: noarch

%description
From summary: %summary

%prep
%setup -q -n %{module_name}-%{version}

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes LICENSE README.md
%perl_vendor_privlib/H*

%changelog
* Tue Feb 14 2017 Igor Vlasenko <viy@altlinux.ru> 0.19-alt1
- automated CPAN update

* Fri Nov 18 2016 Igor Vlasenko <viy@altlinux.ru> 0.18-alt2
- to Sisyphus

* Wed Oct 12 2016 Igor Vlasenko <viy@altlinux.ru> 0.18-alt1
- regenerated from template by package builder

* Thu Nov 19 2015 Igor Vlasenko <viy@altlinux.ru> 0.17-alt1
- regenerated from template by package builder

* Mon May 26 2014 Igor Vlasenko <viy@altlinux.ru> 0.12-alt1
- initial import by package builder

