%define _unpackaged_files_terminate_build 1

Name: apicatalog-titanium-json-ld
Version: 1.7.0
Release: alt1

Summary: An implementation of the JSON-LD 1.1 (JSON-based Serialization for Linked Data) specification in Java
License: Apache-2.0
Group: Development/Java
Url: https://apicatalog.com
Vcs: https://github.com/filip26/titanium-json-ld.git
BuildArch: noarch

Source0: %name-%version.tar
Patch0: 0001-Remove-unwanted-okhttp-dep-alt-patch.patch

BuildRequires(pre): rpm-macros-java
BuildRequires: /proc
BuildRequires: rpm-build-java
BuildRequires: jpackage-11-compat
BuildRequires: maven-local
BuildRequires: maven-source-plugin
BuildRequires: jakarta-json2
BuildRequires: apicatalog-titanium-rdf-api
BuildRequires: apicatalog-titanium-rdf-n-quads
BuildRequires: apicatalog-titanium-jcs
BuildRequires: apicatalog-titanium-rdf-primitives
BuildRequires: apicatalog-titanium-rdfc
BuildRequires: maven-plugin-build-helper
BuildRequires: guava

%package javadoc
Group: Development/Java
Summary: Javadoc for %name

%description
%summary.

%description javadoc
This package contains javadoc for %name.

%prep
%setup
%autopatch -p1
%pom_remove_dep com.squareup.okhttp3:okhttp pom_jre8.xml

%pom_remove_plugin :maven-javadoc-plugin pom_parent.xml
%pom_remove_plugin :flatten-maven-plugin pom_parent.xml

%pom_remove_dep com.github.tomakehurst:wiremock-jre8 pom_parent.xml
rm -f src/test/java/com/apicatalog/jsonld/RemoteTest.java \
  src/test/java/com/apicatalog/jsonld/loader/HttpLoaderTest.java \
  src/test/java/com/apicatalog/jsonld/test/JsonLdMockServer.java \
  src/test/java/com/apicatalog/jsonld/earl/EarlGenerator.java

%pom_add_dep com.google.guava:guava:test pom.xml
%pom_add_dep com.google.guava:guava:test pom_jre8.xml

%build
%mvn_build -- --file=pom.xml
%mvn_build -- --file=pom_jre8.xml

%install
%mvn_install

%files -f .mfiles

%files javadoc -f .mfiles-javadoc

%changelog
* Sat Nov 08 2025 Ivan Khanas <xeno@altlinux.org> 1.7.0-alt1
- First build for ALT.
