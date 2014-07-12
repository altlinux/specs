# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-java
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-compat
# vim: set ts=4 sw=4 sts=4 et:
Name:           ws-xmlschema
Version:        2.0.2
Release:        alt2_4jpp7
Summary:        Apache XMLSchema
Group:          Development/Java
License:        ASL 2.0
URL:            http://ws.apache.org/commons/xmlschema20/

# wget -c http://apache.osuosl.org/ws/xmlschema/2.0.2/xmlschema-2.0.2-source-release.zip
# unzip xmlschema-2.0.2-source-release.zip
# rm -r xmlschema-2.0.2/w3c-testcases
# tar cafJ ws-xmlschema-2.0.2.tar.xz xmlschema-2.0.2
Source0:        %{name}-%{version}.tar.xz

Patch0:         xmlschema-2.0.2-no-w3c-testcase-module.patch

BuildArch:      noarch

BuildRequires:  jpackage-utils
BuildRequires: apache-resource-bundles apache-jar-resource-bundle
BuildRequires:  maven
BuildRequires:  maven-assembly-plugin
BuildRequires:  maven-compiler-plugin
BuildRequires:  maven-install-plugin
BuildRequires:  maven-jar-plugin
BuildRequires:  maven-javadoc-plugin
BuildRequires:  maven-remote-resources-plugin
BuildRequires:  maven-shade-plugin
BuildRequires:  maven-surefire-plugin
BuildRequires:  xmlunit

Requires:       jpackage-utils
Source44: import.info

%description
Apache XMLSchema is a light weight schema object model that can be
used to manipulate or generate XML schema. It has very few external
dependencies and can be easily integrated into an existing project.


%package javadoc
Summary:        Javadocs for %{name}
Group:          Development/Java
Requires:       jpackage-utils
BuildArch: noarch

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q -n xmlschema-%{version}
%patch0 -p1

%build
# fastinstall profile avoids some build dependencies
# tests require unavailable dependencies
mvn-rpmbuild \
    -Pfastinstall \
    -Dmaven.test.skip=true \
    -Dproject.build.sourceEncoding=UTF-8 \
    package javadoc:aggregate

%install

install -d -m 755 %{buildroot}%{_javadir}
install -d -m 755 %{buildroot}%{_mavenpomdir}
install -d -m 755 %{buildroot}%{_javadocdir}/%{name}

install -pm 644 xmlschema-core/target/xmlschema-core-%{version}.jar %{buildroot}%{_javadir}/xmlschema-core.jar
install -pm 644 xmlschema-core/pom.xml %{buildroot}%{_mavenpomdir}/JPP-xmlschema-core.pom
%add_maven_depmap JPP-xmlschema-core.pom xmlschema-core.jar

install -pm 644 pom.xml %{buildroot}%{_mavenpomdir}/JPP-%{name}.pom
%add_maven_depmap JPP-%{name}.pom

# javadoc
cp -rp target/site/apidocs/* %{buildroot}%{_javadocdir}/%{name}

%files
%doc LICENSE NOTICE README.txt RELEASE-NOTE.txt
%{_mavenpomdir}/*
%{_mavendepmapfragdir}/*
%{_javadir}/*

%files javadoc
%doc LICENSE NOTICE
%{_javadocdir}/%{name}

%changelog
* Sat Jul 12 2014 Igor Vlasenko <viy@altlinux.ru> 2.0.2-alt2_4jpp7
- rebuild with new apache-resource-bundles

* Sun Sep 16 2012 Igor Vlasenko <viy@altlinux.ru> 2.0.2-alt1_4jpp7
- new version

