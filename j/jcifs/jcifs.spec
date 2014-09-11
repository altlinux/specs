Epoch: 0
Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-java
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-compat
Name:          jcifs
Version:       1.3.17
Release:       alt1_10jpp7
Summary:       Common Internet File System Client in 100% Java
# Licenses:
#   src/jcifs/util/DES.java: BSD and MIT
#   src/jcifs/util/MD4.java: BSD
#   all the rest:            LGPLv2+
License:       LGPLv2+ and BSD and MIT
URL:           http://jcifs.samba.org/
Source0:       http://jcifs.samba.org/src/%{name}-%{version}.tgz
Source1:       http://mirrors.ibiblio.org/pub/mirrors/maven2/%{name}/%{name}/%{version}/%{name}-%{version}.pom
# fix javac executable
Patch0:        %{name}-%{version}-build.patch
BuildRequires: jpackage-utils

BuildRequires: ant

BuildRequires: tomcat-servlet-3.0-api
Requires:      tomcat-servlet-3.0-api

Requires:      jpackage-utils
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
Summary:       Javadocs for %{name}
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
Requires:      %{name} = %{?epoch:%epoch:}%{version}-%{release}

%description demo
Demonstrations and samples for %{name}.

%prep
%setup -q -n %{name}_%{version}
find -name '*.class' -delete
find -name '*.jar' -delete
%patch0 -p0
cp -p %{SOURCE1} pom.xml
%pom_remove_plugin :maven-gpg-plugin

%build

export CLASSPATH=$(build-classpath tomcat-servlet-3.0-api)
export OPT_JAR_LIST=:
%ant jar javadoc docs

%install

mkdir -p %{buildroot}%{_javadir}
install -p -m 644 %{name}-%{version}.jar %{buildroot}%{_javadir}/%{name}.jar

mkdir -p %{buildroot}%{_mavenpomdir}
install -pm 644 pom.xml %{buildroot}%{_mavenpomdir}/JPP-%{name}.pom
%add_maven_depmap -a org.samba.jcifs:jcifs

mkdir -p %{buildroot}%{_javadocdir}/%{name}
cp -pr docs/api/* %{buildroot}%{_javadocdir}/%{name}

mkdir -p %{buildroot}%{_datadir}/%{name}/examples
cp -pr examples/*.java  %{buildroot}%{_datadir}/%{name}/examples

%files -f .mfiles
%doc LICENSE.txt README.txt docs/*.{html,txt,gif}

%files javadoc
%{_javadocdir}/%{name}
%doc LICENSE.txt

%files demo
%{_datadir}/%{name}/*
%doc LICENSE.txt

%changelog
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

