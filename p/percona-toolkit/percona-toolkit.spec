Name: percona-toolkit
Version: 2.2.5
Release: alt1

Summary: Percona Toolkit for MySQL

License: GPL2
Group: Databases
Url: http://www.percona.com/software/percona-toolkit

Packager: Evgenii Terechkov <evg@altlinux.org>

BuildArch: noarch
Source: %name-%version.tar.gz

BuildRequires: perl-devel perl-podlators
AutoReq: yes, noperl

Requires: perl-DBI, perl-DBD-mysql

%description
Percona Toolkit for MySQL is a collection of advanced command-line
tools used by Percona MySQL Support staff to perform a variety of
MySQL server and system tasks that are too difficult or complex to
perform manually.

%prep
%setup -n %name-%version
%build
%perl_vendor_build

%check
make test

%install
%perl_vendor_install
mkdir -p %buildroot%_man1dir
cp -p blib/man1/*.1p %buildroot%_man1dir

%files
%_bindir/pt-*
%_man1dir/*.1p.*
%doc Changelog README

%changelog
* Wed Nov 20 2013 Terechkov Evgenii <evg@altlinux.org> 2.2.5-alt1
- 2.2.5

* Tue Aug 20 2013 Evgenii Terechkov <evg@altlinux.org> 2.2.4-alt1
- initial build for ALT Linux Sisyphus

