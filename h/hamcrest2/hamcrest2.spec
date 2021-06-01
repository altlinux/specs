Group: Development/Java
BuildRequires: /proc rpm-build-java
BuildRequires: jpackage-11-compat
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%global srcname hamcrest

Name:           hamcrest2
Version:        2.2
Release:        alt1_3jpp11
Summary:        Library of matchers for building test expressions
License:        BSD

URL:            https://github.com/hamcrest/JavaHamcrest
Source0:        %{url}/archive/v%{version}/%{srcname}-%{version}.tar.gz
Source1:        https://repo1.maven.org/maven2/org/%{srcname}/%{srcname}/%{version}/%{srcname}-%{version}.pom

BuildArch:      noarch

BuildRequires:  java-1.8.0-openjdk-devel
BuildRequires:  maven-local
BuildRequires:  mvn(junit:junit)
Source44: import.info

%description
Provides a library of matcher objects (also known as constraints or predicates)
allowing 'match' rules to be defined declaratively, to be used in other
frameworks. Typical scenarios include testing frameworks, mocking libraries and
UI validation rules.


%package javadoc
Group: Development/Java
Summary:        Javadoc for %{name}
BuildArch: noarch

%description javadoc
Javadoc for %{name}.


%prep
%setup -q -n JavaHamcrest-%{version}

# drop docs and unused gradle build system
rm -r docs
rm -r *gradle*
rm -r */*.gradle

# drop everything but hamcrest itself
# -core:        empty legacy module, only contains a deprecation warning
# -integration: legacy module, stuck at an old version
# -library:     empty legacy module, only contains a deprecation warning
mv hamcrest/src .
rm -r hamcrest
rm -r hamcrest-core
rm -r hamcrest-integration
rm -r hamcrest-library

# use pom.xml from maven central and add junit dependency manually
cp -p %{SOURCE1} pom.xml
%pom_add_dep junit:junit

# convert LICENSE.txt to unix line endings
sed -i 's/\r//' LICENSE.txt


%build
# build against OpenJDK 8, code is not compatible with Java 9+ yet
export JAVA_HOME=%{_jvmdir}/java-1.8.0
# forcing Java 8 because of required language features
%mvn_build -- -Dmaven.compiler.source=1.8 -Dmaven.compiler.target=1.8


%install
%mvn_install


%files -f .mfiles
%doc README.md
%doc --no-dereference LICENSE.txt

%files javadoc -f .mfiles-javadoc
%doc --no-dereference LICENSE.txt


%changelog
* Tue Jun 01 2021 Igor Vlasenko <viy@altlinux.org> 2.2-alt1_3jpp11
- new version

