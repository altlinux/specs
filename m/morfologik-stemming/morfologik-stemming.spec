Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
# END SourceDeps(oneline)
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
Name:          morfologik-stemming
Version:       2.0.1
Release:       alt1_3jpp8
Summary:       Morfologik stemming library
License:       BSD
URL:           http://morfologik.blogspot.com/
Source0:       https://github.com/morfologik/morfologik-stemming/archive/%{version}.tar.gz

BuildRequires: maven-local
BuildRequires: mvn(com.beust:jcommander)
BuildRequires: mvn(com.carrotsearch:hppc)
BuildRequires: mvn(com.google.guava:guava)
BuildRequires: mvn(commons-cli:commons-cli)
BuildRequires: mvn(commons-lang:commons-lang)
BuildRequires: mvn(org.sonatype.oss:oss-parent:pom:)

%if 0
# test deps
BuildRequires: mvn(com.carrotsearch:junit-benchmarks)
BuildRequires: mvn(org.hamcrest:hamcrest-core)
BuildRequires: mvn(junit:junit)
BuildRequires: mvn(org.easytesting:fest-assert-core:2.0M10)
%endif

BuildArch:     noarch
Source44: import.info

%description
Morfologik provides high quality lemmatisation for the Polish language,
along with tools for building and using byte-based finite state automata.

%package javadoc
Group: Development/Java
Summary:       Javadoc for %{name}
BuildArch: noarch

%description javadoc
This package contains javadoc for %{name}.

%prep
%setup -q
find . -name "*.class" -print -delete
find . -name "*.jar" -print -delete

chmod 644 README.txt
# Convert from dos to unix line ending
for file in CHANGES.txt CONTRIBUTING.txt README.txt LICENSE.txt; do
 sed -i.orig 's|\r||g' $file
 touch -r $file.orig $file
 rm $file.orig
done

%pom_add_dep org.hamcrest:hamcrest-core::test morfologik-tools
%pom_remove_plugin com.carrotsearch.randomizedtesting:junit4-maven-plugin
%pom_remove_plugin de.thetaphi:forbiddenapis
%pom_remove_plugin :maven-javadoc-plugin

# Remove classpath from manifest file
%pom_xpath_set pom:addClasspath false morfologik-tools
# Unwanted task
%pom_remove_plugin :maven-assembly-plugin morfologik-tools

%pom_change_dep :morfologik-polish ::'${project.version}' morfologik-speller

%build
# Test skipped for unavailable test deps
%mvn_build -f -- -Dproject.build.sourceEncoding=UTF-8

%install
%mvn_install

%files -f .mfiles
%doc CHANGES.txt CONTRIBUTING.txt README.txt
%doc LICENSE.txt

%files javadoc -f .mfiles-javadoc
%doc LICENSE.txt

%changelog
* Mon Nov 28 2016 Igor Vlasenko <viy@altlinux.ru> 2.0.1-alt1_3jpp8
- new version

* Sat Feb 06 2016 Igor Vlasenko <viy@altlinux.ru> 1.8.3-alt1_4jpp8
- java 8 mass update

