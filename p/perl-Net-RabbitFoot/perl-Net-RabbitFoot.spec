BuildRequires: perl-podlators
# BEGIN SourceDeps(oneline):
BuildRequires: perl(AnyEvent/RabbitMQ.pm) perl(AnyEvent/RabbitMQ/Channel.pm) perl(AnyEvent/RabbitMQ/LocalQueue.pm) perl(CPAN.pm) perl(Carp.pm) perl(Config.pm) perl(Config/Any.pm) perl(Coro.pm) perl(Coro/AnyEvent.pm) perl(Cwd.pm) perl(ExtUtils/MM_Unix.pm) perl(ExtUtils/MakeMaker.pm) perl(ExtUtils/Manifest.pm) perl(Fcntl.pm) perl(File/Basename.pm) perl(File/Find.pm) perl(File/Spec.pm) perl(FileHandle.pm) perl(FindBin.pm) perl(JSON.pm) perl(JSON/XS.pm) perl(LWP/Simple.pm) perl(List/MoreUtils.pm) perl(Module/Build.pm) perl(Moose.pm) perl(Moose/Role.pm) perl(MooseX/App/Cmd.pm) perl(MooseX/AttributeHelpers.pm) perl(MooseX/ConfigFromFile.pm) perl(Net/FTP.pm) perl(Parse/CPAN/Meta.pm) perl(Socket.pm) perl(Test/Exception.pm) perl(Test/More.pm) perl(YAML/Tiny.pm) perl(inc/Module/Install.pm) perl(version.pm)
# END SourceDeps(oneline)
%define module_version 1.03
%define module_name Net-RabbitFoot
%define _unpackaged_files_terminate_build 1
BuildRequires: rpm-build-perl perl-devel perl-podlators

Name: perl-%module_name
Version: 1.03
Release: alt2
Summary: An Asynchronous and multi channel Perl AMQP client.
Group: Development/Perl
License: perl
Url: %CPAN %module_name

Source0: http://cpan.org.ua/authors/id/I/IK/IKUTA/%module_name-%module_version.tar.gz
BuildArch: noarch

%description
Net::RabbitFoot is an AMQP(Advanced Message Queuing Protocol) client library, that is intended to allow you to interact with AMQP-compliant message brokers/servers such as RabbitMQ in an asynchronous fashion.

You can use Net::RabbitFoot to -

  * Declare and delete exchanges
  * Declare, delete, bind and unbind queues
  * Set QoS
  * Publish, consume, get, ack and recover messages
  * Select, commit and rollback transactions

Net::RabbitFoot is known to work with RabbitMQ versions 2.3.1 and version 0-8 of the AMQP specification.

%package scripts
Summary: %name scripts
Group: Development/Perl
Requires: %{?epoch:%epoch:}%name = %version-%release

%description scripts
scripts for %name



%prep
%setup -n %module_name-%module_version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc README Changes
%perl_vendor_privlib/N*

%files scripts
%_bindir/*
%perl_vendor_privlib/auto/*

%changelog
* Fri Oct 29 2021 Igor Vlasenko <viy@altlinux.org> 1.03-alt2
- to Siayphus for ALT bugzilla

* Thu Apr 17 2014 Igor Vlasenko <viy@altlinux.ru> 1.03-alt1
- initial import by package builder

