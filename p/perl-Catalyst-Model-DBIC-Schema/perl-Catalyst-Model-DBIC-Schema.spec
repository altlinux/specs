%define _unpackaged_files_terminate_build 1
%add_findreq_skiplist %perl_vendor_privlib/Catalyst/TraitFor/Model/DBIC/Schema/*
# BEGIN SourceDeps(oneline):
BuildRequires: perl(CPAN.pm) perl(Carp.pm) perl(Carp/Clan.pm) perl(Catalyst.pm) perl(Catalyst/Component/InstancePerContext.pm) perl(Catalyst/Devel.pm) perl(Catalyst/Runtime.pm) perl(CatalystX/Component/Traits.pm) perl(Class/C3.pm) perl(Config.pm) perl(Cwd.pm) perl(DBD/Pg.pm) perl(DBD/SQLite.pm) perl(DBD/mysql.pm) perl(DBI.pm) perl(DBIx/Class.pm) perl(DBIx/Class/Core.pm) perl(DBIx/Class/Cursor/Cached.pm) perl(DBIx/Class/ResultSet.pm) perl(DBIx/Class/Schema.pm) perl(DBIx/Class/Schema/Loader.pm) perl(ExtUtils/MM_Unix.pm) perl(ExtUtils/MakeMaker.pm) perl(ExtUtils/Manifest.pm) perl(Fcntl.pm) perl(File/Basename.pm) perl(File/Find.pm) perl(File/Spec.pm) perl(File/Spec/Functions.pm) perl(File/Temp.pm) perl(FileHandle.pm) perl(FindBin.pm) perl(Hash/Merge.pm) perl(IPC/Open3.pm) perl(JSON.pm) perl(LWP/Simple.pm) perl(List/MoreUtils.pm) perl(List/Util.pm) perl(Module/Build.pm) perl(Module/Runtime.pm) perl(Moose.pm) perl(Moose/Role.pm) perl(MooseX/ClassAttribute.pm) perl(MooseX/NonMoose.pm) perl(MooseX/Types.pm) perl(MooseX/Types/LoadableClass.pm) perl(MooseX/Types/Moose.pm) perl(Net/FTP.pm) perl(Parse/CPAN/Meta.pm) perl(Scalar/Util.pm) perl(Socket.pm) perl(Storable.pm) perl(Test/Exception.pm) perl(Test/More.pm) perl(Test/Requires.pm) perl(Tie/IxHash.pm) perl(Try/Tiny.pm) perl(YAML/Tiny.pm) perl(base.pm) perl(inc/Module/Install.pm) perl(lib.pm) perl(mro.pm) perl(namespace/autoclean.pm) perl(namespace/clean.pm) perl-devel
# END SourceDeps(oneline)
%define module_name Catalyst-Model-DBIC-Schema
%define dist Catalyst-Model-DBIC-Schema
Name: perl-%dist
Version: 0.66
Release: alt1

Summary: DBIx::Class::Schema Model Class
License: perl
Group: Development/Perl

URL: %CPAN %dist
Source0: http://www.cpan.org/authors/id/H/HA/HAARG/%{module_name}-%{version}.tar.gz

BuildArch: noarch

# Automatically added by buildreq on Tue Nov 15 2011
BuildRequires: perl-Catalyst-Component-InstancePerContext perl-Catalyst-Devel perl-CatalystX-Component-Traits perl-Class-C3 perl-DBD-SQLite perl-DBIx-Class-Schema-Loader perl-SQL-Abstract perl-Test-Exception perl-Test-Pod perl-Test-Requires perl-Tie-IxHash perl(MooseX/MarkAsMethods.pm)

%description
This is a Catalyst Model for DBIx::Class::Schema-based Models.  See the
documentation for Catalyst::Helper::Model::DBIC::Schema for information
on generating these Models via Helper scripts.

%prep
%setup -q -n %{module_name}-%{version}

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README
%perl_vendor_privlib/Catalyst

%changelog
* Sun Jul 30 2023 Igor Vlasenko <viy@altlinux.org> 0.66-alt1
- automated CPAN update

* Mon Oct 27 2014 Igor Vlasenko <viy@altlinux.ru> 0.65-alt1
- automated CPAN update

* Tue May 13 2014 Igor Vlasenko <viy@altlinux.ru> 0.63-alt1
- automated CPAN update

* Thu Mar 06 2014 Igor Vlasenko <viy@altlinux.ru> 0.62-alt1
- uploaded to Sisyphus as dependency

* Wed Jul 24 2013 Igor Vlasenko <viy@altlinux.ru> 0.61-alt1
- automated CPAN update

* Tue Sep 25 2012 Igor Vlasenko <viy@altlinux.ru> 0.60-alt1
- automated CPAN update

* Tue Nov 15 2011 Alexey Tourbin <at@altlinux.ru> 0.59-alt1
- 0.55 -> 0.59

* Thu Sep 29 2011 Igor Vlasenko <viy@altlinux.ru> 0.55-alt1
- automated CPAN update

* Mon Nov 22 2010 Igor Vlasenko <viy@altlinux.ru> 0.41-alt1.1
- repair after perl 5.12 upgrade using girar-nmu

* Tue Jul 13 2010 Igor Vlasenko <viy@altlinux.ru> 0.41-alt1
- automated CPAN update

* Wed Apr 21 2010 Alexey Tourbin <at@altlinux.ru> 0.40-alt2
- rebuilt with rpm-build-perl 0.72

* Tue Apr 20 2010 Alexey Tourbin <at@altlinux.ru> 0.40-alt1
- 0.21 -> 0.40

* Mon Sep 08 2008 Michael Bochkaryov <misha@altlinux.ru> 0.21-alt1
- 0.21 version build
- fix directory ownership violation

* Mon Jun 30 2008 Michael Bochkaryov <misha@altlinux.ru> 0.20-alt1
- 0.20 version build
  + small bugfixes
  + requirements update
  + switch to Module::Install
- spec file sleanup

* Thu Mar 22 2007 Sir Raorn <raorn@altlinux.ru> 0.18-alt1
- first build for ALT Linux Sisyphus
