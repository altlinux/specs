Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires: rpm-build-java
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:          protoparser
Version:       3.1.5
Release:       alt1_4jpp8
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
%doc --no-dereference LICENSE.txt

%files javadoc -f .mfiles-javadoc
%doc --no-dereference LICENSE.txt

%changelog
* Thu Apr 19 2018 Igor Vlasenko <viy@altlinux.ru> 3.1.5-alt1_4jpp8
- java update

* Thu Nov 09 2017 Igor Vlasenko <viy@altlinux.ru> 3.1.5-alt1_3jpp8
- fc27 update

* Sun Oct 22 2017 Igor Vlasenko <viy@altlinux.ru> 3.1.5-alt1_2jpp8
- new jpp release

* Tue Dec 20 2016 Igor Vlasenko <viy@altlinux.ru> 3.1.5-alt1_1jpp8
- new version

