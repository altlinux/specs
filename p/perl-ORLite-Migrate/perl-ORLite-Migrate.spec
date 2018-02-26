Name: perl-ORLite-Migrate
Version: 1.09
Release: alt1
Summary: ORLite::Migrate - Extremely light weight SQLite-specific schema

Group: Development/Perl
License: Perl
Url: %CPAN ORLite-Migrate

BuildArch: noarch
Source: %name-%version.tar
BuildRequires: perl-devel perl-File-Which perl-File-pushd perl-IPC-Run3 perl-Probe-Perl perl-Params-Util perl-DBI perl-DBD-SQLite perl-ORLite

%description
%summary

%prep
%setup -q

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%perl_vendor_privlib/ORLite/Migrate*
%doc Changes README 

%changelog
* Mon Nov 14 2011 Vladimir Lettiev <crux@altlinux.ru> 1.09-alt1
- New version 1.09

* Tue Apr 06 2010 Vladimir Lettiev <crux@altlinux.ru> 1.07-alt1
- New version 1.07

* Fri Jan 29 2010 Vladimir Lettiev <crux@altlinux.ru> 1.06-alt1
- initial build
