Name: runawfe-jboss
License: LGPL
Group: System/Servers
Version: 4.2.3.GA
Release: alt0.1
Packager: Konstantinov Aleksey <kana@altlinux.ru>
Summary: JBOSS 4.2.3.GA for RUNA WFE Workflow/BPM management system.
Url: http://sourceforge.net/projects/runawfe
Source0: runawfe-jboss-%{version}.tar.gz
BuildArch: noarch
AutoReq: no
Requires: java >= 1.6.0

%description
RUNA WFE is a cross-platform end user solution for business process management. It provides rich web interface with tasklist, form player, graphical process designer, bots and more.

This package provides embedded JBOSS 4.0.5.GA for RUNA WFE Workflow/BPM management system.

%prep
%setup 
%build

%install
mkdir -p $RPM_BUILD_ROOT%_datadir
cp -R ../runawfe-jboss-%{version}  $RPM_BUILD_ROOT%_datadir/runawfe-jboss

%files
%_datadir/runawfe-jboss

%changelog
* Sat Sep 11 2010 Konstantinov Aleksey <kana@altlinux.ru> 4.2.3.GA-alt0.1
- package upgraded to 4.2.3 version

* Wed Nov 19 2008 Igor Vlasenko <viy@altlinux.ru> 4.0.5.GA-alt0.2
- NMU (by repocop): the following fixes applied:

* Thu Jan 10 2008 Igor Vlasenko <viy@altlinux.ru> 4.0.5.GA-alt0.1
- temporary package until jbosses will be built properly.


