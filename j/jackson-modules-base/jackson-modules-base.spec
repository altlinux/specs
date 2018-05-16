Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires: rpm-build-java
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:          jackson-modules-base
Version:       2.9.4
Release:       alt1_2jpp8
Summary:       Jackson modules: Base
License:       ASL 2.0
URL:           https://github.com/FasterXML/jackson-modules-base
Source0:       https://github.com/FasterXML/jackson-modules-base/archive/%{name}-%{version}.tar.gz

BuildRequires:  maven-local
BuildRequires:  mvn(cglib:cglib)
BuildRequires:  mvn(com.fasterxml.jackson.core:jackson-annotations) >= %{version}
BuildRequires:  mvn(com.fasterxml.jackson.core:jackson-core) >= %{version}
BuildRequires:  mvn(com.fasterxml.jackson.core:jackson-databind) >= %{version}
BuildRequires:  mvn(com.fasterxml.jackson:jackson-base:pom:) >= %{version}
BuildRequires:  mvn(com.google.code.maven-replacer-plugin:replacer)
BuildRequires:  mvn(com.google.inject:guice)
BuildRequires:  mvn(com.thoughtworks.paranamer:paranamer)
BuildRequires:  mvn(junit:junit)
BuildRequires:  mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires:  mvn(org.mockito:mockito-all)
BuildRequires:  mvn(org.osgi:osgi.core)
BuildRequires:  mvn(org.ow2.asm:asm)

BuildArch:      noarch
Source44: import.info

%description
Jackson "base" modules: modules that build directly on databind,
and are not data-type, data format, or JAX-RS provider modules.

%package -n jackson-module-afterburner
Group: Development/Java
Summary: Jackson module that uses byte-code generation to further speed up data binding

%description -n jackson-module-afterburner
Module that will add dynamic bytecode generation for standard Jackson POJO
serializers and deserializers, eliminating majority of remaining data binding
overhead.

%package -n jackson-module-guice
Group: Development/Java
Summary: Jackson module to make integration with Guice a bit easier

%description -n jackson-module-guice
This extension allows Jackson to delegate ObjectMapper creation and value
injection to Guice when handling data bindings.

%package -n jackson-module-jaxb-annotations
Group: Development/Java
Summary: Support for using JAXB annotations as an alternative to "native" Jackson annotations

%description -n jackson-module-jaxb-annotations
This Jackson extension module provides support for using JAXB (javax.xml.bind)
annotations as an alternative to native Jackson annotations. It is most often
used to make it easier to reuse existing data beans that used with JAXB
framework to read and write XML.

%package -n jackson-module-mrbean
Group: Development/Java
Summary: Functionality for implementing interfaces and abstract types dynamically

%description -n jackson-module-mrbean
Mr Bean is an extension that implements support for "POJO type materialization"
ability for databinder to construct implementation classes for Java interfaces
and abstract classes, as part of deserialization.

%package -n jackson-module-osgi
Group: Development/Java
Summary: Jackson module to inject OSGI services in deserialized beans

%description -n jackson-module-osgi
This module provides a way to inject OSGI services into deserialized objects.
Thanks to the JacksonInject annotations, the OsgiJacksonModule will search for
the required service in the OSGI service registry and injects it in the object
while deserializing.

%package -n jackson-module-paranamer
Group: Development/Java
Summary: Jackson module that uses Paranamer to introspect names of constructor params

%description -n jackson-module-paranamer
Module that uses Paranamer library to auto-detect names of Creator
(constructor, static factory method, annotated with @JsonCreator) methods.

%package javadoc
Group: Development/Java
Summary: Javadoc for %{name}
# Obsoletes standalone jackson-module-jaxb-annotations since F28
Obsoletes: jackson-module-jaxb-annotations-javadoc < %{version}-%{release}
Provides:  jackson-module-jaxb-annotations-javadoc = %{version}-%{release}
BuildArch: noarch

%description javadoc
This package contains API documentation for %{name}.

%prep
%setup -q -n %{name}-%{name}-%{version}

# Disable bundling of asm
%pom_remove_plugin ":maven-shade-plugin" afterburner mrbean paranamer
%pom_xpath_remove "pom:properties/pom:osgi.private" mrbean paranamer

sed -i 's/\r//' mrbean/src/main/resources/META-INF/{LICENSE,NOTICE}
cp -p mrbean/src/main/resources/META-INF/{LICENSE,NOTICE} .

# Fix OSGi dependency
%pom_change_dep org.osgi:org.osgi.core org.osgi:osgi.core osgi

# NoClassDefFoundError: net/sf/cglib/core/CodeGenerationException
%pom_add_dep cglib:cglib:3.2.4:test guice

# This is provided by modern JREs
%pom_remove_dep "javax.xml.bind:jaxb-api" jaxb

%mvn_file ":{*}" jackson-modules/@1

%build
%mvn_build -s

%install
%mvn_install

%files -f .mfiles-jackson-modules-base
%doc README.md release-notes
%doc --no-dereference LICENSE NOTICE

%files -n jackson-module-afterburner -f .mfiles-jackson-module-afterburner
%doc afterburner/README.md afterburner/release-notes
%doc --no-dereference LICENSE NOTICE

%files -n jackson-module-guice -f .mfiles-jackson-module-guice
%doc guice/README.md
%doc --no-dereference LICENSE NOTICE

%files -n jackson-module-jaxb-annotations -f .mfiles-jackson-module-jaxb-annotations
%doc jaxb/README.md jaxb/release-notes
%doc --no-dereference LICENSE NOTICE

%files -n jackson-module-mrbean -f .mfiles-jackson-module-mrbean
%doc mrbean/README.md mrbean/release-notes
%doc --no-dereference LICENSE NOTICE

%files -n jackson-module-osgi -f .mfiles-jackson-module-osgi
%doc osgi/README.md osgi/release-notes
%doc --no-dereference LICENSE NOTICE

%files -n jackson-module-paranamer -f .mfiles-jackson-module-paranamer
%doc paranamer/README.md paranamer/release-notes
%doc --no-dereference LICENSE NOTICE

%files javadoc -f .mfiles-javadoc
%doc --no-dereference LICENSE NOTICE

%changelog
* Tue May 15 2018 Igor Vlasenko <viy@altlinux.ru> 2.9.4-alt1_2jpp8
- java update

* Sat Nov 04 2017 Igor Vlasenko <viy@altlinux.ru> 2.7.6-alt1_4jpp8
- new version

