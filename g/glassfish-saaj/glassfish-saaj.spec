# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-java
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-compat
Name:             glassfish-saaj
Version:          1.3.19
Release:          alt1_1jpp7
Summary:          JSR-67 implementation
Group:            Development/Java
License:          CDDL and GPLv2 with exceptions
URL:              http://java.net/projects/saaj

# svn export https://svn.java.net/svn/saaj~svn/tags/saaj-impl-1.3.19 glassfish-saaj-1.3.19
# find glassfish-saaj-1.3.19/ -name '*.jar' -delete
# find glassfish-saaj-1.3.19/ -name '*.zip' -delete
# tar cafJ glassfish-saaj-1.3.19.tar.xz glassfish-saaj-1.3.19
Source0:          glassfish-saaj-%{version}.tar.xz

BuildArch:        noarch

BuildRequires:    jpackage-utils
BuildRequires:    maven1
BuildRequires:    maven-compiler-plugin
BuildRequires:    maven-install-plugin
BuildRequires:    maven-jar-plugin
BuildRequires:    maven-javadoc-plugin
BuildRequires:    maven-enforcer-plugin
BuildRequires:    mimepull
BuildRequires:    geronimo-saaj
BuildRequires:    jvnet-parent

Requires:         jpackage-utils
Requires:         mimepull
Requires:         geronimo-saaj
Source44: import.info

%description
Open source Reference Implementation of JSR-67: SOAP with Attachments
API for Java (SAAJ MR: 1.3)

%package javadoc
Summary:          Javadocs for %{name}
Group:            Development/Java
Requires:         jpackage-utils
BuildArch: noarch

%description javadoc
This package contains the API documentation for %%{name}.

%prep
%setup -q

%build
mvn-rpmbuild package javadoc:aggregate

%install
install -d -m 755 $RPM_BUILD_ROOT%{_javadir}
install -d -m 755 $RPM_BUILD_ROOT%{_mavenpomdir}
install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}

# JAR
install -pm 644 target/saaj-impl-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}.jar

# POM
install -pm 644 pom.xml $RPM_BUILD_ROOT%{_mavenpomdir}/JPP-%{name}.pom

# DEPMAP
%add_maven_depmap

# APIDOCS
cp -rp target/site/apidocs/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}

%files
%{_mavenpomdir}/*
%{_mavendepmapfragdir}/*
%{_javadir}/*
%doc license.html

%files javadoc
%{_javadocdir}/%{name}
%doc license.html

%changelog
* Tue Jan 15 2013 Igor Vlasenko <viy@altlinux.ru> 1.3.19-alt1_1jpp7
- initial build

