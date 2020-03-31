Group: Development/Java
BuildRequires: /proc rpm-build-java
BuildRequires: jpackage-1.8-compat
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:           plexus-languages
Version:        0.9.10
Release:        alt1_5jpp8
Summary:        Plexus Languages
License:        ASL 2.0
URL:            https://github.com/codehaus-plexus/plexus-languages
BuildArch:      noarch

# ./generate-tarball.sh
Source0:        %{name}-%{version}.tar.gz
Source1:        http://www.apache.org/licenses/LICENSE-2.0.txt
# Sources contain bundled jars that we cannot verify for licensing
Source2:        generate-tarball.sh

BuildRequires:  maven-local
BuildRequires:  mvn(com.thoughtworks.qdox:qdox)
BuildRequires:  mvn(javax.inject:javax.inject)
BuildRequires:  mvn(org.apache.maven.plugins:maven-failsafe-plugin)
BuildRequires:  mvn(org.codehaus.plexus:plexus-component-annotations)
BuildRequires:  mvn(org.codehaus.plexus:plexus-component-metadata)
BuildRequires:  mvn(org.codehaus.plexus:plexus:pom:)
BuildRequires:  mvn(org.ow2.asm:asm)
Source44: import.info

%description
Plexus Languages is a set of Plexus components that maintain shared
language features.

%{?javadoc_package}

%prep
%setup -q -n plexus-languages-plexus-languages-%{version}

cp %{SOURCE1} .

%build
# we don't have mockito 2 yet + many tests rely on bundled test jars/classes
%mvn_build -f

%install
%mvn_install

%files -f .mfiles
%doc --no-dereference LICENSE-2.0.txt

%changelog
* Tue Mar 31 2020 Igor Vlasenko <viy@altlinux.ru> 0.9.10-alt1_5jpp8
- fc update

* Fri May 24 2019 Igor Vlasenko <viy@altlinux.ru> 0.9.10-alt1_4jpp8
- new version

* Tue Jun 05 2018 Igor Vlasenko <viy@altlinux.ru> 0.9.3-alt2_4jpp8
- fixed build with new objectweb-asm

* Thu May 24 2018 Igor Vlasenko <viy@altlinux.ru> 0.9.3-alt1_4jpp8
- fc 28 update

