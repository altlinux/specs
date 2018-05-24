Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires: rpm-build-java
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:           plexus-languages
Version:        0.9.3
Release:        alt1_4jpp8
Summary:        Plexus Languages
License:        ASL 2.0
URL:            https://github.com/codehaus-plexus/plexus-languages
BuildArch:      noarch

Source0:        https://github.com/codehaus-plexus/plexus-languages/archive/plexus-languages-%{version}.tar.gz
Source1:        http://www.apache.org/licenses/LICENSE-2.0.txt

BuildRequires:  maven-local
BuildRequires:  mvn(com.google.inject:guice)
BuildRequires:  mvn(com.thoughtworks.qdox:qdox)
BuildRequires:  mvn(javax.inject:javax.inject)
BuildRequires:  mvn(junit:junit)
BuildRequires:  mvn(org.codehaus.plexus:plexus-component-annotations)
BuildRequires:  mvn(org.codehaus.plexus:plexus-component-metadata)
BuildRequires:  mvn(org.codehaus.plexus:plexus:pom:)
BuildRequires:  mvn(org.mockito:mockito-core)
BuildRequires:  mvn(org.ow2.asm:asm)
# test deps
BuildRequires:  jdom
BuildRequires:  objectweb-asm
Source44: import.info

%description
Plexus Languages is a set of Plexus components that maintain shared
language features.

%{?javadoc_package}

%prep
%setup -q -n plexus-languages-plexus-languages-%{version}
cp %{SOURCE1} .
# Replace bundled class file from ASM6
jar xf $(find-jar objectweb-asm/asm-all) module-info.class
mv module-info.class plexus-java/src/test/resources/dir.descriptor/out/
# Replace JARs used as test resources with symlinks to system JARs
ln -sf $(find-jar jdom) plexus-java/src/test/resources/jar.unsupported/jdom-1.0.jar
ln -sf $(find-jar objectweb-asm/asm) plexus-java/src/test/resources/jar.descriptor/asm-6.0_BETA.jar

%build
%mvn_build

%install
%mvn_install

%files -f .mfiles
%doc --no-dereference LICENSE-2.0.txt

%changelog
* Thu May 24 2018 Igor Vlasenko <viy@altlinux.ru> 0.9.3-alt1_4jpp8
- fc 28 update

