Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
# END SourceDeps(oneline)
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
Name:          shibboleth-java-parent-v3
Version:       8
Release:       alt1_1jpp8
Summary:       Shibboleth Project V3 Super POM
License:       ASL 2.0
URL:           http://shibboleth.net/
#git clone git://git.shibboleth.net/java-parent-project-v3
#(cd java-parent-project-v3/ && git archive --format=tar --prefix=shibboleth-java-parent-v3-8/ 8 | xz > ../shibboleth-java-parent-v3-8.tar.xz)
Source0:       %{name}-%{version}.tar.xz

BuildRequires: maven-local
BuildRequires: mvn(ch.qos.logback:logback-classic)
BuildRequires: mvn(org.apache.maven.plugins:maven-checkstyle-plugin)
BuildRequires: mvn(org.slf4j:jcl-over-slf4j)
BuildRequires: mvn(org.slf4j:jul-to-slf4j)
BuildRequires: mvn(org.slf4j:log4j-over-slf4j)
BuildRequires: mvn(org.slf4j:slf4j-api)
BuildRequires: mvn(org.testng:testng)
BuildRequires: mvn(xmlunit:xmlunit)

# com.unboundid:unboundid-ldapsdk:2.3.8
# org.cryptacular:cryptacular:1.0
# org.ldaptive:ldaptive:1.0.6
BuildArch:     noarch
Source44: import.info

%description
A POM containing properties, profiles, plugin configurations,
etc. that are common across all Shibboleth V3 projects.

%prep
%setup -q -n %{name}-%{version}

%build

%mvn_build -j

%install
%mvn_install

%files -f .mfiles
%doc resources/doc/RELEASE-NOTES.txt
%doc resources/doc/LICENSE.txt

%changelog
* Tue Dec 20 2016 Igor Vlasenko <viy@altlinux.ru> 8-alt1_1jpp8
- new version

