Name:    pdfbox-graphics2d
Version: 3.0.5
Release: alt1
Summary: Graphics2D Bridge for pdfbox

License: Apache-2.0
Group:   Development/Java
URL:     https://github.com/rototor/pdfbox-graphics2d
Source0: %name-%version.tar

BuildRequires(pre): rpm-build-java
BuildRequires: java-devel
BuildRequires: /proc
BuildRequires: maven-local
BuildRequires: mvn(org.apache.maven.plugins:maven-source-plugin)
BuildRequires: mvn(org.apache.pdfbox:pdfbox)

BuildArch: noarch
Requires: java

%description
Using this library you can use any Graphics2D API based SVG / graph / chart
library to embed those graphics as vector drawing in a PDF.

#javadoc_package

%prep
%setup
%pom_remove_plugin :central-publishing-maven-plugin
%pom_remove_plugin :maven-javadoc-plugin
%pom_remove_plugin :maven-bundle-plugin

%build
%mvn_build -f -j

%install
%mvn_install

%files -f .mfiles
%doc *.md

%changelog
* Thu Jun 18 2026 Andrey Cherepanov <cas@altlinux.org> 3.0.5-alt1
- Initial build for Sisyphus.
