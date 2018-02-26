# Spec file for Perl module Mail::Folder

Name: perl-Mail-Folder
Version: 0.07
Release: alt1.1

Summary: Perl module Mail::Folder
Summary(ru_RU.UTF-8): модуль Perl Mail::Folder

%define real_name MailFolder

License: GPL or Artistic
Group: Development/Perl
URL: http://search.cpan.org/~kjohnson/MailFolder/

Packager: Nikolay Fetisov <naf@altlinux.ru>
BuildArch: noarch

Source: http://search.cpan.org/CPAN/authors/id/K/KJ/KJOHNSON/%real_name-%version.tar.gz
Patch0: MailFolder-0.07-alt-Perl_5.8.patch

AutoReqProv: perl, yes
BuildPreReq: perl-devel perl-MailTools perl-MIME-tools perl-TimeDate
BuildPreReq: perl-File-Sync

%description
Perl module Mail::Folder provides an interface to email folders
that is independent from the physical folders.

%description -l ru_RU.UTF-8
Модуль Perl Mail::Folder предоставляет интерфейс к папкам почтовых
сообщений, позволяющий абстрагироваться от физических каталогов.

%prep
%setup -q -n %real_name-%version
%patch0

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc README BUGS CREDITS NEWS TODO ANNOUNCE examples*
%exclude /.perl.req
%perl_vendor_privlib/Mail/Folder*

%changelog
* Mon Nov 22 2010 Igor Vlasenko <viy@altlinux.ru> 0.07-alt1.1
- repair after perl 5.12 upgrade using girar-nmu

* Sat Sep 16 2006 Nikolay A. Fetisov <naf@altlinux.ru> 0.07-alt1
- Initial build for ALT Linux Sisyphus

* Sun Jul 02 2006 Nikolay A. Fetisov <naf@altlinux.ru> 0.07-alt0
- First build

