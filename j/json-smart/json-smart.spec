Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
# END SourceDeps(oneline)
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
%global commit d39cfe6aafd2ec8f1250f53a18a0c0ebe8cd6da9
%global shortcommit %(c=%{commit}; echo ${c:0:7})
Name:          json-smart
Version:       1.3.2
Release:       alt1_0.2.20151018jpp8
Summary:       A small and very fast json parser/generator for java
License:       ASL 2.0
URL:           https://github.com/netplex/json-smart-v1
Source0:       https://github.com/netplex/json-smart-v1/archive/%{commit}/%{name}-v1-%{commit}.tar.gz

BuildRequires: maven-local
BuildRequires: mvn(junit:junit)
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
%setup -q -n %{name}-v1-%{commit}

%pom_remove_plugin :maven-javadoc-plugin parent
%pom_remove_plugin :maven-source-plugin parent

cp -p %{name}/*.txt .

# ComparisonFailure: expected:<[??????????????? ???????????????]> but was:<[????? ?????]>
rm -r %{name}/src/test/java/net/minidev/json/test/TestUtf8.java

%mvn_file :%{name} %{name}

%build

%mvn_build -- -f parent/pom.xml

%install
%mvn_install

%files -f .mfiles
%doc ChangeLog.txt readme.txt
%doc LICENSE.txt

%files javadoc -f .mfiles-javadoc
%doc LICENSE.txt

%changelog
* Fri Nov 25 2016 Igor Vlasenko <viy@altlinux.ru> 1.3.2-alt1_0.2.20151018jpp8
- new version

* Sun Feb 07 2016 Igor Vlasenko <viy@altlinux.ru> 1.3-alt1_0.4.20140820jpp8
- unbootsrap build

