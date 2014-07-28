# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-java
BuildRequires: maven
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-compat
# %%name or %%version is ahead of its definition. Predefining for rpm 4.0 compatibility.
%define name felix-osgi-obr-resolver
%define version 0.1.0
%global namedreltag .Beta1
%global namedversion %{version}%{?namedreltag}
%global osginame org.apache.felix.resolver

Name:             felix-osgi-obr-resolver
Version:          0.1.0
Release:          alt2_0.7.Beta1jpp7
Summary:          Apache Felix Resolver
Group:            Development/Java
License:          ASL 2.0
URL:              https://github.com/tdiesler/obr-resolver

# git clone git://github.com/tdiesler/obr-resolver.git
# cd obr-resolver/ && git archive --format=tar --prefix=felix-osgi-obr-resolver-0.1.0.Beta1/ 0.1.0.Beta1 | xz > felix-osgi-obr-resolver-0.1.0.Beta1.tar.xz
Source0:          felix-osgi-obr-resolver-%{namedversion}.tar.xz

# Provided osgi.core in Fedora is old and the felix impl is the right one in this case
Patch0:           0001-Use-felix-directly.patch
Patch1:           0002-JDK7-support.patch
Patch2:           0003-Compile-with-target-1.5-or-greater.patch

BuildArch:        noarch

BuildRequires:    jpackage-utils
BuildRequires:    maven-local
BuildRequires:    maven-compiler-plugin
BuildRequires:    maven-install-plugin
BuildRequires:    maven-jar-plugin
BuildRequires:    maven-javadoc-plugin
BuildRequires:    maven-surefire-provider-junit4
BuildRequires:    felix-framework
BuildRequires:    apache-rat-plugin

Requires:         jpackage-utils
Requires:         felix-framework
Source44: import.info

%description
This package contains the Apache Felix Resolver

%package javadoc
Summary:          Javadocs for %{name}
Group:            Development/Java
Requires:         jpackage-utils
BuildArch: noarch

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q -n felix-osgi-obr-resolver-%{namedversion}

%patch0 -p1
%patch1 -p1
%patch2 -p1

# This is diabled because we don't have OSGi 5 provider in Fedora.
# TODO We need to remove this after OSGi 5 lands in Fedora.
#
# https://bugzilla.redhat.com/show_bug.cgi?id=832420#c2
# rm -rf src/main/java/org/osgi/framework/wiring

%build
mvn-rpmbuild install javadoc:aggregate

%install
install -d -m 755 $RPM_BUILD_ROOT%{_javadir}/felix
install -d -m 755 $RPM_BUILD_ROOT%{_mavenpomdir}
install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}

# JAR
install -pm 644 target/%{osginame}-%{namedversion}.jar $RPM_BUILD_ROOT%{_javadir}/felix/%{osginame}.jar

# POM
install -pm 644 pom.xml $RPM_BUILD_ROOT%{_mavenpomdir}/JPP.felix-%{osginame}.pom

# DEPMAP
%add_maven_depmap JPP.felix-%{osginame}.pom felix/%{osginame}.jar

# APIDOCS
cp -rp target/site/apidocs/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}

%files
%{_mavenpomdir}/*
%{_mavendepmapfragdir}/*
%{_javadir}/*

%files javadoc
%{_javadocdir}/%{name}

%changelog
* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 0.1.0-alt2_0.7.Beta1jpp7
- new release

* Mon Jul 14 2014 Igor Vlasenko <viy@altlinux.ru> 0.1.0-alt2_0.5.Beta1jpp7
- NMU rebuild to move poms and fragments

* Fri Sep 07 2012 Igor Vlasenko <viy@altlinux.ru> 0.1.0-alt1_0.5.Beta1jpp7
- new version

