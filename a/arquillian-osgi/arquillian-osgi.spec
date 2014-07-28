# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-java
BuildRequires: maven
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-compat
# %%name or %%version is ahead of its definition. Predefining for rpm 4.0 compatibility.
%define name arquillian-osgi
%define version 1.0.2
%global namedreltag .Final
%global namedversion %{version}%{?namedreltag}

Name:             arquillian-osgi
Version:          1.0.2
Release:          alt2_5jpp7
Summary:          Arquillian OSGi
Group:            Development/Java
License:          ASL 2.0 and LGPLv2+
URL:              http://arquillian.org

# git clone git://github.com/arquillian/arquillian-container-osgi.git
# cd arquillian-container-osgi/ && git archive --format=tar --prefix=arquillian-container-osgi-1.0.2/ 1.0.2.Final | xz > arquillian-container-osgi-1.0.2.tar.xz
Source0:          arquillian-container-osgi-%{version}.tar.xz

Patch0:           0001-Disable-checkstyle.patch
Patch1:           0002-Remove-osgi.enterprise-dependency.patch
Patch2:           0003-Disable-assembly-plugin.patch
Patch3:           0004-Disable-remote-container-module.patch

BuildArch:        noarch

BuildRequires:    jpackage-utils
BuildRequires:    maven-local
BuildRequires:    maven-compiler-plugin
BuildRequires:    maven-install-plugin
BuildRequires:    maven-jar-plugin
BuildRequires:    maven-javadoc-plugin
BuildRequires:    maven-enforcer-plugin
BuildRequires:    jbosgi-parent
BuildRequires:    jbosgi-spi
BuildRequires:    jbosgi-vfs
BuildRequires:    jbosgi-framework
BuildRequires:    shrinkwrap-resolver

Requires:         jpackage-utils
Requires:         jbosgi-spi
Requires:         jbosgi-vfs
Requires:         jbosgi-framework
Requires:         shrinkwrap-resolver
Source44: import.info

%description
This package contains Arquillian OSGi support.

%package javadoc
Summary:          Javadocs for %{name}
Group:            Development/Java
Requires:         jpackage-utils
BuildArch: noarch

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q -n arquillian-container-osgi-%{version}

%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1

%build
# Couldn't start the osgi framework
mvn-rpmbuild -Dmaven.test.skip=true install javadoc:aggregate

%install
install -d -m 755 $RPM_BUILD_ROOT%{_javadir}/%{name}
install -d -m 755 $RPM_BUILD_ROOT%{_mavenpomdir}
install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}

# JAR
install -pm 644 container-embedded/target/arquillian-container-osgi-embedded-%{namedversion}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/arquillian-container-osgi-embedded.jar
install -pm 644 container-common/target/arquillian-container-osgi-%{namedversion}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/arquillian-container-osgi.jar
install -pm 644 protocol-osgi/target/arquillian-protocol-osgi-%{namedversion}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/arquillian-protocol-osgi.jar
install -pm 644 testenricher-osgi/target/arquillian-testenricher-osgi-%{namedversion}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/arquillian-testenricher-osgi.jar

# POM
install -pm 644 container-embedded/pom.xml $RPM_BUILD_ROOT%{_mavenpomdir}/JPP.%{name}-arquillian-container-osgi-embedded.pom
install -pm 644 container-common/pom.xml $RPM_BUILD_ROOT%{_mavenpomdir}/JPP.%{name}-arquillian-container-osgi.pom
install -pm 644 protocol-osgi/pom.xml $RPM_BUILD_ROOT%{_mavenpomdir}/JPP.%{name}-arquillian-protocol-osgi.pom
install -pm 644 testenricher-osgi/pom.xml $RPM_BUILD_ROOT%{_mavenpomdir}/JPP.%{name}-arquillian-testenricher-osgi.pom

# DEPMAP
for m in container-osgi-embedded container-osgi protocol-osgi testenricher-osgi; do
  %add_maven_depmap JPP.%{name}-arquillian-${m}.pom %{name}/arquillian-${m}.jar
done

# POM
install -pm 644 pom.xml $RPM_BUILD_ROOT%{_mavenpomdir}/JPP.%{name}-parent.pom

# DEPMAP
%add_maven_depmap JPP.%{name}-parent.pom

# APIDOCS
cp -rp target/site/apidocs/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}

%files
%{_mavenpomdir}/*
%{_mavendepmapfragdir}/*
%{_javadir}/*

%files javadoc
%{_javadocdir}/%{name}

%changelog
* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 1.0.2-alt2_5jpp7
- new release

* Mon Jul 14 2014 Igor Vlasenko <viy@altlinux.ru> 1.0.2-alt2_3jpp7
- NMU rebuild to move poms and fragments

* Thu Sep 13 2012 Igor Vlasenko <viy@altlinux.ru> 1.0.2-alt1_3jpp7
- new version

