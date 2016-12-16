Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
BuildRequires: unzip
# END SourceDeps(oneline)
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
Name:             rmic-maven-plugin
Version:          1.2.1
Release:          alt1_13jpp8
Summary:          Uses the java rmic compiler to generate classes used in remote method invocation
License:          MIT
URL:              http://mojo.codehaus.org/%{name}
BuildArch:        noarch

Source0:          http://repo2.maven.org/maven2/org/codehaus/mojo/%{name}/%{version}/%{name}-%{version}-source-release.zip

Patch0:           pom-compiler-source-target.patch

BuildRequires:  maven-local
BuildRequires:  mvn(junit:junit)
BuildRequires:  mvn(org.apache.maven:maven-model:2.0.6)
BuildRequires:  mvn(org.apache.maven:maven-plugin-api)
BuildRequires:  mvn(org.apache.maven:maven-project)
BuildRequires:  mvn(org.apache.maven.plugins:maven-invoker-plugin)
BuildRequires:  mvn(org.codehaus.mojo:mojo-parent:pom:)
BuildRequires:  mvn(org.codehaus.plexus:plexus-archiver)
BuildRequires:  mvn(org.codehaus.plexus:plexus-compiler-api)
BuildRequires:  mvn(org.codehaus.plexus:plexus-utils)
BuildRequires:  mvn(org.apache.maven.plugins:maven-plugin-plugin)
Source44: import.info

%description
This plugin works with Maven 2 and uses the java rmic compiler to generate
classes used in remote method invocation.

%package javadoc
Group: Development/Java
Summary:          Javadoc for %{name}
BuildArch: noarch

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q
sed -i -e "s|groupId>plexus|groupId>org.codehaus.plexus|g" pom.xml

%patch0 -p0

%pom_add_dep "junit:junit::test"

%build
# Unit tests pass, but for some reason the integrations fail in mock
%mvn_build -- -Dmaven.test.failure.ignore=true

%install
%mvn_install

%files -f .mfiles
%doc License.txt

%files javadoc -f .mfiles-javadoc
%doc License.txt

%changelog
* Fri Dec 16 2016 Igor Vlasenko <viy@altlinux.ru> 1.2.1-alt1_13jpp8
- new fc release

* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 1.2.1-alt1_12jpp8
- new fc release

* Sun Jan 31 2016 Igor Vlasenko <viy@altlinux.ru> 1.2.1-alt1_11jpp8
- new version

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 1.2.1-alt1_6jpp7
- new release

* Fri Aug 01 2014 Igor Vlasenko <viy@altlinux.ru> 1.2.1-alt1_4jpp7
- new version

* Fri Jul 18 2014 Igor Vlasenko <viy@altlinux.ru> 1.2.0-alt4_1jpp7
- fixed build

* Mon Jul 14 2014 Igor Vlasenko <viy@altlinux.ru> 1.2.0-alt3_1jpp7
- NMU rebuild to move poms and fragments

* Tue Sep 11 2012 Igor Vlasenko <viy@altlinux.ru> 1.2.0-alt2_1jpp7
- fixed build

* Fri Aug 31 2012 Igor Vlasenko <viy@altlinux.ru> 1.2.0-alt1_1jpp7
- new version

