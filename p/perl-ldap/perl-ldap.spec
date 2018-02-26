
Name: perl-ldap
Version: 0.4001
Release: alt1

Summary: %name - A Client interface to LDAP servers
License: GPL
Group: Development/Perl
Url: http://www.cpan.org/modules/by-module/Net

BuildArch: noarch
Source: %url/%name-%version.tar.gz

# Automatically added by buildreq on Mon Nov 15 2010
BuildRequires: perl-Authen-SASL perl-Convert-ASN1 perl-IO-Socket-SSL perl-Module-Install perl-XML-SAX-Writer perl-libwww

BuildRequires: perl-Tk

%package contrib
Summary: %name - some useful progs for work with ldap thru perl
Group: Development/Perl
Requires: %name = %version

%description
   Several modules in the distribution contain documentation. Once installed
you  can  use  the  'perldoc Net::LDAP' command to obtain the documentation.
This documentation will contain pointers to the other modules.

%description contrib
Some useful progs for work with ldap thru perl.

%prep
%setup -q -n %name-%version
#fix "strange" permissions on files
chmod 644 lib/Net/LDAP/DSML.pm
find . -type f -exec %__perl -pi -e "s|/usr/local/bin/perl|%__perl|g" {} \;
mv contrib/tklkup contrib/tklkup.pl

%build
%perl_vendor_build

%install
%perl_vendor_install
%__install -d %buildroot%_bindir
%__install contrib/*.pl %buildroot%_bindir

%files
%doc CREDITS Changes README TODO
%perl_vendor_privlib/Bundle*
%perl_vendor_privlib/LWP*
%perl_vendor_privlib/Net*

%files contrib
%doc contrib/README contrib/dot.tklkup
%_bindir/*

%changelog
* Mon Nov 15 2010 Alexey Shabalin <shaba@altlinux.ru> 0.4001-alt1
- 0.4001
- drop %%perl_vendor_man3dir
- update buildreq

* Wed Dec 03 2008 Alexey Shabalin <shaba@altlinux.ru> 0.39-alt1
- new version 0.39

* Fri Oct 17 2008 Alexey Shabalin <shaba@altlinux.ru> 0.38-alt1
- new version 0.38

* Wed Jun 18 2008 Alexey Shabalin <shaba@altlinux.ru> 0.36-alt1
- new version 0.36
- updated build requires

* Mon Apr 09 2007 Alexey Shabalin <shaba@altlinux.ru> 0.34-alt1
- new version 0.34
- fix build requires

* Sat Feb 19 2005 ALT QA Team Robot <qa-robot@altlinux.org> 0.29-alt1.1
- Rebuilt with rpm-build-perl-0.5.1.

* Wed Oct  1 2003 Grigory Milev <week@altlinux.ru> 0.29-alt1
- new version released
- fix build requires

* Fri Mar 21 2003 Grigory Milev <week@altlinux.ru> 0.27.01-alt1
- new version released
- fix spec

* Tue May 28 2002 Grigory Milev <week@altlinux.ru> 0.25.1-alt1
- new version released

* Wed Oct 31 2001 Grigory Milev <week@altlinux.ru> 0.25-alt1
- New version released

* Mon Sep 03 2001 Grigory Milev <week@altlinux.ru> 0.24-alt2
- New version released (0.2401)

* Wed Aug 01 2001 Grigory Milev <week@altlinux.ru> 0.24-alt1
- First build for Sisyphus

