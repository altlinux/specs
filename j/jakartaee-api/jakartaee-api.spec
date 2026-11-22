%define _unpackaged_files_terminate_build 1

Name: jakartaee-api
Version: 10.0.0
Release: alt1

Summary: Jakarta EE 10 platform BOM metadata
License: EPL-2.0 or GPL-2.0 with Classpath-exception-2.0
Group: Development/Java
URL: https://jakarta.ee/
VCS: https://github.com/jakartaee/jakartaee-api.git

Source0: %name-%version.tar
Source1: install-generated-bom.py
BuildArch: noarch

BuildRequires(pre): rpm-macros-java
BuildRequires: maven-local
BuildRequires: java-21-openjdk-devel
BuildRequires: ee4j-parent
BuildRequires: glassfish-build-maven-plugin-compat
BuildRequires: mvn(org.apache.maven.plugins:maven-resources-plugin)
BuildRequires: mvn(org.apache.maven.plugins:maven-compiler-plugin)
BuildRequires: mvn(org.apache.maven.plugins:maven-jar-plugin)

%description
Build the Jakarta EE 10 BOM and its parent for consumers of the EE 10 platform.

%package ee10-parent
Summary: Jakarta EE 10 upstream Maven parent
Group: Development/Java

%description ee10-parent
Maven parent metadata for the Jakarta EE 10 platform.

%package ee10-bom
Summary: Jakarta EE 10 upstream Maven BOM
Group: Development/Java

%description ee10-bom
Dependency management metadata for the Jakarta EE 10 APIs.

%prep
%setup -q
%mvn_compat_version : 10.0.0
%mvn_package jakarta.platform:jakartaee-api-parent:pom:* ee10-parent
%mvn_package jakarta.platform:jakarta.jakartaee-bom:pom:* ee10-bom

%build
%mvn_build -s -j

%install
%__python3 %SOURCE1
%mvn_install

%files ee10-parent -f .mfiles-ee10-parent
%doc LICENSE.txt

%files ee10-bom -f .mfiles-ee10-bom

%changelog
* Thu Nov 19 2026 Ivan Khanas <xeno@altlinux.org> 10.0.0-alt1
- Initial build for ALT.
