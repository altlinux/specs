Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
# END SourceDeps(oneline)
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
Name:          jackson-databind
Version:       2.6.3
Release:       alt1_2jpp8
Summary:       General data-binding package for Jackson (2.x)
License:       ASL 2.0 and LGPLv2+
URL:           http://wiki.fasterxml.com/JacksonHome
Source0:       https://github.com/FasterXML/jackson-databind/archive/%{name}-%{version}.tar.gz

BuildRequires: maven-local
BuildRequires: mvn(com.fasterxml.jackson:jackson-parent:pom:)
BuildRequires: mvn(com.fasterxml.jackson.core:jackson-annotations) >= 2.4.1
BuildRequires: mvn(com.fasterxml.jackson.core:jackson-core) >= 2.4.1
BuildRequires: mvn(com.google.guava:guava)
BuildRequires: mvn(com.google.code.maven-replacer-plugin:replacer)
BuildRequires: mvn(org.powermock:powermock-api-mockito)
BuildRequires: mvn(org.powermock:powermock-module-junit4)

BuildArch:     noarch
Source44: import.info

%description
General data-binding functionality for Jackson:
works on core streaming API.

%package javadoc
Group: Development/Java
Summary:       Javadoc for %{name}
BuildArch: noarch

%description javadoc
This package contains javadoc for %{name}.

%prep
%setup -q -n %{name}-%{name}-%{version}

cp -p src/main/resources/META-INF/LICENSE .
cp -p src/main/resources/META-INF/NOTICE .
sed -i 's/\r//' LICENSE NOTICE

# unavailable test deps
%pom_remove_dep javax.measure:jsr-275
rm src/test/java/com/fasterxml/jackson/databind/introspect/NoClassDefFoundWorkaroundTest.java
%pom_xpath_remove pom:classpathDependencyExcludes

%pom_xpath_inject "pom:plugin[pom:artifactId='maven-javadoc-plugin']/pom:configuration" "<additionalparam>-Xdoclint:none</additionalparam>"
%pom_xpath_remove pom:failOnError

# org.powermock.reflect.exceptions.FieldNotFoundException: Field 'fTestClass' was not found in class org.junit.internal.runners.MethodValidator.
rm src/test/java/com/fasterxml/jackson/databind/type/TestTypeFactoryWithClassLoader.java

# Off test that require connection with the web
rm src/test/java/com/fasterxml/jackson/databind/ser/TestJdkTypes.java \
 src/test/java/com/fasterxml/jackson/databind/deser/TestJdkTypes.java \
 src/test/java/com/fasterxml/jackson/databind/TestJDKSerialization.java

%mvn_file : %{name}

%build

%mvn_build -- -Dmaven.test.failure.ignore=true

%install
%mvn_install

%files -f .mfiles
%doc README.md release-notes/*
%doc LICENSE NOTICE

%files javadoc -f .mfiles-javadoc
%doc LICENSE NOTICE

%changelog
* Tue Dec 06 2016 Igor Vlasenko <viy@altlinux.ru> 2.6.3-alt1_2jpp8
- new version

* Wed Feb 03 2016 Igor Vlasenko <viy@altlinux.ru> 2.5.0-alt1_2jpp8
- new version

* Thu Jan 28 2016 Igor Vlasenko <viy@altlinux.ru> 2.5.0-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

