# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-perl
BuildRequires: perl(AnyEvent.pm) perl(AnyEvent/Handle.pm) perl(AnyEvent/Socket.pm) perl(App/Daemon.pm) perl(CHI.pm) perl(Catalyst/Runtime.pm) perl(Class/C3.pm) perl(Compress/Bzip2.pm) perl(Data/Structure/Util.pm) perl(DateTime.pm) perl(DateTime/Format/DateParse.pm) perl(DateTime/Format/Mail.pm) perl(DateTime/Format/Natural.pm) perl(DateTime/Format/Strptime.pm) perl(Directory/Scratch.pm) perl(Email/Sender/Simple.pm) perl(Email/Sender/Transport/SMTP.pm) perl(Email/Simple.pm) perl(English.pm) perl(Fcntl.pm) perl(File/Find/Rule.pm) perl(File/MimeInfo/Magic.pm) perl(File/ShareDir.pm) perl(File/Type.pm) perl(File/stat.pm) perl(FindBin.pm) perl(HTML/Mason.pm) perl(HTTP/Daemon.pm) perl(HTTP/Status.pm) perl(Hash/Merge.pm) perl(Hash/Merge/Simple.pm) perl(IO/Handle.pm) perl(IO/Scalar.pm) perl(IO/Select.pm) perl(IO/Socket.pm) perl(IO/String.pm) perl(IPC/Open3.pm) perl(JSON.pm) perl(LWP/UserAgent.pm) perl(LockFile/Simple.pm) perl(Log/Log4perl.pm) perl(MRO/Compat.pm) perl(Memoize.pm) perl(Moose/Role.pm) perl(Net/OpenSSH.pm) perl(Perl6/Junction.pm) perl(Pod/Usage.pm) perl(Scalar/Util.pm) perl(Socket.pm) perl(Sub/Exporter.pm) perl(Sys/Syslog.pm) perl(TAP/Parser.pm) perl(TAP/Parser/Aggregator.pm) perl(Template.pm) perl(Template/Stash.pm) perl(Test/Deep.pm) perl(Test/Differences.pm) perl(Test/Exception.pm) perl(Test/MockModule.pm) perl(Test/WWW/Mechanize/Catalyst.pm) perl(Text/Balanced.pm) perl(Try/Tiny.pm) perl(UNIVERSAL.pm) perl(URI/Escape.pm) perl(XML/Feed.pm) perl(YAML.pm) perl(YAML/Tiny.pm) perl(YAML/XS.pm) perl(common/sense.pm) perl(namespace/autoclean.pm) perl(parent.pm) perl(subs.pm) perl-devel perl-podlators
# END SourceDeps(oneline)
%define upstream_name    Tapper-TestSuite-AutoTest
%define upstream_version 4.1.0

Name:       perl-%{upstream_name}
Version:    %{upstream_version}
Release:    alt1_2

Summary:    Complete OS testing in a box via autotest for Tapper
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/Tapper/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(Archive/Tar.pm)
BuildRequires: perl(Cwd.pm)
BuildRequires: perl(Digest/MD5.pm)
BuildRequires: perl(File/Slurp.pm)
BuildRequires: perl(File/Spec/Functions.pm)
BuildRequires: perl(Getopt/Long.pm)
BuildRequires: perl(IO/Socket/INET.pm)
BuildRequires: perl(Moose.pm)
BuildRequires: perl(MooseX/Log/Log4perl.pm)
BuildRequires: perl(Sys/Hostname.pm)
BuildRequires: perl(Test/More.pm)
BuildRequires: perl(YAML/Syck.pm)
BuildRequires: perl(strict.pm)
BuildRequires: perl(warnings.pm)
BuildArch: noarch
Source44: import.info

%description
This distribution provides a complete OS testing in a box via autotest for
Tapper.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLMAN1DIR=%_man1dir INSTALLMAN1DIR=%_man1dir INSTALLDIRS=vendor

%make

%check
%make test

%install
%makeinstall_std

%files
%doc META.json META.yml Changes LICENSE README
%perl_vendor_privlib/*




%changelog
* Mon Dec 10 2012 Igor Vlasenko <viy@altlinux.ru>  4.1.0-alt1_2
- mageia import by cas@ requiest

