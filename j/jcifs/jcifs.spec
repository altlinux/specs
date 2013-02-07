Epoch: 0
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-java
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-compat
Name:          jcifs
Version:       1.3.17
Release:       alt1_5jpp7
Summary:       Common Internet File System Client in 100% Java
Group:         Development/Java
License:       LGPLv2+ and BSD
Url:           http://jcifs.samba.org/
Source0:       http://jcifs.samba.org/src/%{name}-%{version}.tgz
Source1:       http://mirrors.ibiblio.org/pub/mirrors/maven2/%{name}/%{name}/%{version}/%{name}-%{version}.pom
# fix javac executable
Patch0:        %{name}-%{version}-build.patch
# remove maven-gpg-plugin
Patch1:        %{name}-%{version}-pom.patch
BuildRequires: jpackage-utils

BuildRequires: ant

BuildRequires: tomcat-servlet-3.0-api
Requires:      tomcat-servlet-3.0-api

Requires:      jpackage-utils
BuildArch:     noarch
Source44: import.info

%description
The jCIFS SMB client library enables any Java application to remotely
access shared files and directories on SMB file servers(i.e. a Microsoft
Windows "share") in addition to domain, workgroup, and server
enumeration of NetBIOS over TCP/IP networks. It is an advanced
implementation of the CIFS protocol supporting Unicode, batching,
multiplexing of threaded callers, encrypted authentication,
transactions, the Remote Access Protocol (RAP), and much more. It is
licensed under LGPL which means commercial organizations can
legitimately use it with their proprietary code(you just can't sell or
give away a modified binary only version of the library itself without
reciprocation).

%package javadoc
Summary:       Javadocs for %{name}
Group:         Development/Java
License:       LGPLv2+ and GPLv2+
Requires:      jpackage-utils
BuildArch: noarch

%description javadoc
This package contains the API documentation for %%{name}.

%package demo
Summary:       Demo for %{name}
Group:         Development/Java
License:       LGPLv2+ and GPLv2+ and BSD
Requires:      %{name} = %{?epoch:%epoch:}%{version}-%{release}

%description demo
Demonstrations and samples for %%{name}.

%prep
%setup -q -n %{name}_%{version}
find -name '*.class' -delete
find -name '*.jar' -delete
%patch0 -p0
cp -p %{SOURCE1} pom.xml
%patch1 -p0

%build

export CLASSPATH=$(build-classpath tomcat-servlet-3.0-api)
export OPT_JAR_LIST=:
%ant jar javadoc docs

%install

mkdir -p %{buildroot}%{_javadir}
install -p -m 644 %{name}-%{version}.jar %{buildroot}%{_javadir}/%{name}.jar

mkdir -p %{buildroot}%{_mavenpomdir}
install -pm 644 pom.xml %{buildroot}%{_mavenpomdir}/JPP-%{name}.pom
%add_maven_depmap JPP-%{name}.pom %{name}.jar -a "org.samba.jcifs:jcifs"

mkdir -p %{buildroot}%{_javadocdir}/%{name}
cp -pr docs/api/* %{buildroot}%{_javadocdir}/%{name}

mkdir -p %{buildroot}%{_datadir}/%{name}/examples
cp -pr examples/*.java  %{buildroot}%{_datadir}/%{name}/examples

%files
%{_javadir}/%{name}.jar
%{_mavenpomdir}/JPP-%{name}.pom
%{_mavendepmapfragdir}/%{name}
%doc LICENSE.txt README.txt docs/*.{html,txt,gif}

%files javadoc
%{_javadocdir}/%{name}
%doc LICENSE.txt

%files demo
%{_datadir}/%{name}/*
%doc LICENSE.txt

%changelog
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

