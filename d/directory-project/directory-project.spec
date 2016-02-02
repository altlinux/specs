Group: Development/Java
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
Name:          directory-project
Version:       27
Release:       alt2_10jpp8
Summary:       Apache Directory Project Root pom
License:       ASL 2.0
Url:           http://directory.apache.org/
# svn export http://svn.apache.org/repos/asf/directory/project/tags/27 directory-project-27
# tar czf directory-project-27-src-svn.tar.gz directory-project-27
Source0:       directory-project-27-src-svn.tar.gz
BuildRequires: maven-local
BuildRequires: maven-site-plugin
BuildArch:     noarch
Source44: import.info

%description
The Apache Directory Project provides directory solutions
entirely written in Java. These include a directory server,
which has been certified as LDAP v3 compliant by the
Open Group (Apache Directory Server), and Eclipse-based
directory tools (Apache Directory Studio).

%prep
%setup -q
%pom_remove_plugin :tools-maven-plugin
%pom_remove_plugin :maven-xbean-plugin
%pom_remove_plugin :clirr-maven-plugin
%pom_remove_plugin :dashboard-maven-plugin
%pom_remove_plugin :findbugs-maven-plugin
%pom_remove_plugin :javancss-maven-plugin
%pom_remove_plugin :jdepend-maven-plugin
%pom_remove_plugin :l10n-maven-plugin
%pom_remove_plugin :taglist-maven-plugin
%pom_remove_plugin :versions-maven-plugin
%pom_remove_plugin :docbkx-maven-plugin

%build

%mvn_build

%install
%mvn_install

%files -f .mfiles
%doc README.txt
%doc LICENSE.txt NOTICE.txt

%changelog
* Tue Feb 02 2016 Igor Vlasenko <viy@altlinux.ru> 27-alt2_10jpp8
- new version

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 27-alt2_5jpp7
- new release

* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 27-alt2_3jpp7
- new release

* Mon Jul 14 2014 Igor Vlasenko <viy@altlinux.ru> 27-alt2_1jpp7
- NMU rebuild to move poms and fragments

* Sun Sep 09 2012 Igor Vlasenko <viy@altlinux.ru> 27-alt1_1jpp7
- new version

