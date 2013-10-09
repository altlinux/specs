# BEGIN SourceDeps(oneline):
BuildRequires: perl(AnyEvent.pm) perl(AnyEvent/Impl/Perl.pm) perl(Event.pm) perl(Event/Watcher.pm) perl(ExtUtils/MakeMaker.pm) perl(FindBin.pm) perl(IO/Handle.pm) perl(IO/Socket/INET.pm) perl(IO/Socket/UNIX.pm) perl(List/MoreUtils.pm) perl(Scalar/Util.pm) perl(Socket.pm) perl(Symbol.pm) perl(Test/Simple.pm) perl(Time/HiRes.pm) perl(diagnostics.pm)
# END SourceDeps(oneline)
%define module_version 0.813
%define module_name IO-Event
%define _unpackaged_files_terminate_build 1
BuildRequires: rpm-build-perl perl-devel perl-podlators

Name: perl-%module_name
Version: 0.813
Release: alt2
Summary: Tied Filehandles for Nonblocking IO with Object Callbacks
Group: Development/Perl
License: perl
Url: %CPAN %module_name

Source0: http://cpan.org.ua/authors/id/M/MU/MUIR/modules/%module_name-%module_version.tar.gz
BuildArch: noarch

%description
%summary

%prep
%setup -n %module_name-%module_version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README
%perl_vendor_privlib/I*

%changelog
* Wed Oct 09 2013 Igor Vlasenko <viy@altlinux.ru> 0.813-alt2
- build for Sisyphus

* Sat Sep 28 2013 Igor Vlasenko <viy@altlinux.ru> 0.813-alt1
- regenerated from template by package builder

* Fri Sep 06 2013 Igor Vlasenko <viy@altlinux.ru> 0.812-alt1
- initial import by package builder

