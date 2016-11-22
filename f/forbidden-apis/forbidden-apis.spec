# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
# END SourceDeps(oneline)
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
Name:          forbidden-apis
Version:       1.7
Release:       alt1_3jpp8
Summary:       Generics Policeman's Forbidden API check

Group:         Development/Java
License:       ASL 2.0
URL:           http://code.google.com/p/forbidden-apis/
BuildArch:     noarch

Source0:       https://oss.sonatype.org/content/repositories/releases/de/thetaphi/forbiddenapis/%{version}/forbiddenapis-%{version}-sources.jar

# Customized pom file
# Add build/test deps
# Add maven plugins configuration
Source1:       %{name}-pom.xml

BuildRequires: maven-local
BuildRequires: ant
BuildRequires: objectweb-asm >= 5
BuildRequires: dos2unix

Requires: objectweb-asm >= 5
Source44: import.info




%description
This project implements the ANT task (+ Maven Mojo) announced in the Generics
Policeman Blog. It checks Java byte code against a list of "forbidden" API
signatures. 
Allows to parse Java byte code to find invocations of method/class/field
signatures and fail build (Apache Ant, Apache Maven, or CLI).

%package javadoc
Group: Development/Java
Summary:       Javadoc for %{name}
BuildArch: noarch

%description javadoc
This package contains javadoc for %{name}.

%prep
%setup -q -n forbiddenapis-%{version}
find . -name "*.jar" -print -delete
find . -name "*.class" -print -delete
dos2unix LICENSE.txt
dos2unix NOTICE.txt
dos2unix README.txt

cp -p %{SOURCE1} pom.xml
%pom_xpath_inject pom:project "<version>%{version}</version>"

%build

%mvn_file ":%{name}" %{name}
# Skip test: 
# - Demo2 needs JDK8 to compile
# - Not able to run test with maven, requires itself
%mvn_build -f

%install
%mvn_install

mkdir -p %{buildroot}%{_sysconfdir}/ant.d
echo "ant commons-cli %{name} maven/maven-plugin-api maven-plugin-tools/maven-plugin-annotations objectweb-asm/asm objectweb-asm/asm-commons plexus/utils" > %{name}-ant
install -pm 644 %{name}-ant %{buildroot}%{_sysconfdir}/ant.d/%{name}

%files -f .mfiles
%config(noreplace) %{_sysconfdir}/ant.d/%{name}
%doc LICENSE.txt NOTICE.txt README.txt

%files javadoc -f .mfiles-javadoc
%doc LICENSE.txt NOTICE.txt

%changelog
* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 1.7-alt1_3jpp8
- new fc release

* Sat Feb 06 2016 Igor Vlasenko <viy@altlinux.ru> 1.7-alt1_2jpp8
- java 8 mass update

