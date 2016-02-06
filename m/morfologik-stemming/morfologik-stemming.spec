Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-java
# END SourceDeps(oneline)
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
Name:          morfologik-stemming
Version:       1.8.3
Release:       alt1_4jpp8
Summary:       Morfologik stemming library
License:       BSD
URL:           http://morfologik.blogspot.com/
Source0:       https://github.com/morfologik/morfologik-stemming/archive/%{version}.tar.gz

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

BuildRequires: maven-local

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

# remove classpath from manifest files
for m in morfologik-polish morfologik-speller %{name} morfologik-tools ;do
%pom_xpath_set "pom:project/pom:build/pom:plugins/pom:plugin[pom:artifactId = 'maven-jar-plugin']/pom:configuration/pom:archive/pom:manifest/pom:addClasspath" false ${m}
done

%pom_remove_dep org.easytesting:fest-assert-core %{name}

%pom_disable_module morfologik-distribution
%pom_remove_plugin com.pyx4me:proguard-maven-plugin morfologik-tools

chmod 644 README
sed -i 's/\r//' CHANGES CONTRIBUTOR README morfologik.LICENSE

%pom_add_dep org.hamcrest:hamcrest-core::test morfologik-tools
sed -i "s|org.junit.internal.matchers.StringContains|org.hamcrest.core.StringContains|" \
 morfologik-tools/src/test/java/morfologik/tools/FSABuildToolTest.java

%build
# Test skipped for unavailable test deps
%mvn_build -f

%install
%mvn_install

%files -f .mfiles
%dir %{_javadir}/%{name}
%doc CHANGES CONTRIBUTOR README
%doc morfologik.LICENSE

%files javadoc -f .mfiles-javadoc
%doc morfologik.LICENSE

%changelog
* Sat Feb 06 2016 Igor Vlasenko <viy@altlinux.ru> 1.8.3-alt1_4jpp8
- java 8 mass update

