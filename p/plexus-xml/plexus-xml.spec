Name: plexus-xml
Version: 3.0.0
Release: alt1

Summary: Plexus XML Utilities
License: Apache-2.0
Group: Development/Java
Url: https://github.com/codehaus-plexus/plexus-xml

Source: %name-%version.tar

BuildRequires(pre): rpm-build-java
BuildRequires: java-devel >= 1.6.0
BuildRequires: /proc
BuildRequires: maven-local
BuildRequires: plexus-utils
BuildRequires: mvn(org.codehaus.plexus:plexus:pom:)

%description
A collection of various utility classes to ease working with XML in Maven 3.
This library consists of XML classes (org.codehaus.plexus.util.xml)
that have been extracted from plexus-utils 3:
* plexus-utils 3 = plexus-utils 4 + #plexus-xml 3.

%package javadoc
Summary: API documentation for  plexus-xml
Group: Development/Java

%description javadoc
API documentation for  plexus-xml

%prep
%setup

%build
%mvn_build -f

%install
%mvn_install

%files -f .mfiles
%doc README.md
%doc --no-dereference NOTICE.txt LICENSE.txt

%files javadoc -f .mfiles-javadoc

%changelog
* Wed Feb 19 2025 Anton Meleshnikov <alton@altlinux.org> 3.0.0-alt1
- Initial build for Sisyphus.
