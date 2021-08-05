Group: Development/Java
BuildRequires: /proc rpm-build-java
BuildRequires: jpackage-default
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%global vertag 29e2699b80fc

Name:           snakeyaml
Summary:        YAML parser and emitter for Java
Version:        1.27
Release:        alt1_4jpp11
License:        ASL 2.0

URL:            https://bitbucket.org/asomov/%{name}
Source0:        %{url}/get/%{name}-%{version}.tar.gz

# Upstream has forked gdata-java and base64 and refuses [1] to
# consider replacing them by external dependencies.  Bundled libraries
# need to be removed and their use replaced by system libraries.
# See rhbz#875777 and http://code.google.com/p/snakeyaml/issues/detail?id=175
#
# Replace use of bundled Base64 implementation with java.util.Base64
Patch0:         0001-replace-bundled-base64coder-with-java.util.Base64.patch
# We don't have gdata-java in Fedora any longer, use commons-codec instead
Patch1:         0002-Replace-bundled-gdata-java-client-classes-with-commo.patch
Patch2:         reader_bom_test_fix.patch

BuildArch:      noarch

BuildRequires:  maven-local
BuildRequires:  mvn(commons-codec:commons-codec)
BuildRequires:  mvn(commons-io:commons-io)
BuildRequires:  mvn(junit:junit)
BuildRequires:  mvn(org.apache.commons:commons-lang3)
BuildRequires:  mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-source-plugin)
BuildRequires:  mvn(org.apache.velocity:velocity)
Source44: import.info

%description
SnakeYAML features:
    * a complete YAML 1.1 parser. In particular,
      SnakeYAML can parse all examples from the specification.
    * Unicode support including UTF-8/UTF-16 input/output.
    * high-level API for serializing and deserializing
      native Java objects.
    * support for all types from the YAML types repository.
    * relatively sensible error messages.


%package        javadoc
Group: Development/Java
Summary:        API documentation for %{name}
BuildArch: noarch

%description    javadoc
This package contains %{summary}.


%prep
%setup -q -n asomov-%{name}-%{vertag}
%patch0 -p1
%patch1 -p1
%patch2 -p2


%mvn_file : %{name}

%pom_remove_plugin :cobertura-maven-plugin
%pom_remove_plugin :maven-changes-plugin
%pom_remove_plugin :maven-enforcer-plugin
%pom_remove_plugin :maven-license-plugin
%pom_remove_plugin :maven-javadoc-plugin
%pom_remove_plugin :maven-site-plugin
%pom_remove_plugin :nexus-staging-maven-plugin

# Replacement for bundled gdata-java-client
%pom_add_dep commons-codec:commons-codec

# Unnecessary test-time only dependency
%pom_remove_dep joda-time:joda-time
rm -rf src/test/java/examples/jodatime

# fails in rpmbuild only due to different locale
rm src/test/java/org/yaml/snakeyaml/issues/issue67/NonAsciiCharsInClassNameTest.java
# fails after unbundling
rm src/test/java/org/yaml/snakeyaml/issues/issue318/ContextClassLoaderTest.java

# Problematic test resources for maven-resources-plugin 3.2
rm src/test/resources/issues/issue99.jpeg
rm src/test/resources/reader/unicode-16be.txt
rm src/test/resources/reader/unicode-16le.txt
rm src/test/resources/pyyaml/spec-05-01-utf16be.data
rm src/test/resources/pyyaml/spec-05-01-utf16le.data
rm src/test/resources/pyyaml/spec-05-02-utf16le.data
rm src/test/resources/pyyaml/odd-utf16.stream-error
rm src/test/resources/pyyaml/invalid-character.loader-error
rm src/test/resources/pyyaml/invalid-character.stream-error
rm src/test/resources/pyyaml/invalid-utf8-byte.loader-error
rm src/test/resources/pyyaml/invalid-utf8-byte.stream-error
rm src/test/resources/pyyaml/empty-document-bug.data
rm src/test/resources/pyyaml/spec-05-02-utf16be.data
# Test using the jpeg data removed above
rm src/test/java/org/yaml/snakeyaml/issues/issue99/YamlBase64Test.java

# convert CR+LF to LF
sed -i 's/\r//g' LICENSE.txt


%build
%mvn_build -- -Dmaven.compiler.source=1.8 -Dmaven.compiler.target=1.8 -Dmaven.javadoc.source=1.8 -Dmaven.compiler.release=8


%install
%mvn_install


%files -f .mfiles
%doc LICENSE.txt

%files javadoc -f .mfiles-javadoc
%doc LICENSE.txt


%changelog
* Wed Aug 04 2021 Igor Vlasenko <viy@altlinux.org> 1.27-alt1_4jpp11
- update

* Thu Jun 10 2021 Igor Vlasenko <viy@altlinux.org> 1.27-alt1_2jpp11
- new version

* Tue Jun 01 2021 Igor Vlasenko <viy@altlinux.org> 1.26-alt1_4jpp11
- new version

* Thu Apr 29 2021 Igor Vlasenko <viy@altlinux.org> 1.25-alt1_4jpp11
- update

* Fri Oct 09 2020 Igor Vlasenko <viy@altlinux.ru> 1.25-alt1_1jpp8
- new version

* Sun May 26 2019 Igor Vlasenko <viy@altlinux.ru> 1.17-alt1_7jpp8
- new version

* Thu Apr 19 2018 Igor Vlasenko <viy@altlinux.ru> 1.17-alt1_5jpp8
- java update

* Thu Nov 09 2017 Igor Vlasenko <viy@altlinux.ru> 1.17-alt1_4jpp8
- fc27 update

* Wed Oct 18 2017 Igor Vlasenko <viy@altlinux.ru> 1.17-alt1_3jpp8
- new jpp release

* Tue Dec 06 2016 Igor Vlasenko <viy@altlinux.ru> 1.16-alt1_2jpp8
- new version

* Sun Feb 07 2016 Igor Vlasenko <viy@altlinux.ru> 1.13-alt1_9jpp8
- unbootsrap build

* Thu Jan 28 2016 Igor Vlasenko <viy@altlinux.ru> 1.13-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 1.11-alt1_7jpp7
- new release

* Fri Aug 01 2014 Igor Vlasenko <viy@altlinux.ru> 1.11-alt1_4jpp7
- new version

* Sun Jul 27 2014 Igor Vlasenko <viy@altlinux.ru> 1.9-alt3_3jpp7
- fixed build

* Thu Feb 14 2013 Igor Vlasenko <viy@altlinux.ru> 1.9-alt2_3jpp7
- fixed maven1 dependency

* Thu Feb 07 2013 Igor Vlasenko <viy@altlinux.ru> 1.9-alt1_3jpp7
- fc update

* Mon Oct 01 2012 Igor Vlasenko <viy@altlinux.ru> 1.9-alt1_2jpp7
- new fc release

* Sat Apr 07 2012 Igor Vlasenko <viy@altlinux.ru> 1.9-alt1_1jpp7
- new version

