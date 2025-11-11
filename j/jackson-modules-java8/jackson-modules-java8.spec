%define _unpackaged_files_terminate_build 1

Name: jackson-modules-java8
Version: 2.20.1
Release: alt1

Summary: Set of Jackson modules providing support for Java 8 features
License: Apache-2.0
Group: Development/Java
Url: https://github.com/FasterXML/jackson-modules-java8
Vcs: https://github.com/FasterXML/jackson-modules-java8.git
BuildArch: noarch

Source0: %name-%version.tar

BuildRequires(pre): rpm-macros-java
BuildRequires: /proc
BuildRequires: rpm-build-java
BuildRequires: jpackage-default
BuildRequires: maven-local
BuildRequires: jackson-annotations
BuildRequires: jackson-databind
BuildRequires: jackson-core
BuildRequires: jackson-bom
BuildRequires: junit
BuildRequires: maven-enforcer
BuildRequires: replacer
BuildRequires: moditect-maven-plugin

%description
Jackson Modules for Java 8 is a collection of extensions that enable the
Jackson JSON processor to fully support core Java 8 language and library
features. It provides modules for handling Optional types, the new Date and
Time API (JSR-310), and automatic discovery of constructor and method parameter
names. Together, these modules make it easier to use Jackson in modern Java 8
applications and ensure seamless integration with updated language constructs
and APIs.

%package -n jackson-datatype-jdk8
Summary: Jackson module for Java 8 core types (Optional and related types)
Group: Development/Java
BuildArch: noarch

%description -n jackson-datatype-jdk8
Jackson module that provides support for selected Java 8 core library types.
It adds serialization and deserialization support for classes such as Optional,
OptionalInt, OptionalLong, and OptionalDouble.  This module also enables
parameter name introspection for constructors and methods, allowing Jackson to
bind values without requiring explicit annotations. It is useful when working
with Java 8 language features and data models that use optional types.

%package -n jackson-datatype-jsr310
Summary: Jackson module for Java 8 Date and Time API (JSR-310)
Group: Development/Java
BuildArch: noarch

%description -n jackson-datatype-jsr310
Jackson module that adds support for the Java 8 Date and Time API defined in
JSR-310. It provides serialization and deserialization for core types such as
Instant, LocalDate, LocalDateTime, OffsetDateTime, and ZonedDateTime.  This
module allows Jackson to correctly handle Java 8 time values in JSON
representations and is essential for modern applications that rely on the
java.time package.

%package -n jackson-module-parameter-names
Summary: Jackson module for automatic access to constructor and method parameter names
Group: Development/Java
BuildArch: noarch

%description -n jackson-module-parameter-names
Jackson module that enables the use of Java 8 reflection to discover actual
parameter names for constructors and methods without requiring explicit
annotations. When compiled with the -parameters compiler flag, this module
allows Jackson to use those names for property binding during serialization and
deserialization.  It simplifies data binding for immutable objects and value
classes that rely on constructor parameters instead of standard setter methods.

%prep
%setup

# Off tests beacause of broken mockito.
rm -rf parameter-names/src/test
%pom_remove_dep org.mockito:mockito-core parameter-names/pom.xml

%pom_remove_plugin -r :maven-enforcer-plugin
%pom_remove_plugin -r :gradle-module-metadata-maven-plugin
%pom_remove_plugin -r :cyclonedx-maven-plugin

%build
%mvn_build -s -f -j -- -Dmaven.compiler.source=1.8 \
  -Dmaven.compiler.target=1.8 \
  -Dmaven.javadoc.source=1.8 \
  -Dmaven.compiler.release=8 \
  #

%install
%mvn_install 

%files -f .mfiles-jackson-modules-java8

%files -n jackson-datatype-jdk8 -f .mfiles-jackson-datatype-jdk8

%files -n jackson-datatype-jsr310 -f .mfiles-jackson-datatype-jsr310

%files -n jackson-module-parameter-names -f .mfiles-jackson-module-parameter-names

%changelog
* Mon Nov 10 2025 Ivan Khanas <xeno@altlinux.org> 2.20.1-alt1
- First build for ALT.
