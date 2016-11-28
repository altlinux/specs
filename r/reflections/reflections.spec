Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
# END SourceDeps(oneline)
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
%global githash 91af9aa088b9e29d36c44b53e63b378a2ba501cd

Name:          reflections
Version:       0.9.10
Release:       alt1_2jpp8
Summary:       Java run-time meta-data analysis
License:       WTFPL
URL:           https://github.com/ronmamo/reflections
Source0:       https://github.com/ronmamo/reflections/archive/%{githash}/%{name}-%{githash}.tar.gz

BuildRequires: maven-local
BuildRequires: mvn(com.google.code.findbugs:annotations)
BuildRequires: mvn(com.google.code.gson:gson)
BuildRequires: mvn(com.google.guava:guava)
BuildRequires: mvn(dom4j:dom4j)
BuildRequires: mvn(javax.servlet:javax.servlet-api)
BuildRequires: mvn(junit:junit)
BuildRequires: mvn(org.apache.commons:commons-vfs2)
BuildRequires: mvn(org.javassist:javassist)
BuildRequires: mvn(org.jsr-305:ri)
BuildRequires: mvn(org.slf4j:slf4j-api)
BuildRequires: mvn(org.slf4j:slf4j-simple)

BuildArch:     noarch
Source44: import.info

%description
A Java run-time meta-data analysis, in the spirit of Scannotations

Reflections scans your class-path, indexes the meta-data, allows you
to query it on run-time and may save and collect that information
for many modules within your project.

Using Reflections you can query your meta-data such as:
* get all sub types of some type
* get all types/methods/fields annotated with some annotation,
  w/o annotation parameters matching
* get all resources matching matching a regular expression

%package javadoc
Group: Development/Java
Summary:       Javadoc for %{name}
BuildArch: noarch

%description javadoc
This package contains javadoc for %{name}.

%prep
%setup -q -n %{name}-%{githash}
find -name "*.class" -print -delete
find -name "*.jar" -print -delete

# Unwanted
%pom_remove_plugin :maven-clean-plugin
%pom_remove_plugin :maven-enforcer-plugin
%pom_remove_plugin :maven-source-plugin
# Use system maven default conf
%pom_remove_plugin :maven-javadoc-plugin

# Force servlet 3.1 apis
%pom_change_dep :servlet-api :javax.servlet-api:3.1.0

# Cannot find symbol package javax.annotation
%pom_add_dep org.jsr-305:ri

%mvn_file :%{name} %{name}

%build

%mvn_build -- -Dproject.build.sourceEncoding=UTF-8

%install
%mvn_install

%files -f .mfiles
%doc README.md
%doc COPYING.txt

%files javadoc -f .mfiles-javadoc
%doc COPYING.txt

%changelog
* Fri Nov 25 2016 Igor Vlasenko <viy@altlinux.ru> 0.9.10-alt1_2jpp8
- new version

* Wed Feb 03 2016 Igor Vlasenko <viy@altlinux.ru> 0.9.9-alt1_4jpp8
- new version

