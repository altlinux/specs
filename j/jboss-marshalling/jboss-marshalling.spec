BuildRequires: /proc
BuildRequires: jpackage-compat
# %name or %version is ahead of its definition. Predefining for rpm 4.0 compatibility.
%define name jboss-marshalling
%define version 1.3.13
%global namedreltag .GA
%global namedversion %{version}%{?namedreltag}

Name:             jboss-marshalling
Version:          1.3.13
Release:          alt2_3jpp7
Summary:          JBoss Marshalling
Group:            Development/Java
License:          LGPLv2+
URL:              http://www.jboss.org/jbossmarshalling

# git clone git://github.com/jboss-remoting/jboss-marshalling.git
# cd jboss-marshalling/ && git archive --format=tar --prefix=jboss-marshalling-1.3.13.GA/ 1.3.13.GA | xz > jboss-marshalling-1.3.13.GA.tar.xz
Source0:          %{name}-%{namedversion}.tar.xz
Patch0:           %{name}-%{namedversion}-pom.patch

BuildArch:        noarch

BuildRequires:    jpackage-utils
BuildRequires:    maven
BuildRequires:    jboss-parent
BuildRequires:    maven-compiler-plugin
BuildRequires:    maven-install-plugin
BuildRequires:    maven-jar-plugin
BuildRequires:    maven-javadoc-plugin
BuildRequires:    maven-release-plugin
BuildRequires:    maven-resources-plugin
BuildRequires:    maven-surefire-plugin
BuildRequires:    maven-injection-plugin
BuildRequires:    maven-surefire-provider-testng
BuildRequires:    maven-enforcer-plugin
BuildRequires:    testng
BuildRequires:    jboss-modules
BuildRequires:    qdox
BuildRequires:    apiviz
BuildRequires:    jdepend
BuildRequires:    graphviz
BuildRequires:    gdata-java

Requires:         jboss-modules
Requires:         jpackage-utils
Source44: import.info

%description
This package contains JBoss Marshalling

%package javadoc
Summary:          Javadocs for %{name}
Group:            Development/Java
Requires:         jpackage-utils
BuildArch: noarch

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q -n %{name}-%{namedversion}
%patch0 -p1

%build
# Caused by: java.lang.ClassNotFoundException: com.thoughtworks.qdox.model.AbstractInheritableJavaEntity
# But the clss exists in qdox WTF?
mvn-rpmbuild install -Dmaven.test.skip=true javadoc:aggregate

%install
install -d -m 755 $RPM_BUILD_ROOT%{_javadir}/%{name}
install -d -m 755 $RPM_BUILD_ROOT%{_mavenpomdir}

for m in river serial; do
  cp -p ${m}/target/%{name}-${m}-%{namedversion}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}-${m}.jar
  install -pm 644 ${m}/pom.xml $RPM_BUILD_ROOT%{_mavenpomdir}/JPP-%{name}-${m}.pom
  %add_maven_depmap JPP-%{name}-${m}.pom %{name}-${m}.jar
done

# JARS
cp -p api/target/%{name}-%{namedversion}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}.jar

# POMS
install -pm 644 api/pom.xml $RPM_BUILD_ROOT%{_mavenpomdir}/JPP-%{name}.pom
install -pm 644 pom.xml $RPM_BUILD_ROOT%{_mavenpomdir}/JPP-%{name}-parent.pom

# DEPMAP
%add_maven_depmap JPP-%{name}.pom %{name}.jar
%add_maven_depmap JPP-%{name}-parent.pom

# JAVADOC
install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}
cp -rp target/site/apidocs/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}

%files
%{_mavenpomdir}/*
%{_mavendepmapfragdir}/*
%{_javadir}/*
%doc COPYING.txt

%files javadoc
%{_javadocdir}/%{name}
%doc COPYING.txt

%changelog
* Mon Jul 14 2014 Igor Vlasenko <viy@altlinux.ru> 1.3.13-alt2_3jpp7
- NMU rebuild to move poms and fragments

* Thu Sep 13 2012 Igor Vlasenko <viy@altlinux.ru> 1.3.13-alt1_3jpp7
- new version

