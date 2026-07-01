%def_without vfs

Name:           apache-ivy
Version:        2.5.3
Release:        alt2

Summary:        Java-based dependency manager
License:        Apache-2.0
Group:          Development/Java
URL:            https://ant.apache.org/ivy
VCS:            https://github.com/apache/ant-ivy

Source0:        %name-%version.tar

Patch0:         00-global-settings.patch
Patch1:         java17-pack200.patch

BuildRequires(pre):  rpm-build-java
BuildRequires:  jpackage-default

BuildRequires:  ant
BuildRequires:  ivy-local

BuildRequires:  mvn(org.apache.httpcomponents:httpclient)
BuildRequires:  mvn(oro:oro)
BuildRequires:  mvn(com.jcraft:jsch)
BuildRequires:  mvn(com.jcraft:jsch.agentproxy.connector-factory)
BuildRequires:  mvn(com.jcraft:jsch.agentproxy.jsch)
BuildRequires:  mvn(org.bouncycastle:bcpg-jdk15on)
BuildRequires:  mvn(org.bouncycastle:bcprov-jdk15on)
BuildRequires:  mvn(org.apache.ant:ant-testutil)
BuildRequires:  mvn(org.apache.ant:ant-junit)
BuildRequires:  mvn(org.apache.ant:ant-junit4)
BuildRequires:  mvn(ant-contrib:ant-contrib)
BuildRequires:  mvn(xmlunit:xmlunit)

%if_with vfs
BuildRequires:  mvn(org.apache.commons:commons-vfs2)	
%endif

BuildArch:      noarch

%description
Apache Ivy is a tool for managing (recording, tracking, resolving and
reporting) project dependencies.  It is designed as process agnostic and is
not tied to any methodology or structure. while available as a standalone
tool, Apache Ivy works particularly well with Apache Ant providing a number
of powerful Ant tasks ranging from dependency resolution to dependency
reporting and publication.

%javadoc_package

%prep
%setup
%autopatch -p1

%if_without vfs
%pom_remove_dep :commons-vfs2

rm src/java/org/apache/ivy/plugins/repository/vfs/VfsRepository.java
rm src/java/org/apache/ivy/plugins/repository/vfs/VfsResource.java
rm src/java/org/apache/ivy/plugins/repository/vfs/ivy_vfs.xml
rm src/java/org/apache/ivy/plugins/resolver/VfsResolver.java
%endif

%mvn_file : %name/ivy ivy

rm -rf asciidoc

%pom_xpath_set ivy:publish/@resolver xmvn build.xml

%build
mkdir -p ~/.ant
cp /etc/ant.conf ~/.ant
sed -i '$a JAVA_HOME=/usr/lib/jvm/java-11-openjdk' ~/.ant/ant.conf
 
ant -Divy.mode=local \
    -f build-release.xml \
    release-version jar javadoc publish-local

%install
%mvn_install -J build/reports/api

mkdir -p %buildroot%_sysconfdir/ant.d
echo "apache-ivy/ivy" > %buildroot%_sysconfdir/ant.d/%name

%files -f .mfiles
%doc LICENSE NOTICE
%doc README.adoc
%_sysconfdir/ant.d/%name

%changelog
* Mon Jun 29 2026 Evgeniy Serov <scala@altlinux.org> 2.5.3-alt2
- Fixed FTBFS: fix build on JDK 17 by avoiding Pack200 API.

* Wed Apr 15 2026 Evgeniy Serov <scala@altlinux.org> 2.5.3-alt1
- Updated to 2.5.3.

* Sun Jun 12 2022 Igor Vlasenko <viy@altlinux.org> 0:2.5.0-alt1_10jpp11
- update

* Tue Jun 01 2021 Igor Vlasenko <viy@altlinux.org> 0:2.5.0-alt1_1jpp11
- new version

* Wed May 12 2021 Igor Vlasenko <viy@altlinux.org> 0:2.4.0-alt1_20jpp8
- fc update

* Sun May 09 2021 Igor Vlasenko <viy@altlinux.org> 0:2.4.0-alt1_18jpp8
- update

* Mon May 27 2019 Igor Vlasenko <viy@altlinux.ru> 0:2.4.0-alt1_16jpp8
- new version

* Fri Jun 01 2018 Igor Vlasenko <viy@altlinux.ru> 0:2.4.0-alt1_12jpp8
- java fc28+ update

* Wed May 09 2018 Igor Vlasenko <viy@altlinux.ru> 0:2.4.0-alt1_10jpp8
- java update

* Sat Nov 04 2017 Igor Vlasenko <viy@altlinux.ru> 0:2.4.0-alt1_9jpp8
- new fc release

* Mon Nov 28 2016 Igor Vlasenko <viy@altlinux.ru> 0:2.4.0-alt1_5jpp8
- new fc release

* Fri Feb 05 2016 Igor Vlasenko <viy@altlinux.ru> 0:2.4.0-alt1_4jpp8
- java 8 mass update

* Fri Jan 29 2016 Igor Vlasenko <viy@altlinux.ru> 0:2.4.0-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

* Fri Aug 01 2014 Igor Vlasenko <viy@altlinux.ru> 0:2.3.0-alt1_1jpp7
- new version

* Thu Sep 20 2012 Igor Vlasenko <viy@altlinux.ru> 0:2.2.0-alt3_5jpp7
- fc release

* Sat Sep 08 2012 Igor Vlasenko <viy@altlinux.ru> 0:2.2.0-alt3_1jpp6
- build with new commons-vfs2

* Tue Aug 28 2012 Igor Vlasenko <viy@altlinux.ru> 0:2.2.0-alt2_1jpp6
- fixed build

* Wed Sep 07 2011 Igor Vlasenko <viy@altlinux.ru> 0:2.2.0-alt1_1jpp6
- new version

* Mon Sep 20 2010 Igor Vlasenko <viy@altlinux.ru> 0:2.0.0-alt1_2jpp6
- new version

