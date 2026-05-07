Name:           graph-convert
Version:        1.0.3
Release:        alt1

Summary:        Java docx to pdf using Microsoft Graph
License:        Apache-2.0
Group:          Development/Java
URL:            https://github.com/plutext/java-docx-to-pdf-using-Microsoft-Graph
VCS:            https://github.com/plutext/java-docx-to-pdf-using-Microsoft-Graph

Source0:        %name-%version.tar

BuildRequires(pre):  maven-local
BuildRequires:  jpackage-default

BuildRequires:  mvn(org.sonatype.oss:oss-parent:pom:)
BuildRequires:  mvn(com.github.scribejava:scribejava-apis)

BuildArch:      noarch

%description
This project shows you how to use Microsoft's Graph for OpenXML (docx/pptx/xlsx)
to PDF conversion from Java.

%javadoc_package

%prep
%setup

%pom_remove_plugin :maven-javadoc-plugin

%pom_disable_module without-graph-sdk-using-msal4j
%pom_disable_module using-graph-sdk-core-only
%pom_disable_module using-graph-sdk
%pom_disable_module graph-convert-sample

%build
%mvn_build

%install
%mvn_install

%files -f .mfiles
%doc LICENSE README.md

%changelog
* Thu May 07 2026 Evgeniy Serov <scala@altlinux.org> 1.0.3-alt1
- Initial build for Sisyphus.
