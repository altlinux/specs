%define _unpackaged_files_terminate_build 1

Name: jakarta-json
Version: 2.1.3
Release: alt2

Summary: Jakarta JSON Processing API
License: EPL-2.0
Group: Development/Java
Url: https://eclipse-ee4j.github.io/jsonp/
Vcs: https://github.com/eclipse-ee4j/jsonp.git
BuildArch: noarch

Source0: %name-%version.tar
Patch0:  %name-%version-alt-patch.patch
Source1: jsonp-1.1-1.1.6-RELEASE.tar.gz

BuildRequires(pre): rpm-macros-java
BuildRequires: /proc
BuildRequires: rpm-build-java
BuildRequires: maven-local
BuildRequires: jpackage-11-compat
BuildRequires: maven-plugin-bundle
BuildRequires: maven-plugin-build-helper
BuildRequires: spec-version-maven-plugin
BuildRequires: maven-enforcer-plugin
BuildRequires: maven-antrun-plugin

%description
Jakarta JSON Processing provides portable APIs to parse, generate,
transform, and query JSON documents. The JAR contains both the 2.1
(jakarta.json.*) and legacy 1.1 (javax.json.*) API classes.

%package api
Summary: Jakarta JSON Processing API
Group: Development/Java
Provides: %name = %EVR

%description api
Jakarta JSON Processing provides portable APIs to parse, generate,
transform, and query JSON documents. The JAR contains both the 2.1
(jakarta.json.*) and legacy 1.1 (javax.json.*) API classes.

%package impl
Summary: Legacy JSON-P implementation for javax.json
Group: Development/Java
Requires: %name-api = %EVR

%description impl
Legacy JSON-P implementation classes from version 1.1.6, packaged
separately for javax.json runtime compatibility.

%prep
%setup -a1
%autopatch -p1

%pom_remove_parent
%pom_remove_plugin -r org.glassfish.copyright:glassfish-copyright-maven-plugin
%pom_remove_plugin com.github.spotbugs:spotbugs-maven-plugin
%pom_remove_plugin :maven-javadoc-plugin
%pom_remove_plugin :maven-source-plugin
%pom_remove_plugin :buildnumber-maven-plugin

%pom_remove_parent jsonp-1.1-1.1.6-RELEASE/pom.xml
%pom_remove_plugin org.codehaus.mojo:build-helper-maven-plugin jsonp-1.1-1.1.6-RELEASE/pom.xml
%pom_remove_plugin org.apache.maven.plugins:maven-source-plugin jsonp-1.1-1.1.6-RELEASE/pom.xml

%pom_remove_plugin org.glassfish.build:spec-version-maven-plugin jsonp-1.1-1.1.6-RELEASE/api/pom.xml
%pom_remove_plugin org.apache.maven.plugins:maven-source-plugin jsonp-1.1-1.1.6-RELEASE/api/pom.xml
%pom_remove_plugin org.apache.maven.plugins:maven-javadoc-plugin jsonp-1.1-1.1.6-RELEASE/api/pom.xml
%pom_remove_plugin org.apache.felix:maven-bundle-plugin jsonp-1.1-1.1.6-RELEASE/api/pom.xml
%pom_remove_plugin org.glassfish.build:spec-version-maven-plugin jsonp-1.1-1.1.6-RELEASE/impl/pom.xml
%pom_remove_plugin org.apache.maven.plugins:maven-source-plugin jsonp-1.1-1.1.6-RELEASE/impl/pom.xml
%pom_remove_plugin org.apache.maven.plugins:maven-dependency-plugin jsonp-1.1-1.1.6-RELEASE/impl/pom.xml
%pom_remove_plugin org.apache.maven.plugins:maven-javadoc-plugin jsonp-1.1-1.1.6-RELEASE/impl/pom.xml
%pom_remove_plugin org.apache.felix:maven-bundle-plugin jsonp-1.1-1.1.6-RELEASE/impl/pom.xml

%pom_xpath_set "/*[local-name()='project']/*[local-name()='packaging']" jar jsonp-1.1-1.1.6-RELEASE/api/pom.xml
%pom_xpath_set "/*[local-name()='project']/*[local-name()='packaging']" jar jsonp-1.1-1.1.6-RELEASE/impl/pom.xml

%mvn_alias "jakarta.json:jakarta.json-api:%version" \
  "jakarta.json:jakarta.json-api" \
  "javax.json:javax.json-api" \
  "javax.json:javax.json-api:1.1.6" \
  #
%mvn_alias "org.glassfish:jakarta.json" "org.glassfish:javax.json"

%build
%mvn_build -j
mv .xmvn-reactor .xmvn-reactor-api
%mvn_build -j -- -f jsonp-1.1-1.1.6-RELEASE/pom.xml -pl api,impl -am
mv .xmvn-reactor .xmvn-reactor-legacy

%install
xmvn-install -R .xmvn-reactor-api -n %{name} -d %{buildroot}
mv .mfiles .mfiles-api
legacy_buildroot="$(mktemp -d)"
xmvn-install -R .xmvn-reactor-legacy -n %{name}-impl -d "${legacy_buildroot}"
mv .mfiles .mfiles-legacy
grep 'jakarta.json-api' .mfiles-legacy > .mfiles-legacy-api || :
grep -v 'jakarta.json-api' .mfiles-legacy > .mfiles-impl
sed -e 's/^%%attr([^)]*) //' -e 's/^%%dir //' .mfiles-impl > .mfiles-impl-paths
while read -r path; do
    [ -e "${legacy_buildroot}${path}" ] || continue
    if [ -d "${legacy_buildroot}${path}" ]; then
        mkdir -p "%{buildroot}${path}"
    else
        mkdir -p "%{buildroot}$(dirname "${path}")"
        cp -a "${legacy_buildroot}${path}" "%{buildroot}${path}"
    fi
done < .mfiles-impl-paths
impl_metadata="%{buildroot}/usr/share/maven-metadata/%{name}-impl.xml"
if [ -f "${impl_metadata}" ]; then
    perl -0777 -i -pe '
        s|
            <artifact>\s*
            <groupId>jakarta\.json</groupId>\s*
            <artifactId>jakarta\.json-api</artifactId>.*?
            </artifact>\n
        ||sgx;
        s|
            <dependency>\s*
            <groupId>jakarta\.json</groupId>\s*
            <artifactId>jakarta\.json-api</artifactId>.*?
            </dependency>\n
        ||sgx;
    ' "${impl_metadata}"
fi
rm -rf "${legacy_buildroot}"

%files api -f .mfiles-api

%files impl -f .mfiles-impl

%changelog
* Tue Mar 31 2026 Ivan Khanas <xeno@altlinux.org> 2.1.3-alt2
- Fix jakarta.json-api provides.

* Wed Mar 25 2026 Ivan Khanas <xeno@altlinux.org> 2.1.3-alt1
- Update to 2.1.3. Legacy 1.1 (javax.json.*) classes merged into JAR.
- Add separate legacy impl binary package from 1.1.6 sources

* Fri Jul 01 2022 Igor Vlasenko <viy@altlinux.org> 1.1.6-alt1_7jpp11
- update

* Thu May 26 2022 Igor Vlasenko <viy@altlinux.org> 1.1.6-alt1_3jpp11
- update

* Sat Jun 05 2021 Igor Vlasenko <viy@altlinux.org> 1.1.6-alt1_2jpp11
- new version
