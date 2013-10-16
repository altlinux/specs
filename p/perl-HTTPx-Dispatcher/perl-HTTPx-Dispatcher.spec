%define module_version 0.10
%define module_name HTTPx-Dispatcher
# BEGIN SourceDeps(oneline):
BuildRequires: perl(CPAN.pm) perl(Class/Accessor/Fast.pm) perl(Config.pm) perl(Cwd.pm) perl(Exporter.pm) perl(ExtUtils/MM_Unix.pm) perl(ExtUtils/MakeMaker.pm) perl(ExtUtils/Manifest.pm) perl(Fcntl.pm) perl(File/Basename.pm) perl(File/Find.pm) perl(FileHandle.pm) perl(HTTP/Request.pm) perl(JSON.pm) perl(LWP/Simple.pm) perl(Module/Build.pm) perl(Net/FTP.pm) perl(Parse/CPAN/Meta.pm) perl(Scalar/Util.pm) perl(Socket.pm) perl(Test/Base.pm) perl(Test/More.pm) perl(Test/Requires.pm) perl(URI.pm) perl(YAML.pm) perl(YAML/Tiny.pm) perl(base.pm) perl(inc/Module/Install.pm)
# END SourceDeps(oneline)
%define _unpackaged_files_terminate_build 1
BuildRequires: rpm-build-perl perl-devel perl-podlators

Name: perl-%module_name
Version: 0.10
Release: alt2
Summary: the uri dispatcher(DEPRECATED)
Group: Development/Perl
License: perl
Url: %CPAN %module_name

Source0: http://cpan.org.ua/authors/id/T/TO/TOKUHIROM/%module_name-%module_version.tar.gz
BuildArch: noarch

%description
THIS MODULE WAS NO LONGER MAINTAIN. USE the Router::Simple manpage INSTEAD.


%prep
%setup -n %module_name-%module_version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README
%perl_vendor_privlib/H*

%changelog
* Wed Oct 16 2013 Igor Vlasenko <viy@altlinux.ru> 0.10-alt2
- build for Sisyphus (required for perl update)

* Mon Sep 23 2013 Igor Vlasenko <viy@altlinux.ru> 0.10-alt1
- initial import by package builder

