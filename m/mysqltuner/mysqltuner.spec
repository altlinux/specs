Name: mysqltuner
Version: 1.2.0
Release: alt1

Summary: MySQL high performance tuning script
License: GPLv3+
Group: Databases

Url: http://mysqltuner.com/
Source0: http://mysqltuner.com/mysqltuner.pl

BuildArch: noarch

# Automatically added by buildreq on Wed Sep 10 2008 (-bi)
BuildRequires: perl-devel

%description
MySQLTuner is a MySQL high performance tuning script written in perl that will
provide you with a snapshot of a MySQL server's health. Based on the statistics
gathered, specific recommendations will be provided that will increase a MySQL
server's efficiency and performance. The script gives you automated MySQL tuning
that is on the level of what you would receive from a MySQL DBA.

%prep
%setup -c -T

%build

%install
install -Dp -m755 %SOURCE0 %buildroot%_bindir/mysqltuner

%files
%_bindir/*

%changelog
* Mon Mar 14 2011 Victor Forsiuk <force@altlinux.org> 1.2.0-alt1
- 1.2.0

* Wed Dec 23 2009 Victor Forsyuk <force@altlinux.org> 1.1.1-alt1
- 1.1.1

* Wed Dec 24 2008 Victor Forsyuk <force@altlinux.org> 1.0.0-alt1
- 1.0.0

* Wed Sep 10 2008 Victor Forsyuk <force@altlinux.org> 0.9.9-alt1
- Initial build.
