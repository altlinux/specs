%define _unpackaged_files_terminate_build 1
%define module_name Inline-C
# BEGIN SourceDeps(oneline):
BuildRequires: perl(Config.pm) perl(Exporter.pm) perl(ExtUtils/MakeMaker.pm) perl(File/Copy/Recursive.pm) perl(File/Path.pm) perl(File/ShareDir/Install.pm) perl(File/Spec.pm) perl(FindBin.pm) perl(IO/All.pm) perl(IPC/Cmd.pm) perl(Inline.pm) perl(Inline/MakeMaker.pm) perl(Parse/RecDescent.pm) perl(Pegex.pm) perl(Pegex/Base.pm) perl(Pegex/Parser.pm) perl(Test/More.pm) perl(Test/Pod.pm) perl(Test/Warn.pm) perl(YAML/XS.pm) perl(autodie.pm) perl(base.pm) perl(diagnostics.pm) perl(if.pm) perl(version.pm)
# END SourceDeps(oneline)
BuildRequires: rpm-build-perl perl-devel perl-podlators

Name: perl-%module_name
Version: 0.82
Release: alt1
Summary: C Language Support for Inline
Group: Development/Perl
License: perl
URL: https://github.com/ingydotnet/inline-c-pm

Source0: http://www.cpan.org/authors/id/E/ET/ETJ/%{module_name}-%{version}.tar.gz
BuildArch: noarch

%description
From summary: %summary

%prep
%setup -q -n %{module_name}-%{version}

%ifarch %ix86
if [ %version = "0.82" ]; then
rm -f t/26fork.t
fi
%endif

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc README Changes example CONTRIBUTING
%perl_vendor_privlib/I*
%perl_vendor_privlib/auto/*

%changelog
* Fri Mar 25 2022 Igor Vlasenko <viy@altlinux.org> 0.82-alt1
- automated CPAN update

* Sun May 12 2019 Igor Vlasenko <viy@altlinux.ru> 0.81-alt1
- automated CPAN update

* Tue Apr 23 2019 Igor Vlasenko <viy@altlinux.ru> 0.80-alt1
- automated CPAN update

* Wed Aug 02 2017 Igor Vlasenko <viy@altlinux.ru> 0.78-alt1
- automated CPAN update

* Tue Dec 08 2015 Igor Vlasenko <viy@altlinux.ru> 0.76-alt1.1
- to Sisyphus

* Mon Nov 30 2015 Igor Vlasenko <viy@altlinux.ru> 0.76-alt1
- new version

* Sat Dec 13 2014 Cronbuild Service <cronbuild@altlinux.org> 0.64-alt2
- rebuild to get rid of unmets

* Wed Oct 15 2014 Igor Vlasenko <viy@altlinux.ru> 0.64-alt1
- initial import by package builder

