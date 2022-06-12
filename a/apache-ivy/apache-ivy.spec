Epoch: 0
Group: Development/Java
BuildRequires: /proc rpm-build-java
BuildRequires: jpackage-default
# fedora bcond_with macro
%define bcond_with() %{expand:%%{?_with_%{1}:%%global with_%{1} 1}}
%define bcond_without() %{expand:%%{!?_without_%{1}:%%global with_%{1} 1}}
# redefine altlinux specific with and without
%define with()         %{expand:%%{?with_%{1}:1}%%{!?with_%{1}:0}}
%define without()      %{expand:%%{?with_%{1}:0}%%{!?with_%{1}:1}}
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%bcond_without httpclient
%bcond_without oro
%bcond_with vfs
%bcond_without sftp

%global jarname ivy

Name:           apache-%{jarname}
Version:        2.5.0
Release:        alt1_10jpp11
Summary:        Java-based dependency manager
License:        ASL 2.0
URL:            https://ant.apache.org/ivy
BuildArch:      noarch

Source0:        https://archive.apache.org/dist/ant/%{jarname}/%{version}/%{name}-%{version}-src.tar.gz
Source1:        https://archive.apache.org/dist/ant/%{jarname}/%{version}/%{name}-%{version}-src.tar.gz.asc
Source2:        https://archive.apache.org/dist/ant/KEYS
Source3:        https://repo1.maven.org/maven2/org/apache/ivy/%{jarname}/%{version}/%{jarname}-%{version}.pom

# Non-upstreamable.  Add /etc/ivy/ivysettings.xml at the end list of
# settings files Ivy tries to load.  This file will be used only as
# last resort, when no other setting files exist.
Patch0:         00-global-settings.patch

BuildRequires:  gnupg2
BuildRequires:  maven-local
BuildRequires:  mvn(org.apache.ant:ant)
BuildRequires:  mvn(org.apache.maven.plugins:maven-antrun-plugin)
BuildRequires:  mvn(org.bouncycastle:bcpg-jdk15on)
BuildRequires:  mvn(org.bouncycastle:bcprov-jdk15on)

%if %{with httpclient}
BuildRequires:  mvn(org.apache.httpcomponents:httpclient)
%endif

%if %{with oro}
BuildRequires:  mvn(oro:oro)
%endif

%if %{with vfs}
BuildRequires:  mvn(org.apache.commons:commons-vfs2)
%endif

%if %{with sftp}
BuildRequires:  mvn(com.jcraft:jsch)
BuildRequires:  mvn(com.jcraft:jsch.agentproxy.connector-factory)
BuildRequires:  mvn(com.jcraft:jsch.agentproxy.jsch)
%endif

Provides:       ivy = %{version}-%{release}
Source44: import.info
AutoReqProv: yes,noosgi
Obsoletes: ivy < 2

%description
Apache Ivy is a tool for managing (recording, tracking, resolving and
reporting) project dependencies.  It is designed as process agnostic and is
not tied to any methodology or structure. while available as a standalone
tool, Apache Ivy works particularly well with Apache Ant providing a number
of powerful Ant tasks ranging from dependency resolution to dependency
reporting and publication.

%{?javadoc_package}

%prep


%setup -q
%patch0 -p1


# Don't hardcode sysconfdir path
sed -i 's:/etc/ivy/:%{_sysconfdir}/ivy/:' src/java/org/apache/ivy/ant/IvyAntSettings.java

find -type f '(' -iname '*.jar' -o -iname '*.class' ')' -print -delete

cp %{SOURCE3} pom.xml

%pom_remove_parent

# apparently this is not a dependency, reporting upstream
%pom_remove_dep :jsch.agentproxy

%if %{without httpclient}
%pom_remove_dep :httpclient
rm src/java/org/apache/ivy/util/url/HttpClientHandler.java
%endif

%if %{without oro}
%pom_remove_dep :oro
rm src/java/org/apache/ivy/plugins/matcher/GlobPatternMatcher.java
%endif

%if %{without vfs}
%pom_remove_dep :commons-vfs2
rm src/java/org/apache/ivy/plugins/repository/vfs/VfsRepository.java
rm src/java/org/apache/ivy/plugins/repository/vfs/VfsResource.java
rm src/java/org/apache/ivy/plugins/repository/vfs/ivy_vfs.xml
rm src/java/org/apache/ivy/plugins/resolver/VfsResolver.java
%endif

%if %{without sftp}
%pom_remove_dep :jsch
%pom_remove_dep :jsch.agentproxy
%pom_remove_dep :jsch.agentproxy.connector-factory
%pom_remove_dep :jsch.agentproxy.jsch
rm src/java/org/apache/ivy/plugins/repository/sftp/SFTPRepository.java
rm src/java/org/apache/ivy/plugins/repository/sftp/SFTPResource.java
rm src/java/org/apache/ivy/plugins/repository/ssh/AbstractSshBasedRepository.java
rm src/java/org/apache/ivy/plugins/repository/ssh/RemoteScpException.java
rm src/java/org/apache/ivy/plugins/repository/ssh/Scp.java
rm src/java/org/apache/ivy/plugins/repository/ssh/SshCache.java
rm src/java/org/apache/ivy/plugins/repository/ssh/SshRepository.java
rm src/java/org/apache/ivy/plugins/repository/ssh/SshResource.java
rm src/java/org/apache/ivy/plugins/resolver/AbstractSshBasedResolver.java
rm src/java/org/apache/ivy/plugins/resolver/SFTPResolver.java
rm src/java/org/apache/ivy/plugins/resolver/SshResolver.java
%endif

%pom_xpath_inject pom:project '
<build>
  <sourceDirectory>src/java</sourceDirectory>
  <resources>
    <resource>
      <directory>src/java</directory>
      <includes>
        <include>**/*.css</include>
        <include>**/*.ent</include>
        <include>**/*.png</include>
        <include>**/*.properties</include>
        <include>**/*.template</include>
        <include>**/*.xml</include>
        <include>**/*.xsd</include>
        <include>**/*.xsl</include>
      </includes>
      <excludes>
        <exclude>**/*.java</exclude>
      </excludes>
    </resource>
  </resources>
</build>'

%pom_add_plugin :maven-antrun-plugin '
<executions>
  <execution>
    <id>compile</id>
    <phase>compile</phase>
    <goals>
      <goal>run</goal>
    </goals>
    <configuration>
      <target>
        <!-- copy licenses -->
        <copy file="${project.basedir}/NOTICE" 
          tofile="${project.build.outputDirectory}/META-INF/NOTICE"/> 
        <copy file="${project.basedir}/LICENSE" 
          tofile="${project.build.outputDirectory}/META-INF/LICENSE"/> 

        <!-- copy settings files for backward compatibility with ivyconf naming -->
        <copy file="${project.build.outputDirectory}/org/apache/ivy/core/settings/ivysettings-local.xml" 
          tofile="${project.build.outputDirectory}/org/apache/ivy/core/settings/ivyconf-local.xml"/> 
        <copy file="${project.build.outputDirectory}/org/apache/ivy/core/settings/ivysettings-default-chain.xml" 
          tofile="${project.build.outputDirectory}/org/apache/ivy/core/settings/ivyconf-default-chain.xml"/> 
        <copy file="${project.build.outputDirectory}/org/apache/ivy/core/settings/ivysettings-main-chain.xml" 
          tofile="${project.build.outputDirectory}/org/apache/ivy/core/settings/ivyconf-main-chain.xml"/> 
        <copy file="${project.build.outputDirectory}/org/apache/ivy/core/settings/ivysettings-public.xml" 
          tofile="${project.build.outputDirectory}/org/apache/ivy/core/settings/ivyconf-public.xml"/> 
        <copy file="${project.build.outputDirectory}/org/apache/ivy/core/settings/ivysettings-shared.xml" 
          tofile="${project.build.outputDirectory}/org/apache/ivy/core/settings/ivyconf-shared.xml"/> 
        <copy file="${project.build.outputDirectory}/org/apache/ivy/core/settings/ivysettings.xml" 
          tofile="${project.build.outputDirectory}/org/apache/ivy/core/settings/ivyconf.xml"/> 

        <!-- copy antlib for backward compatibility with fr.jayasoft.ivy package -->
        <copy file="${project.build.outputDirectory}/org/apache/ivy/ant/antlib.xml"
          todir="${project.build.outputDirectory}/fr/jayasoft/ivy/ant"/>

        <!--
          there is a default Bundle-Version attribute in the source MANIFEST, used to ease
          development in eclipse.
          We remove this line to make sure we get the Bundle-Version as set in the jar task
        -->
        <copy file="${project.basedir}/META-INF/MANIFEST.MF" tofile="${project.build.outputDirectory}/META-INF/MANIFEST.MF">
          <filterchain>
            <replaceregex pattern="Bundle-Version:.*" replace="Bundle-Version: ${project.version}" byline="true"/>
            <replaceregex pattern="Bundle-RequiredExecutionEnvironment:.*" replace="Bundle-RequiredExecutionEnvironment: ${java.version} (${java.vendor})" byline="true"/>
          </filterchain>
        </copy>
      </target>
    </configuration>
  </execution>
</executions>'

%pom_add_plugin :maven-jar-plugin '
<configuration>
  <archive>
    <manifestEntries>
      <Specification-Title>Apache Ivy with Ant tasks</Specification-Title>
      <Specification-Version>${project.version}</Specification-Version>
      <Specification-Vendor>Apache Software Foundation</Specification-Vendor>
      <Implementation-Title>${project.groupId}</Implementation-Title>
      <Implementation-Version>${project.version}</Implementation-Version>
      <Implementation-Vendor>Apache Software Foundation</Implementation-Vendor>
      <Implementation-Vendor-Id>org.apache</Implementation-Vendor-Id>
      <Extension-name>${project.groupId}</Extension-name>
      <Build-Version>${project.version}</Build-Version>
    </manifestEntries>
    <manifestFile>${project.build.outputDirectory}/META-INF/MANIFEST.MF</manifestFile>
  </archive>
</configuration>'

%mvn_alias : jayasoft:ivy
%mvn_file : %{name}/ivy ivy

# Remove prebuilt documentation
rm -rf asciidoc

# girar noarch diff
sed -i -e s,yyyyMMddHHmmss,yyyyMMddHH, build.xml


%build
#export JAVA_HOME=%{_jvmdir}/java-11
%mvn_build -f -- -Dmaven.compiler.source=1.8 -Dmaven.compiler.target=1.8 -Dmaven.compiler.release=8

%install
%mvn_install

mkdir -p %{buildroot}%{_sysconfdir}/ant.d
echo "apache-ivy/ivy" > %{buildroot}%{_sysconfdir}/ant.d/%{name}

%files -f .mfiles
%doc --no-dereference LICENSE NOTICE
%doc README.adoc
%{_sysconfdir}/ant.d/%{name}

%changelog
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

