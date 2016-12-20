Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
# END SourceDeps(oneline)
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
Name:          protoparser
Version:       3.1.5
Release:       alt1_1jpp8
Summary:       Java parser for .proto schema declarations
# Source files without license headers https://github.com/square/protoparser/issues/105
License:       ASL 2.0
URL:           https://github.com/square/protoparser
Source0:       https://github.com/square/protoparser/archive/%{name}-%{version}.tar.gz

BuildRequires: maven-local
BuildRequires: mvn(com.google.auto.value:auto-value)
BuildRequires: mvn(junit:junit)
BuildRequires: mvn(org.assertj:assertj-core)
BuildRequires: mvn(org.sonatype.oss:oss-parent:pom:)

BuildArch:     noarch
Source44: import.info

%description
ProtoParser will parse a standalone File or schema data directly and
return an object representation as a ProtoFile instance.

%package javadoc
Group: Development/Java
Summary:       Javadoc for %{name}
BuildArch: noarch

%description javadoc
This package contains javadoc for %{name}.

%prep
%setup -q -n %{name}-%{name}-%{version}

%pom_remove_plugin :maven-checkstyle-plugin

%pom_change_dep org.easytesting:fest-assert-core org.assertj:assertj-core:2.0.0
find ./ -name "*.java" -exec sed -i "s/org.fest.assertions/org.assertj.core/g" {} +

%mvn_file : %{name}

%build

%mvn_build

%install
%mvn_install

%files -f .mfiles
%doc CHANGELOG.md CONTRIBUTING.md README.md
%doc LICENSE.txt

%files javadoc -f .mfiles-javadoc
%doc LICENSE.txt

%changelog
* Tue Dec 20 2016 Igor Vlasenko <viy@altlinux.ru> 3.1.5-alt1_1jpp8
- new version

