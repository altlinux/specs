BuildRequires: /proc
BuildRequires: jpackage-compat
Name: geronimo-commonj
Version: 1.1.0
Release: alt2_3jpp7
Summary: CommonJ Specification
Group: Development/Java
License: ASL 2.0
URL: http://geronimo.apache.org/

# svn export https://svn.apache.org/repos/asf/geronimo/specs/tags/specs-1.4/geronimo-commonj_1.1_spec geronimo-commonj-1.1.0
# tar cvfJ geronimo-commonj-1.1.0.tar.xz geronimo-commonj-1.1.0
Source: %{name}-%{version}.tar.xz

# Remove the SNAPSHOT tag from the version in the POM file:
Patch0: %{name}-version-fix.patch

BuildArch: noarch

BuildRequires: jpackage-utils
BuildRequires: maven
BuildRequires: maven-compiler-plugin
BuildRequires: maven-install-plugin
BuildRequires: maven-jar-plugin
BuildRequires: maven-javadoc-plugin


Requires: jpackage-utils
Source44: import.info


%description
Geronimo CommonJ Specification.


%package javadoc
Summary: Javadocs for %{name}
Group: Development/Java
Requires: jpackage-utils
BuildArch: noarch


%description javadoc
This package contains the API documentation for %{name}.


%prep
%setup -q
%patch0 -p0


%build
mvn-rpmbuild \
  -Dproject.build.sourceEncoding=UTF-8 \
  install \
  javadoc:aggregate


%install

# Jar files:
install -d -m 755 %{buildroot}%{_javadir}
install -pm 644 target/%{name}_1.1_spec-%{version}.jar %{buildroot}%{_javadir}/%{name}.jar

# POM files:
install -d -m 755 %{buildroot}%{_mavenpomdir}
install -pm 644 pom.xml %{buildroot}%{_mavenpomdir}/JPP-%{name}.pom

# Javadoc files:
install -d -m 755 %{buildroot}%{_javadocdir}/%{name}
cp -rp target/site/apidocs/* %{buildroot}%{_javadocdir}/%{name}

# Dependencies map:
%add_maven_depmap JPP-%{name}.pom %{name}.jar


%files
%{_javadir}/*
%{_mavenpomdir}/*
%{_mavendepmapfragdir}/*
%doc LICENSE.txt
%doc NOTICE.txt


%files javadoc
%{_javadocdir}/%{name}
%doc LICENSE.txt
%doc NOTICE.txt


%changelog
* Mon Jul 14 2014 Igor Vlasenko <viy@altlinux.ru> 1.1.0-alt2_3jpp7
- NMU rebuild to move poms and fragments

* Thu Aug 30 2012 Igor Vlasenko <viy@altlinux.ru> 1.1.0-alt1_3jpp7
- new version

