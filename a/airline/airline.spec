Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
# END SourceDeps(oneline)
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
Name:          airline
Version:       0.7
Release:       alt1_4jpp8
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
%doc license.txt notice.md

%files javadoc -f .mfiles-javadoc
%doc license.txt notice.md

%changelog
* Mon Dec 19 2016 Igor Vlasenko <viy@altlinux.ru> 0.7-alt1_4jpp8
- new version

