Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
# END SourceDeps(oneline)
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
%define api_version 1.0
%define pkg_name geronimo-jaspic_%{api_version}_spec
Name:          geronimo-jaspic-spec
Version:       1.1
Release:       alt3_13jpp8
Summary:       Java Authentication SPI for Containers
License:       ASL 2.0 and W3C
URL:           http://geronimo.apache.org/
Source0:       http://repo2.maven.org/maven2/org/apache/geronimo/specs/%{pkg_name}/%{version}/%{pkg_name}-%{version}-source-release.tar.gz

BuildArch:     noarch

BuildRequires: maven-local
BuildRequires: maven-plugin-bundle
BuildRequires: geronimo-osgi-support
BuildRequires: geronimo-parent-poms
BuildRequires: javapackages-tools rpm-build-java

Provides:      javax.security.auth.message
Source44: import.info

%description
Java Authentication Service Provider Interface for Containers (JSR-196) api.

%package javadoc
Group: Development/Java
Summary:        API documentation for %{name}
BuildArch: noarch

%description javadoc
%{summary}.


%prep
%setup -q -n %{pkg_name}-%{version}

for d in LICENSE NOTICE ; do
  iconv -f iso8859-1 -t utf-8 $d > $d.conv && mv -f $d.conv $d
  sed -i 's/\r//' $d
done

%pom_xpath_remove "pom:parent"
%pom_xpath_inject "pom:project" "
    <parent>
      <groupId>org.apache.geronimo.specs</groupId>
      <artifactId>specs</artifactId>
      <version>any</version>
    </parent>"

%build
%mvn_file  : %{name}
%mvn_alias : org.eclipse.jetty.orbit:javax.security.auth.message
%mvn_build

%install
%mvn_install

install -d -m 755 %{buildroot}%{_javadir}/javax.security.auth.message/
ln -sf ../%{name}.jar %{buildroot}%{_javadir}/javax.security.auth.message/

%files -f .mfiles
%doc LICENSE NOTICE
%{_javadir}/javax.security.auth.message/

%files javadoc -f .mfiles-javadoc
%doc LICENSE NOTICE

%changelog
* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 1.1-alt3_13jpp8
- new fc release

* Tue Feb 02 2016 Igor Vlasenko <viy@altlinux.ru> 1.1-alt3_12jpp8
- new version

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 1.1-alt3_9jpp7
- new release

* Sat Aug 23 2014 Igor Vlasenko <viy@altlinux.ru> 1.1-alt3_7jpp7
- new release

* Thu Aug 07 2014 Igor Vlasenko <viy@altlinux.ru> 1.1-alt3_3jpp7
- rebuild with maven-local

* Mon Jul 14 2014 Igor Vlasenko <viy@altlinux.ru> 1.1-alt2_3jpp7
- NMU rebuild to move poms and fragments

* Fri Sep 07 2012 Igor Vlasenko <viy@altlinux.ru> 1.1-alt1_3jpp7
- new version

* Mon Aug 13 2012 Igor Vlasenko <viy@altlinux.ru> 1.0-alt1_2jpp7
- full version

