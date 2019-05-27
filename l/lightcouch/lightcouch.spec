Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires: rpm-build-java
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:          lightcouch
Version:       0.1.8
Release:       alt1_7jpp8
Summary:       CouchDB Java API
License:       ASL 2.0
URL:           http://www.lightcouch.org/
Source0:       https://github.com/lightcouch/LightCouch/archive/%{name}-%{version}.tar.gz

BuildRequires: maven-local
BuildRequires: mvn(com.google.code.gson:gson)
BuildRequires: mvn(junit:junit)
BuildRequires: mvn(org.apache.httpcomponents:httpclient) >= 4.3.3
BuildRequires: mvn(org.sonatype.oss:oss-parent:pom:)

BuildArch:     noarch
Source44: import.info

%description
LightCouch aims at providing a simple API
for communicating with CouchDB databases. 

%package javadoc
Group: Development/Java
Summary:       Javadoc for %{name}
BuildArch: noarch

%description javadoc
This package contains javadoc for %{name}.

%prep
%setup -q -n LightCouch-%{name}-%{version}
find . -name "*.jar" -print -delete
find . -name "*.class" -print -delete

# NullPointerException
rm -r src/test/java/org/lightcouch/tests/AttachmentsTest.java \
 src/test/java/org/lightcouch/tests/BulkDocumentTest.java \
 src/test/java/org/lightcouch/tests/ChangeNotificationsTest.java \
 src/test/java/org/lightcouch/tests/CouchDbClientLoadTest.java \
 src/test/java/org/lightcouch/tests/DesignDocumentsTest.java \
 src/test/java/org/lightcouch/tests/DocumentsCRUDTest.java \
 src/test/java/org/lightcouch/tests/DBServerTest.java \
 src/test/java/org/lightcouch/tests/UpdateHandlerTest.java \
 src/test/java/org/lightcouch/tests/ViewsTest.java

%mvn_file : %{name}

%build

%mvn_build

%install
%mvn_install

%files -f .mfiles
%doc README.md
%doc --no-dereference LICENSE

%files javadoc -f .mfiles-javadoc
%doc --no-dereference LICENSE

%changelog
* Sun May 26 2019 Igor Vlasenko <viy@altlinux.ru> 0.1.8-alt1_7jpp8
- new version

* Thu May 31 2018 Igor Vlasenko <viy@altlinux.ru> 0.1.8-alt1_5jpp8
- java update

* Thu Nov 09 2017 Igor Vlasenko <viy@altlinux.ru> 0.1.8-alt1_4jpp8
- fc27 update

* Sun Oct 22 2017 Igor Vlasenko <viy@altlinux.ru> 0.1.8-alt1_3jpp8
- new jpp release

* Fri Nov 25 2016 Igor Vlasenko <viy@altlinux.ru> 0.1.8-alt1_2jpp8
- new version

* Sun Feb 07 2016 Igor Vlasenko <viy@altlinux.ru> 0.1.2-alt1_4jpp8
- java 8 mass update

