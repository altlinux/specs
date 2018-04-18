Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
BuildRequires: rpm-build-java
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%global patchlvl 1

Name:           jenkins-xstream
Version:        1.4.7
Release:        alt4_13.jenkins1jpp8
Summary:        Jenkins XStream library

License:        BSD
URL:            https://github.com/jenkinsci/xstream
Source0:        https://github.com/jenkinsci/xstream/archive/%{version}-jenkins-%{patchlvl}.tar.gz

# Fixes deserialization of void
# https://bugzilla.redhat.com/show_bug.cgi?id=1441541
# backport of https://github.com/x-stream/xstream/commit/b3570be2f39234e61f99f9a20640756ea71b1b40
Patch0:         0001-Prevent-deserialization-of-void.patch

BuildRequires:  maven-local
BuildRequires:  mvn(cglib:cglib)
BuildRequires:  mvn(commons-lang:commons-lang)
BuildRequires:  mvn(com.thoughtworks.xstream:xstream-parent:pom:)
BuildRequires:  mvn(dom4j:dom4j)
BuildRequires:  mvn(joda-time:joda-time)
BuildRequires:  mvn(junit:junit)
BuildRequires:  mvn(net.sf.kxml:kxml2)
BuildRequires:  mvn(org.apache.maven.plugins:maven-eclipse-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-enforcer-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-release-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-source-plugin)
BuildRequires:  mvn(org.codehaus:codehaus-parent:pom:)
BuildRequires:  mvn(org.codehaus.jettison:jettison)
BuildRequires:  mvn(org.codehaus.woodstox:wstx-asl)
BuildRequires:  mvn(org.jdom:jdom)
BuildRequires:  mvn(org.jdom:jdom2)
BuildRequires:  mvn(org.json:json)
BuildRequires:  mvn(oro:oro)
BuildRequires:  mvn(stax:stax)
BuildRequires:  mvn(stax:stax-api)
BuildRequires:  mvn(xom:xom)
BuildRequires:  mvn(xpp3:xpp3_min)

BuildArch:      noarch
Source44: import.info

%description
XStream is a simple library to serialize objects to XML
and back again. A high level facade is supplied that
simplifies common use cases. Custom objects can be serialized
without need for specifying mappings. Speed and low memory
footprint are a crucial part of the design, making it suitable
for large object graphs or systems with high message throughput.
No information is duplicated that can be obtained via reflection.
This results in XML that is easier to read for humans and more
compact than native Java serialization. XStream serializes internal
fields, including private and final. Supports non-public and inner
classes. Classes are not required to have default constructor.
Duplicate references encountered in the object-model will be
maintained. Supports circular references. By implementing an
interface, XStream can serialize directly to/from any tree
structure (not just XML). Strategies can be registered allowing
customization of how particular types are represented as XML.
When an exception occurs due to malformed XML, detailed diagnostics
are provided to help isolate and fix the problem.

This package contains XStream fork used in Jenkins.


%package        javadoc
Group: Development/Java
Summary:        Javadoc for %{name}
BuildArch: noarch

%description javadoc
API documentation for %{name}.

%prep
%setup -q -n xstream-%{version}-jenkins-%{patchlvl}

%patch0 -p1

# no need for uber artifact
%pom_disable_module xstream-distribution
# and Jenkins doesn't use hibernate and benchmark artifact
%pom_disable_module xstream-hibernate
%pom_disable_module xstream-benchmark

# fix gIds for parent POM, Jenkins upstream uses "org.jvnet.hudson"
%pom_xpath_set "pom:project/pom:groupId" "org.jvnet.hudson"

# unavailable deps
%pom_xpath_remove "pom:extension[pom:artifactId[text()='wagon-webdav']]"
%pom_remove_dep :xml-writer xstream
%pom_remove_dep :kxml2-min xstream

# Replace old xmlpull dependency with xpp3
%pom_change_dep :xmlpull xpp3:xpp3:1.1.4c xstream

# missing dep proxytoys:proxytoys
%pom_remove_plugin :maven-dependency-plugin xstream

# use cglib 3.x
%pom_remove_dep :cglib-nodep xstream
%pom_add_dep cglib:cglib xstream "<optional>true</optional>"

# remove OSGi metadata - it would duplicate vanilla xstream
%pom_remove_plugin -r :maven-jar-plugin
%pom_remove_plugin -r :maven-bundle-plugin

%build
# tests require old JMock library (version 1.x)
%mvn_build -f

%install
%mvn_install

%files -f .mfiles
%dir %{_javadir}/%{name}
%doc LICENSE.txt
%files javadoc -f .mfiles-javadoc
%doc LICENSE.txt

%changelog
* Sun Apr 15 2018 Igor Vlasenko <viy@altlinux.ru> 1.4.7-alt4_13.jenkins1jpp8
- java update

* Thu Nov 09 2017 Igor Vlasenko <viy@altlinux.ru> 1.4.7-alt4_12.jenkins1jpp8
- fc27 update

* Sun Oct 22 2017 Igor Vlasenko <viy@altlinux.ru> 1.4.7-alt4_11.jenkins1jpp8
- new jpp release

* Fri Dec 16 2016 Igor Vlasenko <viy@altlinux.ru> 1.4.7-alt4_8.jenkins1jpp8
- removed alias; should have org.jvnet.hudson

* Thu Dec 15 2016 Igor Vlasenko <viy@altlinux.ru> 1.4.7-alt3_8.jenkins1jpp8
- added org.jvnet.hudson:xstream alias

* Wed Dec 07 2016 Igor Vlasenko <viy@altlinux.ru> 1.4.7-alt2_8.jenkins1jpp8
- fixed build

* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 1.4.7-alt1_8.jenkins1jpp8
- new fc release

* Tue Feb 09 2016 Igor Vlasenko <viy@altlinux.ru> 1.4.7-alt1_6.jenkins1jpp8
- java 8 mass update

