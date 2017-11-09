Group: Development/Other
# BEGIN SourceDeps(oneline):
BuildRequires: rpm-build-java
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:          ws-xmlschema
Version:       2.2.1
Release:       alt1_3jpp8
Summary:       Apache XMLSchema
License:       ASL 2.0
URL:           http://ws.apache.org/xmlschema/
# wget -c http://www.apache.org/dist/ws/xmlschema/2.2.1/xmlschema-2.2.1-source-release.zip
# unzip xmlschema-2.2.1-source-release.zip
# rm -r xmlschema-2.2.1/w3c-testcases
# tar cafJ ws-xmlschema-2.2.1.tar.xz xmlschema-2.2.1
Source0:       %{name}-%{version}.tar.xz

BuildRequires: maven-local
BuildRequires: mvn(org.apache:apache:pom:)
BuildRequires: mvn(org.apache:apache-jar-resource-bundle)
BuildRequires: mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires: mvn(org.apache.maven.plugins:maven-assembly-plugin)
BuildRequires: mvn(org.apache.maven.plugins:maven-remote-resources-plugin)

BuildArch:     noarch
Source44: import.info

%description
Apache XMLSchema is a light weight schema object model that can be
used to manipulate or generate XML schema. It has very few external
dependencies and can be easily integrated into an existing project.

%package javadoc
Group: Development/Java
Summary:       Javadoc for %{name}
BuildArch: noarch

%description javadoc
This package contains the API documentation for %{name}.

%package parent
Group: Development/Other
Summary:       XMLSchema Parent POM

%description parent
XMLSchema Parent POM.

%package walker
Group: Development/Other
Summary:       XMLSchema Walker

%description walker
Code to walk an XML Schema and confirm an XML Document conforms to it.

%prep
%setup -q -n xmlschema-%{version}

%pom_disable_module xmlschema-bundle-test
%pom_disable_module w3c-testcases

# Convert from dos to unix line ending
sed -i.orig 's|\r||g' RELEASE-NOTE.txt
touch -r RELEASE-NOTE.txt.orig RELEASE-NOTE.txt
rm RELEASE-NOTE.txt.orig

%build

# fastinstall profile avoids some build dependencies
# tests require unavailable dependencies
%mvn_build -sf -- -Pfastinstall

%install
%mvn_install

%files -f .mfiles-xmlschema-core
%doc README.txt RELEASE-NOTE.txt
%doc LICENSE NOTICE

%files parent -f .mfiles-xmlschema
%doc LICENSE NOTICE

%files walker -f .mfiles-xmlschema-walker

%files javadoc -f .mfiles-javadoc
%doc LICENSE NOTICE

%changelog
* Thu Nov 09 2017 Igor Vlasenko <viy@altlinux.ru> 2.2.1-alt1_3jpp8
- fc27 update

* Sun Oct 22 2017 Igor Vlasenko <viy@altlinux.ru> 2.2.1-alt1_2jpp8
- new jpp release

* Fri Dec 16 2016 Igor Vlasenko <viy@altlinux.ru> 2.2.1-alt1_1jpp8
- new version

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

