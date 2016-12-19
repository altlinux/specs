Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
# END SourceDeps(oneline)
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
Name:          javawriter
Version:       2.5.1
Release:       alt1_3jpp8
Summary:       A Java API for generating .java source files
License:       ASL 2.0
URL:           https://github.com/square/javapoet
Source0:       https://github.com/square/javapoet/archive/%{name}-%{version}.tar.gz

BuildRequires: maven-local
BuildRequires: mvn(org.sonatype.oss:oss-parent:pom:)

%if 0
# Test deps
BuildRequires: mvn(junit:junit)
# Unavailable test deps
BuildRequires: mvn(org.easytesting:fest-assert-core:2.0M8)
%endif

BuildArch:     noarch
Source44: import.info

%description
A utility class which aids in generating Java source files.

%package javadoc
Group: Development/Java
Summary:       Javadoc for %{name}
BuildArch: noarch

%description javadoc
This package contains javadoc for %{name}.

%prep
%setup -q -n javapoet-%{name}-%{version}

%pom_xpath_remove "pom:dependency[pom:scope = 'test']" 

%pom_remove_plugin :maven-checkstyle-plugin

%mvn_file : %{name}

%build

# Unavailable test deps: org.easytesting:fest-assert-core:2.0M8
%mvn_build -f

%install
%mvn_install

%files -f .mfiles
%doc CHANGELOG.md CONTRIBUTING.md README.md
%doc LICENSE.txt

%files javadoc -f .mfiles-javadoc
%doc LICENSE.txt

%changelog
* Mon Dec 19 2016 Igor Vlasenko <viy@altlinux.ru> 2.5.1-alt1_3jpp8
- new version

