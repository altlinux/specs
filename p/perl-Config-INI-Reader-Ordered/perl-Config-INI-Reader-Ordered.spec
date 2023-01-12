%define _unpackaged_files_terminate_build 1
%define module_name Config-INI-Reader-Ordered
# BEGIN SourceDeps(oneline):
BuildRequires: perl(CPAN.pm) perl(Config.pm) perl(Config/INI/Reader.pm) perl(Cwd.pm) perl(ExtUtils/MM_Unix.pm) perl(ExtUtils/MakeMaker.pm) perl(ExtUtils/Manifest.pm) perl(File/Basename.pm) perl(File/Find.pm) perl(FileHandle.pm) perl(LWP/Simple.pm) perl(Module/Build.pm) perl(Net/FTP.pm) perl(Socket.pm) perl(Test/More.pm) perl(YAML/Tiny.pm) perl(inc/Module/Install.pm)
# END SourceDeps(oneline)
BuildRequires: rpm-build-perl perl-devel perl-podlators

Name: perl-%module_name
Version: 0.022
Release: alt1
Summary: - .ini-file parser that returns sections in order
Group: Development/Perl
License: perl
Url: %CPAN %module_name

Source0: http://www.cpan.org/authors/id/R/RJ/RJBS/%{module_name}-%{version}.tar.gz
BuildArch: noarch

%description
Config::INI::Reader::Ordered is a subclass of the Config::INI::Reader manpage which
preserves section order.  See the Config::INI::Reader manpage for all documentation; the
only difference is as presented in the the SYNOPSIS entry elsewhere in this document.


%prep
%setup -q -n %{module_name}-%{version}

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README
%perl_vendor_privlib/C*

%changelog
* Thu Jan 12 2023 Igor Vlasenko <viy@altlinux.org> 0.022-alt1
- automated CPAN update

* Thu Jul 01 2021 Igor Vlasenko <viy@altlinux.org> 0.021-alt1
- automated CPAN update

* Sun Oct 11 2015 Igor Vlasenko <viy@altlinux.ru> 0.020-alt1
- automated CPAN update

* Wed Dec 04 2013 Igor Vlasenko <viy@altlinux.ru> 0.011-alt2
- uploaded to Sisyphus as Scalar-Does dependency

* Tue Sep 03 2013 Igor Vlasenko <viy@altlinux.ru> 0.011-alt1
- initial import by package builder

