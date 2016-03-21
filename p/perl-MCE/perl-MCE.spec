%define _unpackaged_files_terminate_build 1
%define module_version 1.703
%define module_name MCE
%define __spec_autodep_custom_pre export PERL5OPT='-I%buildroot%perl_vendor_privlib -MMCE::Util'
%add_findreq_skiplist %perl_vendor_privlib/MCE/Core/Input*
%add_findreq_skiplist %perl_vendor_privlib/MCE/Core/Manager*
%add_findreq_skiplist %perl_vendor_privlib/MCE/Core/Validation*
%add_findreq_skiplist %perl_vendor_privlib/MCE/Core/Worker*
# BEGIN SourceDeps(oneline):
BuildRequires: perl(Carp.pm) perl(DBD/SQLite.pm) perl(DBI.pm) perl(Exporter.pm) perl(ExtUtils/MakeMaker.pm) perl(Fcntl.pm) perl(File/Path.pm) perl(Getopt/Long.pm) perl(IO/Handle.pm) perl(IPC/Open2.pm) perl(Inline.pm) perl(Net/Ping.pm) perl(Scalar/Util.pm) perl(Socket.pm) perl(Storable.pm) perl(Symbol.pm) perl(Sys/Mmap.pm) perl(Test/More.pm) perl(Thread/Queue.pm) perl(Time/HiRes.pm) perl(base.pm) perl(bytes.pm) perl(constant.pm) perl(open.pm) perl(threads.pm) perl(threads/shared.pm)
# END SourceDeps(oneline)
BuildRequires: rpm-build-perl perl-devel perl-podlators

Name: perl-%module_name
Version: 1.703
Release: alt1
Summary: Many-Core Engine for Perl. Provides parallel processing capabilities.
Group: Development/Perl
License: perl
URL: http://code.google.com/p/many-core-engine-perl/

Source: http://www.cpan.org/authors/id/M/MA/MARIOROY/MCE-%{version}.tar.gz
BuildArch: noarch

%description
%summary

%package scripts
Summary: %module_name scripts
Group: Development/Perl
Requires: %name = %{?epoch:%epoch:}%version-%release

%description scripts
scripts for %module_name

%prep
%setup -n %{module_name}-%{module_version}

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc README* Changes
%perl_vendor_privlib/M*

#%files scripts
#%_bindir/*

%changelog
* Mon Mar 21 2016 Igor Vlasenko <viy@altlinux.ru> 1.703-alt1
- automated CPAN update

* Wed Oct 14 2015 Igor Vlasenko <viy@altlinux.ru> 1.608-alt1
- regenerated from template by package builder

* Wed Sep 04 2013 Igor Vlasenko <viy@altlinux.ru> 1.415-alt1
- initial import by package builder

