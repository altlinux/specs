Name:           maven-wagon
Version:        3.5.3
Release:        alt2.1

Summary:        Tools to manage artifacts and deployment
License:        Apache-2.0
Group:          Development/Java
URL:            https://maven.apache.org/wagon
VCS:            https://github.com/apache/maven-wagon

Source0:        wagon-%version-source-release.zip

BuildRequires(pre):  maven-local
BuildRequires:  jpackage-default
BuildRequires:  unzip

BuildRequires:  mvn(org.apache.maven:maven-parent:pom:)
BuildRequires:  mvn(org.codehaus.plexus:plexus-component-metadata)
BuildRequires:  mvn(commons-net:commons-net)
BuildRequires:  mvn(org.apache.maven.plugins:maven-shade-plugin)
BuildRequires:  mvn(org.apache.maven.scm:maven-scm-api)
BuildRequires:  mvn(org.codehaus.plexus:plexus-interactivity-api)
BuildRequires:  mvn(com.jcraft:jsch.agentproxy.connector-factory)
BuildRequires:  mvn(com.jcraft:jsch.agentproxy.jsch)

BuildArch:      noarch

%description
Maven Wagon is a transport abstraction that is used in Maven's
artifact and repository handling code. Currently wagon has the
following providers:
* File
* HTTP
* FTP
* SSH/SCP
* WebDAV
* SCM (in progress)

%javadoc_package

%prep
%setup -n wagon-%version

%pom_remove_plugin :animal-sniffer-maven-plugin

%pom_disable_module wagon-provider-test
%pom_disable_module wagon-ssh-common-test wagon-providers
%pom_disable_module wagon-webdav-jackrabbit wagon-providers
%pom_disable_module wagon-tck-http wagon-tcks

%mvn_file :wagon-{*} %name/@1
%mvn_package :wagon

%build
%mvn_build -f -- -Dmaven.compiler.source=1.8 -Dmaven.compiler.target=1.8 -Dmaven.javadoc.source=1.8 -Dmaven.compiler.release=8

# Maven requires Wagon HTTP with classifier "shaded"
%mvn_alias :wagon-http :::shaded:

%install
%mvn_install

%files -f .mfiles
%doc LICENSE NOTICE DEPENDENCIES *.md

%changelog
* Wed Mar 04 2026 Evgeniy Serov <scala@altlinux.org> 3.5.3-alt2.1
- Cosmetic fixes.

* Sun Feb 22 2026 Evgeniy Serov <scala@altlinux.org> 3.5.3-alt2
- Enabled previously disabled modules.

* Wed Apr 30 2025 Anton Meleshnikov <alton@altlinux.org> 0:3.5.3-alt1
- New version 3.5.3.

* Sun Jul 10 2022 Igor Vlasenko <viy@altlinux.org> 0:3.4.2-alt2_4jpp11
- added proper Obsoletes/Confilcts: on old wagon

* Tue Aug 17 2021 Igor Vlasenko <viy@altlinux.org> 0:3.4.2-alt1_4jpp11
- update

* Thu Jun 10 2021 Igor Vlasenko <viy@altlinux.org> 0:3.4.2-alt1_1jpp11
- new version

* Tue Jun 01 2021 Igor Vlasenko <viy@altlinux.org> 0:3.4.1-alt1_3jpp11
- new version

* Fri Oct 09 2020 Igor Vlasenko <viy@altlinux.ru> 0:3.3.3-alt1_4jpp8
- new version

* Sat Jul 13 2019 Igor Vlasenko <viy@altlinux.ru> 0:3.2.0-alt1_2jpp8
- new version

* Thu Jun 20 2019 Igor Vlasenko <viy@altlinux.ru> 0:3.1.0-alt1_2jpp8
- new version

* Wed Nov 22 2017 Igor Vlasenko <viy@altlinux.ru> 0:3.0.0-alt1_1jpp8
- new version

* Tue Nov 14 2017 Igor Vlasenko <viy@altlinux.ru> 0:2.10-alt1_4jpp8
- fc27 update

* Sun Oct 22 2017 Igor Vlasenko <viy@altlinux.ru> 0:2.10-alt1_3jpp8
- new jpp release

* Tue Nov 29 2016 Igor Vlasenko <viy@altlinux.ru> 0:2.10-alt1_2jpp8
- new version

* Fri Feb 05 2016 Igor Vlasenko <viy@altlinux.ru> 0:2.9-alt1_4jpp8
- java 8 mass update

* Wed Jan 20 2016 Igor Vlasenko <viy@altlinux.ru> 0:2.9-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

* Tue Aug 26 2014 Igor Vlasenko <viy@altlinux.ru> 0:2.5-alt1_2jpp7
- new release

* Sat Aug 23 2014 Igor Vlasenko <viy@altlinux.ru> 0:2.4-alt0.2jpp
- rebuild to add provides

* Fri Aug 22 2014 Igor Vlasenko <viy@altlinux.ru> 0:2.4-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

* Thu Aug 21 2014 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt10_6jpp7
- added maven-local BR:

* Mon Oct 01 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt9_6jpp7
- new fc release

* Fri Mar 30 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt9_3jpp7
- complete build

* Sun Mar 11 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt8jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

