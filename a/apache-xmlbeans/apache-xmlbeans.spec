%global reldate 20241203
%define _unpackaged_files_terminate_build 1

Name: apache-xmlbeans
Version: 5.3.0
Release: alt3
Summary: XMLBeans is a technology for accessing XML by binding it to Java types
License: Apache-2.0
Group: Development/Java
URL: http://xmlbeans.apache.org/

Source0: %{name}-src-%{version}-%{?reldate}.tar.gz
Patch0: apache-xmlbeans-alt-java-version.patch

BuildArch: noarch

BuildRequires(pre): rpm-macros-gradle
BuildRequires: java-21-openjdk-devel
BuildRequires: xgradle
BuildRequires: maven-local
# The accepted genuine JAR bootstraps the first schema bindings only.
BuildRequires: apache-xmlbeans
BuildRequires: mvn(de.thetaphi:forbiddenapis)
BuildRequires: mvn(org.apache.ant:ant)
BuildRequires: mvn(org.osgi:osgi.core)
BuildRequires: mvn(org.jspecify:jspecify)
BuildRequires: mvn(com.github.javaparser:javaparser-core)
BuildRequires: mvn(com.github.javaparser:javaparser-symbol-solver-core)
BuildRequires: mvn(net.sf.saxon:Saxon-HE)
BuildRequires: mvn(org.xmlresolver:xmlresolver)
BuildRequires: mvn(org.xmlresolver:xmlresolver::data:)
BuildRequires: mvn(org.apache.logging.log4j:log4j-api)
BuildRequires: mvn(org.apache.logging.log4j:log4j-core)
BuildRequires: mvn(org.apache.maven:maven-core)
BuildRequires: mvn(org.apache.maven:maven-model)
BuildRequires: mvn(org.apache.maven:maven-plugin-api)
BuildRequires: mvn(org.apache.maven.plugin-tools:maven-plugin-annotations)
BuildRequires: mvn(org.junit.jupiter:junit-jupiter-api)
BuildRequires: mvn(org.junit.jupiter:junit-jupiter-params)
BuildRequires: mvn(org.junit.jupiter:junit-jupiter-engine)
BuildRequires: mvn(org.junit.platform:junit-platform-launcher)
BuildRequires: mvn(commons-io:commons-io)
BuildRequires: mvn(org.hamcrest:hamcrest)
BuildRequires: mvn(xerces:xercesImpl)
BuildRequires: mvn(xml-resolver:xml-resolver)
BuildRequires: mvn(org.jacoco:org.jacoco.agent::runtime:)
BuildRequires: mvn(org.jacoco:org.jacoco.ant)

%description
XMLBeans is a technology for accessing XML by binding it to Java types.
XMLBeans provides several ways to get at the XML, including:

* Through XML schema that has been compiled to generate Java types that
represent schema types. In this way, you can access instances of the schema
through JavaBeans-style accessors after the fashion of "getFoo" and "setFoo".

* The XMLBeans API also allows you to reflect into the XML schema itself
through an XML Schema Object model.

* A cursor model through which you can traverse the full XML infoset.

* Support for XML DOM.

%javadoc_package

%prep
%setup -n %{name}-src-%{version}-%{?reldate}
%patch0 -p1
%mvn_file :xmlbeans xmlbeans/xmlbeans

%build
%gradle_publish -PjdkVersion=21

%install
%gradle_register --artifacts=xmlbeans-
%gradle_register_javadoc --artifacts=xmlbeans-
%gradle_install

%check
%gradle_check -PjdkVersion=21

%files -f .mfiles
%doc README.md LICENSE.txt NOTICE.txt

%changelog
* Sun Nov 15 2026 Ivan Khanas <xeno@altlinux.org> 5.3.0-alt3
- Stop vendoring JARs and build with xgradle.
- Fix Maven metadata and Saxon 13 integration.
- Package Javadoc separately.

* Mon Jan 12 2026 Andrey Cherepanov <cas@altlinux.org> 5.3.0-alt2
- Packaged xmvn metadata file.
- Removed com.sun.org.apache.xml.internal:resolver from requirements.

* Sun Jul 06 2025 Andrey Cherepanov <cas@altlinux.org> 5.3.0-alt1
- Initial build for Sisyphus.
