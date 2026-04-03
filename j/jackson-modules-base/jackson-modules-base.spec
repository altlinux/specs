Name:           jackson-modules-base
Version:        2.20.1
Release:        alt3

Summary:        Uber-project for foundational modules of Jackson that build directly on core components but nothing else; not including data format or datatype modules
License:        Apache-2.0
Group:          Development/Java
URL:            https://github.com/FasterXML/jackson-modules-base
VCS:            https://github.com/FasterXML/jackson-modules-base

Source:         %name-%version.tar

Patch1:         0001-Replace-javax-with-jakarta.patch

BuildRequires(pre):  maven-local
BuildRequires:  jpackage-default

BuildRequires:  mvn(com.google.code.maven-replacer-plugin:maven-replacer-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-shade-plugin)
BuildRequires:  mvn(org.moditect:moditect-maven-plugin)
BuildRequires:  mvn(com.fasterxml.jackson:jackson-base:pom:)
BuildRequires:  mvn(com.fasterxml.jackson.core:jackson-core)
BuildRequires:  mvn(com.fasterxml.jackson.core:jackson-databind)
BuildRequires:  mvn(jakarta.xml.bind:jakarta.xml.bind-api)
BuildRequires:  mvn(jakarta.activation:jakarta.activation-api)
BuildRequires:  mvn(org.mockito:mockito-core)
BuildRequires:  mvn(org.glassfish.jaxb:jaxb-runtime)

BuildArch:      noarch

%description
This is a multi-module umbrella project for Jackson modules that are considered
foundational, building on core databind, but not including datatype or data
format modules, or JAX-RS providers. Not all "general" modules are included
here; this grouping is to be used for more mature (and generally slower moving,
stable) modules.

%javadoc_package

%package -n jackson-module-afterburner
Summary:        Jackson extension module used to enhance performance using bytecode generation to replace use of Reflection for field access and method calls
Group:          Development/Java
%description -n jackson-module-afterburner
Module that will add dynamic bytecode generation for standard Jackson POJO
serializers and deserializers, eliminating majority of remaining data binding
overhead.

%package -n jackson-module-blackbird
Summary:        Jackson extension module that uses LambdaMetafactory based code generation to replace reflection calls
Group:          Development/Java
%description -n jackson-module-blackbird
The Afterburner has long been your engine of choice for maximum Jackson
performance. But in the brave new Java 11 world, the trusty Afterburner
is showing its age. It uses horrifying bytecode manipulation and cracks
Unsafe.defineClass which will stop working soon.

%package -n jackson-module-guice
Summary:        Stuff to make integration with Guice a bit easier
Group:          Development/Java
%description -n jackson-module-guice
This extension allows Jackson to delegate ObjectMapper creation and value
injection to Guice when handling data bindings.

%package -n jackson-module-jakarta-xmlbind-annotations
Summary:        Jackson module: Jakarta XML Bind Annotations (jakarta.xml.bind)
Group:          Development/Java
%description -n jackson-module-jakarta-xmlbind-annotations
Support for using Jakarta XML Bind (aka JAXB 3.0) annotations as an alternative
to "native" Jackson annotations, for configuring data-binding.

%package -n jackson-module-jaxb-annotations
Summary:        Support for using JAXB annotations as an alternative to "native" Jackson annotations
Group:          Development/Java
%description -n jackson-module-jaxb-annotations
This Jackson extension module provides support for using JAXB (javax.xml.bind)
annotations as an alternative to native Jackson annotations. It is most often
used to make it easier to reuse existing data beans that used with JAXB
framework to read and write XML.

%package -n jackson-module-mrbean
Summary:        Functionality for implementing interfaces and abstract types dynamically ("bean materialization"), integrated with Jackson (although usable externally as well)
Group:          Development/Java
%description -n jackson-module-mrbean
Mr Bean is an extension that implements support for "POJO type materialization";
ability for databinder to construct implementation classes for Java interfaces
and abstract classes, as part of deserialization. Extension plugs in using
standard Module interface, and requires Jackson 2.0 or above.

%package -n jackson-module-osgi
Summary:        Jackson module to inject OSGI services in deserialized beans
Group:          Development/Java
%description -n jackson-module-osgi
This module provides a way to inject OSGI services into deserialized objects.
Thanks to the JacksonInject annotations, the OsgiJacksonModule will search for
the required service in the OSGI service registry and injects it in the object
while deserializing.

%prep
%setup
%autopatch -p1

%pom_disable_module guice7

# rename mockito
%pom_change_dep :mockito-all :mockito-core osgi

# revert jaxb annotation dependency
%pom_change_dep javax.xml.bind:jaxb-api jakarta.xml.bind:jakarta.xml.bind-api jaxb

# test fails since mockito was upgraded to 2.x
rm osgi/src/test/java/com/fasterxml/jackson/module/osgi/InjectOsgiServiceTest.java

# paranamer removed from sisyphus
%pom_disable_module paranamer

%pom_disable_module no-ctor-deser

# no need
%pom_disable_module android-record

%pom_remove_plugin -r :gradle-module-metadata-maven-plugin
%pom_remove_plugin -r :cyclonedx-maven-plugin

%mvn_file ":{*}" jackson-modules/@1

%build
%mvn_build -s -- \
    -Dmaven.compiler.source=1.8 \
    -Dmaven.compiler.target=1.8 \
    -Dmaven.javadoc.source=1.8 \
    -Dmaven.compiler.release=8 \

%install
%mvn_install

%files -f .mfiles-jackson-modules-base
%doc README.md release-notes
%doc LICENSE

%files -n jackson-module-afterburner -f .mfiles-jackson-module-afterburner
%doc afterburner/README.md afterburner/release-notes
%doc LICENSE

%files -n jackson-module-blackbird -f .mfiles-jackson-module-blackbird
%doc blackbird/README.md
%doc LICENSE

%files -n jackson-module-guice -f .mfiles-jackson-module-guice
%doc guice/README.md
%doc LICENSE

%files -n jackson-module-jakarta-xmlbind-annotations -f .mfiles-jackson-module-jakarta-xmlbind-annotations
%doc jakarta-xmlbind/README.md
%doc LICENSE

%files -n jackson-module-jaxb-annotations -f .mfiles-jackson-module-jaxb-annotations
%doc jaxb/README.md jaxb/release-notes
%doc LICENSE

%files -n jackson-module-mrbean -f .mfiles-jackson-module-mrbean
%doc mrbean/README.md mrbean/release-notes
%doc LICENSE

%files -n jackson-module-osgi -f .mfiles-jackson-module-osgi
%doc osgi/README.md osgi/release-notes
%doc LICENSE

%changelog
* Fri Apr 03 2026 Anton Meleshnikov <alton@altlinux.org> 2.20.1-alt3
- fixed FTBFS.

* Wed Mar 04 2026 Evgeniy Serov <scala@altlinux.org> 2.20.1-alt2.1
- Cosmetic fixes.

* Mon Jan 20 2026 Evgeniy Serov <scala@altlinux.org> 2.20.1-alt2
- Added new JAXB module.
- Updated older JAXB module (javax-based) to Jakarta APIs.

* Sat Dec 27 2025 Evgeniy Serov <scala@altlinux.org> 2.20.1-alt1
- fixed FTBFS
- new version 2.20.1
- removed import.info

* Fri Jun 10 2022 Igor Vlasenko <viy@altlinux.org> 2.11.4-alt1_5jpp11
- update

* Wed Aug 04 2021 Igor Vlasenko <viy@altlinux.org> 2.11.4-alt1_4jpp11
- update

* Thu Jun 10 2021 Igor Vlasenko <viy@altlinux.org> 2.11.4-alt1_2jpp11
- new version

* Tue Jun 01 2021 Igor Vlasenko <viy@altlinux.org> 2.11.2-alt1_1jpp11
- new version

* Wed May 12 2021 Igor Vlasenko <viy@altlinux.org> 2.10.2-alt1_2jpp8
- new version

* Sat Jul 13 2019 Igor Vlasenko <viy@altlinux.ru> 2.9.8-alt1_2jpp8
- new version

* Mon Jun 17 2019 Igor Vlasenko <viy@altlinux.ru> 2.9.4-alt1_4jpp8
- new version

* Tue May 15 2018 Igor Vlasenko <viy@altlinux.ru> 2.9.4-alt1_2jpp8
- java update

* Sat Nov 04 2017 Igor Vlasenko <viy@altlinux.ru> 2.7.6-alt1_4jpp8
- new version

