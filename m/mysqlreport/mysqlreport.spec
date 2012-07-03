Name: mysqlreport
Summary: mysqlreport makes a friendly report of important MySQL status values
Group: Databases
Version: 3.2
Release: alt1
License: GPL
#Source: http://hackmysql.com/scripts/%name-3.2.tgz
Source0: %name
Source1: %{name}doc.html
Source2: %{name}guide.html
Url: http://hackmysql.com/
Packager: Mikhail Pokidko <pma@altlinux.org>
Buildrequires: perl-DBI
Requires: perl-DBI perl-DBD-mysql


%description
mysqlreport makes a friendly report of important MySQL status values. 
mysqlreport transforms the values from SHOW STATUS into an easy-to-read report 
that provides an in-depth understanding of how well MySQL is running. 
mysqlreport is a better alternative (and practically the only alternative) to manually interpreting SHOW STATUS.


%install
install -pD -m755 %SOURCE0 %buildroot%_bindir/%name
install -pD -m755 %SOURCE1 %buildroot%_defaultdocdir/%name/%{name}doc.html
install -pD -m755 %SOURCE2 %buildroot%_defaultdocdir/%name/%{name}guide.html


%files
%_bindir/*
%_defaultdocdir/%name/*.html

%changelog
* Wed Jul 04 2007 Pokidko Mikhail <pma@altlinux.org> 3.2-alt1
- Initial ALT build

