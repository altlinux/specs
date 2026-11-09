Name: openpdf
Version: 3.0.5
Release: alt1

Summary: Java library for working with PDF files
License: LGPL-2.1-or-later, MPL-2.0
Group: Development/Java
Url: https://github.com/LibrePDF/OpenPDF
Vcs: https://github.com/LibrePDF/OpenPDF
ExclusiveArch: x86_64 aarch64

Source0: https://github.com/LibrePDF/OpenPDF/archive/%version.tar.gz

BuildRequires: maven-local
BuildRequires: /proc rpm-build-java
BuildRequires: java-21-openjdk-devel

BuildRequires: mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires: mvn(com.ibm.icu:icu4j)
BuildRequires: mvn(org.apache.xmlgraphics:fop)
BuildRequires: mvn(org.apache.maven.plugins:maven-enforcer-plugin)
BuildRequires: mvn(org.apache.maven.plugins:maven-source-plugin)
BuildRequires: mvn(org.jfree:jfreechart)
BuildRequires: mvn(org.jfree:jcommon)
BuildRequires: mvn(org.htmlunit:neko-htmlunit)
BuildRequires: mvn(com.aayushatharva.brotli4j:brotli4j)
BuildRequires: mvn(org.jetbrains.kotlin:kotlin-maven-plugin)
BuildRequires: mvn(org.apache.maven.plugin-tools:maven-plugin-annotations)

%description
OpenPDF is an open-source Java library for creating,
editing, rendering, and encrypting PDF documents,
as well as generating PDFs from HTML.

%prep
%setup

%pom_remove_plugin :jacoco-maven-plugin
%pom_remove_plugin -r :maven-javadoc-plugin
%pom_remove_plugin -r :build-helper-maven-plugin

%build
%mvn_build -f -j

%install
%mvn_install

%files -f .mfiles
%doc README.md Security.md
%doc --no-dereference LICENSE.md

%changelog
* Mon Nov 09 2026 Anton Meleshnikov <alton@altlinux.org> 3.0.5-alt1
- Initial build for Sisyphus.