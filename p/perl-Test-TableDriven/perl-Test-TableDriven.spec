%define module_version 0.02
%define module_name Test-TableDriven
# BEGIN SourceDeps(oneline):
BuildRequires: perl(CPAN.pm) perl(Config.pm) perl(Cwd.pm) perl(Data/Dumper.pm) perl(ExtUtils/MM_Unix.pm) perl(ExtUtils/MakeMaker.pm) perl(ExtUtils/Manifest.pm) perl(File/Basename.pm) perl(File/Find.pm) perl(FileHandle.pm) perl(LWP/Simple.pm) perl(Module/Build.pm) perl(Net/FTP.pm) perl(Socket.pm) perl(Test/More.pm) perl(YAML.pm) perl(inc/Module/Install.pm)
# END SourceDeps(oneline)
%define _unpackaged_files_terminate_build 1
BuildRequires: rpm-build-perl perl-devel perl-podlators

Name: perl-%module_name
Version: 0.02
Release: alt2
Summary: write tests, not scripts that run them
Group: Development/Perl
License: perl
Url: %CPAN %module_name

Source0: http://cpan.org.ua/authors/id/J/JR/JROCKWAY/%module_name-%module_version.tar.gz
BuildArch: noarch

%description
Writing table-driven tests is usually a good idea.  Adding a test case
doesn't require adding code, so it's easy to avoid fucking up the
other tests.  However, actually going from a table of tests to a test
that runs is non-trivial.

`Test::TableDriven' makes writing the test drivers trivial.  You
simply define your test cases and write a function that turns the
input data into output data to compare against.  `Test::TableDriven'
will compute how many tests need to be run, and then run the tests.

Concentrate on your data and what you're testing, not `plan tests ='
scalar keys %%test_cases> and a big foreach loop.


%prep
%setup -n %module_name-%module_version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README
%perl_vendor_privlib/T*

%changelog
* Thu Oct 17 2013 Igor Vlasenko <viy@altlinux.ru> 0.02-alt2
- regenerated from template by package builder

* Tue Sep 03 2013 Igor Vlasenko <viy@altlinux.ru> 0.02-alt1
- initial import by package builder

