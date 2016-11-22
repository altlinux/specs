# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
# END SourceDeps(oneline)
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
# vim: set ts=4 sw=4 sts=4 et:
Name:           ws-xmlschema
Version:        2.0.2
Release:        alt2_13jpp8
Summary:        Apache XMLSchema
Group:          Development/Other
License:        ASL 2.0
URL:            http://ws.apache.org/commons/xmlschema20/

# wget -c http://apache.osuosl.org/ws/xmlschema/2.0.2/xmlschema-2.0.2-source-release.zip
# unzip xmlschema-2.0.2-source-release.zip
# rm -r xmlschema-2.0.2/w3c-testcases
# tar cafJ ws-xmlschema-2.0.2.tar.xz xmlschema-2.0.2
Source0:        %{name}-%{version}.tar.xz

BuildArch:      noarch

BuildRequires: javapackages-tools rpm-build-java
BuildRequires:  apache-resource-bundles
BuildRequires:  maven-local
BuildRequires:  maven-assembly-plugin
BuildRequires:  maven-compiler-plugin
BuildRequires:  maven-install-plugin
BuildRequires:  maven-jar-plugin
BuildRequires:  maven-javadoc-plugin
BuildRequires:  maven-remote-resources-plugin
BuildRequires:  maven-shade-plugin
BuildRequires:  maven-surefire-plugin
BuildRequires:  xmlunit
BuildRequires:  maven-shared
Source44: import.info

%description
Apache XMLSchema is a light weight schema object model that can be
used to manipulate or generate XML schema. It has very few external
dependencies and can be easily integrated into an existing project.


%package javadoc
Summary:        Javadocs for %{name}
Group:          Development/Java
BuildArch: noarch

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q -n xmlschema-%{version}

%pom_disable_module xmlschema-bundle-test
%pom_disable_module w3c-testcases

%build
# fastinstall profile avoids some build dependencies
# tests require unavailable dependencies
%mvn_build -f -- -Pfastinstall

%install
%mvn_install

%files -f .mfiles
%dir %{_javadir}/%{name}
%doc LICENSE NOTICE README.txt RELEASE-NOTE.txt

%files javadoc -f .mfiles-javadoc
%doc LICENSE NOTICE

%changelog
* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 2.0.2-alt2_13jpp8
- new fc release

* Tue Feb 02 2016 Igor Vlasenko <viy@altlinux.ru> 2.0.2-alt2_12jpp8
- new version

* Tue Aug 26 2014 Igor Vlasenko <viy@altlinux.ru> 2.0.2-alt2_9jpp7
- new release

* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 2.0.2-alt2_7jpp7
- new release

* Sat Jul 12 2014 Igor Vlasenko <viy@altlinux.ru> 2.0.2-alt2_4jpp7
- rebuild with new apache-resource-bundles

* Sun Sep 16 2012 Igor Vlasenko <viy@altlinux.ru> 2.0.2-alt1_4jpp7
- new version

