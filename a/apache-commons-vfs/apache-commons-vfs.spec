Epoch: 0
Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires: rpm-build-java
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
# fedora bcond_with macro
%define bcond_with() %{expand:%%{?_with_%{1}:%%global with_%{1} 1}}
%define bcond_without() %{expand:%%{!?_without_%{1}:%%global with_%{1} 1}}
# redefine altlinux specific with and without
%define with()         %{expand:%%{?with_%{1}:1}%%{!?with_%{1}:0}}
%define without()      %{expand:%%{?with_%{1}:0}%%{!?with_%{1}:1}}
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
# hadoop was retired
%bcond_without hadoop
%bcond_without ftp
%bcond_without ssh

Name:          apache-commons-vfs
Version:       2.1
Release:       alt1_12jpp8
Summary:       Commons Virtual File System
License:       ASL 2.0
Url:           http://commons.apache.org/vfs/
Source0:       http://www.apache.org/dist/commons/vfs/source/commons-vfs-%{version}-src.tar.gz

BuildRequires:  maven-local
BuildRequires:  mvn(commons-httpclient:commons-httpclient)
BuildRequires:  mvn(commons-logging:commons-logging)
BuildRequires:  mvn(commons-net:commons-net)
BuildRequires:  mvn(org.apache.ant:ant)
BuildRequires:  mvn(org.apache.commons:commons-collections4)
BuildRequires:  mvn(org.apache.commons:commons-compress)
BuildRequires:  mvn(org.apache.commons:commons-parent:pom:)
BuildRequires:  mvn(org.apache.maven.plugins:maven-antrun-plugin)
%if %{with hadoop}
BuildRequires:  mvn(org.apache.hadoop:hadoop-common)
BuildRequires:  mvn(org.apache.hadoop:hadoop-hdfs)
%endif
%if %{with ssh}
BuildRequires:  mvn(com.jcraft:jsch)
%endif
%if %{with ftp}
BuildRequires:  mvn(org.apache.ftpserver:ftpserver-core)
%endif

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
Requires:      %{name} = %{?epoch:%epoch:}%{version}-%{release}

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

%pom_remove_plugin :apache-rat-plugin

# Convert from dos to unix line ending
for file in LICENSE.txt NOTICE.txt README.txt RELEASE-NOTES.txt; do
 sed -i.orig 's|\r||g' $file
 touch -r $file.orig $file
 rm $file.orig
done

# Disable unwanted module
%pom_disable_module dist

# Fix ant gId
%pom_change_dep -r :ant org.apache.ant:
# Upadate bouncycastle aId
%pom_change_dep -r :bcprov-jdk16 :bcprov-jdk15on

# Remove unwanted dependency jackrabbit-{standalone,webdav}
%pom_remove_dep -r org.apache.jackrabbit:

rm -rf core/src/{main,test}/java/org/apache/commons/vfs2/provider/webdav

# Use old version of sshd-core
%pom_remove_dep -r :sshd-core

# hadoop has been retired
%if %{without hadoop}
%pom_remove_dep -r org.apache.hadoop
rm -r core/src/{main,test}/java/org/apache/commons/vfs2/provider/hdfs
%endif

# not really needed
%pom_remove_plugin :maven-checkstyle-plugin
%pom_remove_plugin :findbugs-maven-plugin

%if %{without ssh}
%pom_remove_dep -r :jsch
rm -r core/src/{main,test}/java/org/apache/commons/vfs2/provider/sftp
rm examples/src/main/java/org/apache/commons/vfs2/libcheck/SftpCheck.java
%endif

%if %{without ftp}
%pom_remove_dep -r :ftpserver-core
rm -r core/src/{main,test}/java/org/apache/commons/vfs2/provider/ftps
%endif


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
%mvn_build -sf

%install
%mvn_install

mkdir -p %{buildroot}%{_sysconfdir}/ant.d
echo "ant commons-logging commons-vfs" > commons-vfs
install -p -m 644 commons-vfs %{buildroot}%{_sysconfdir}/ant.d/commons-vfs

%files -f .mfiles-commons-vfs2
%doc README.txt RELEASE-NOTES.txt
%doc --no-dereference LICENSE.txt NOTICE.txt

%files examples -f .mfiles-commons-vfs2-examples
%files project -f .mfiles-commons-vfs2-project
%doc --no-dereference LICENSE.txt NOTICE.txt

%files javadoc -f .mfiles-javadoc
%doc --no-dereference LICENSE.txt NOTICE.txt

%files ant
%config %{_sysconfdir}/ant.d/commons-vfs

%changelog
* Sun Apr 15 2018 Igor Vlasenko <viy@altlinux.ru> 0:2.1-alt1_12jpp8
- java update

* Thu Nov 09 2017 Igor Vlasenko <viy@altlinux.ru> 0:2.1-alt1_11jpp8
- fc27 update

* Sun Oct 22 2017 Igor Vlasenko <viy@altlinux.ru> 0:2.1-alt1_10jpp8
- new jpp release

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

