Group: Development/Java
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
%define fedora 23
Name:          jackson-module-mrbean
Version:       2.5.0
Release:       alt1_2jpp8
Summary:       An extension that implements support for POJO type materialization
License:       ASL 2.0
URL:           http://wiki.fasterxml.com/JacksonFeatureMaterializedBeans
Source0:       https://github.com/FasterXML/jackson-module-mrbean/archive/%{name}-%{version}.tar.gz

%if %{?fedora} > 20
BuildRequires: mvn(com.fasterxml.jackson:jackson-parent:pom:)
%else
BuildRequires: mvn(com.fasterxml.jackson:jackson-parent)
%endif
BuildRequires: mvn(com.fasterxml.jackson.core:jackson-core)
BuildRequires: mvn(com.fasterxml.jackson.core:jackson-databind)
BuildRequires: mvn(org.ow2.asm:asm) >= 5.0.2

# test deps
BuildRequires: mvn(junit:junit)

BuildRequires: maven-local
BuildRequires: maven-enforcer-plugin
BuildRequires: maven-plugin-build-helper
BuildRequires: maven-plugin-bundle
BuildRequires: maven-site-plugin
BuildRequires: maven-surefire-provider-junit
BuildRequires: replacer
# bundle-plugin Requires
#BuildRequires: mvn(org.sonatype.aether:aether)

BuildArch:     noarch
Source44: import.info

%description
Functionality for implementing interfaces and abstract types
dynamically ("bean materialization"), integrated with Jackson
(although usable externally as well).

%package javadoc
Group: Development/Java
Summary:       Javadoc for %{name}
BuildArch: noarch

%description javadoc
This package contains javadoc for %{name}.

%prep
%setup -q -n %{name}-%{name}-%{version}

# disabled asm embedded copy
%pom_remove_plugin :maven-shade-plugin

%pom_xpath_remove "pom:properties/pom:osgi.private"
%pom_xpath_remove "pom:properties/pom:osgi.import"
%pom_xpath_inject "pom:properties" "
    <osgi.import>
com.fasterxml.jackson.core
,com.fasterxml.jackson.core.type
,com.fasterxml.jackson.core.util
,com.fasterxml.jackson.databind
,com.fasterxml.jackson.databind.cfg
,com.fasterxml.jackson.databind.module,
,com.fasterxml.jackson.databind.type
,org.objectweb.asm
,org.objectweb.asm.signature
</osgi.import>"

cp -p src/main/resources/META-INF/LICENSE .
cp -p src/main/resources/META-INF/NOTICE .
sed -i 's/\r//' LICENSE NOTICE

%mvn_file : %{name}

%build

%mvn_build

%install
%mvn_install

%files -f .mfiles
%doc README.md
%doc LICENSE NOTICE

%files javadoc -f .mfiles-javadoc
%doc LICENSE NOTICE

%changelog
* Wed Feb 03 2016 Igor Vlasenko <viy@altlinux.ru> 2.5.0-alt1_2jpp8
- new version

* Thu Jan 28 2016 Igor Vlasenko <viy@altlinux.ru> 2.5.0-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

