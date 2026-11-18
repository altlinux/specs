%define _unpackaged_files_terminate_build 1

Group: Development/Java
BuildRequires: rpm-build-java
BuildRequires: java-21-openjdk-devel
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%global srcname saaj-api
%global javax_version 1.4.2

Name:           jakarta-saaj
Version:        3.0.2
Release:        alt2
Summary:        SOAP with Attachments API for Java
License:        BSD-3-Clause and EPL-2.0 and LicenseRef-EFSL-1.0
URL:            https://github.com/jakartaee/saaj-api
BuildArch:      noarch

Source0:        %{srcname}-%{version}.tar.gz
Source1:        %{srcname}-%{javax_version}.tar.gz

BuildRequires:  maven-local
BuildRequires:  mvn(jakarta.activation:jakarta.activation-api)
BuildRequires:  mvn(jakarta.activation:jakarta.activation-api:1.2.2)
BuildRequires:  mvn(junit:junit)
BuildRequires:  asciidoctor
BuildRequires:  mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-enforcer-plugin)
BuildRequires:  mvn(org.codehaus.mojo:build-helper-maven-plugin)
BuildRequires:  mvn(org.glassfish.build:spec-version-maven-plugin)

%description
Jakarta SOAP with Attachments defines an API enabling developers to
produce and consume messages conforming to the SOAP 1.1, SOAP 1.2, and
SOAP Attachments Feature.

%package javadoc
Group: Development/Java
Summary:        API documentation for %{name}
BuildArch: noarch
%description javadoc
API documentation for %{name}.

%package javax
Group: Development/Java
Summary: SOAP with Attachments 1.4 API in the javax namespace

%description javax
The complete upstream 1.4.2 SOAP API for applications using javax.xml.soap.
Its versioned Maven coordinate and installed paths coexist with Jakarta 3.

%package manual
Group: Development/Documentation
Summary: SOAP with Attachments specifications

%description manual
Offline HTML specifications for Jakarta SOAP 3.0 and SOAP 1.4.

%prep
%setup -q -n %{srcname}-%{version} -a1

pushd api
# remove unnecessary dependency on parent POM
%pom_remove_parent
# remove unnecessary maven plugins
%pom_remove_plugin :glassfish-copyright-maven-plugin
%pom_remove_plugin :spotbugs-maven-plugin
%pom_remove_plugin :buildnumber-maven-plugin
%pom_remove_plugin :maven-source-plugin
%mvn_file : %{name}/jakarta.xml.soap-api
popd

pushd %{srcname}-%{javax_version}/api
%pom_remove_parent
%pom_remove_plugin :glassfish-copyright-maven-plugin
%pom_remove_plugin :spotbugs-maven-plugin
%pom_remove_plugin :buildnumber-maven-plugin
%pom_remove_plugin :maven-source-plugin
%mvn_package : javax
%mvn_compat_version : %{javax_version}
%mvn_file : %{name}-javax/jakarta.xml.soap-api
popd

%build
pushd api
%mvn_build
popd

pushd %{srcname}-%{javax_version}/api
# Exercise every upstream configuration scenario using an isolated JDK conf.
test_jdk_home="$PWD/.test-jdk"
system_jdk_home="$(dirname "$(dirname "$(readlink -f "$(command -v java)")")")"
mkdir -p "$test_jdk_home"
cp -as "$system_jdk_home"/. "$test_jdk_home"/
if [ -L "$test_jdk_home/conf" ]; then
    rm "$test_jdk_home/conf"
fi
cp -rL "$system_jdk_home/conf" "$test_jdk_home/conf"
chmod u+rwx "$test_jdk_home/conf"
%mvn_build -- -Dsurefire.useModulePath=false -DrunUnsafe=true \
    "-DargLine=-Djava.security.manager=allow -Djava.home=$test_jdk_home"
popd

mkdir -p manual
asciidoctor -a source-highlighter! -a data-uri -a revnumber=3.0 \
    -o manual/soap-3.0.html spec/src/main/asciidoc/soap-spec.adoc
asciidoctor -a source-highlighter! -a data-uri -a revnumber=1.4 \
    -o manual/soap-1.4.html %{srcname}-%{javax_version}/spec/src/main/asciidoc/jakarta.xml.soap-spec.adoc

%install
pushd api
%mvn_install
popd

pushd %{srcname}-%{javax_version}/api
xmvn-install -R .xmvn-reactor -n %{name} -d %{buildroot}
javadoc_dir=target/site/apidocs
[ ! -d .xmvn/apidocs ] || javadoc_dir=.xmvn/apidocs
install -d %{buildroot}%{_javadocdir}/%{name}-javax
cp -a "$javadoc_dir"/. %{buildroot}%{_javadocdir}/%{name}-javax/
popd

install -d %{buildroot}%{_docdir}/%{name}-manual
cp -a manual/*.html spec/LICENSE %{buildroot}%{_docdir}/%{name}-manual/

%files -f api/.mfiles
%doc --no-dereference LICENSE.md NOTICE.md
%doc README.md

%files javax -f %{srcname}-%{javax_version}/api/.mfiles-javax
%doc --no-dereference %{srcname}-%{javax_version}/LICENSE.md %{srcname}-%{javax_version}/NOTICE.md

%files javadoc -f api/.mfiles-javadoc
%doc --no-dereference LICENSE.md NOTICE.md
%{_javadocdir}/%{name}-javax

%files manual
%{_docdir}/%{name}-manual

%changelog
* Sun Nov 15 2026 Ivan Khanas <xeno@altlinux.org> 3.0.2-alt2
- Add javax SOAP 1.4.2 alongside Jakarta SOAP 3.

* Fri Apr 17 2026 Anton Meleshnikov <alton@altlinux.org> 3.0.2-alt1
- new version

* Mon Mar 20 2023 Igor Vlasenko <viy@altlinux.org> 1.4.2-alt1_8jpp11
- update

* Fri Jun 04 2021 Igor Vlasenko <viy@altlinux.org> 1.4.2-alt1_2jpp11
- new version

