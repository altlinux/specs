Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
# END SourceDeps(oneline)
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
Name:          cli-parser
Version:       1.1.2
Release:       alt1_5jpp8
Summary:       Command Line Interface Parser for Java
License:       ASL 2.0
URL:           https://github.com/spullara/cli-parser
Source0:       https://github.com/spullara/cli-parser/archive/%{name}-%{version}.tar.gz

# Test deps
BuildRequires: mvn(junit:junit)

BuildRequires: maven-local
BuildArch:     noarch
Source44: import.info

%description
An annotation-based command line interface parser.

%package javadoc
Group: Development/Java
Summary:       Javadoc for %{name}
BuildArch: noarch

%description javadoc
This package contains javadoc for %{name}.

%prep
%setup -q -n %{name}-%{name}-%{version}
find . -name "*.class" -print -delete
find . -name "*.jar" -print -delete

%pom_remove_plugin :maven-gpg-plugin

%mvn_file : %{name}

%build

%mvn_build -- -Dproject.build.sourceEncoding=UTF-8

%install
%mvn_install

%files -f .mfiles
%doc README.md

%files javadoc -f .mfiles-javadoc
%doc README.md

%changelog
* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 1.1.2-alt1_5jpp8
- new fc release

* Mon Feb 08 2016 Igor Vlasenko <viy@altlinux.ru> 1.1.2-alt1_4jpp8
- new version

