Epoch: 1
BuildRequires: /proc
BuildRequires: jpackage-compat
Name:           jbossxb
Version:        2.0.3
Release:        alt2_1jpp7
Summary:        JBoss XML Binding

Group:          Development/Java

License:        LGPLv2+
URL:            http://www.jboss.org

# svn export http://anonsvn.jboss.org/repos/common/jbossxb/tags/2.0.3.GA/ jbossxb-2.0.3
# tar cJf jbossxb-2.0.3.tar.xz jbossxb-2.0.3/
Source0:        %{name}-%{version}.tar.xz
Patch0:         %{name}-pom.patch

BuildArch:      noarch

BuildRequires:  jpackage-utils

BuildRequires:  bea-stax
BuildRequires:  javassist
BuildRequires:  jboss-classpool-scoped
BuildRequires:  jboss-common-core
BuildRequires:  jboss-jaxb-2.2-api
BuildRequires:  jboss-logging
BuildRequires:  jboss-reflect
BuildRequires:  maven
BuildRequires:  maven-compiler-plugin
BuildRequires:  maven-enforcer-plugin
BuildRequires:  maven-jar-plugin
BuildRequires:  maven-javadoc-plugin
BuildRequires:  maven-resources-plugin
BuildRequires:  maven-source-plugin
BuildRequires:  maven-surefire-plugin
BuildRequires:  maven-surefire-provider-junit4
BuildRequires:  xerces-j2

Requires:       bea-stax
Requires:       javassist
Requires:       jboss-classpool-scoped
Requires:       jboss-common-core
Requires:       jboss-logging
Requires:       jboss-reflect
Requires:       jpackage-utils
Requires:       xerces-j2
Source44: import.info

%description
JBoss XML Binding.

%package javadoc
Summary:        Javadocs for %{name}
Group:          Development/Java
Requires:       jpackage-utils
BuildArch: noarch

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q

# can't compile stuff in the test dir...missing deps
rm -rf src/test

find -type f -name *.jar -delete
find -type f -name *.class -delete

%patch0

%build
export LANG=en_US.ISO8859-1
mvn-rpmbuild package javadoc:aggregate

%install

# jar is named jboss-xml-binding.jar by default; Renamed to jbossxb.jar.
mkdir -p $RPM_BUILD_ROOT%{_javadir}
cp -p target/jboss-xml-binding.jar $RPM_BUILD_ROOT%{_javadir}/%{name}.jar

mkdir -p $RPM_BUILD_ROOT%{_javadocdir}/%{name}
cp -rp target/site/apidocs/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}

install -d -m 755 $RPM_BUILD_ROOT%{_mavenpomdir}
install -pm 644 pom.xml $RPM_BUILD_ROOT%{_mavenpomdir}/JPP-%{name}.pom

%add_maven_depmap JPP-%{name}.pom %{name}.jar

# jpp compat symlink
mkdir -p $RPM_BUILD_ROOT%{_javadir}/jboss
ln -s ../%{name}.jar $RPM_BUILD_ROOT%{_javadir}/jboss/jboss-xml-binding.jar

%files
%{_mavenpomdir}/JPP-%{name}.pom
%{_mavendepmapfragdir}/%{name}
%{_javadir}/%{name}.jar
%{_javadir}/jboss/jboss-xml-binding.jar

%files javadoc
%{_javadocdir}/%{name}


%changelog
* Mon Jul 14 2014 Igor Vlasenko <viy@altlinux.ru> 1:2.0.3-alt2_1jpp7
- NMU rebuild to move poms and fragments

* Fri Sep 07 2012 Igor Vlasenko <viy@altlinux.ru> 1:2.0.3-alt1_1jpp7
- new version

* Sun Jan 02 2011 Igor Vlasenko <viy@altlinux.ru> 1:1.0.0-alt3_3.SP3.9jpp5
- updated repolib

* Mon Dec 06 2010 Igor Vlasenko <viy@altlinux.ru> 1:1.0.0-alt2_3.SP3.9jpp5
- rebuild with new xerces repolib

* Fri May 22 2009 Igor Vlasenko <viy@altlinux.ru> 1:1.0.0-alt1_3.SP3.9jpp5
- new jpp release

