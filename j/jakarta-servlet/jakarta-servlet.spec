%define _unpackaged_files_terminate_build 1

Name:           jakarta-servlet
Version:        6.1.0
Release:        alt1
Summary:        Server-side API for handling HTTP requests and responses
License:        (EPL-2.0 OR GPL-2.0-only WITH Classpath-exception-2.0) AND (CDDL-1.1 OR GPL-2.0-only WITH Classpath-exception-2.0) AND Apache-2.0 AND LicenseRef-EFSL-1.0
Group:          Development/Java
URL:            https://jakarta.ee/specifications/servlet/
VCS:            https://github.com/jakartaee/servlet.git
BuildArch:      noarch

Source0:        %name-%version.tar
Patch0:         %name-system.patch

BuildRequires(pre): rpm-macros-java
BuildRequires:  rpm-build-java
BuildRequires:  java-21-openjdk-devel
BuildRequires:  maven-local
BuildRequires:  mvn(org.apache.maven.plugins:maven-javadoc-plugin)
BuildRequires:  mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires:  mvn(org.codehaus.mojo:build-helper-maven-plugin)
BuildRequires:  mvn(org.junit.jupiter:junit-jupiter-engine)
BuildRequires:  mvn(org.junit.jupiter:junit-jupiter-params)
BuildRequires:  mvn(org.hamcrest:hamcrest)
BuildRequires:  asciidoctor

Provides:       glassfish-servlet-api = %version-%release

%description
Jakarta Servlet defines a server-side API for handling HTTP requests
and responses.

%package javax
Summary:        Genuine javax Servlet 4.0 API
Group:          Development/Java

%description javax
Original javax.servlet:javax.servlet-api 4.0.1 from the official Java EE
upstream, preserving actual coordinates, classes and legal notices.

%package api5
Summary:        Genuine Jakarta Servlet 5.0 API
Group:          Development/Java

%description api5
Genuine versioned Jakarta Servlet 5.0 API for EE9 applications.

%package javax4
Summary:        Genuine Servlet 4.0 API in the javax namespace
Group:          Development/Java

%description javax4
Genuine versioned Servlet 4.0 API for EE8 applications, using its actual
upstream jakarta.servlet coordinates and javax.servlet classes.

%package javadoc
Summary:        API documentation for Servlet APIs
Group:          Development/Documentation

%description javadoc
Independent Javadoc for all four genuine Servlet API versions.

%package manual
Summary:        Offline Servlet specifications
Group:          Development/Documentation

%description manual
Offline HTML specifications for Servlet 6.1 and 5.0, and the original
Servlet 4.0 specification scope document.

%prep
%setup -q
%patch0 -p1
# The optional upstream CI build cache is unavailable and unnecessary offline.
rm -f .mvn/extensions.xml

mkdir -p compat-licenses
for version in 4 5; do
    install -m644 compat/servlet$version/LICENSE.md \
    \
    compat-licenses/LICENSE-servlet$version.md
    install -m644 compat/servlet$version/NOTICE.md \
    \
    compat-licenses/NOTICE-servlet$version.md
    install -m644 compat/servlet$version/spec/src/main/asciidoc/license-efsl.adoc \
    \
    compat-licenses/license-efsl-servlet$version.adoc
done

for module in api compat/servlet4/api compat/servlet5/api \
    compat/javax-servlet; do
    pushd "$module"
    %pom_remove_parent
    %pom_remove_plugin -f :formatter-maven-plugin
    %pom_remove_plugin -f :impsort-maven-plugin
    %pom_remove_plugin -f :maven-enforcer-plugin
    %pom_remove_plugin -f :glassfish-copyright-maven-plugin
    %pom_remove_plugin -f :maven-release-plugin
    %pom_remove_plugin -f :maven-source-plugin
    popd
done

# Use the verbatim source license instead of the external legal bundle.
install -m644 compat/javax-servlet/LICENSE \
    compat-licenses/LICENSE-javax-servlet-4.0.1
install -d compat/javax-servlet/src/main/resources/META-INF
install -m644 compat/javax-servlet/LICENSE     compat/javax-servlet/src/main/resources/META-INF/LICENSE
pushd compat/javax-servlet
%pom_remove_plugin :maven-remote-resources-plugin
%mvn_package : javax
%mvn_file : %name-javax/javax.servlet-api
popd

pushd api
%mvn_file : %name/jakarta.servlet-api glassfish-servlet-api
popd
pushd compat/servlet4/api
%mvn_package : javax4
%mvn_compat_version : 4.0.4
%mvn_file : %name-javax4/jakarta.servlet-api
popd
pushd compat/servlet5/api
%mvn_package : api5
%mvn_compat_version : 5.0.0
%mvn_file : %name-api5/jakarta.servlet-api
popd

%build
pushd api
%mvn_build
popd
for module in servlet4 servlet5; do
    pushd compat/$module/api
    %mvn_build -- -Dmaven.compiler.release=8
    popd
done

pushd compat/javax-servlet
%mvn_build -- -Dmaven.compiler.release=8
popd

mkdir -p manual
asciidoctor --failure-level ERROR -a source-highlighter! \
    -a data-uri -a imagesdir=images -a webfonts! -a revnumber=6.1 \
    -o manual/servlet-6.1.html spec/src/main/asciidoc/servlet-spec.adoc
for version in 4 5; do
    asciidoctor --failure-level ERROR -a source-highlighter! \
    -a data-uri -a imagesdir=images -a webfonts! -a revnumber=$version.0 \
        -o manual/servlet-$version.0.html \
        compat/servlet$version/spec/src/main/asciidoc/servlet-spec.adoc
done
mv manual/servlet-4.0.html manual/servlet-4.0-scope.html

%install
pushd api
%mvn_install
popd
for version in 4 5; do
    pushd compat/servlet$version/api
    xmvn-install -R .xmvn-reactor -n %name -d %buildroot
    javadoc_dir=target/site/apidocs
    [ ! -d .xmvn/apidocs ] || javadoc_dir=.xmvn/apidocs
    install -d %buildroot%_javadocdir/%name-api$version
    cp -a "$javadoc_dir"/. %buildroot%_javadocdir/%name-api$version/
    popd
done
pushd compat/javax-servlet
xmvn-install -R .xmvn-reactor -n %name -d %buildroot
javadoc_dir=target/site/apidocs
[ ! -d .xmvn/apidocs ] || javadoc_dir=.xmvn/apidocs
install -d %buildroot%_javadocdir/%name-javax
cp -a "$javadoc_dir"/. %buildroot%_javadocdir/%name-javax/
popd
install -d %buildroot%_docdir/%name-manual
cp manual/*.html %buildroot%_docdir/%name-manual/

%files -f api/.mfiles
%doc --no-dereference LICENSE.md NOTICE.md compat-licenses
%doc spec/src/main/asciidoc/license-efsl.adoc

%files javax -f compat/javax-servlet/.mfiles-javax

%files api5 -f compat/servlet5/api/.mfiles-api5

%files javax4 -f compat/servlet4/api/.mfiles-javax4

%files javadoc -f api/.mfiles-javadoc
%_javadocdir/%name-api4
%_javadocdir/%name-api5
%_javadocdir/%name-javax

%files manual
%_docdir/%name-manual

%changelog
* Sun Nov 15 2026 Ivan Khanas <xeno@altlinux.org> 6.1.0-alt1
- New version.
- Add Servlet 4.0 and 5.0 compatibility APIs.

* Wed Aug 04 2021 Igor Vlasenko <viy@altlinux.org> 5.0.0-alt1_8jpp11
- update

* Fri Jun 04 2021 Igor Vlasenko <viy@altlinux.org> 5.0.0-alt1_5jpp11
- new version

