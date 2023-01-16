%define _unpackaged_files_terminate_build 1
%define module_name Redis
# BEGIN SourceDeps(oneline):
BuildRequires: perl(Digest/SHA.pm) perl(ExtUtils/MakeMaker.pm) perl(File/Spec.pm) perl(IO/Handle.pm) perl(IO/Socket/Timeout.pm) perl(IO/String.pm) perl(IPC/Cmd.pm) perl(IPC/Open3.pm) perl(Module/Build/Tiny.pm) perl(Pod/Coverage/TrustPod.pm) perl(Test/CPAN/Meta.pm) perl(Test/Deep.pm) perl(Test/Fatal.pm) perl(Test/More.pm) perl(Test/Pod/Coverage.pm) perl(Test/SharedFork.pm) perl(Test/TCP.pm) perl(Try/Tiny.pm)
# END SourceDeps(oneline)
BuildRequires: rpm-build-perl perl-devel perl-podlators

Name: perl-%module_name
Version: 2.000
Release: alt1
Summary: Perl binding for Redis database
Group: Development/Perl
License: artistic_2
URL: https://github.com/PerlRedis/perl-redis

Source0: http://www.cpan.org/authors/id/D/DA/DAMS/%{module_name}-%{version}.tar.gz
BuildArch: noarch

%description
Pure perl bindings for http://redis.io/

This version supports protocol 2.x (multi-bulk) or later of Redis available at
https://github.com/antirez/redis/.

This documentation lists commands which are exercised in test suite, but
additional commands will work correctly since protocol specifies enough
information to support almost all commands with same piece of code with a
little help of `AUTOLOAD'.

%prep
%setup -q -n %{module_name}-%{version}

%build
%perl_vendor_build --install_path bindoc=%_man1dir

%install
%perl_vendor_install

%files
%doc README Changes README.pod
%perl_vendor_privlib/R*

%changelog
* Mon Jan 16 2023 Igor Vlasenko <viy@altlinux.org> 2.000-alt1
- automated CPAN update

* Wed Jan 19 2022 Igor Vlasenko <viy@altlinux.org> 1.999-alt1
- automated CPAN update

* Tue Sep 01 2020 Igor Vlasenko <viy@altlinux.ru> 1.998-alt1
- automated CPAN update

* Sat Mar 14 2020 Igor Vlasenko <viy@altlinux.ru> 1.996-alt1
- automated CPAN update

* Tue Aug 06 2019 Igor Vlasenko <viy@altlinux.ru> 1.995-alt1
- automated CPAN update

* Thu Apr 11 2019 Ilfat Aminov <aminov@altlinux.org> 1.991-alt2
- Build for Sisyphus classic

* Thu Sep 01 2016 Igor Vlasenko <viy@altlinux.ru> 1.991-alt1
- regenerated from template by package builder

* Fri Mar 04 2016 Igor Vlasenko <viy@altlinux.ru> 1.982-alt1
- regenerated from template by package builder

* Wed Oct 14 2015 Igor Vlasenko <viy@altlinux.ru> 1.981-alt1
- regenerated from template by package builder

* Tue Feb 10 2015 Igor Vlasenko <viy@altlinux.ru> 1.978-alt1
- regenerated from template by package builder

* Wed Oct 22 2014 Igor Vlasenko <viy@altlinux.ru> 1.976-alt1
- regenerated from template by package builder

* Fri Sep 05 2014 Igor Vlasenko <viy@altlinux.ru> 1.975-alt1
- regenerated from template by package builder

* Mon Jun 23 2014 Igor Vlasenko <viy@altlinux.ru> 1.974-alt1
- regenerated from template by package builder

* Tue Apr 15 2014 Igor Vlasenko <viy@altlinux.ru> 1.972-alt1
- regenerated from template by package builder

* Thu Oct 03 2013 Igor Vlasenko <viy@altlinux.ru> 1.961-alt1
- initial import by package builder
