%define module_version 0.16
%define module_name Log-Minimal
# BEGIN SourceDeps(oneline):
BuildRequires: perl(CPAN/Meta.pm) perl(CPAN/Meta/Prereqs.pm) perl(Data/Dumper.pm) perl(Exporter.pm) perl(Module/Build.pm) perl(Scalar/Util.pm) perl(Term/ANSIColor.pm) perl(Test/More.pm) perl(base.pm) perl(overload.pm)
# END SourceDeps(oneline)
%define _unpackaged_files_terminate_build 1
BuildRequires: rpm-build-perl perl-devel perl-podlators

Name: perl-%module_name
Version: 0.16
Release: alt2
Summary: Minimal but customizable logger.
Group: Development/Perl
License: perl
URL: https://github.com/kazeburo/Log-Minimal

Source0: http://cpan.org.ua/authors/id/K/KA/KAZEBURO/%module_name-%module_version.tar.gz
BuildArch: noarch

%description
%summary

%prep
%setup -n %module_name-%module_version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc README.md Changes LICENSE
%perl_vendor_privlib/L*

%changelog
* Tue Oct 15 2013 Igor Vlasenko <viy@altlinux.ru> 0.16-alt2
- Sisyphus build

* Wed Sep 04 2013 Igor Vlasenko <viy@altlinux.ru> 0.16-alt1
- initial import by package builder

