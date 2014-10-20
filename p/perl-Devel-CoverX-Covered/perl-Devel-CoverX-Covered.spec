# BEGIN SourceDeps(oneline):
BuildRequires: perl(DBD/SQLite.pm) perl(DBIx/Simple.pm) perl(Devel/Cover/DB.pm) perl(ExtUtils/MakeMaker.pm) perl(File/chdir.pm) perl(Memoize.pm) perl(Moose.pm) perl(Path/Class.pm) perl(Pod/Usage.pm) perl(Test/Differences.pm) perl(Test/Exception.pm) perl(Test/More.pm)
# END SourceDeps(oneline)
%define module_version 0.016
%define module_name Devel-CoverX-Covered
%define _unpackaged_files_terminate_build 1
BuildRequires: rpm-build-perl perl-devel perl-podlators

Name: perl-%module_name
Version: 0.016
Release: alt1
Summary: Collect and report caller (test file) and
Group: Development/Perl
License: perl
Url: %CPAN %module_name

Source: http://www.cpan.org/authors/id/J/JO/JOHANL/Devel-CoverX-Covered-%{version}.tar.gz
BuildArch: noarch

%description
%summary

%package scripts
Summary: %module_name scripts
Group: Development/Perl
Requires: %{?epoch:%epoch:}%name = %version-%release

%description scripts
scripts for %module_name

%prep
%setup -n %module_name-%module_version

%build
%perl_vendor_build INSTALLMAN1DIR=%_man1dir

%install
%perl_vendor_install

%files
%doc Changes README LICENSE
%perl_vendor_privlib/D*

%files scripts
%_bindir/*
%_man1dir/*

%changelog
* Mon Oct 20 2014 Igor Vlasenko <viy@altlinux.ru> 0.016-alt1
- automated CPAN update

* Tue Feb 18 2014 Igor Vlasenko <viy@altlinux.ru> 0.015-alt2
- moved to Sisyphus for Slic3r (by dd@ request)

* Thu Sep 26 2013 Igor Vlasenko <viy@altlinux.ru> 0.015-alt1
- initial import by package builder

