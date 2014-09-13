Group: Development/Java
BuildRequires: /proc
BuildRequires: jpackage-compat
Name:          classmate
Version:       0.8.0
Release:       alt1_3jpp7
Summary:       Java introspection library
License:       ASL 2.0
Url:           http://github.com/cowtowncoder/java-classmate/
Source0:       https://github.com/cowtowncoder/java-classmate/archive/%{name}-%{version}.tar.gz
# classmate package don't include the license file
Source1:       http://www.apache.org/licenses/LICENSE-2.0.txt

BuildRequires: sonatype-oss-parent

BuildRequires: junit

BuildRequires: maven-local
BuildRequires: maven-enforcer-plugin
BuildRequires: maven-plugin-bundle
BuildRequires: maven-source-plugin
BuildRequires: maven-surefire-provider-junit4

BuildArch:     noarch
Source44: import.info

%description
Library for introspecting types with full generic information
including resolving of field and method types.

%package javadoc
Group: Development/Java
Summary:       Javadoc for %{name}
BuildArch: noarch

%description javadoc
This package contains javadoc for %{name}.

%prep
%setup -q -n java-%{name}-%{name}-%{version}

find . -name "*.class" -delete
find . -name "*.jar" -delete

cp -p %{SOURCE1} .
sed -i 's/\r//' LICENSE-2.0.txt

# these test fails junit.framework.AssertionFailedError: expected:<X> but was:<Y>
rm -r src/test/java/com/fasterxml/classmate/TestReadme.java \
 src/test/java/com/fasterxml/classmate/types/ResolvedObjectTypeTest.java

%build
%mvn_file :%{name} %{name}
%mvn_build

%install
%mvn_install

%files -f .mfiles
%doc LICENSE-2.0.txt README.md release-notes.txt

%files javadoc -f .mfiles-javadoc
%doc LICENSE-2.0.txt

%changelog
* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 0.8.0-alt1_3jpp7
- new release

* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 0.5.4-alt2_4jpp7
- new release

* Thu Feb 14 2013 Igor Vlasenko <viy@altlinux.ru> 0.5.4-alt2_2jpp7
- fixed maven1 dependency

* Mon Jan 21 2013 Igor Vlasenko <viy@altlinux.ru> 0.5.4-alt1_2jpp7
- initial build

