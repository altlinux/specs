%global _unpackaged_files_terminate_build 1

Name: eclipse-collections
Version: 13.0.0
Release: alt1
Summary: Collections framework for Java with optimized data structures
License: EPL-1.0 or EDL-1.0
Group: Development/Java
Url: https://github.com/eclipse/%name
Vcs: https://github.com/eclipse/%name

BuildArch: noarch

Source0: %name-%version.tar

BuildRequires(pre): rpm-macros-java
BuildRequires: /proc
BuildRequires: rpm-build-java
BuildRequires: maven-local
BuildRequires: java-17-openjdk-devel
BuildRequires: mvn(org.antlr:ST4)
BuildRequires: mvn(biz.aQute.bnd:biz.aQute.bnd.annotation)
BuildRequires: mvn(org.apache.maven.plugins:maven-plugin-plugin)

%description
Eclipse Collections is a collections framework for Java with optimized
data structures and a rich, functional and fluent API.

%package -n %name-api
Summary: Eclipse Collections API
Group: Development/Java

%description -n %name-api
API module of Eclipse Collections framework.

%package -n %name-lib
Summary: Eclipse Collections Main Library
Group: Development/Java
Requires: %name-api = %EVR

%description -n %name-lib
Main library module of Eclipse Collections framework.

%package javadoc
Summary: API documentation for %name
Group: Development/Java

%description javadoc
API documentation for the %name library.

%prep
%setup
# Disable modules we don't need
%pom_disable_module %name-testutils
%pom_disable_module %name-forkjoin
%pom_disable_module unit-tests
%pom_disable_module serialization-tests
%pom_disable_module jcstress-tests
%pom_disable_module unit-tests-java8
%pom_disable_module test-coverage
%pom_disable_module p2-site

# Remove unnecessary plugins
for plugin in maven-release-plugin maven-gpg-plugin nexus-staging-maven-plugin \
              maven-checkstyle-plugin jacoco-maven-plugin; do
    %pom_remove_plugin :$plugin || :
done

%pom_xpath_inject "pom:plugin[pom:artifactId='maven-plugin-plugin']" \
    "<version>3.9.0</version>" %name-code-generator-maven-plugin

%mvn_package ":%name-api" %name-api
%mvn_package ":%name" %name-lib

%build
%mvn_build -f

%install
%mvn_install

%files -f .mfiles
%doc README.md
%doc --no-dereference LICENSE-EDL-1.0.txt LICENSE-EPL-1.0.txt

%files -n %name-api -f .mfiles-%name-api

%files -n %name-lib -f .mfiles-%name-lib

%files javadoc -f .mfiles-javadoc

%changelog
* Thu May 29 2026 Timofei Fedotov <sovtouch@altlinux.org> 13.0.0-alt1
- Initial built for ALT Sisyphus.
