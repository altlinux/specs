Epoch: 0
Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
# END SourceDeps(oneline)
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
Name:          jcifs
Version:       1.3.18
Release:       alt1_4jpp8
Summary:       Common Internet File System Client in 100% Java
# Licenses:
#   src/jcifs/util/DES.java: BSD and MIT
#   src/jcifs/util/MD4.java: BSD
#   all the rest:            LGPLv2+
License:       LGPLv2+ and BSD and MIT
URL:           http://jcifs.samba.org/
Source0:       http://jcifs.samba.org/src/%{name}-%{version}.tgz
Source1:       http://mirrors.ibiblio.org/pub/mirrors/maven2/jcifs/jcifs/1.3.17/jcifs-1.3.17.pom
# fix javac executable
Patch0:        %{name}-1.3.17-build.patch
BuildRequires: ant
BuildRequires: javapackages-local
BuildRequires: mvn(javax.servlet:javax.servlet-api)
BuildArch:     noarch
Source44: import.info

%description
The jCIFS SMB client library enables any Java application to remotely
access shared files and directories on SMB file servers (i.e. a
Microsoft Windows "share") in addition to domain, workgroup, and
server enumeration of NetBIOS over TCP/IP networks. It is an advanced
implementation of the CIFS protocol supporting Unicode, batching,
multiplexing of threaded callers, encrypted authentication,
transactions, the Remote Access Protocol (RAP), and much more. It is
licensed under LGPL which means commercial organizations can
legitimately use it with their proprietary code(you just can't sell or
give away a modified binary only version of the library itself without
reciprocation).

%package javadoc
Group: Development/Java
Summary:       Javadoc for %{name}
# Neither DES.java nor MD4.java (see License comment) are documented here
License:       LGPLv2+
BuildArch: noarch

%description javadoc
This package contains the API documentation for %{name}.

%package demo
Group: Development/Java
Summary:       Demo for %{name}
# Files from the directory 'examples' are here, some are under GPLv2+
License:       LGPLv2+ and GPLv2+
Requires:      %{name} = %{version}

%description demo
Demonstrations and samples for %{name}.

%prep
%setup -q -n %{name}_%{version}
find -name '*.class' -delete
find -name '*.jar' -delete
%patch0 -p0
sed -i "s|1.5|1.6|" build.xml
cp -p %{SOURCE1} pom.xml
sed -i "s|<version>1.3.17|<version>%{version}|" pom.xml
%pom_remove_plugin :maven-gpg-plugin

%pom_xpath_set "pom:dependency[pom:groupId = 'javax.servlet']/pom:version" 3.1.0
%pom_xpath_set "pom:dependency[pom:groupId = 'javax.servlet']/pom:artifactId" javax.servlet-api

%mvn_file %{name}:%{name} %{name}
%mvn_alias %{name}:%{name} org.samba.jcifs:jcifs

%build

export CLASSPATH=$(build-classpath glassfish-servlet-api)
export OPT_JAR_LIST=:
%ant jar javadoc docs

%mvn_artifact pom.xml %{name}-%{version}.jar

%install
%mvn_install -J docs/api

mkdir -p %{buildroot}%{_datadir}/%{name}/examples
cp -pr examples/*.java  %{buildroot}%{_datadir}/%{name}/examples

%files -f .mfiles
%doc README.txt docs/*.{html,txt,gif}
%doc LICENSE.txt

%files javadoc -f .mfiles-javadoc
%doc LICENSE.txt

%files demo
%{_datadir}/%{name}/*
%doc LICENSE.txt

%changelog
* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 0:1.3.18-alt1_4jpp8
- new fc release

* Tue Feb 02 2016 Igor Vlasenko <viy@altlinux.ru> 0:1.3.18-alt1_3jpp8
- new version

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 0:1.3.17-alt1_10jpp7
- new release

* Tue Mar 05 2013 Igor Vlasenko <viy@altlinux.ru> 0:1.3.17-alt1_7jpp7
- fc update

* Thu Feb 07 2013 Igor Vlasenko <viy@altlinux.ru> 0:1.3.17-alt1_5jpp7
- fc update

* Wed Sep 19 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.3.17-alt1_4jpp7
- new release

* Mon Jan 16 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.3.16-alt1_1jpp6
- new jpp relase

* Sun Feb 21 2010 Igor Vlasenko <viy@altlinux.ru> 0:1.2.24-alt1_1jpp5
- new jpackage release

* Mon Jul 09 2007 Igor Vlasenko <viy@altlinux.ru> 0:1.2.9-alt1_1jpp1.7
- converted from JPackage by jppimport script

