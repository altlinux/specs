Epoch: 0
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
# END SourceDeps(oneline)
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
%global short_name      commons-parent

Name:             apache-%{short_name}
Version:          40
Release:          alt1_2jpp8
Summary:          Apache Commons Parent Pom
Group:            Development/Other
License:          ASL 2.0
URL:              http://svn.apache.org/repos/asf/commons/proper/%{short_name}/tags/%{short_name}-%{version}/

# svn export http://svn.apache.org/repos/asf/commons/proper/commons-parent/tags/commons-parent-%{version}
# tar caf commons-parent-%{version}.tar.xz commons-parent-%{version}
Source0:          %{short_name}-%{version}.tar.xz

BuildArch:        noarch

BuildRequires:    maven-local
BuildRequires:    mvn(org.apache:apache:pom:)
BuildRequires:    mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires:    mvn(org.apache.maven.plugins:maven-antrun-plugin)
BuildRequires:    mvn(org.apache.maven.plugins:maven-assembly-plugin)
BuildRequires:    mvn(org.apache.maven.plugins:maven-enforcer-plugin)
BuildRequires:    mvn(org.apache.rat:apache-rat-plugin)
BuildRequires:    mvn(org.codehaus.mojo:build-helper-maven-plugin)
BuildRequires:    mvn(org.codehaus.mojo:buildnumber-maven-plugin)
Requires:         mvn(org.codehaus.mojo:build-helper-maven-plugin)
Requires:         mvn(org.codehaus.mojo:buildnumber-maven-plugin)
Source44: import.info

%description
The Project Object Model files for the apache-commons packages.

%prep
%setup -q -n %{short_name}-%{version}

# Plugin is not in fedora
%pom_remove_plugin org.apache.commons:commons-build-plugin
%pom_remove_plugin org.apache.maven.plugins:maven-scm-publish-plugin

%pom_remove_plugin :maven-site-plugin

%pom_xpath_remove "pom:profile[pom:id='animal-sniffer']"

%build
%mvn_build

%install
%mvn_install

%files -f .mfiles
%doc LICENSE.txt NOTICE.txt RELEASE-NOTES.txt

%changelog
* Fri Dec 16 2016 Igor Vlasenko <viy@altlinux.ru> 0:40-alt1_2jpp8
- new version

* Fri Nov 25 2016 Igor Vlasenko <viy@altlinux.ru> 0:39-alt1_2jpp8
- new version

* Wed Feb 03 2016 Igor Vlasenko <viy@altlinux.ru> 0:38-alt1_1jpp8
- new version

* Fri Jan 22 2016 Igor Vlasenko <viy@altlinux.ru> 0:38-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

* Sun Sep 14 2014 Igor Vlasenko <viy@altlinux.ru> 0:32-alt1_2jpp7
- new version

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 0:26-alt1_5jpp7
- fc update

* Thu Aug 07 2014 Igor Vlasenko <viy@altlinux.ru> 0:22-alt2_4jpp7
- rebuild with maven-local

* Tue Sep 18 2012 Igor Vlasenko <viy@altlinux.ru> 0:22-alt1_4jpp7
- new version

* Fri Aug 24 2012 Igor Vlasenko <viy@altlinux.ru> 0:12-alt6_2jpp6
- build with maven-jxr

* Mon Apr 16 2012 Igor Vlasenko <viy@altlinux.ru> 0:12-alt5_2jpp6
- dropped commons-build-plugin dependency

* Thu Sep 29 2011 Igor Vlasenko <viy@altlinux.ru> 0:12-alt4_2jpp6
- added maven-plugin-bundle as replacement for felix-maven

* Wed Sep 28 2011 Igor Vlasenko <viy@altlinux.ru> 0:12-alt3_2jpp6
- removed felix-maven from requires

* Wed Jan 05 2011 Igor Vlasenko <viy@altlinux.ru> 0:12-alt2_2jpp6
- removed mojo-maven2-plugin-* from requires

* Fri Dec 10 2010 Igor Vlasenko <viy@altlinux.ru> 0:12-alt1_2jpp6
- new jpp release

* Mon Oct 18 2010 Igor Vlasenko <viy@altlinux.ru> 0:12-alt1_1jpp6
- fixed init script

