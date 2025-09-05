Name: plexus-testing
Version: 1.3.0
Release: alt1

Summary: Library to help testing plexus components
License: Apache-2.0
Group: Development/Java
Url: https://github.com/codehaus-plexus/plexus-testing
BuildArch: noarch

Source0: https://github.com/codehaus-plexus/%name/archive/%name-%version.tar.gz

BuildRequires: maven-local
BuildRequires: /proc rpm-build-java
BuildRequires: jpackage-default

BuildRequires:  mvn(org.codehaus.plexus:plexus:pom:)
BuildRequires:  mvn(org.eclipse.sisu:org.eclipse.sisu.plexus)
BuildRequires:  mvn(org.eclipse.sisu:org.eclipse.sisu.inject)
BuildRequires:  mvn(com.google.inject:guice)
BuildRequires:  mvn(org.junit.jupiter:junit-jupiter-api)

%description
The Plexus Testing contains the necessary classes to be able to test
Plexus components.

%package javadoc
Group: Development/Java
Summary: Javadoc for %name
BuildArch: noarch

%description javadoc
This package contains the API documentation for %name.

%prep
%setup

# Some tests rely on Jakarta Injection API, which is not packaged
rm src/test/java/org/codehaus/plexus/testing/TestJakartaComponent.java
rm src/test/java/org/codehaus/plexus/testing/PlexusTestJakartaTest.java

%build
%mvn_build

%install
%mvn_install

%files -f .mfiles
%doc README.md
%doc --no-dereference LICENSE

%files javadoc -f .mfiles-javadoc

%changelog
* Fri Sep 05 2025 Anton Meleshnikov <alton@altlinux.org> 1.3.0-alt1
- Initial build for Sisyphus (thanks fedora for the spec).
