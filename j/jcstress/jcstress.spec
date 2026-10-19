Name: jcstress
Version: 0.16
Release: alt1

Summary: the experimental harness and a suite of tests
License: GPL-2.0
Group: Development/Java
Url: https://openjdk.org/projects/code-tools/jcstress
Vcs: https://github.com/openjdk/jcstress
BuildArch: noarch

Source0: https://github.com/openjdk/jcstress/archive/%version.tar.gz

BuildRequires: maven-local
BuildRequires: /proc rpm-build-java
BuildRequires: jpackage-default

BuildRequires: mvn(org.apache.maven.archetype:archetype-packaging)
BuildRequires: mvn(org.apache.maven.plugins:maven-shade-plugin)
BuildRequires: mvn(org.codehaus.mojo:exec-maven-plugin)
BuildRequires: mvn(org.codehaus.mojo:build-helper-maven-plugin)
BuildRequires: mvn(org.apache.maven.plugins:maven-source-plugin)
BuildRequires: mvn(com.google.jimfs:jimfs)
BuildRequires: mvn(net.sf.jopt-simple:jopt-simple)
BuildRequires: mvn(org.openjdk.jmh:jmh-core)
BuildRequires: mvn(org.openjdk.jmh:jmh-generator-annprocess)

%description
The Java Concurrency Stress (jcstress) is the experimental harness
and a suite of tests to aid the research in the correctness of concurrency
support in the JVM, class libraries, and hardware.

%prep
%setup -n %version

%pom_remove_plugin :license-maven-plugin
%pom_remove_plugin :maven-javadoc-plugin
%pom_remove_plugin :buildnumber-maven-plugin
%pom_remove_plugin :maven-enforcer-plugin

%pom_disable_module jcstress-java-test-archetype

%build
%mvn_build -f -j

%install
%mvn_install

%files -f .mfiles
%doc README.md
%doc --no-dereference LICENSE

%changelog
* Wed Oct 14 2026 Anton Meleshnikov <alton@altlinux.org> 0.16-alt1
- Initial build for Sisyphus.
