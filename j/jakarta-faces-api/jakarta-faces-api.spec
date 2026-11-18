%define _unpackaged_files_terminate_build 1

Name: jakarta-faces-api
Version: 4.1.2
Release: alt1

Summary: Jakarta Faces API and specification
License: (EPL-2.0 or GPL-2.0-only with Classpath-exception-2.0) and EFSL
Group: Development/Java
URL: https://jakarta.ee/specifications/faces/
VCS: https://github.com/jakartaee/faces.git
BuildArch: noarch

Source: %name-%version.tar
Source1: mojarra-4.1.21.tar

BuildRequires(pre): rpm-macros-java
BuildRequires: maven-local
BuildRequires: java-21-openjdk-devel
BuildRequires: cdi-api-compat4
BuildRequires: cdi-api-compat4-el
BuildRequires: jakarta-servlet
BuildRequires: jaxb-api
BuildRequires: asciidoctor
BuildRequires: gem-coderay
BuildRequires: mvn(org.eclipse.ee4j:project:pom:)
BuildRequires: mvn(jakarta.websocket:jakarta.websocket-api)
BuildRequires: mvn(jakarta.websocket:jakarta.websocket-client-api)
BuildRequires: mvn(jakarta.el:jakarta.el-api)
BuildRequires: mvn(jakarta.validation:jakarta.validation-api)
BuildRequires: mvn(jakarta.transaction:jakarta.transaction-api)
BuildRequires: mvn(jakarta.json:jakarta.json-api)
BuildRequires: mvn(jakarta.ejb:jakarta.ejb-api)
BuildRequires: mvn(jakarta.persistence:jakarta.persistence-api)
BuildRequires: mvn(jakarta.annotation:jakarta.annotation-api)
BuildRequires: mvn(jakarta.inject:jakarta.inject-api)
BuildRequires: mvn(jakarta.xml.bind:jakarta.xml.bind-api)
BuildRequires: mvn(org.apache.felix:maven-bundle-plugin)

%description
Jakarta Faces defines a component framework for web user interfaces.
This package builds the upstream API from genuine Mojarra sources and
retains its JPMS descriptor and OSGi metadata.

%package javadoc
Summary: API documentation for Jakarta Faces
Group: Development/Java

%description javadoc
Independent Javadoc for the Jakarta Faces API.

%package manual
Summary: Jakarta Faces specification and TCK guide
Group: Documentation

%description manual
HTML specification and TCK user guide from the upstream source tree.
Original draft labels and documented release versions are preserved.

%prep
%setup -a 1
# Select genuine CDI 4.1 API and EL integration with versioned bindings.
%pom_change_dep jakarta.enterprise:jakarta.enterprise.cdi-api \
    jakarta.enterprise:jakarta.enterprise.cdi-api:4.1.0 api
%pom_change_dep jakarta.enterprise:jakarta.enterprise.cdi-el-api \
    jakarta.enterprise:jakarta.enterprise.cdi-el-api:4.1.0 api
cp -a mojarra-4.1.21/impl/src/main/java api/src/main/
cp -a mojarra-4.1.21/impl/src/main/resources api/src/main/
cp -a api/src/main/module/module-info.java api/src/main/java/
pushd api
%mvn_file :jakarta.faces-api %name/jakarta.faces-api
popd

%build
pushd api
%mvn_build
popd
python3 .gear/build-docs.py

%install
pushd api
rm -f .xmvn/apidocs/args
rm -rf .xmvn/apidocs/module-source-path
%mvn_install
popd
install -Dm644 api/src/main/javadoc/doc-files/speclicense.html \
    %buildroot%_javadocdir/%name/doc-files/speclicense.html
install -d %buildroot%_docdir/%name-manual
cp -a manual/. %buildroot%_docdir/%name-manual/

%files -f api/.mfiles
%doc LICENSE.md NOTICE.md
%doc spec/src/main/asciidoc/license-efsl.adoc

%files javadoc -f api/.mfiles-javadoc

%files manual
%_docdir/%name-manual

%changelog
* Sun Nov 15 2026 Ivan Khanas <xeno@altlinux.org> 4.1.2-alt1
- Initial build for ALT.
