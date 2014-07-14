Epoch: 0
BuildRequires: /proc
BuildRequires: jpackage-compat
%global base_name vfs
%global short_name commons-%{base_name}
Name:          apache-commons-vfs
Version:       2.0
Release:       alt4_4jpp7
Summary:       Commons Virtual File System
Group:         Development/Java
License:       ASL 2.0
Url:           http://commons.apache.org/%{base_name}/
Source0:       http://www.apache.org/dist/commons/%{base_name}/source/%{short_name}-%{version}-src.tar.gz
# add maven-compiler-plugin configuration
# fix ant gId
# remove/disable jackrabbit-webdav support
# remove org.apache.commons commons-build-plugin
# remove org.codehaus.mojo findbugs-maven-plugin
# remove maven-scm
# remove old vfs stuff
Patch0:        %{name}-%{version}-build.patch

BuildRequires: jpackage-utils
BuildRequires: apache-commons-parent

BuildRequires: maven
BuildRequires: maven-antrun-plugin
BuildRequires: maven-compiler-plugin
BuildRequires: maven-install-plugin
BuildRequires: maven-jar-plugin
BuildRequires: maven-javadoc-plugin
BuildRequires: maven-plugin-bundle
BuildRequires: maven-resources-plugin
BuildRequires: maven-site-plugin
BuildRequires: maven-surefire-plugin
BuildRequires: maven-surefire-provider-junit4

BuildRequires: ant
BuildRequires: apache-commons-collections
BuildRequires: apache-commons-compress
BuildRequires: apache-commons-logging
BuildRequires: apache-commons-net
BuildRequires: jakarta-commons-httpclient
BuildRequires: javamail
BuildRequires: jcifs
BuildRequires: jdom
BuildRequires: jsch

# test deps
BuildRequires: junit4
BuildRequires: slf4j

Requires:      apache-commons-collections
Requires:      apache-commons-compress
Requires:      apache-commons-logging
Requires:      apache-commons-net
Requires:      jakarta-commons-httpclient
Requires:      javamail
Requires:      jcifs
Requires:      jsch

Requires:      jpackage-utils
BuildArch:     noarch
Provides:      %{name}2 = %{version}-%{release}
Provides:      jakarta-%{short_name} = %{version}-%{release}
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
Summary:       Development files for Commons VFS
Group:         Development/Java
Requires:      ant
Requires:      apache-commons-logging
Requires:      %{name} = %{?epoch:%epoch:}%{version}-%{release}

%description ant
This package enables support for the Commons VFS ant tasks.

%package examples
Group:         Development/Java
Summary:       Commons VFS Examples
Requires:      jdom
Requires:      jpackage-utils
Requires:      %{name} = %{?epoch:%epoch:}%{version}-%{release}
Provides:      %{name}2-examples = %{version}-%{release}

%description examples
VFS is a Virtual File System library - Examples.

%package javadoc
Group:         Development/Java
Summary:       Javadoc for %{name}
Requires:      jpackage-utils
BuildArch: noarch

%description javadoc
This package contains javadoc for %{name}.

%prep
%setup -q -n %{short_name}-%{version}
perl -pi -e 's/\r$//g;' *.txt

%patch0 -p1
rm -rf core/src/main/java/org/apache/commons/vfs2/provider/webdav
rm -rf core/src/test/java/org/apache/commons/vfs2/provider/webdav
sed -i 's|"webdav",||' core/src/test/java/org/apache/commons/vfs2/util/DelegatingFileSystemOptionsBuilderTest.java

sed -i "s|<module>dist</module>|<!--module>dist</module-->|" pom.xml

%build

mvn-rpmbuild -Dmaven.test.skip=true -Dmaven.test.failure.ignore=true install javadoc:aggregate

%install

mkdir -p %{buildroot}%{_javadir}
install -m 644 core/target/%{short_name}2-%{version}.jar %{buildroot}%{_javadir}/%{name}.jar
install -m 644 examples/target/%{short_name}2-examples-%{version}.jar %{buildroot}%{_javadir}/%{name}-examples.jar

pushd %{buildroot}%{_javadir}
  ln -s %{name}.jar %{short_name}.jar
  ln -s %{name}-examples.jar %{short_name}-examples.jar
  ln -s %{name}.jar jakarta-%{short_name}.jar
  ln -s %{name}-examples.jar jakarta-%{short_name}-examples.jar
  ln -s %{name}.jar %{name}2.jar
  ln -s %{name}-examples.jar %{name}2-examples.jar
  ln -s %{name}.jar %{short_name}2.jar
  ln -s %{name}-examples.jar %{short_name}2-examples.jar
popd

mkdir -p %{buildroot}%{_mavenpomdir}
install -pm 644 pom.xml %{buildroot}%{_mavenpomdir}/JPP-%{short_name}-project.pom
%add_maven_depmap JPP-%{short_name}-project.pom
install -pm 644 core/pom.xml %{buildroot}%{_mavenpomdir}/JPP-%{short_name}.pom
%add_maven_depmap JPP-%{short_name}.pom %{short_name}.jar -a "org.apache.commons:%{short_name},%{short_name}:%{short_name}"
install -pm 644 examples/pom.xml %{buildroot}%{_mavenpomdir}/JPP-%{short_name}-examples.pom
%add_maven_depmap -f examples JPP-%{short_name}-examples.pom %{short_name}-examples.jar -a "org.apache.commons:%{short_name}-examples,%{short_name}:%{short_name}-examples"

mkdir -p %{buildroot}%{_javadocdir}/%{name}
cp -pr target/site/apidocs/* %{buildroot}%{_javadocdir}/%{name}

mkdir -p %{buildroot}%{_sysconfdir}/ant.d
echo "ant commons-logging %{short_name}" > %{short_name}
install -p -m 644 %{short_name} %{buildroot}%{_sysconfdir}/ant.d/%{short_name}

%files
%{_javadir}/%{name}.jar
%{_javadir}/%{name}2.jar
%{_javadir}/%{short_name}.jar
%{_javadir}/%{short_name}2.jar
%{_javadir}/jakarta-%{short_name}.jar
%{_mavenpomdir}/JPP-%{short_name}.pom
%{_mavenpomdir}/JPP-%{short_name}-project.pom
%{_mavendepmapfragdir}/%{name}
%doc LICENSE.txt NOTICE.txt README.txt RELEASE-NOTES.txt

%files examples
%{_javadir}/%{name}-examples.jar
%{_javadir}/%{name}2-examples.jar
%{_javadir}/%{short_name}-examples.jar
%{_javadir}/%{short_name}2-examples.jar
%{_javadir}/jakarta-%{short_name}-examples.jar
%{_mavenpomdir}/JPP-%{short_name}-examples.pom
%{_mavendepmapfragdir}/%{name}-examples

%files javadoc
%{_javadocdir}/%{name}
%doc LICENSE.txt NOTICE.txt

%files ant
%config %{_sysconfdir}/ant.d/%{short_name}

%changelog
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

