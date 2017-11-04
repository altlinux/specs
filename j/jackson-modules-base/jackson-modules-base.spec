Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:          jackson-modules-base
Version:       2.7.6
Release:       alt1_4jpp8
Summary:       Jackson modules: Base
License:       ASL 2.0
URL:           https://github.com/FasterXML/jackson-modules-base
Source0:       https://github.com/FasterXML/jackson-modules-base/archive/%{name}-%{version}.tar.gz

BuildRequires: maven-local
BuildRequires: mvn(cglib:cglib)
BuildRequires: mvn(com.fasterxml.jackson:jackson-parent:pom:)
BuildRequires: mvn(com.fasterxml.jackson.core:jackson-annotations)
BuildRequires: mvn(com.fasterxml.jackson.core:jackson-core)
BuildRequires: mvn(com.fasterxml.jackson.core:jackson-databind)
BuildRequires: mvn(com.google.code.maven-replacer-plugin:replacer)
BuildRequires: mvn(com.google.inject:guice)
BuildRequires: mvn(com.thoughtworks.paranamer:paranamer)
BuildRequires: mvn(junit:junit)
BuildRequires: mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires: mvn(org.eclipse.osgi:org.eclipse.osgi)
BuildRequires: mvn(org.mockito:mockito-all)
BuildRequires: mvn(org.ow2.asm:asm)

BuildArch:     noarch
Source44: import.info

%description
Jackson "base" modules: modules that build directly on databind,
and are not data-type, data format, or JAX-RS provider modules.

%package -n jackson-module-afterburner
Group: Development/Java
Summary:       Jackson module that uses byte-code generation to further speed up data binding

%description -n jackson-module-afterburner
Jackson extension module used to enhance performance
using byte-code generation to replace use of Reflection
for field access and method calls.

%package -n jackson-module-guice
Group: Development/Java
Summary:       Jackson Stuff to make integration with Guice a bit easier

%description -n jackson-module-guice
This extension allows Jackson to delegate ObjectMapper creation and
value injection to Guice when handling data bindings.

%package -n jackson-module-mrbean
Group: Development/Java
Summary:       An extension that implements support for POJO type materialization

%description -n jackson-module-mrbean
Functionality for implementing interfaces and abstract types
dynamically ("bean materialization"), integrated with Jackson
(although usable externally as well).

%package -n jackson-module-osgi
Group: Development/Java
Summary:       Jackson module to inject OSGI services in deserialized beans

%description -n jackson-module-osgi
This module provides a way to inject OSGI services into deserialized objects.

%package -n jackson-module-paranamer
Group: Development/Java
Summary:       Jackson Paranamer Extension

%description -n jackson-module-paranamer
Jackson extension that implements custom AnnotationIntrospectors that
use Paranamer to introspect names of constructor (and factory method)
parameters.

%package javadoc
Group: Development/Java
Summary:       Javadoc for %{name}
BuildArch: noarch

%description javadoc
This package contains javadoc for %{name}.

%prep
%setup -q -n %{name}-%{name}-%{version}

# disable asm copy
%pom_remove_plugin -r :maven-shade-plugin afterburner mrbean paranamer
%pom_xpath_remove "pom:properties/pom:osgi.private" mrbean
# disable paranamer copy
%pom_xpath_remove pom:properties/pom:osgi.private paranamer

sed -i 's/\r//' mrbean/src/main/resources/META-INF/{LICENSE,NOTICE}
cp -p mrbean/src/main/resources/META-INF/{LICENSE,NOTICE} .

# Use osgi.core:5.0.0
%pom_xpath_set "pom:properties/pom:version.osgi.core" 3.10.102.v20160416-2200 osgi
%pom_change_dep org.osgi:org.osgi.core org.eclipse.osgi:org.eclipse.osgi osgi

# NoClassDefFoundError: net/sf/cglib/core/CodeGenerationException
%pom_add_dep cglib:cglib:3.2.4:test guice

%build

%mvn_build -s

%install
%mvn_install

%files -f .mfiles-jackson-modules-base
%doc README.md release-notes
%doc LICENSE NOTICE

%files -n jackson-module-afterburner -f .mfiles-jackson-module-afterburner
%doc afterburner/README.md afterburner/release-notes
%doc LICENSE NOTICE

%files -n jackson-module-guice -f .mfiles-jackson-module-guice
%doc guice/README.md
%doc LICENSE NOTICE

%files -n jackson-module-mrbean -f .mfiles-jackson-module-mrbean
%doc mrbean/README.md mrbean/release-notes
%doc LICENSE NOTICE

%files -n jackson-module-osgi -f .mfiles-jackson-module-osgi
%doc osgi/README.md osgi/release-notes
%doc LICENSE NOTICE

%files -n jackson-module-paranamer -f .mfiles-jackson-module-paranamer
%doc paranamer/README.md paranamer/release-notes
%doc LICENSE NOTICE

%files javadoc -f .mfiles-javadoc
%doc LICENSE NOTICE

%changelog
* Sat Nov 04 2017 Igor Vlasenko <viy@altlinux.ru> 2.7.6-alt1_4jpp8
- new version

