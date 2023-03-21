# BEGIN SourceDeps(oneline):
BuildRequires: unzip
# END SourceDeps(oneline)
BuildRequires: /proc rpm-build-java
BuildRequires: jpackage-default
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
# %%version is ahead of its definition. Predefining for rpm 4.0 compatibility.
%define version 0.3.218
%global project     clojure
%global artifactId  spec.alpha
%global archivename %{artifactId}-%{artifactId}
%global full_version %{version}

Name:           clojure-spec-alpha
Epoch:          1
Version:        0.3.218
Release:        alt1_3jpp11
Summary:        Spec is a Clojure library to describe the structure of data and functions

Group:          Development/Other
License:        EPL-1.0
URL:            https://github.com/%{project}/%{artifactId}/
Source0:        https://github.com/%{project}/%{artifactId}/archive/refs/tags/v%{full_version}.zip


BuildArch:      noarch

BuildRequires:  maven-local
BuildRequires:  mvn(org.codehaus.mojo:exec-maven-plugin)
BuildRequires:  mvn(com.theoryinpractise:clojure-maven-plugin)
BuildRequires:  mvn(org.codehaus.mojo:build-helper-maven-plugin)
BuildRequires:  mvn(org.clojure:clojure)
Source44: import.info


%description 
Spec is a Clojure library to describe the structure of data and functions.
Specs can be used to validate data, conform (destructure) data, explain
invalid data, generate examples that conform to the specs, and automatically
use generative testing to test functions.

%prep
%setup -q -n %{artifactId}-%{version}
# Remove unpackaged parent pom and add the required groupId
%pom_remove_parent pom.xml
%pom_xpath_inject pom:project "<groupId>org.clojure</groupId>"
%pom_xpath_inject pom:project/pom:properties "<project.build.sourceEncoding>UTF-8</project.build.sourceEncoding>"
%pom_xpath_inject pom:project/pom:properties "<clojure.source.dir>src/main/clojure</clojure.source.dir>"
%pom_xpath_inject pom:project/pom:properties "<clojure.testSource.dir>src/test/clojure</clojure.testSource.dir>"
 
# Hook clojure-maven-plugin to maven phases
%pom_xpath_inject "pom:execution[pom:id='clojure-compile']" "<goals><goal>compile</goal></goals>"
%pom_xpath_inject "pom:execution[pom:id='clojure-test']" "<goals><goal>test</goal></goals>"

# Add builder helper to copy clojure source files so that
# compiler finds them.
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
%doc CHANGES.md README.md CONTRIBUTING.md
%changelog
* Mon Mar 20 2023 Igor Vlasenko <viy@altlinux.org> 1:0.3.218-alt1_3jpp11
- new version

* Fri Jun 11 2021 Igor Vlasenko <viy@altlinux.org> 1:0.2.194-alt1_2jpp11
- new version

* Fri Jun 04 2021 Igor Vlasenko <viy@altlinux.org> 1:0.2.187-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

