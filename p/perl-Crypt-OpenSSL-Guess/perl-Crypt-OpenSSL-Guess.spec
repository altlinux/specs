# BEGIN SourceDeps(oneline):
BuildRequires: perl(Config.pm) perl(Exporter.pm) perl(Module/Build/Tiny.pm) perl(Symbol.pm) perl(Test/More.pm)
# END SourceDeps(oneline)
%define module_name Crypt-OpenSSL-Guess
%define _unpackaged_files_terminate_build 1
BuildRequires: rpm-build-perl perl-devel perl-podlators

Name: perl-%module_name
Version: 0.01
Release: alt1
Summary: Guess OpenSSL include path
Group: Development/Perl
License: perl
URL: https://github.com/akiym/Crypt-OpenSSL-Guess

Source0: http://mirror.yandex.ru/mirrors/cpan/authors/id/A/AK/AKIYM/%{module_name}-%{version}.tar.gz
BuildArch: noarch

%description
Crypt::OpenSSL::Guess provides helpers to guess OpenSSL include path on any platforms.

Often MacOS's homebrew OpenSSL cause a problem on installation due to include path is not added.
Some CPAN module provides to modify include path with configure-args, but the Carton manpage or the Module::CPANfile manpage
is not supported to pass configure-args to each modules. Crypt::OpenSSL::* modules should use it on your the Makefile.PL manpage.

This module resolves the include path by the Net::SSLeay manpage's workaround.
Original code is taken from `inc/Module/Install/PRIVATE/Net/SSLeay.pm' by the Net::SSLeay manpage.

%prep
%setup -q -n %{module_name}-%{version}

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc LICENSE Changes README.md
%perl_vendor_privlib/C*

%changelog
* Sat Apr 14 2018 Igor Vlasenko <viy@altlinux.ru> 0.01-alt1
- new version

