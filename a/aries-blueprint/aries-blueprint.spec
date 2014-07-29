# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-java
BuildRequires: maven
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-compat
Name:          aries-blueprint
Version:       0.3.1
Release:       alt2_5jpp7
Summary:       Apache Aries Blueprint
License:       ASL 2.0
Group:         Development/Java
URL:           http://aries.apache.org/

# svn export http://svn.apache.org/repos/asf/aries/tags/blueprint-0.3.1/ aries-blueprint-0.3.1
# tar cafJ aries-blueprint-0.3.1.tar.xz aries-blueprint-0.3.1

Source0:       %{name}-%{version}.tar.xz
Patch0:        %{name}-%{version}-xml.patch
Patch1:        %{name}-%{version}-java.patch

BuildArch:     noarch

BuildRequires: jpackage-utils
BuildRequires: maven-local
BuildRequires: maven-compiler-plugin
BuildRequires: maven-install-plugin
BuildRequires: maven-jar-plugin
BuildRequires: maven-javadoc-plugin
BuildRequires: maven-release-plugin
BuildRequires: maven-resources-plugin
BuildRequires: maven-surefire-plugin
BuildRequires: aries-util
BuildRequires: aries-proxy
BuildRequires: aries-quiesce
BuildRequires: asm2
BuildRequires: felix-osgi-compendium
BuildRequires: felix-osgi-core
BuildRequires: xbean

Requires:      jpackage-utils
Requires:      aries-util
Requires:      aries-proxy
Requires:      aries-quiesce
Requires:      asm2
Requires:      felix-osgi-compendium
Requires:      felix-osgi-core
Requires:      xbean
Source44: import.info

%description
Implementation of the Blueprint Container Specification.

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
# tests disabled because of
# missing dependency on org.apache.aries.unittest
mvn-rpmbuild \
  -Dmaven.test.skip=true \
  -Dproject.build.sourceEncoding=UTF-8 \
  package javadoc:aggregate

%install

install -d -m 755 %{buildroot}%{_javadir}/%{name}
install -d -m 755 %{buildroot}%{_mavenpomdir}
install -d -m 755 %{buildroot}%{_javadocdir}/%{name}

# modules
for module in blueprint-annotation-api blueprint-api blueprint-cm \
              blueprint-core blueprint-sample;
do
  pushd $module
  jarname=`echo org.apache.aries.$module | tr - .`
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
%doc README LICENSE NOTICE
%{_mavenpomdir}/*
%{_mavendepmapfragdir}/*
%{_javadir}/*

%files javadoc
%doc LICENSE
%{_javadocdir}/%{name}

%changelog
* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 0.3.1-alt2_5jpp7
- new release

* Mon Jul 14 2014 Igor Vlasenko <viy@altlinux.ru> 0.3.1-alt2_3jpp7
- NMU rebuild to move poms and fragments

* Wed Sep 12 2012 Igor Vlasenko <viy@altlinux.ru> 0.3.1-alt1_3jpp7
- new version

