BuildRequires: /proc
BuildRequires: jpackage-compat
Name: apache-mina
Version: 2.0.4
Release: alt2_4jpp7
Summary: Apache MINA

Group: Development/Java
License: ASL 2.0
URL: http://mina.apache.org

Source0: http://mina.apache.org/dyn/closer.cgi/mina/%{version}/%{name}-%{version}-src.tar.gz

# Build only the core:
Patch0: %{name}-build-core-only.patch

BuildArch: noarch

Requires: jpackage-utils

BuildRequires: jpackage-utils
BuildRequires: maven
BuildRequires: pmd

BuildRequires: maven-compiler-plugin
BuildRequires: maven-install-plugin
BuildRequires: maven-jar-plugin
BuildRequires: maven-javadoc-plugin
BuildRequires: maven-release-plugin
BuildRequires: maven-resources-plugin
BuildRequires: maven-surefire-plugin
BuildRequires: maven-shade-plugin
Source44: import.info


%description
Apache MINA is a network application framework which helps users develop high
performance and high scalability network applications easily. It provides an
abstract event-driven asynchronous API over various transports such as TCP/IP
and UDP/IP via Java NIO.


%package javadoc
Summary: Javadocs for %{name}
Group: Development/Java
Requires: jpackage-utils
BuildArch: noarch


%description javadoc
This package contains javadoc for %{name}.


%prep
%setup -q
%patch0 -p1


%build

# In the tarball distributed by Apache the source code is inside the src
# directory:
cd src

# Skip the tests for now:
mvn-rpmbuild \
  -Dmaven.test.skip=true \
  -Dproject.build.sourceEncoding=UTF-8 \
  install \
  javadoc:aggregate 


%install

# Jar files:
mkdir -p %{buildroot}%{_javadir}/%{name}
cp -p src/mina-core/target/mina-core-%{version}.jar %{buildroot}%{_javadir}/%{name}/mina-core.jar

# POM files:
install -d -m 755 %{buildroot}%{_mavenpomdir}
install -pm 644 src/pom.xml %{buildroot}%{_mavenpomdir}/JPP.%{name}-mina-parent.pom
install -pm 644 src/mina-core/pom.xml %{buildroot}%{_mavenpomdir}/JPP.%{name}-mina-core.pom

# Dependency map:
%add_maven_depmap JPP.%{name}-mina-parent.pom
%add_maven_depmap JPP.%{name}-mina-core.pom %{name}/mina-core.jar

# Javadoc files:
install -d -m 755 %{buildroot}%{_javadocdir}/%{name}
cp -rp src/target/site/apidocs/* %{buildroot}%{_javadocdir}/%{name}/.


%files
%{_mavenpomdir}/*
%{_mavendepmapfragdir}/*
%{_javadir}/%{name}/*
%doc LICENSE.txt
%doc NOTICE.txt


%files javadoc
%{_javadocdir}/%{name}
%doc LICENSE.txt
%doc NOTICE.txt


%changelog
* Mon Jul 14 2014 Igor Vlasenko <viy@altlinux.ru> 2.0.4-alt2_4jpp7
- NMU rebuild to move poms and fragments

* Wed Sep 05 2012 Igor Vlasenko <viy@altlinux.ru> 2.0.4-alt1_4jpp7
- new release

