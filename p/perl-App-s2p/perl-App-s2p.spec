%define _unpackaged_files_terminate_build 1
Conflicts: perl-devel < 5.22
# BEGIN SourceDeps(oneline):
BuildRequires: perl(Devel/FindPerl.pm) perl(ExtUtils/MakeMaker.pm) perl(File/Copy.pm) perl(File/Spec.pm) perl(IO/Handle.pm) perl(IPC/Open2.pm) perl(IPC/Open3.pm) perl(Symbol.pm) perl(Test/More.pm) perl(integer.pm) perl(strict.pm) perl(vars.pm) perl(warnings.pm)
# END SourceDeps(oneline)
%define module_name App-s2p
BuildRequires: rpm-build-perl perl-devel perl-podlators

Name: perl-%module_name
Version: 1.003
Release: alt1
Summary: a stream editor
Group: Development/Perl
License: open_source
Url: %CPAN %module_name

Source0: http://www.cpan.org/authors/id/L/LE/LEONT/%{module_name}-%{version}.tar.gz
BuildArch: noarch

%description
From summary: %summary

%prep
%setup -q -n %{module_name}-%{version}

%build
%perl_vendor_build

%install
%perl_vendor_install
ln -snf s2p %buildroot%_bindir/psed

%files
%doc Changes README
%_bindir/*
%_man1dir/*
%_bindir/psed

%changelog
* Tue Nov 19 2019 Igor Vlasenko <viy@altlinux.ru> 1.003-alt1
- automated CPAN update

* Thu Nov 19 2015 Igor Vlasenko <viy@altlinux.ru> 1.002-alt1
- new version

