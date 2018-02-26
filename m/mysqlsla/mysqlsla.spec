Summary: MySQL log parser, filter, analizer
Name: mysqlsla
Version: 2.03
Release: alt1.1
License: GPL
Group: Databases
Packager: Boris Savelev <boris@altlinux.org>
Url: http://hackmysql.com
Source: http://hackmysql.com/scripts/%name-%version.tar.gz

# Automatically added by buildreq on Thu Jan 29 2009
BuildRequires: perl-devel perl-DBI perl-Memoize
BuildArch: noarch

%description
mysqlsla parses, filters, analyzes and sorts MySQL slow, general, binary
and microslow patched slow logs in order to create a customizable report
of the queries and their meta-property values.

Since these reports are customizable, they can be used for human consumption
or be fed into other scripts to further analyze the queries.

%prep
%setup

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc README Changes
%_bindir/%name
%perl_vendorlib/%name.pm

%changelog
* Thu Nov 25 2010 Igor Vlasenko <viy@altlinux.ru> 2.03-alt1.1
- repair after perl 5.12 upgrade using girar-nmu

* Thu Jan 29 2009 Boris Savelev <boris@altlinux.org> 2.03-alt1
- initial build for Sisyphus

