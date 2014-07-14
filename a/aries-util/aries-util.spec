BuildRequires: /proc
BuildRequires: jpackage-compat
Name:          aries-util
Version:       0.4
Release:       alt2_2jpp7
Summary:       Apache Aries Util
License:       ASL 2.0
Group:         Development/Java
URL:           http://aries.apache.org/

# svn export http://svn.apache.org/repos/asf/aries/tags/org.apache.aries.util-0.4/ aries-util-0.4
# tar cafJ aries-util-0.4.tar.xz aries-util-0.4

Source0:       %{name}-%{version}.tar.xz
Patch0:        %{name}-%{version}-xml.patch
Patch1:        %{name}-%{version}-java.patch

BuildArch:     noarch

BuildRequires: jpackage-utils
BuildRequires: maven
BuildRequires: maven-compiler-plugin
BuildRequires: maven-install-plugin
BuildRequires: maven-jar-plugin
BuildRequires: maven-javadoc-plugin
BuildRequires: maven-release-plugin
BuildRequires: maven-resources-plugin
BuildRequires: maven-surefire-plugin
BuildRequires: felix-osgi-compendium
BuildRequires: felix-osgi-core

Requires:      jpackage-utils
Requires:      felix-osgi-compendium
Requires:      felix-osgi-core
Source44: import.info

%description
This package contains the OSGi common util for Apache Aries.

%package javadoc
Summary:       Javadocs for %{name}
Group:         Development/Java
Requires:      jpackage-utils
BuildArch: noarch

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q -n %{name}-%{version}
%patch0 -p1
%patch1 -p1

%build
# test disabled because of missing dependency:
# org.apache.aries.testsupport:org.apache.aries.testsupport.unit:jar
mvn-rpmbuild \
  -Dmaven.test.skip=true \
  -Dproject.build.sourceEncoding=UTF-8 \
  package javadoc:aggregate

%install

install -d -m 755 $RPM_BUILD_ROOT%{_javadir}
install -d -m 755 $RPM_BUILD_ROOT%{_mavenpomdir}
install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}

# jar
install -pm 644 target/org.apache.aries.util-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}.jar

# pom
install -pm 644 pom.xml $RPM_BUILD_ROOT%{_mavenpomdir}/JPP-%{name}.pom

# depmap
%add_maven_depmap JPP-%{name}.pom %{name}.jar

# javadoc
cp -rp target/site/apidocs/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}

%files
%doc LICENSE NOTICE
%{_mavenpomdir}/*
%{_mavendepmapfragdir}/*
%{_javadir}/*

%files javadoc
%doc LICENSE NOTICE
%{_javadocdir}/%{name}

%changelog
* Mon Jul 14 2014 Igor Vlasenko <viy@altlinux.ru> 0.4-alt2_2jpp7
- NMU rebuild to move poms and fragments

* Wed Sep 12 2012 Igor Vlasenko <viy@altlinux.ru> 0.4-alt1_2jpp7
- new version

