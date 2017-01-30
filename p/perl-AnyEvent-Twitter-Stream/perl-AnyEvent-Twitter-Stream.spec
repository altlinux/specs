%define module_version 0.28
%define module_name AnyEvent-Twitter-Stream
# BEGIN SourceDeps(oneline):
BuildRequires: perl(AnyEvent.pm) perl(AnyEvent/HTTP.pm) perl(Compress/Raw/Zlib.pm) perl(JSON.pm) perl(MIME/Base64.pm) perl(Module/Build/Tiny.pm) perl(Net/OAuth.pm) perl(Test/More.pm) perl(Test/Pod.pm) perl(Test/Requires.pm) perl(Test/TCP.pm) perl(URI.pm)
# END SourceDeps(oneline)
%define _unpackaged_files_terminate_build 1
BuildRequires: rpm-build-perl perl-devel perl-podlators

Name: perl-%module_name
Version: 0.28
Release: alt2
Summary: Receive Twitter streaming API in an event loop
Group: Development/Perl
License: perl
URL: https://github.com/miyagawa/AnyEvent-Twitter-Stream

Source0: http://mirror.yandex.ru/mirrors/cpan/authors/id/M/MI/MIYAGAWA/%{module_name}-%{module_version}.tar.gz
BuildArch: noarch

%description
AnyEvent::Twitter::Stream is an AnyEvent user to receive Twitter streaming
API, available at http://dev.twitter.com/pages/streaming_api and
http://dev.twitter.com/pages/user_streams.

See the track.pl entry in the eg manpage for more client code example.


%prep
%setup -q -n %{module_name}-%{module_version}

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc README Changes LICENSE
%perl_vendor_privlib/A*

%changelog
* Mon Jan 30 2017 Igor Vlasenko <viy@altlinux.ru> 0.28-alt2
- to Sisyphus

* Sun Aug 07 2016 Igor Vlasenko <viy@altlinux.ru> 0.28-alt1
- regenerated from template by package builder

* Tue May 06 2014 Igor Vlasenko <viy@altlinux.ru> 0.27-alt1
- regenerated from template by package builder

* Thu Sep 19 2013 Igor Vlasenko <viy@altlinux.ru> 0.26-alt1
- initial import by package builder

