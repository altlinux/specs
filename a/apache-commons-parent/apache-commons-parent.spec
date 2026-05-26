Name:           apache-commons-parent
Version:        99
Release:        alt1

Summary:        Apache Commons Parent
License:        Apache-2.0
Group:          Development/Java
URL:            https://commons.apache.org/commons-parent-pom.html
VCS:            https://github.com/apache/commons-parent

Source0:        %name-%version.tar

BuildRequires(pre):  maven-local
BuildRequires:  jpackage-default

BuildRequires:  mvn(org.apache:apache:pom:)
BuildRequires:  mvn(org.codehaus.mojo:build-helper-maven-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-antrun-plugin)
BuildRequires:  mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-assembly-plugin)

Requires:       mvn(org.codehaus.mojo:build-helper-maven-plugin)

BuildArch:      noarch

%description
The Apache Commons Parent POM provides common settings for all Apache Commons
components.

%prep
%setup

%pom_remove_plugin :maven-source-plugin
%pom_remove_plugin :maven-site-plugin
%pom_remove_plugin :maven-artifact-plugin
%pom_remove_plugin :cyclonedx-maven-plugin
%pom_remove_plugin :spdx-maven-plugin
%pom_remove_plugin :maven-changes-plugin
%pom_remove_plugin :commons-build-plugin
%pom_remove_plugin :apache-rat-plugin
%pom_remove_plugin :maven-scm-publish-plugin
%pom_remove_plugin :versions-maven-plugin
%pom_remove_plugin :moditect-maven-plugin
%pom_remove_plugin :jacoco-maven-plugin
%pom_remove_plugin :japicmp-maven-plugin

%build
%mvn_build

%install
%mvn_install

%files -f .mfiles
%doc LICENSE.txt NOTICE.txt RELEASE-NOTES.txt
%doc *.md

%changelog
* Fri May 15 2026 Evgeniy Serov <scala@altlinux.org> 99-alt1
- Updated to 99.

* Wed Aug 04 2021 Igor Vlasenko <viy@altlinux.org> 0:52-alt1_4jpp11
- update

* Tue Jun 01 2021 Igor Vlasenko <viy@altlinux.org> 0:52-alt1_1jpp11
- new version

* Wed Jan 29 2020 Igor Vlasenko <viy@altlinux.ru> 0:47-alt1_4jpp8
- fc update

* Fri May 24 2019 Igor Vlasenko <viy@altlinux.ru> 0:47-alt1_2jpp8
- new version

* Tue Feb 05 2019 Igor Vlasenko <viy@altlinux.ru> 0:43-alt1_3jpp8
- fc29 update

* Tue May 08 2018 Igor Vlasenko <viy@altlinux.ru> 0:43-alt1_2jpp8
- java update

* Thu Nov 09 2017 Igor Vlasenko <viy@altlinux.ru> 0:42-alt1_4jpp8
- fc27 update

* Mon Oct 30 2017 Igor Vlasenko <viy@altlinux.ru> 0:42-alt1_3jpp8
- new jpp release

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

