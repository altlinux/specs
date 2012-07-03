# SPEC file for building Perl module Config-YAML

%define real_name Config-YAML
%define version 1.42
%define release alt2

Name: perl-Config-YAML
Version: %version
Release: alt2.1

Summary: Perl module Config::YAML - simple configuration automation
Summary(ru_RU.UTF-8): модуль Perl для простой работы с файлами конфигурации

License: Artistic
Group: Development/Perl
URL: http://search.cpan.org/~mdxi/Config-YAML/

Packager: Nikolay A. Fetisov <naf@altlinux.ru>

Source: http://search.cpan.org/CPAN/authors/id/M/MD/MDXI/%real_name-%version.tar.gz

AutoReqProv: perl, yes
BuildPreReq: perl-devel, perl-YAML
BuildArch: noarch

%description
Perl module Config::YAML is a somewhat object-oriented 
wrapper around the YAML module which makes reading and
writing configuration files simple.  Handling multiple
config files  (e.g. system and per-user configuration,
or a gallery app with per-directory configuration)  is 
a snap.

%description -l ru_RU.UTF-8
Модуль Perl  Comfig::YAML  - объектно-ориентированная оболочка
вокруг модуля  YAML,  упрощающая задачи чтения и записи файлов
конфигурации. Модуль обеспечивает простую поддержку нескольких
файлов конфигурации  (т.е.  общесистемной  и  пользовательской 
конфигураций,  или приложений вида галереи  картинок с файлами
конфигурации в каждом каталоге).

%prep
%setup -q -n %real_name-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc README Changes
%perl_vendor_privlib/Config/YAML*

%changelog
* Wed Nov 24 2010 Igor Vlasenko <viy@altlinux.ru> 1.42-alt2.1
- repair after perl 5.12 upgrade using girar-nmu

* Sat Nov 15 2008 Nikolay A. Fetisov <naf@altlinux.ru> 1.42-alt2
- Fix directory ownership

* Mon Jan 09 2006 Nikolay A. Fetisov <naf@altlinux.ru> 1.42-alt1
- Initial build for ALTLinux Sisyphus
