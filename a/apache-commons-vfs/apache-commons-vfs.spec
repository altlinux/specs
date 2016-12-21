Epoch: 0
Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
# END SourceDeps(oneline)
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
# fedora bcond_with macro
%define bcond_with() %{expand:%%{?_with_%{1}:%%global with_%{1} 1}}
%define bcond_without() %{expand:%%{!?_without_%{1}:%%global with_%{1} 1}}
# redefine altlinux specific with and without
%define with()         %{expand:%%{?with_%{1}:1}%%{!?with_%{1}:0}}
%define without()      %{expand:%%{?with_%{1}:0}%%{!?with_%{1}:1}}
# hadoop was retired
#def_with hadoop
%bcond_with hadoop
Name:          apache-commons-vfs
Version:       2.1
Release:       alt1_5jpp8
Summary:       Commons Virtual File System
License:       ASL 2.0
Url:           http://commons.apache.org/vfs/
Source0:       http://www.apache.org/dist/commons/vfs/source/commons-vfs-%{version}-src.tar.gz

BuildRequires: maven-local
BuildRequires: mvn(com.jcraft:jsch)
BuildRequires: mvn(commons-httpclient:commons-httpclient)
BuildRequires: mvn(commons-io:commons-io)
BuildRequires: mvn(commons-logging:commons-logging)
BuildRequires: mvn(commons-net:commons-net)
BuildRequires: mvn(javax.ws.rs:jsr311-api)
BuildRequires: mvn(junit:junit)
BuildRequires: mvn(org.apache.ant:ant)
%if %{with hadoop}
BuildRequires: mvn(org.apache.hadoop:hadoop-common)
BuildRequires: mvn(org.apache.hadoop:hadoop-hdfs)
BuildRequires: mvn(org.apache.hadoop:hadoop-common::tests:)
BuildRequires: mvn(org.apache.hadoop:hadoop-hdfs::tests:)
%endif
BuildRequires: mvn(org.apache.commons:commons-collections4)
BuildRequires: mvn(org.apache.commons:commons-compress)
BuildRequires: mvn(org.apache.commons:commons-lang3)
BuildRequires: mvn(org.apache.commons:commons-parent:pom:)
BuildRequires: mvn(org.apache.ftpserver:ftpserver-core)
BuildRequires: mvn(org.apache.httpcomponents:httpcore-nio)
BuildRequires: mvn(org.apache.maven.plugins:maven-antrun-plugin)
BuildRequires: mvn(org.bouncycastle:bcprov-jdk15on)
BuildRequires: mvn(org.slf4j:slf4j-api)
BuildRequires: /usr/bin/perl

BuildArch:     noarch
Provides:      %{name}2 = %{version}-%{release}
Source44: import.info

%description
Commons VFS provides a single API for accessing various
different file systems. It presents a uniform view of the
files from various different sources, such as the files on
local disk, on an HTTP server, or inside a Zip archive.
Some of the features of Commons VFS are:
* A single consistent API for accessing files of different
 types.
* Support for numerous file system types.
* Caching of file information. Caches information in-JVM,
 and optionally can cache remote file information on the
 local file system.
* Event delivery.
* Support for logical file systems made up of files from
 various different file systems.
* Utilities for integrating Commons VFS into applications,
 such as a VFS-aware ClassLoader and URLStreamHandlerFactory.
* A set of VFS-enabled Ant tasks.

%package ant
Group: Development/Java
Summary:       Development files for Commons VFS
Requires:      %{name} = %{version}

%description ant
This package enables support for the Commons VFS ant tasks.

%package examples
Group: Development/Java
Summary:       Commons VFS Examples

%description examples
VFS is a Virtual File System library - Examples.

%package project
Group: Development/Java
Summary:       Commons VFS Parent POM

%description project
Commons VFS Parent POM.

%package javadoc
Group: Development/Java
Summary:       Javadoc for %{name}
BuildArch: noarch

%description javadoc
This package contains javadoc for %{name}.

%prep
%setup -q -n commons-vfs-%{version}
perl -pi -e 's/\r$//g;' *.txt

# Disable unwanted module
%pom_disable_module dist

# Fix ant gId
%pom_change_dep -r :ant org.apache.ant:
# Upadate bouncycastle aId
%pom_change_dep -r :bcprov-jdk16 :bcprov-jdk15on

# Remove unwanted dependency jackrabbit-{standalone,webdav}
%pom_remove_dep -r org.apache.jackrabbit:
# Fix plugin configuration
%pom_xpath_inject "pom:project/pom:reporting/pom:plugins/pom:plugin[pom:artifactId='maven-javadoc-plugin']/pom:configuration" "
<excludePackageNames>*.webdav.*</excludePackageNames>"

# Disable jackrabbit-webdav support
%pom_add_plugin org.apache.maven.plugins:maven-compiler-plugin core "
<executions>
  <execution>
    <id>default-compile</id>
    <phase>compile</phase>
    <configuration>
      <excludes>
       <exclude>**/webdav/*</exclude>
      </excludes>
    </configuration>
    <goals>
      <goal>compile</goal>
    </goals>
  </execution>
  <execution>
    <id>default-testCompile</id>
    <phase>test-compile</phase>
    <configuration>
      <testExcludes>
       <exclude>**/webdav/test/*</exclude>
      </testExcludes>
    </configuration>
    <goals>
      <goal>testCompile</goal>
    </goals>
  </execution>
</executions>"

rm -rf core/src/main/java/org/apache/commons/vfs2/provider/webdav
rm -rf core/src/test/java/org/apache/commons/vfs2/provider/webdav
sed -i 's|"webdav",||' core/src/test/java/org/apache/commons/vfs2/util/DelegatingFileSystemOptionsBuilderTest.java

rm core/src/test/java/org/apache/commons/vfs2/provider/ram/test/CustomRamProviderTest.java

# UnknownHostException: www.apache.org
rm core/src/test/java/org/apache/commons/vfs2/provider/http/test/GetContentInfoFunctionalTest.java \
 core/src/test/java/org/apache/commons/vfs2/provider/https/test/GetContentInfoFunctionalTest.java
# org.apache.commons.vfs2.FileSystemException: Could not connect to FTP server on "localhost".
rm core/src/test/java/org/apache/commons/vfs2/test/ProviderWriteAppendTests.java \
 core/src/test/java/org/apache/commons/vfs2/test/ProviderWriteTests.java
sed -i /ProviderWriteAppendTests/d core/src/test/java/org/apache/commons/vfs2/test/ProviderTestSuite.java
sed -i /ProviderWriteTests/d core/src/test/java/org/apache/commons/vfs2/test/ProviderTestSuite.java
# java.lang.IllegalStateException: The embedded HTTP server has not completed startup, increase wait time
rm core/src/test/java/org/apache/commons/vfs2/provider/http/test/HttpProviderTestCase.java \
 core/src/test/java/org/apache/commons/vfs2/provider/url/test/UrlProviderHttpTestCase.java
# Use old version of sshd-core
rm core/src/test/java/org/apache/commons/vfs2/provider/sftp/test/SftpProviderTestCase.java
%pom_remove_dep -r :sshd-core

# hadoop has been retired
%if %{without hadoop}
%pom_remove_dep -r org.apache.hadoop
rm -r core/src/{main,test}/java/org/apache/commons/vfs2/provider/hdfs
%endif

# not really needed
%pom_remove_plugin :maven-checkstyle-plugin
%pom_remove_plugin :findbugs-maven-plugin

# Fix installation directory and symlink
%mvn_file :commons-vfs2 %{name}
%mvn_file :commons-vfs2 %{name}2
%mvn_file :commons-vfs2 commons-vfs
%mvn_file :commons-vfs2 commons-vfs2
%mvn_file :commons-vfs2-examples %{name}-examples
%mvn_file :commons-vfs2-examples %{name}2-examples
%mvn_file :commons-vfs2-examples commons-vfs-examples
%mvn_file :commons-vfs2-examples commons-vfs2-examples

%mvn_alias :commons-vfs2 "org.apache.commons:commons-vfs" "commons-vfs:commons-vfs"
%mvn_alias :commons-vfs2-examples "org.apache.commons:commons-vfs-examples" "commons-vfs:commons-vfs-examples"

%build

# @ random tests fails
# junit.framework.TestSuite@74e52303(org.apache.commons.vfs2.test.ProviderTestSuite)  Time elapsed: 4.092 sec  <<< ERROR!
# java.lang.NullPointerException
%mvn_build -s -- -Dmaven.test.failure.ignore=true

%install
%mvn_install

mkdir -p %{buildroot}%{_sysconfdir}/ant.d
echo "ant commons-logging commons-vfs" > commons-vfs
install -p -m 644 commons-vfs %{buildroot}%{_sysconfdir}/ant.d/commons-vfs

%files -f .mfiles-commons-vfs2
%doc README.txt RELEASE-NOTES.txt
%doc LICENSE.txt NOTICE.txt

%files examples -f .mfiles-commons-vfs2-examples
%files project -f .mfiles-commons-vfs2-project
%doc LICENSE.txt NOTICE.txt

%files javadoc -f .mfiles-javadoc
%doc LICENSE.txt NOTICE.txt

%files ant
%config %{_sysconfdir}/ant.d/commons-vfs

%changelog
* Fri Dec 16 2016 Igor Vlasenko <viy@altlinux.ru> 0:2.1-alt1_5jpp8
- new version

* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 0:2.0-alt4_17jpp8
- new fc release

* Wed Feb 03 2016 Igor Vlasenko <viy@altlinux.ru> 0:2.0-alt4_16jpp8
- new version

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 0:2.0-alt4_11jpp7
- new release

* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 0:2.0-alt4_6jpp7
- new release

* Mon Jul 14 2014 Igor Vlasenko <viy@altlinux.ru> 0:2.0-alt4_4jpp7
- NMU rebuild to move poms and fragments

* Sat Sep 08 2012 Igor Vlasenko <viy@altlinux.ru> 0:2.0-alt3_4jpp7
- fc version

* Sat Sep 08 2012 Igor Vlasenko <viy@altlinux.ru> 0:2.0-alt3_0.r834424.5jpp6
- fixed jackrabbit dependency

* Mon Mar 19 2012 Igor Vlasenko <viy@altlinux.ru> 0:2.0-alt2_0.r834424.5jpp6
- fixed build with maven3

* Mon Feb 14 2011 Igor Vlasenko <viy@altlinux.ru> 0:2.0-alt1_0.r834424.5jpp6
- new version

