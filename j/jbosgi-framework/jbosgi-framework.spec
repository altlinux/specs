BuildRequires: /proc
BuildRequires: jpackage-compat
# %name or %version is ahead of its definition. Predefining for rpm 4.0 compatibility.
%define name jbosgi-framework
%define version 1.1.8
%global namedreltag .Final
%global namedversion %{version}%{?namedreltag}

Name:             jbosgi-framework
Version:          1.1.8
Release:          alt2_4jpp7
Summary:          JBoss OSGi Core Framework
Group:            Development/Java
License:          LGPLv2+
URL:              http://www.jboss.org/

# git clone git://github.com/jbosgi/jbosgi-framework.git
# cd jbosgi-framework/ && git archive --format=tar --prefix=jbosgi-framework-1.1.8.Final/ 1.1.8.Final | xz > jbosgi-framework-1.1.8.Final.tar.xz
Source0:          jbosgi-framework-%{namedversion}.tar.xz

Patch0:           0001-Disable-assembly-plugin.patch
Patch1:           0002-Disable-itest-module.patch

BuildArch:        noarch

BuildRequires:    jpackage-utils
BuildRequires:    jbosgi-parent
BuildRequires:    maven
BuildRequires:    maven-compiler-plugin
BuildRequires:    maven-install-plugin
BuildRequires:    maven-jar-plugin
BuildRequires:    maven-javadoc-plugin
BuildRequires:    maven-surefire-provider-junit4
BuildRequires:    arquillian-core
BuildRequires:    jboss-logging
BuildRequires:    jboss-logmanager
BuildRequires:    jboss-modules
BuildRequires:    jboss-msc
BuildRequires:    jbosgi-deployment
BuildRequires:    jbosgi-spi
BuildRequires:    jbosgi-vfs
BuildRequires:    jbosgi-resolver1
BuildRequires:    felix-osgi-compendium
BuildRequires:    felix-framework

Requires:         jpackage-utils
Requires:         arquillian-core
Requires:         jboss-logging
Requires:         jboss-logmanager
Requires:         jboss-modules
Requires:         jboss-msc
Requires:         jbosgi-deployment
Requires:         jbosgi-spi
Requires:         jbosgi-vfs
Requires:         jbosgi-resolver1
Requires:         felix-osgi-compendium
Requires:         felix-framework
Source44: import.info

%description
This package contains the JBoss OSGi Core Framework.

%package javadoc
Summary:          Javadocs for %{name}
Group:            Development/Java
Requires:         jpackage-utils
BuildArch: noarch

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q -n jbosgi-framework-%{namedversion}

%patch0 -p1
%patch1 -p1

rm -rf core/src/main/java/org/osgi/util/

%build
# org.jboss.osgi.testing:jbosgi-testing is not available
mvn-rpmbuild -Dmaven.test.skip=true install javadoc:aggregate

%install
install -d -m 755 $RPM_BUILD_ROOT%{_javadir}
install -d -m 755 $RPM_BUILD_ROOT%{_mavenpomdir}
install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}

# JAR
install -pm 644 core/target/jbosgi-framework-core-%{namedversion}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}-core.jar

# POM
install -pm 644 core/pom.xml $RPM_BUILD_ROOT%{_mavenpomdir}/JPP-%{name}-core.pom
install -pm 644 pom.xml $RPM_BUILD_ROOT%{_mavenpomdir}/JPP-%{name}-parent.pom

# DEPMAP
%add_maven_depmap JPP-%{name}-parent.pom
%add_maven_depmap JPP-%{name}-core.pom %{name}-core.jar

# APIDOCS
cp -rp target/site/apidocs/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}

%files
%{_mavenpomdir}/*
%{_mavendepmapfragdir}/*
%{_javadir}/*
%doc README.md

%files javadoc
%{_javadocdir}/%{name}

%changelog
* Mon Jul 14 2014 Igor Vlasenko <viy@altlinux.ru> 1.1.8-alt2_4jpp7
- NMU rebuild to move poms and fragments

* Thu Sep 13 2012 Igor Vlasenko <viy@altlinux.ru> 1.1.8-alt1_4jpp7
- new version

