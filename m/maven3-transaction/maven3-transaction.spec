Name: maven3-transaction
Version: 1.0.1
Summary: Maven3 transaction files
License: ASL 2.0
Packager: Igor Vlasenko <viy@altlinux.ru>
BuildArch: noarch
Group: Development/Java
Release: alt0.3jpp

#i586-runawfe-gpd.32bit#3.6.0-alt1.svn4700       i586-eclipse-swt
#i586-runawfe-notifier.32bit#3.6.0-alt1.svn4700  i586-eclipse-swt
Provides: i586-eclipse-swt = 4.0
Provides: kde3-freedesktop-menu

%description
Maven3 transaction unfinished files.
Temporary package to keep them alive.

%prep
%build
%install
mkdir -p $RPM_BUILD_ROOT

%files

%changelog
* Sat Sep 23 2017 Igor Vlasenko <viy@altlinux.ru> 1.0.1-alt0.3jpp
- updated dependencies

* Thu Feb 25 2016 Igor Vlasenko <viy@altlinux.ru> 1.0.1-alt0.2jpp
- updated dependencies

* Fri Feb 12 2016 Igor Vlasenko <viy@altlinux.ru> 1.0.1-alt0.1jpp
- updated dependencies
