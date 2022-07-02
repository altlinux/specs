Group: Development/Java
BuildRequires: /proc rpm-build-java
BuildRequires: jpackage-default
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:          ed25519-java
Version:       0.3.0
Release:       alt1_14jpp11
Summary:       Implementation of EdDSA (Ed25519) in Java
License:       CC0
URL:           https://github.com/str4d/ed25519-java
Source0:       https://github.com/str4d/ed25519-java/archive/v%{version}/%{name}-%{version}.tar.gz

# https://github.com/str4d/ed25519-java/commit/e0ac35769db8553fb714b09f0d3f3d2b001fd033
Patch0: 0001-EdDSAEngine.initVerify-Handle-any-non-EdDSAPublicKey.patch

Patch1: 0002-Disable-test-that-relies-on-internal-sun-JDK-classes.patch

BuildRequires: maven-local
BuildRequires: mvn(junit:junit)
BuildRequires: mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires: mvn(org.hamcrest:hamcrest-all)

BuildArch:     noarch
Source44: import.info

%description
This is an implementation of EdDSA in Java. Structurally, it
is based on the ref10 implementation in SUPERCOP (see
http://ed25519.cr.yp.to/software.html).

There are two internal implementations:

* A port of the radix-2^51 operations in ref10
  - fast and constant-time, but only useful for Ed25519.
* A generic version using BigIntegers for calculation
  - a bit slower and not constant-time, but compatible
    with any EdDSA parameter specification.

%package javadoc
Group: Development/Java
Summary:       Javadoc for %{name}
BuildArch: noarch

%description javadoc
This package contains javadoc for %{name}.

%prep
%setup -q -n %{name}-%{version}
%patch0 -p1
%patch1 -p1

# Unwanted tasks
%pom_remove_plugin :maven-gpg-plugin
%pom_remove_plugin :maven-javadoc-plugin
%pom_remove_plugin :maven-source-plugin
# Unavailable plugin
%pom_remove_plugin :nexus-staging-maven-plugin

%mvn_file net.i2p.crypto:eddsa %{name} eddsa

# Remove hard-coded source/target
%pom_xpath_remove pom:plugin/pom:configuration/pom:target
%pom_xpath_remove pom:plugin/pom:configuration/pom:source

%build
%mvn_build -- -Dmaven.compiler.source=1.8 -Dmaven.compiler.target=1.8 -Dmaven.javadoc.source=1.8 -Dmaven.compiler.release=8 -Dmaven.compiler.release=11

%install
%mvn_install

%files -f .mfiles
%doc README.md
%doc --no-dereference LICENSE.txt

%files javadoc -f .mfiles-javadoc
%doc --no-dereference LICENSE.txt

%changelog
* Fri Jul 01 2022 Igor Vlasenko <viy@altlinux.org> 0.3.0-alt1_14jpp11
- update

* Mon Jun 13 2022 Igor Vlasenko <viy@altlinux.org> 0.3.0-alt1_8jpp11
- java11 build

* Thu Jun 03 2021 Igor Vlasenko <viy@altlinux.org> 0.3.0-alt1_8jpp8
- jvm8 update

* Sat Jul 13 2019 Igor Vlasenko <viy@altlinux.ru> 0.3.0-alt1_3jpp8
- new version

