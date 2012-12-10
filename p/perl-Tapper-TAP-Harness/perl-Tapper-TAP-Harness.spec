# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-perl
BuildRequires: perl(AnyEvent.pm) perl(AnyEvent/Handle.pm) perl(AnyEvent/Socket.pm) perl(App/Daemon.pm) perl(App/Rad.pm) perl(CHI.pm) perl(Catalyst/Runtime.pm) perl(Class/C3.pm) perl(Compress/Bzip2.pm) perl(Daemon/Daemonize.pm) perl(Data/DPath.pm) perl(Data/DPath/Path.pm) perl(Data/Structure/Util.pm) perl(DateTime.pm) perl(DateTime/Format/DateParse.pm) perl(DateTime/Format/Mail.pm) perl(DateTime/Format/Natural.pm) perl(English.pm) perl(File/Find/Rule.pm) perl(File/MimeInfo/Magic.pm) perl(File/ShareDir.pm) perl(File/Type.pm) perl(File/stat.pm) perl(FindBin.pm) perl(HTML/Mason.pm) perl(HTTP/Daemon.pm) perl(Hash/Merge.pm) perl(Hash/Merge/Simple.pm) perl(IO/Handle.pm) perl(IO/Select.pm) perl(IO/Socket.pm) perl(IO/Socket/INET.pm) perl(IPC/Open3.pm) perl(JSON.pm) perl(Kwalify.pm) perl(LWP/UserAgent.pm) perl(Log/Log4perl.pm) perl(MRO/Compat.pm) perl(Memoize.pm) perl(Moose/Role.pm) perl(Net/OpenSSH.pm) perl(Perl6/Junction.pm) perl(Pod/Usage.pm) perl(Scalar/Util.pm) perl(Socket.pm) perl(Sub/Exporter.pm) perl(Sys/Hostname.pm) perl(Sys/Syslog.pm) perl(Tapper/Remote/Config.pm) perl(Template.pm) perl(Template/Stash.pm) perl(Test/Exception.pm) perl(Test/MockModule.pm) perl(Test/WWW/Mechanize/Catalyst.pm) perl(Text/Balanced.pm) perl(Try/Tiny.pm) perl(UNIVERSAL.pm) perl(URI/Escape.pm) perl(XML/Feed.pm) perl(YAML.pm) perl(YAML/Syck.pm) perl(YAML/XS.pm) perl(common/sense.pm) perl(namespace/autoclean.pm) perl(parent.pm) perl(subs.pm) perl-devel perl-podlators
# END SourceDeps(oneline)
%define upstream_name    Tapper-TAP-Harness
%define upstream_version 4.1.0

Name:       perl-%{upstream_name}
Version:    %{upstream_version}
Release:    alt1_1

Summary:    Tapper - Tapper specific TAP handling
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/Tapper/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(Archive/Tar.pm)
BuildRequires: perl(Class/XSAccessor.pm)
BuildRequires: perl(Data/Dumper.pm)
BuildRequires: perl(Directory/Scratch.pm)
BuildRequires: perl(File/Slurp.pm)
BuildRequires: perl(File/Temp.pm)
BuildRequires: perl(IO/Scalar.pm)
BuildRequires: perl(IO/String.pm)
BuildRequires: perl(Moose.pm)
BuildRequires: perl(TAP/DOM.pm)
BuildRequires: perl(TAP/Parser.pm)
BuildRequires: perl(TAP/Parser/Aggregator.pm)
BuildRequires: perl(Test/Deep.pm)
BuildRequires: perl(Test/More.pm)
BuildRequires: perl(YAML/Tiny.pm)
BuildRequires: perl(strict.pm)
BuildRequires: perl(warnings.pm)
BuildArch: noarch
Source44: import.info

%description
This package provides a Tapper-specific TAP handling.

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
* Mon Dec 10 2012 Igor Vlasenko <viy@altlinux.ru> 4.1.0-alt1_1
- mageia import by cas@ requiest

