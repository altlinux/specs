Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires: rpm-build-java
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:          airline
Version:       0.7
Release:       alt1_7jpp8
Summary:       Java annotation-based framework
License:       ASL 2.0
URL:           https://github.com/airlift/airline
Source0:       https://github.com/airlift/airline/archive/%{version}.tar.gz

BuildRequires: maven-local
BuildRequires: mvn(com.google.code.findbugs:annotations)
BuildRequires: mvn(com.google.code.findbugs:jsr305)
BuildRequires: mvn(com.google.guava:guava)
BuildRequires: mvn(javax.inject:javax.inject)
BuildRequires: mvn(org.testng:testng)
BuildArch:     noarch
Source44: import.info

%description
Airline is a Java annotation-based framework
for parsing Git like command line structures.

%package javadoc
Group: Development/Java
Summary:       Javadoc for %{name}
BuildArch: noarch

%description javadoc
This package contains javadoc for %{name}.

%prep
%setup -q
find -name '*.class' -delete
find -name '*.jar' -delete

# io.airlift:airbase:pom:28
%pom_remove_parent
%pom_xpath_inject "pom:project" "<groupId>io.airlift</groupId>"
# cannot find symbol javax.annotation.Nullable
%pom_add_dep com.google.code.findbugs:jsr305:2.0.3

%pom_xpath_inject "pom:dependency[pom:artifactId='annotations']" '<version>2.0.3</version>'
%pom_xpath_inject "pom:dependency[pom:artifactId='guava']" '<version>18.0</version>'
%pom_xpath_inject "pom:dependency[pom:artifactId='testng']" '<version>6.8.7</version>'

%mvn_file :%{name} %{name}

%build

%mvn_build -- -Dproject.build.sourceEncoding=UTF-8

%install
%mvn_install

%files -f .mfiles
%doc README.md
%doc --no-dereference license.txt notice.md

%files javadoc -f .mfiles-javadoc
%doc --no-dereference license.txt notice.md

%changelog
* Sun Apr 15 2018 Igor Vlasenko <viy@altlinux.ru> 0.7-alt1_7jpp8
- java update

* Thu Nov 09 2017 Igor Vlasenko <viy@altlinux.ru> 0.7-alt1_6jpp8
- fc27 update

* Sun Oct 22 2017 Igor Vlasenko <viy@altlinux.ru> 0.7-alt1_5jpp8
- new jpp release

* Mon Dec 19 2016 Igor Vlasenko <viy@altlinux.ru> 0.7-alt1_4jpp8
- new version

