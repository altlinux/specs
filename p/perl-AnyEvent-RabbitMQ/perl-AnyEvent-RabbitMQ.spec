%define module_name AnyEvent-RabbitMQ
# BEGIN SourceDeps(oneline):
BuildRequires: perl(AnyEvent.pm) perl(Devel/GlobalDestruction.pm) perl(ExtUtils/MakeMaker.pm) perl(File/ShareDir.pm) perl(File/ShareDir/Install.pm) perl(List/MoreUtils.pm) perl(Net/AMQP.pm) perl(Pod/Wordlist.pm) perl(Readonly.pm) perl(Test/Exception.pm) perl(Test/More.pm) perl(Test/Perl/Critic.pm) perl(Test/Spelling.pm) perl(namespace/clean.pm) perl(version.pm)
# END SourceDeps(oneline)
%define _unpackaged_files_terminate_build 1
BuildRequires: rpm-build-perl perl-devel perl-podlators

Name: perl-%module_name
Version: 1.22
Release: alt2
Summary: An asynchronous and multi channel Perl AMQP client.
Group: Development/Perl
License: perl
Url: %CPAN %module_name

Source0: http://mirror.yandex.ru/mirrors/cpan/authors/id/D/DL/DLAMBLEY/%{module_name}-%{version}.tar.gz
BuildArch: noarch

%description
AnyEvent::RabbitMQ is an AMQP(Advanced Message Queuing Protocol) client library, that is intended to allow you to interact with AMQP-compliant message brokers/servers such as RabbitMQ in an asynchronous fashion.

You can use AnyEvent::RabbitMQ to -

  * Declare and delete exchanges
  * Declare, delete, bind and unbind queues
  * Set QoS and confirm mode
  * Publish, consume, get, ack, recover and reject messages
  * Select, commit and rollback transactions

AnyEvent::RabbitMQ is known to work with RabbitMQ versions 2.5.1 and versions 0-8 and 0-9-1 of the AMQP specification.

This client is the non-blocking version, for a blocking version with a similar API, see the Net::RabbitFoot manpage.


%prep
%setup -q -n %{module_name}-%{version}

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc README Changes LICENSE
%perl_vendor_privlib/A*
%perl_vendor_privlib/auto/*
%changelog
* Fri Oct 29 2021 Igor Vlasenko <viy@altlinux.org> 1.22-alt2
- to Siayphus for ALT bugzilla

* Sat Jun 13 2020 Igor Vlasenko <viy@altlinux.ru> 1.22-alt1
- updated by package builder

* Thu Jun 04 2020 Igor Vlasenko <viy@altlinux.ru> 1.21-alt1
- updated by package builder

* Mon May 18 2020 Igor Vlasenko <viy@altlinux.ru> 1.20-alt1
- updated by package builder

* Thu Apr 02 2015 Igor Vlasenko <viy@altlinux.ru> 1.19-alt1
- regenerated from template by package builder

* Wed Oct 08 2014 Igor Vlasenko <viy@altlinux.ru> 1.18-alt1
- regenerated from template by package builder

* Fri Sep 05 2014 Igor Vlasenko <viy@altlinux.ru> 1.17-alt1
- regenerated from template by package builder

* Tue Apr 15 2014 Igor Vlasenko <viy@altlinux.ru> 1.16-alt1
- regenerated from template by package builder

* Mon Oct 07 2013 Igor Vlasenko <viy@altlinux.ru> 1.15-alt1
- initial import by package builder

