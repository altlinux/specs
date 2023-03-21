# BEGIN SourceDeps(oneline):
BuildRequires: unzip
# END SourceDeps(oneline)
BuildRequires: /proc rpm-build-java
BuildRequires: jpackage-default
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
# %%version is ahead of its definition. Predefining for rpm 4.0 compatibility.
%define version 0.2.62
%global project     clojure
%global artifactId  core.specs.alpha
%global archivename %{artifactId}-%{artifactId}
%global full_version %{version}

Name:           clojure-core-specs-alpha
Epoch:          1
Version:        0.2.62
Release:        alt1_3jpp11
Summary:        Clojure library containing specs to describe Clojure core macros and functions

Group:          Development/Other
License:        EPL-1.0
URL:            https://github.com/%{project}/%{artifactId}
Source0:        https://github.com/%{project}/%{artifactId}/archive/refs/tags/v%{full_version}.zip

BuildArch:      noarch

BuildRequires:  maven-local
BuildRequires:  mvn(com.theoryinpractise:clojure-maven-plugin)
BuildRequires:  mvn(org.codehaus.mojo:build-helper-maven-plugin)
BuildRequires:  mvn(org.clojure:clojure)
BuildRequires:  mvn(org.clojure:spec.alpha)
Source44: import.info


%description 
Core.specs.alpha is a Clojure library containing specs to describe Clojure
core macros and functions.

%prep
%setup -q -n %{artifactId}-%{full_version}
# Remove unpackaged parent pom and add the required groupId
%pom_remove_parent pom.xml
%pom_xpath_inject pom:project "<groupId>org.clojure</groupId>"

# Hook clojure-maven-plugin to maven phases
%pom_xpath_inject pom:project/pom:properties "<project.build.sourceEncoding>UTF-8</project.build.sourceEncoding>"
%pom_xpath_inject pom:project/pom:properties "<clojure.source.dir>src/main/clojure</clojure.source.dir>"
%pom_xpath_inject pom:project/pom:properties "<clojure.testSource.dir>src/test/clojure</clojure.testSource.dir>"
 
%pom_xpath_inject "pom:execution[pom:id='clojure-compile']" "<goals><goal>compile</goal></goals>"
%pom_xpath_inject "pom:execution[pom:id='clojure-test']" "<goals><goal>test</goal></goals>"
# Copy clojure source files so they are included in the jar
%pom_add_plugin org.codehaus.mojo:build-helper-maven-plugin:1.12 . "
        <executions>
          <execution>
            <id>add-clojure-source-dirs</id>
            <phase>generate-sources</phase>
            <goals>
              <goal>add-source</goal>
              <goal>add-resource</goal>
            </goals>
            <configuration>
              <sources>
                <source>src/main/clojure</source>
              </sources>
              <resources>
                <resource>
                  <directory>src/main/clojure</directory>
                </resource>
              </resources>
            </configuration>
          </execution>
          <execution>
            <id>add-clojure-test-source-dirs</id>
            <phase>generate-sources</phase>
            <goals>
              <goal>add-test-source</goal>
              <goal>add-test-resource</goal>
            </goals>
            <configuration>
              <sources>
                <source>src/test/clojure</source>
              </sources>
              <resources>
                <resource>
                  <directory>src/test/clojure</directory>
                </resource>
              </resources>
            </configuration>
          </execution>
        </executions>"


%build
%mvn_build -f -- -Dmaven.compiler.source=1.8 -Dmaven.compiler.target=1.8 -Dmaven.javadoc.source=1.8 -Dmaven.compiler.release=8

%install
%mvn_install

%files -f .mfiles
%doc --no-dereference LICENSE
%doc epl-v10.html CHANGES.md README.md CONTRIBUTING.md

%changelog
* Mon Mar 20 2023 Igor Vlasenko <viy@altlinux.org> 1:0.2.62-alt1_3jpp11
- new version

* Fri Jun 11 2021 Igor Vlasenko <viy@altlinux.org> 1:0.2.56-alt1_1jpp11
- new version

* Fri Jun 04 2021 Igor Vlasenko <viy@altlinux.org> 1:0.2.44-alt1_4jpp11
- new version

* Fri Jun 04 2021 Igor Vlasenko <viy@altlinux.org> 1:0.2.44-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

