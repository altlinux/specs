Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires: rpm-build-java
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:          json-smart
Version:       2.2
Release:       alt1_4jpp8
Summary:       A small and very fast json parser/generator for java
License:       ASL 2.0
URL:           https://github.com/netplex/json-smart-v2
Source0:       https://github.com/netplex/json-smart-v2/archive/%{version}.tar.gz

BuildRequires: maven-local
BuildRequires: mvn(junit:junit)
BuildRequires: mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires: mvn(org.ow2.asm:asm)
BuildRequires: mvn(org.sonatype.oss:oss-parent:pom:)

BuildArch:     noarch
Source44: import.info

%description
Json-smart is a performance focused, JSON processor lib.

%package javadoc
Group: Development/Java
Summary:       Javadoc for %{name}
BuildArch: noarch

%description javadoc
This package contains javadoc for %{name}.

%prep
%setup -q -n %{name}-v2-%{version}

%pom_remove_dep :json-smart-mini parent
%pom_remove_plugin :maven-javadoc-plugin parent
%pom_remove_plugin :maven-source-plugin parent
%pom_xpath_set "pom:dependency[pom:artifactId='accessors-smart']/pom:version" '${project.version}' parent

%pom_xpath_set "pom:Bundle-Version" "1.1" accessors-smart
%pom_xpath_remove "pom:Embed-Dependency" accessors-smart
%pom_xpath_remove "pom:Embed-Dependency" %{name}

%pom_xpath_inject "pom:dependency[pom:artifactId='accessors-smart']" "<version>%{version}</version>" %{name}
%pom_xpath_remove "pom:project/pom:version" accessors-smart
%pom_xpath_inject "pom:project" "<version>%{version}</version>" accessors-smart

cp -p %{name}/*.txt .

%mvn_file :%{name} %{name}
%mvn_file :accessors-smart accessors-smart

rm accessors-smart/src/test/java/net/minidev/asm/TestDateConvert.java

%build

%mvn_build -- -f parent/pom.xml

%install
%mvn_install

%files -f .mfiles
%doc ChangeLog.txt readme.txt
%doc --no-dereference LICENSE.txt

%files javadoc -f .mfiles-javadoc
%doc --no-dereference LICENSE.txt

%changelog
* Thu Apr 19 2018 Igor Vlasenko <viy@altlinux.ru> 2.2-alt1_4jpp8
- java update

* Thu Nov 09 2017 Igor Vlasenko <viy@altlinux.ru> 2.2-alt1_3jpp8
- fc27 update

* Wed Nov 01 2017 Igor Vlasenko <viy@altlinux.ru> 2.2-alt1_2jpp8
- new jpp release

* Fri Nov 25 2016 Igor Vlasenko <viy@altlinux.ru> 1.3.2-alt1_0.2.20151018jpp8
- new version

* Sun Feb 07 2016 Igor Vlasenko <viy@altlinux.ru> 1.3-alt1_0.4.20140820jpp8
- unbootsrap build

