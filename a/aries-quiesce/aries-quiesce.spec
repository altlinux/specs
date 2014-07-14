BuildRequires: /proc
BuildRequires: jpackage-compat
Name:          aries-quiesce
Version:       0.3
Release:       alt2_2jpp7
Summary:       Apache Aries Quiesce
License:       ASL 2.0
Group:         Development/Java
URL:           http://aries.apache.org/

# svn export http://svn.apache.org/repos/asf/aries/tags/quiesce-0.3/ aries-quiesce-0.3
# tar cafJ aries-quiesce-0.3.tar.xz aries-quiesce-0.3

Source0:       %{name}-%{version}.tar.xz
Patch0:        %{name}-%{version}-xml.patch

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
BuildRequires: apache-commons-lang
BuildRequires: apache-commons-pool
BuildRequires: apache-commons-collections
BuildRequires: aries-util
BuildRequires: felix-osgi-compendium
BuildRequires: felix-osgi-core
BuildRequires: slf4j

Requires:      jpackage-utils
Requires:      apache-commons-lang
Requires:      apache-commons-pool
Requires:      apache-commons-collections
Requires:      aries-util
Requires:      felix-osgi-compendium
Requires:      felix-osgi-core
Requires:      slf4j
Source44: import.info

%description
Quiesce support for Aries.

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

%build
mvn-rpmbuild \
  -Dproject.build.sourceEncoding=UTF-8 \
  package javadoc:aggregate

%install

install -d -m 755 %{buildroot}%{_javadir}/%{name}
install -d -m 755 %{buildroot}%{_mavenpomdir}
install -d -m 755 %{buildroot}%{_javadocdir}/%{name}

# modules
for module in api manager;
do
  pushd quiesce-$module
  jarname=org.apache.aries.quiesce.$module
  install -pm 644 target/$jarname-%{version}.jar %{buildroot}%{_javadir}/%{name}/$jarname.jar
  install -pm 644 pom.xml %{buildroot}%{_mavenpomdir}/JPP.%{name}-$jarname.pom
  %add_maven_depmap JPP.%{name}-$jarname.pom %{name}/$jarname.jar
  popd
done

# pom
install -pm 644 pom.xml %{buildroot}%{_mavenpomdir}/JPP.%{name}.pom

# depmap
%add_maven_depmap JPP.%{name}.pom

# javadoc
cp -rp target/site/apidocs/* %{buildroot}%{_javadocdir}/%{name}


%files
%{_mavenpomdir}/*
%{_mavendepmapfragdir}/*
%{_javadir}/*

%files javadoc
%{_javadocdir}/%{name}

%changelog
* Mon Jul 14 2014 Igor Vlasenko <viy@altlinux.ru> 0.3-alt2_2jpp7
- NMU rebuild to move poms and fragments

* Wed Sep 12 2012 Igor Vlasenko <viy@altlinux.ru> 0.3-alt1_2jpp7
- new version

