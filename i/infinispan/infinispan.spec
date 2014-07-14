BuildRequires: maven-antrun-plugin
BuildRequires: /proc
BuildRequires: jpackage-compat
# %name or %version is ahead of its definition. Predefining for rpm 4.0 compatibility.
%define name infinispan
%define version 5.1.2
%global namedreltag .FINAL
%global namedversion %{version}%{?namedreltag}

Name:             infinispan
Version:          5.1.2
Release:          alt2_3jpp7
Summary:          Data grid platform
Group:            Development/Java
License:          LGPLv2+
URL:              http://www.jboss.org/infinispan

# git clone git://github.com/infinispan/infinispan.git
# cd infinispan/ && git archive --format=tar --prefix=infinispan-5.1.2.FINAL/ 5.1.2.FINAL | xz > infinispan-5.1.2.FINAL.tar.xz
Source0:          %{name}-%{namedversion}.tar.xz

# Removes some of modules not necessary at this point
Patch0:           %{name}-%{namedversion}-pom.patch
# Adds support for new avro library
Patch1:           %{name}-%{namedversion}-avro.patch

BuildArch:        noarch

BuildRequires:    apache-commons-math
BuildRequires:    avro
BuildRequires:    c3p0
BuildRequires:    jcip-annotations
BuildRequires:    jboss-logging-tools
BuildRequires:    jboss-marshalling
BuildRequires:    jboss-naming
BuildRequires:    jboss-transaction-1.1-api
BuildRequires:    jgroups >= 3.0.3
BuildRequires:    jpackage-utils
BuildRequires:    maven
BuildRequires:    maven-enforcer-plugin
BuildRequires:    maven-plugin-exec
BuildRequires:    maven-resources-plugin
BuildRequires:    maven-remote-resources-plugin
BuildRequires:    rhq-plugin-annotations
BuildRequires:    staxmapper

Requires:         apache-commons-math
Requires:         avro
Requires:         c3p0
Requires:         jcip-annotations
Requires:         jboss-logging-tools
Requires:         jboss-marshalling
Requires:         jboss-naming
Requires:         jboss-transaction-1.1-api
Requires:         jgroups >= 3.0.3
Requires:         jpackage-utils
Requires:         staxmapper
Source44: import.info

%description
Infinispan is an extremely scalable, highly available data grid
platform - 100%% open source, and written in Java. The purpose of
Infinispan is to expose a data structure that is highly concurrent,
designed ground-up to make the most of modern multi-processor/multi-core
architectures while at the same time providing distributed cache
capabilities.  At its core Infinispan exposes a Cache interface which
extends java.util.Map. It is also optionally is backed by a peer-to-peer
network architecture to distribute state efficiently around a data grid.

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
%patch1 -p1

# Rename the license file
cp -r license/src/main/resources/META-INF/LICENSE.txt.vm LICENSE.txt

%build
# We don't have one of easymock package
mvn-rpmbuild -Dmaven.test.skip=true install javadoc:aggregate

%install
install -d -m 755 $RPM_BUILD_ROOT%{_javadir}/%{name}
install -d -m 755 $RPM_BUILD_ROOT%{_mavenpomdir}
install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}

for m in core; do
  # JAR
  install -pm 644 ${m}/target/infinispan-${m}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/%{name}-${m}.jar
  # POM
  install -pm 644 ${m}/pom.xml $RPM_BUILD_ROOT%{_mavenpomdir}/JPP.%{name}-%{name}-${m}.pom
  # DEPMAP
  %add_maven_depmap JPP.%{name}-%{name}-${m}.pom %{name}/%{name}-${m}.jar
done

# Cachestore modules
for m in remote jdbc; do
  # JAR
  install -pm 644 cachestore/${m}/target/infinispan-cachestore-${m}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/%{name}-cachestore-${m}.jar
  # POM
  install -pm 644 cachestore/${m}/pom.xml $RPM_BUILD_ROOT%{_mavenpomdir}/JPP.%{name}-%{name}-cachestore-${m}.pom
  # DEPMAP
  %add_maven_depmap JPP.%{name}-%{name}-cachestore-${m}.pom %{name}/%{name}-cachestore-${m}.jar
done

install -pm 644 client/hotrod-client/target/infinispan-client-hotrod.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/%{name}-client-hotrod.jar

# POM
install -pm 644 pom.xml $RPM_BUILD_ROOT%{_mavenpomdir}/JPP.%{name}-%{name}.pom
install -pm 644 parent/pom.xml $RPM_BUILD_ROOT%{_mavenpomdir}/JPP.%{name}-%{name}-parent.pom
install -pm 644 client/hotrod-client/pom.xml $RPM_BUILD_ROOT%{_mavenpomdir}/JPP.%{name}-%{name}-client-hotrod.pom
install -pm 644 cachestore/pom.xml $RPM_BUILD_ROOT%{_mavenpomdir}/JPP.%{name}-%{name}-cachestore-parent.pom

# DEPMAP
%add_maven_depmap JPP.%{name}-%{name}.pom
%add_maven_depmap JPP.%{name}-%{name}-parent.pom
%add_maven_depmap JPP.%{name}-%{name}-cachestore-parent.pom
%add_maven_depmap JPP.%{name}-%{name}-client-hotrod.pom %{name}/%{name}-client-hotrod.jar

# APIDOCS
cp -rp target/site/apidocs/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}

%files
%{_mavenpomdir}/*
%{_mavendepmapfragdir}/*
%{_javadir}/*
%doc LICENSE.txt README.mkdn

%files javadoc
%{_javadocdir}/%{name}
%doc LICENSE.txt

%changelog
* Mon Jul 14 2014 Igor Vlasenko <viy@altlinux.ru> 5.1.2-alt2_3jpp7
- NMU rebuild to move poms and fragments

* Thu Sep 13 2012 Igor Vlasenko <viy@altlinux.ru> 5.1.2-alt1_3jpp7
- new version

