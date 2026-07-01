Name:           awaitility
Version:        4.3.0
Release:        alt2

Summary:        Awaitility is a small Java DSL for synchronizing asynchronous operations
License:        Apache-2.0
Group:          Development/Java
URL:            https://github.com/awaitility/awaitility
VCS:            https://github.com/awaitility/awaitility

Source0:        %name-%version.tar

BuildRequires(pre):  rpm-macros-java
BuildRequires:  jpackage-default
BuildRequires:  maven-local

BuildRequires:  mvn(org.apache.felix:maven-bundle-plugin)

BuildArch:      noarch

%description
Testing asynchronous systems is hard. Not only does it require handling threads,
timeouts, and concurrency issues, but the intent of the test code can be
obscured by all these details. Awaitility is a DSL that allows you to express
expectations of an asynchronous system in a concise and easy-to-read manner.

%javadoc_package

%prep
%setup

%pom_remove_parent

rm awaitility/src/test/java/org/awaitility/AwaitilityTest.java

%pom_remove_plugin :scala-maven-plugin awaitility-scala
%pom_remove_plugin :animal-sniffer-maven-plugin

%pom_disable_module awaitility-groovy
%pom_disable_module awaitility-scala

%mvn_package :%name-parent __noinstall

%build
%mvn_build -- -DargLine=--add-opens=java.base/java.lang=ALL-UNNAMED

%install
%mvn_install

%files -f .mfiles
%doc LICENSE *.md

%changelog
* Wed Jul 01 2026 Evgeniy Serov <scala@altlinux.org> 4.3.0-alt2
- Fixed FTBFS: java.lang for tests on JDK 17.

* Thu Apr 16 2026 Evgeniy Serov <scala@altlinux.org> 4.3.0-alt1
- Initial build for Sisyphus.
