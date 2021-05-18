%define module_name YAML-PP-LibYAML
# BEGIN SourceDeps(oneline):
BuildRequires: perl(Exporter.pm) perl(ExtUtils/MakeMaker.pm) perl(File/Spec.pm) perl(FindBin.pm) perl(IO/Handle.pm) perl(IPC/Open3.pm) perl(Scalar/Util.pm) perl(Test/More.pm) perl(YAML/LibYAML/API.pm) perl(YAML/LibYAML/API/XS.pm) perl(YAML/PP.pm) perl(YAML/PP/Common.pm) perl(YAML/PP/Emitter.pm) perl(YAML/PP/Parser.pm) perl(YAML/PP/Reader.pm) perl(YAML/PP/Writer.pm) perl(base.pm) perl(strict.pm) perl(warnings.pm)
# END SourceDeps(oneline)
%define _unpackaged_files_terminate_build 1
BuildRequires: rpm-build-perl perl-devel perl-podlators

Name: perl-%module_name
Version: 0.005
Release: alt2
Summary: Faster backend for YAML::PP
Group: Development/Perl
License: perl
Url: %CPAN %module_name

Source0: http://mirror.yandex.ru/mirrors/cpan/authors/id/T/TI/TINITA/%{module_name}-%{version}.tar.gz
BuildArch: noarch

%description
the YAML::PP::LibYAML manpage is a subclass of the YAML::PP manpage. Instead of using
the YAML::PP::Parser manpage as a the backend parser, it uses
the YAML::PP::LibYAML::Parser manpage which calls the YAML::LibYAML::API manpage, an XS wrapper
around the `C libyaml'.

%prep
%setup -q -n %{module_name}-%{version}

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes LICENSE README README.md
%perl_vendor_privlib/Y*

%changelog
* Tue May 18 2021 Igor Vlasenko <viy@altlinux.org> 0.005-alt2
- to Sisyphus as YAML-PP dep

* Wed Oct 07 2020 Igor Vlasenko <viy@altlinux.ru> 0.005-alt1
- updated by package builder

* Thu Sep 10 2020 Igor Vlasenko <viy@altlinux.ru> 0.004-alt1
- updated by package builder

* Sat Jun 01 2019 Igor Vlasenko <viy@altlinux.ru> 0.003-alt1
- updated by package builder

* Mon Oct 08 2018 Igor Vlasenko <viy@altlinux.ru> 0.002-alt1
- initial import by package builder

