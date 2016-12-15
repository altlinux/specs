Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
# END SourceDeps(oneline)
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
Name:          jandex-maven-plugin
Version:       1.0.4
Release:       alt1_2jpp8
Summary:       Jandex wrapper for Maven
License:       GPLv3+
URL:           https://github.com/wildfly/jandex-maven-plugin
Source0:       https://github.com/wildfly/jandex-maven-plugin/archive/%{name}-%{version}.tar.gz

BuildRequires: maven-local
BuildRequires: mvn(org.apache.maven:maven:pom:)
BuildRequires: mvn(org.apache.maven:maven-parent:pom:)
BuildRequires: mvn(org.apache.maven:maven-plugin-api)
BuildRequires: mvn(org.apache.maven.plugins:maven-plugin-plugin)
BuildRequires: mvn(org.jboss:jandex)
BuildRequires: mvn(org.jboss:jboss-parent:pom:)

BuildArch:     noarch
Source44: import.info

%description
This is a Maven plugin used to generate Jandex index files.

%package javadoc
Group: Development/Java
Summary:       Javadoc for %{name}
BuildArch: noarch

%description javadoc
This package contains javadoc for %{name}.

%prep
%setup -q -n %{name}-%{name}-%{version}

%mvn_file :%{name} %{name}

%build

%mvn_build

%install
%mvn_install

%files -f .mfiles
%doc README.md
%doc LICENSE.txt

%files javadoc -f .mfiles-javadoc
%doc LICENSE.txt

%changelog
* Thu Dec 15 2016 Igor Vlasenko <viy@altlinux.ru> 1.0.4-alt1_2jpp8
- new version

