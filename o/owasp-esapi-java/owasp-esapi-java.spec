# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-java
BuildRequires: maven
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-compat
Name:             owasp-esapi-java
Version:          2.0.1
Release:          alt2_7jpp7
Summary:          OWASP Enterprise Security API
Group:            Development/Java
License:          BSD
URL:              http://code.google.com/p/owasp-esapi-java/

# svn export http://owasp-esapi-java.googlecode.com/svn/tags/esapi-2.0.1/ owasp-esapi-java-2.0.1 
# tar cafJ owasp-esapi-java-2.0.1.tar.xz owasp-esapi-java-2.0.1
Source0:          owasp-esapi-java-%{version}.tar.xz

# Antisammy is not available
Patch0:           0001-Remove-validator-implementation-bsed-on-Antisammy.patch
# Use different directory in tests
Patch1:           0002-Use-different-directory-to-testing-bin-is-a-symlink.patch
# Missing implementations
Patch2:           0003-Implement-missing-servlet-3.0-methods-in-mock.patch

BuildArch:        noarch

BuildRequires:    jpackage-utils
BuildRequires:    maven-local
BuildRequires:    maven-compiler-plugin
BuildRequires:    maven-dependency-plugin
BuildRequires:    maven-install-plugin
BuildRequires:    maven-jar-plugin
BuildRequires:    maven-javadoc-plugin
BuildRequires:    maven-surefire-plugin
BuildRequires:    maven-surefire-plugin
BuildRequires:    maven-surefire-provider-junit4
BuildRequires:    maven-enforcer-plugin
BuildRequires:    maven-eclipse-plugin
BuildRequires:    sonatype-oss-parent
BuildRequires:    tomcat-servlet-3.0-api
BuildRequires:    tomcat-jsp-2.2-api
BuildRequires:    bsh
BuildRequires:    junit
BuildRequires:    apache-commons-io
BuildRequires:    apache-commons-collections
BuildRequires:    apache-commons-fileupload
BuildRequires:    log4j
BuildRequires:    xom
BuildRequires:    ecj
BuildRequires:    maven-shared

Requires:         jpackage-utils
Requires:         tomcat-servlet-3.0-api
Requires:         tomcat-jsp-2.2-api
Requires:         apache-commons-collections
Requires:         apache-commons-fileupload
Requires:         log4j
Requires:         bsh
Requires:         xom
Requires:         ecj
Source44: import.info

%description
OWASP ESAPI (The OWASP Enterprise Security API) is a free, open source,
web application security control library that makes it easier for programmers
to write lower-risk applications. The ESAPI for Java library is designed to
make it easier for programmers to retrofit security into existing applications.
ESAPI for Java also serves as a solid foundation for new development. 

%package javadoc
Summary:          Javadocs for %{name}
Group:            Development/Java
Requires:         jpackage-utils
BuildArch: noarch

%description javadoc
This package contains the API documentation for %{name}.

%package doc
Summary:          Documentation for %{name}
Group:            Development/Java
License:          CC-BY-SA

%description doc
This package contains the documentation for %{name}.

%prep
%setup -q -n owasp-esapi-java-%{version}

%patch0 -p1
%patch1 -p1
%patch2 -p1

# Plugin not available
%pom_remove_plugin "org.codehaus.mojo:versions-maven-plugin"

# Atisammy not available
%pom_remove_dep "org.owasp.antisamy:antisamy"

# No POM file for bsh-core in Fedora
%pom_xpath_inject "pom:dependencies/pom:dependency[pom:artifactId='bsh-core']" "<systemPath>$(build-classpath bsh-core)</systemPath>"
%pom_xpath_inject "pom:dependencies/pom:dependency[pom:artifactId='bsh-core']" "<scope>system</scope>"

sed -i "s|public void testSetCookie()|public void ignoredSetCookie()|" src/test/java/org/owasp/esapi/reference/HTTPUtilitiesTest.java

%build
mvn-rpmbuild \
    -Dproject.build.sourceEncoding=UTF-8 \
    package javadoc:aggregate

%install
install -d -m 755 $RPM_BUILD_ROOT%{_javadir}
install -d -m 755 $RPM_BUILD_ROOT%{_mavenpomdir}
install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}

# JAR
install -pm 644 target/esapi-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}.jar

# POM
install -pm 644 pom.xml $RPM_BUILD_ROOT%{_mavenpomdir}/JPP-%{name}.pom

# DEPMAP
%add_maven_depmap JPP-%{name}.pom %{name}.jar

# APIDOCS
cp -rp target/site/apidocs/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}

%files
%{_mavenpomdir}/*
%{_mavendepmapfragdir}/*
%{_javadir}/*

%files javadoc
%{_javadocdir}/%{name}

%files doc
%doc documentation/*

%changelog
* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 2.0.1-alt2_7jpp7
- new release

* Sun Jul 27 2014 Igor Vlasenko <viy@altlinux.ru> 2.0.1-alt2_3jpp7
- fixed build

* Tue Feb 26 2013 Igor Vlasenko <viy@altlinux.ru> 2.0.1-alt1_3jpp7
- fc update

