Group: Development/Java
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
%define fedora 23
Name:          jackson-databind
Version:       2.5.0
Release:       alt1_2jpp8
Summary:       General data-binding package for Jackson (2.x)
License:       ASL 2.0 and LGPLv2+
URL:           http://wiki.fasterxml.com/JacksonHome
Source0:       https://github.com/FasterXML/jackson-databind/archive/%{name}-%{version}.tar.gz
%if %{?fedora} > 20
BuildRequires: mvn(com.fasterxml.jackson:jackson-parent:pom:)
%else
BuildRequires: mvn(com.fasterxml.jackson:jackson-parent)
%endif
BuildRequires: mvn(com.fasterxml.jackson.core:jackson-annotations) >= 2.4.1
BuildRequires: mvn(com.fasterxml.jackson.core:jackson-core) >= 2.4.1
# test deps
BuildRequires: mvn(cglib:cglib)
BuildRequires: mvn(junit:junit)
BuildRequires: mvn(org.codehaus.groovy:groovy)

BuildRequires: maven-local
BuildRequires: replacer
# bundle-plugin Requires
#BuildRequires: mvn(org.sonatype.aether:aether)

Provides:      jackson2-databind = %{version}-%{release}
Obsoletes:     jackson2-databind < %{version}-%{release}

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
%pom_remove_dep org.hibernate:hibernate-cglib-repack
rm src/test/java/com/fasterxml/jackson/databind/interop/TestHibernate.java
%pom_remove_dep javax.measure:jsr-275
rm src/test/java/com/fasterxml/jackson/databind/deser/TestNoClassDefFoundDeserializer.java

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
* Wed Feb 03 2016 Igor Vlasenko <viy@altlinux.ru> 2.5.0-alt1_2jpp8
- new version

* Thu Jan 28 2016 Igor Vlasenko <viy@altlinux.ru> 2.5.0-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

