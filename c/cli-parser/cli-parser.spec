Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires: rpm-build-java
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:          cli-parser
Version:       1.1.2
Release:       alt1_8jpp8
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
* Thu Apr 19 2018 Igor Vlasenko <viy@altlinux.ru> 1.1.2-alt1_8jpp8
- java update

* Thu Nov 09 2017 Igor Vlasenko <viy@altlinux.ru> 1.1.2-alt1_7jpp8
- fc27 update

* Sun Oct 22 2017 Igor Vlasenko <viy@altlinux.ru> 1.1.2-alt1_6jpp8
- new jpp release

* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 1.1.2-alt1_5jpp8
- new fc release

* Mon Feb 08 2016 Igor Vlasenko <viy@altlinux.ru> 1.1.2-alt1_4jpp8
- new version

