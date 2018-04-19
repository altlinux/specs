Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires: rpm-build-java
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:          glassfish-transaction-api
Version:       1.2
Release:       alt1_5jpp8
Summary:       Java JTA 1.2 API Design Specification
License:       CDDL or GPLv2 with exceptions
URL:           https://java.net/projects/jta-spec/
# svn export https://svn.java.net/svn/glassfish~svn/tags/javax.transaction-api-1.2 glassfish-transaction-api-1.2
# tar cJf glassfish-transaction-api-1.2.tar.xz glassfish-transaction-api-1.2
Source0:       %{name}-%{version}.tar.xz

BuildRequires: maven-local
BuildRequires: mvn(javax.enterprise:cdi-api)
BuildRequires: mvn(net.java:jvnet-parent:pom:)
BuildRequires: mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires: mvn(org.apache.maven.plugins:maven-remote-resources-plugin)
BuildRequires: mvn(org.glassfish:legal)
BuildRequires: mvn(org.glassfish.build:spec-version-maven-plugin)

BuildArch:     noarch
Source44: import.info

%description
Project GlassFish Java Transaction API.

%package javadoc
Group: Development/Java
Summary:       Javadoc for %{name}
BuildArch: noarch

%description javadoc
This package contains javadoc for %{name}.

%prep
%setup -q

%pom_remove_plugin :findbugs-maven-plugin
%pom_remove_plugin :maven-site-plugin
%pom_remove_plugin :maven-source-plugin
%pom_remove_plugin :maven-javadoc-plugin
%pom_remove_plugin :maven-release-plugin

%mvn_file : %{name}

%build

%mvn_build

cp -p target/classes/META-INF/LICENSE.txt .
sed -i 's/\r//' LICENSE.txt

%install
%mvn_install

%files -f .mfiles
%doc --no-dereference LICENSE.txt

%files javadoc -f .mfiles-javadoc
%doc --no-dereference LICENSE.txt

%changelog
* Thu Apr 19 2018 Igor Vlasenko <viy@altlinux.ru> 1.2-alt1_5jpp8
- java update

* Thu Nov 09 2017 Igor Vlasenko <viy@altlinux.ru> 1.2-alt1_4jpp8
- fc27 update

* Sun Oct 22 2017 Igor Vlasenko <viy@altlinux.ru> 1.2-alt1_3jpp8
- new jpp release

* Tue Dec 20 2016 Igor Vlasenko <viy@altlinux.ru> 1.2-alt1_2jpp8
- new version

