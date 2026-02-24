Name:           plexus-xml
Version:        3.0.2
Release:        alt1

Summary:        Plexus XML Utilities
License:        Apache-2.0
Group:          Development/Java
URL:            https://codehaus-plexus.github.io/plexus-xml/
VCS:            https://github.com/codehaus-plexus/plexus-xml
BuildArch:      noarch

Source0:        %name-%version.tar

BuildRequires:  jpackage-default
BuildRequires:  maven-local

BuildRequires:  mvn(org.codehaus.plexus:plexus:pom:)
BuildRequires:  mvn(org.openjdk.jmh:jmh-core)
BuildRequires:  mvn(org.openjdk.jmh:jmh-generator-annprocess)

%description
A collection of various utility classes to ease working with XML in Maven 3.
This library consists of XML classes (org.codehaus.plexus.util.xml)
that have been extracted from plexus-utils 3:
* plexus-utils 3 = plexus-utils 4 + plexus-xml 3.

%javadoc_package

%prep
%setup

%build
%mvn_build

%install
%mvn_install

%files -f .mfiles
%doc README.md
%doc NOTICE.txt LICENSE.txt

%changelog
* Wed Feb 18 2026 Evgeniy Serov <scala@altlinux.org> 3.0.2-alt1
- Updated to 3.0.2.

* Wed Feb 19 2025 Anton Meleshnikov <alton@altlinux.org> 3.0.0-alt1
- Initial build for Sisyphus.
