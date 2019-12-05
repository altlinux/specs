%define _unpackaged_files_terminate_build 1
%define module_name Object-Remote
# BEGIN SourceDeps(oneline):
BuildRequires: perl(B.pm) perl(Class/C3.pm) perl(Config.pm) perl(Eval/WithLexicals.pm) perl(Exporter.pm) perl(Exporter/Declare.pm) perl(ExtUtils/MakeMaker.pm) perl(FileHandle.pm) perl(FindBin.pm) perl(Future.pm) perl(IO/Async/Loop.pm) perl(IO/Async/Process.pm) perl(IO/Handle.pm) perl(IO/Select.pm) perl(IO/Socket/INET.pm) perl(IO/Socket/UNIX.pm) perl(IPC/Open3.pm) perl(JSON/PP.pm) perl(List/Util.pm) perl(Log/Contextual.pm) perl(MRO/Compat.pm) perl(Module/Runtime.pm) perl(Moo.pm) perl(Scalar/Util.pm) perl(String/ShellQuote.pm) perl(Symbol.pm) perl(Sys/Hostname.pm) perl(Term/ReadLine.pm) perl(Test/Fatal.pm) perl(Tie/Handle.pm) perl(Time/HiRes.pm) perl(base.pm) perl(overload.pm) perl(strictures.pm) perl(Algorithm/C3.pm) perl(Devel/GlobalDestruction.pm)
# END SourceDeps(oneline)
BuildRequires: rpm-build-perl perl-devel perl-podlators

Name: perl-%module_name
Version: 0.004001
Release: alt1
Summary: Call methods on objects in other processes or on other hosts
Group: Development/Perl
License: perl
Url: %CPAN %module_name

Source0: http://www.cpan.org/authors/id/H/HA/HAARG/%{module_name}-%{version}.tar.gz
BuildArch: noarch

%description
Object::Remote allows you to create an object in another process - usually
one running on another machine you can connect to via ssh, although there
are other connection mechanisms available.

The idea here is that in many cases one wants to be able to run a piece of
code on another machine, or perhaps many other machines - but without having
to install anything on the far side.

%package scripts
Summary: %module_name scripts
Group: Development/Perl
Requires: %name = %{?epoch:%epoch:}%version-%release

%description scripts
scripts for %module_name
%prep
%setup -q -n %{module_name}-%{version}

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc README Changes
%perl_vendor_privlib/O*

%files scripts
%_bindir/*

%changelog
* Thu Dec 05 2019 Igor Vlasenko <viy@altlinux.ru> 0.004001-alt1
- automated CPAN update

* Sun Sep 25 2016 Igor Vlasenko <viy@altlinux.ru> 0.004000-alt2
- to Sisyphus

* Thu Sep 01 2016 Igor Vlasenko <viy@altlinux.ru> 0.004000-alt1
- regenerated from template by package builder

* Fri Mar 04 2016 Igor Vlasenko <viy@altlinux.ru> 0.003006-alt1
- regenerated from template by package builder

* Sun Oct 18 2015 Igor Vlasenko <viy@altlinux.ru> 0.003005-alt1
- regenerated from template by package builder

* Wed Dec 17 2014 Igor Vlasenko <viy@altlinux.ru> 0.003004-alt1
- regenerated from template by package builder

* Mon Oct 07 2013 Igor Vlasenko <viy@altlinux.ru> 0.003002-alt1
- initial import by package builder

