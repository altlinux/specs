%define _unpackaged_files_terminate_build 1
# BEGIN SourceDeps(oneline):
BuildRequires: perl(CPAN.pm) perl(Carp.pm) perl(Class/Data/Inheritable.pm) perl(Config.pm) perl(Cwd.pm) perl(DateTime/Format/Natural.pm) perl(DateTime/Locale.pm) perl(ExtUtils/MM_Unix.pm) perl(ExtUtils/MakeMaker.pm) perl(ExtUtils/Manifest.pm) perl(File/Basename.pm) perl(File/Find.pm) perl(File/Spec.pm) perl(FileHandle.pm) perl(JSON.pm) perl(LWP/Simple.pm) perl(List/Util.pm) perl(Module/Build.pm) perl(Net/FTP.pm) perl(Parse/CPAN/Meta.pm) perl(Socket.pm) perl(Test/MockTime.pm) perl(Test/MockTime/HiRes.pm) perl(Test/More.pm) perl(YAML/Tiny.pm) perl(inc/Module/Install.pm) perl(parent.pm)
# END SourceDeps(oneline)
%define module_name Date-Extract
BuildRequires: rpm-build-perl perl-devel perl-podlators

Name: perl-%module_name
Version: 0.07
Release: alt1
Summary: extract probable dates from strings
Group: Development/Perl
License: perl
Url: %CPAN %module_name

Source0: http://www.cpan.org/authors/id/E/ET/ETHER/%{module_name}-%{version}.tar.gz
BuildArch: noarch

%description
my $parser = Date::Extract->new();
    my $dt = $parser->extract($arbitrary_text)
        or die "No date found.";
    return $dt->ymd;


%prep
%setup -q -n %{module_name}-%{version}

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc README Changes CONTRIBUTING
%perl_vendor_privlib/D*

%changelog
* Thu Jan 19 2023 Igor Vlasenko <viy@altlinux.org> 0.07-alt1
- automated CPAN update

* Tue Jun 08 2021 Igor Vlasenko <viy@altlinux.org> 0.06-alt2
- fixed build

* Thu Nov 17 2016 Igor Vlasenko <viy@altlinux.ru> 0.06-alt1
- automated CPAN update

* Tue Jun 10 2014 Igor Vlasenko <viy@altlinux.ru> 0.05-alt1
- automated CPAN update

* Sat Mar 29 2014 Igor Vlasenko <viy@altlinux.ru> 0.04-alt2
- moved to Sisyphus by lav@ request

* Thu Sep 19 2013 Igor Vlasenko <viy@altlinux.ru> 0.04-alt1
- initial import by package builder

