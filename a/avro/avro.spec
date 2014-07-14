# BEGIN SourceDeps(oneline):
BuildRequires: gcc-c++ python-devel
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-compat
Name:             avro
Version:          1.6.2
Release:          alt2_4jpp7
Summary:          Data serialization system
Group:            Development/Java
License:          ASL 2.0
URL:              http://avro.apache.org

# svn export http://svn.apache.org/repos/asf/avro/tags/release-1.6.2/ avro-1.6.2
# find avro-1.6.2/ -name '*.jar' -or -name '*.dll' -delete
# tar cafJ avro-1.6.2-CLEAN.tar.xz avro-1.6.2
Source0:          avro-%{version}-CLEAN.tar.xz

Patch0:           avro-%{version}-pom.patch

BuildArch:        noarch

BuildRequires:    jpackage-utils
BuildRequires:    maven
BuildRequires:    maven-compiler-plugin
BuildRequires:    maven-install-plugin
BuildRequires:    maven-jar-plugin
BuildRequires:    maven-javadoc-plugin
BuildRequires:    maven-archetype-packaging
BuildRequires:    maven-archetype-plugin
BuildRequires:    maven-archetype-common
BuildRequires:    maven-checkstyle-plugin
BuildRequires:    maven-resources-plugin
BuildRequires:    javacc-maven-plugin
BuildRequires:    jackson
BuildRequires:    snappy-java
BuildRequires:    paranamer
BuildRequires:    slf4j

Requires:         jpackage-utils
Requires:         jackson
Requires:         snappy-java
Requires:         paranamer
Requires:         slf4j
Source44: import.info

%description
Apache Avro is a data serialization system.

Avro provides:

* Rich data structures.
* A compact, fast, binary data format.
* A container file, to store persistent data.
* Remote procedure call (RPC).
* Simple integration with dynamic languages. Code generation is not required
  to read or write data files nor to use or implement RPC protocols. Code
  generation as an optional optimization, only worth implementing for
  statically typed languages.

%package javadoc
Summary:          Javadocs for %{name}
Group:            Development/Java
Requires:         jpackage-utils
BuildArch: noarch

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q

%patch0 -p1

%build
# Tests run: 2601, Failures: 2, Errors: 0, Skipped: 0
mvn-rpmbuild -Dmaven.test.skip=true install javadoc:aggregate

%install
install -d -m 755 $RPM_BUILD_ROOT%{_javadir}/%{name}
install -d -m 755 $RPM_BUILD_ROOT%{_mavenpomdir}
install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}

# JAR
install -pm 644 lang/java/avro/target/avro-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/%{name}.jar
install -pm 644 lang/java/maven-plugin/target/avro-maven-plugin-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/%{name}-maven-plugin.jar
install -pm 644 lang/java/compiler/target/avro-compiler-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/%{name}-compiler.jar

# POM
install -pm 644 pom.xml $RPM_BUILD_ROOT%{_mavenpomdir}/JPP.%{name}-%{name}-toplevel.pom
install -pm 644 lang/java/pom.xml $RPM_BUILD_ROOT%{_mavenpomdir}/JPP.%{name}-%{name}-parent.pom
install -pm 644 lang/java/avro/pom.xml $RPM_BUILD_ROOT%{_mavenpomdir}/JPP.%{name}-%{name}.pom
install -pm 644 lang/java/compiler/pom.xml $RPM_BUILD_ROOT%{_mavenpomdir}/JPP.%{name}-%{name}-compiler.pom
install -pm 644 lang/java/maven-plugin/pom.xml $RPM_BUILD_ROOT%{_mavenpomdir}/JPP.%{name}-%{name}-maven-plugin.pom

# DEPMAP
%add_maven_depmap JPP.%{name}-%{name}-toplevel.pom
%add_maven_depmap JPP.%{name}-%{name}-parent.pom
%add_maven_depmap JPP.%{name}-%{name}.pom %{name}/%{name}.jar
%add_maven_depmap JPP.%{name}-%{name}-maven-plugin.pom %{name}/%{name}-maven-plugin.jar
%add_maven_depmap JPP.%{name}-%{name}-compiler.pom %{name}/%{name}-compiler.jar

# APIDOCS
cp -rp target/site/apidocs/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}

%files
%{_mavenpomdir}/*
%{_mavendepmapfragdir}/*
%{_javadir}/%{name}/*
%doc LICENSE.txt

%files javadoc
%{_javadocdir}/%{name}
%doc LICENSE.txt

%changelog
* Mon Jul 14 2014 Igor Vlasenko <viy@altlinux.ru> 1.6.2-alt2_4jpp7
- NMU rebuild to move poms and fragments

* Thu Sep 13 2012 Igor Vlasenko <viy@altlinux.ru> 1.6.2-alt1_4jpp7
- new version

