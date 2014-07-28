# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-java
BuildRequires: maven
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-compat
%global api_version 2.0
%global pkg_name portlet-api_%{api_version}_spec
Name:          portlet-2.0-api
Version:       1.0
Release:       alt2_5jpp7
Summary:       Java Portlet Specification V2.0
Group:         Development/Java
License:       ASL 2.0
Url:           http://portals.apache.org/
# svn export http://svn.apache.org/repos/asf/portals/portlet-spec/tags/portlet-api_2.0_spec-1.0 portlet-2.0-api-1.0
# tar czf portlet-2.0-api-1.0-src-svn.tar.gz portlet-2.0-api-1.0
Source0:       portlet-2.0-api-1.0-src-svn.tar.gz
# force servlet-3.0-api use
Source1:       portlet-2.0-api-1.0-depmap

BuildRequires: jpackage-utils
BuildRequires: portals-pom

BuildRequires: tomcat-servlet-3.0-api

BuildRequires: maven-local
BuildRequires: maven-compiler-plugin
BuildRequires: maven-install-plugin
BuildRequires: maven-javadoc-plugin
BuildRequires: maven-plugin-bundle
BuildRequires: maven-resources-plugin
BuildRequires: maven-surefire-plugin

Requires:      portals-pom
Requires:      tomcat-servlet-3.0-api

Requires:      jpackage-utils
BuildArch:     noarch
Source44: import.info

%description
The Java Portlet API version 2.0 developed by the
Java Community Process JSR-286 Expert Group.

%package javadoc
Group:         Development/Java
Summary:       Javadoc for %{name}
Requires:      jpackage-utils
BuildArch: noarch

%description javadoc
This package contains javadoc for %{name}.

%prep
%setup -q
# cleanup
find . -name '*.class' -delete
find . -name '*.jar' -delete

for p in LICENSE NOTICE;do
  iconv -f iso8859-1 -t utf-8 ${p} > ${p}.conv && mv -f ${p}.conv ${p}
  sed -i 's/\r//' ${p}
done

# change apis version
sed -i "s|javax.servlet.http;version=2.4,*|javax.servlet.http;version=3.0,*|" pom.xml

%build

mvn-rpmbuild -Dproject.build.sourceEncoding=UTF-8 -Dmaven.local.depmap.file="%{SOURCE1}" install javadoc:aggregate

%install

mkdir -p %{buildroot}%{_javadir}
install -pm 644 target/%{pkg_name}-%{version}.jar %{buildroot}%{_javadir}/%{name}.jar

mkdir -p %{buildroot}%{_mavenpomdir}
install -pm 644 pom.xml %{buildroot}%{_mavenpomdir}/JPP-%{name}.pom
%add_maven_depmap JPP-%{name}.pom %{name}.jar -a "javax.portlet:portlet-api"

mkdir -p %{buildroot}%{_javadocdir}/%{name}
cp -rp target/site/apidocs/* %{buildroot}%{_javadocdir}/%{name}

%files
%{_javadir}/%{name}.jar
%{_mavenpomdir}/JPP-%{name}.pom
%{_mavendepmapfragdir}/%{name}
%doc LICENSE NOTICE

%files javadoc
%{_javadocdir}/%{name}
%doc LICENSE NOTICE

%changelog
* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 1.0-alt2_5jpp7
- new release

* Mon Jul 14 2014 Igor Vlasenko <viy@altlinux.ru> 1.0-alt2_3jpp7
- NMU rebuild to move poms and fragments

* Sat Sep 08 2012 Igor Vlasenko <viy@altlinux.ru> 1.0-alt1_3jpp7
- new version

