Name: percona-toolkit
Version: 2.2.19
Release: alt1

Summary: Advanced MySQL and system command-line tools

License: GPLv2
Group: Databases
Url: http://www.percona.com/software/percona-toolkit

Packager: Evgenii Terechkov <evg@altlinux.org>

BuildArch: noarch
Source: %name-%version.tar

BuildRequires: perl-devel perl-podlators
AutoReq: yes, noperl

Requires: perl-DBI, perl-DBD-mysql

%description
Percona Toolkit is a collection of advanced command-line tools used by
Percona (http://www.percona.com/) support staff to perform a variety of
MySQL and system tasks that are too difficult or complex to perform manually.

These tools are ideal alternatives to private or "one-off" scripts because
they are professionally developed, formally tested, and fully documented.
They are also fully self-contained, so installation is quick and easy and
no libraries are installed. 

Percona Toolkit is developed and supported by Percona.  For more
information and other free, open-source software developed by Percona,
visit http://www.percona.com/software/.

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
* Sun Nov  6 2016 Terechkov Evgenii <evg@altlinux.org> 2.2.19-alt1
- 2.2.19
- Build from upstream git repo

* Sat Apr 25 2015 Terechkov Evgenii <evg@altlinux.org> 2.2.14-alt1
- 2.2.14

* Mon Feb 10 2014 Evgenii Terechkov <evg@altlinux.org> 2.2.6-alt1
- 2.2.6

* Wed Nov 20 2013 Terechkov Evgenii <evg@altlinux.org> 2.2.5-alt1
- 2.2.5

* Tue Aug 20 2013 Evgenii Terechkov <evg@altlinux.org> 2.2.4-alt1
- initial build for ALT Linux Sisyphus
