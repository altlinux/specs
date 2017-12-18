%define _unpackaged_files_terminate_build 1
%define module_name Iterator-Simple
# BEGIN SourceDeps(oneline):
BuildRequires: perl(CPAN.pm) perl(Config.pm) perl(Cwd.pm) perl(Exporter.pm) perl(ExtUtils/MM_Unix.pm) perl(ExtUtils/MakeMaker.pm) perl(ExtUtils/Manifest.pm) perl(File/Basename.pm) perl(File/Find.pm) perl(FileHandle.pm) perl(IO/Handle.pm) perl(LWP/Simple.pm) perl(Module/Build.pm) perl(Net/FTP.pm) perl(Scalar/Util.pm) perl(Socket.pm) perl(Test/More.pm) perl(YAML.pm) perl(base.pm) perl(inc/Module/Install.pm) perl(overload.pm)
# END SourceDeps(oneline)
BuildRequires: rpm-build-perl perl-devel perl-podlators

Name: perl-%module_name
Version: 0.07
Release: alt1
Summary: Simple iterator and utilities
Group: Development/Perl
License: perl
Url: %CPAN %module_name

Source0: http://www.cpan.org/authors/id/M/MI/MICHAEL/%{module_name}-%{version}.tar.gz
BuildArch: noarch

%description
Iterator::Simple is yet another general-purpose iterator utilities.

Rather simple, but powerful and fast iterator.


%prep
%setup -q -n %{module_name}-%{version}

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README
%perl_vendor_privlib/I*

%changelog
* Mon Dec 18 2017 Igor Vlasenko <viy@altlinux.ru> 0.07-alt1
- automated CPAN update

* Thu Nov 14 2013 Igor Vlasenko <viy@altlinux.ru> 0.06-alt2
- moved to Sisyphus (for Catalyst-Runtime update)

* Fri Sep 06 2013 Igor Vlasenko <viy@altlinux.ru> 0.06-alt1
- initial import by package builder

