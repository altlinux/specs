%define module_version 1.005001
%define module_name DBIx-Class-QueryLog
# BEGIN SourceDeps(oneline):
BuildRequires: perl(DBIx/Class.pm) perl(DBIx/Class/Storage/Statistics.pm) perl(ExtUtils/MakeMaker.pm) perl(Moo.pm) perl(Test/More.pm) perl(Test/Pod.pm) perl(Time/HiRes.pm) perl(Types/Standard.pm) perl(base.pm)
# END SourceDeps(oneline)
%define _unpackaged_files_terminate_build 1
BuildRequires: rpm-build-perl perl-devel perl-podlators

Name: perl-%module_name
Version: 1.005001
Release: alt2
Summary: Log queries for later analysis.
Group: Development/Perl
License: perl
URL: https://github.com/frioux/DBIx-Class-QueryLog

Source0: http://cpan.org.ua/authors/id/F/FR/FREW/%{module_name}-%{module_version}.tar.gz
BuildArch: noarch

%description
DBIx::Class::QueryLog 'logs' each transaction and query executed so you can
analyze what happened in the 'session'.  It must be installed as the debugobj
in DBIx::Class:

    use DBIx::Class::QueryLog;
    use DBIx::Class::QueryLog::Analyzer;
    
    my $schema = ... # Get your schema!
    my $ql = DBIx::Class::QueryLog->new;
    $schema->storage->debugobj($ql);
    $schema->storage->debug(1);
      ... # do some stuff!
    my $ana = DBIx::Class::QueryLog::Analyzer->new({ querylog => $ql });
    my @queries = $ana->get_sorted_queries;

Every transaction and query executed will have a corresponding Transaction
and Query object stored in order of execution, like so:

    Query
    Query
    Transaction
    Query

This array can be retrieved with the log method.  Queries executed inside
a transaction are stored inside their Transaction object, not inside the
QueryLog directly.

See the DBIx::Class::QueryLog::Analyzer manpage for options on digesting the results
of a QueryLog session.

If you wish to have the QueryLog collecting results, and the normal trace
output of SQL queries from DBIx::Class, then set `passthrough' to 1

  $ql->passthrough(1);


%prep
%setup -q -n %{module_name}-%{module_version}

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc README Changes LICENSE
%perl_vendor_privlib/D*

%changelog
* Mon Mar 21 2016 Igor Vlasenko <viy@altlinux.ru> 1.005001-alt2
- to Sisyphus

* Tue Dec 15 2015 Igor Vlasenko <viy@altlinux.ru> 1.005001-alt1
- regenerated from template by package builder

* Tue Dec 01 2015 Igor Vlasenko <viy@altlinux.ru> 1.004001-alt1
- regenerated from template by package builder

* Sat Nov 14 2015 Igor Vlasenko <viy@altlinux.ru> 1.004000-alt1
- regenerated from template by package builder

* Thu Sep 19 2013 Igor Vlasenko <viy@altlinux.ru> 1.3.3-alt1
- initial import by package builder

