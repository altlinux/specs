Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires: swig unzip
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-compat
%define fedora 21
Name:             snakeyaml
Version:          1.11
Release:          alt1_7jpp7
Summary:          YAML parser and emitter for the Java programming language
License:          ASL 2.0
# http://code.google.com/p/snakeyaml
URL:              http://code.google.com/p/%{name}
# http://snakeyaml.googlecode.com/files/SnakeYAML-all-1.9.zip
Source0:          http://%{name}.googlecode.com/files/SnakeYAML-all-%{version}.zip

# Upstream has forked gdata-java and base64 and refuses [1] to
# consider replacing them by external dependencies.  Bundled libraries
# need to be removed and their use replaced by system libraries.
# See rhbz#875777 and http://code.google.com/p/snakeyaml/issues/detail?id=175
#
# Remove use of bundled Base64 implementation
Patch0:           0001-Replace-bundled-base64-implementation.patch
# We don't have gdata-java in Fedora any longer, use commons-codec instead
Patch1:           0002-Replace-bundled-gdata-java-client-classes-with-commo.patch

BuildArch:        noarch

BuildRequires:    maven-local
BuildRequires:    cobertura
BuildRequires:    joda-time
BuildRequires:    gnu-getopt
BuildRequires:    base64coder
BuildRequires:    apache-commons-codec
%{?fedora:BuildRequires: springframework}
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


%package javadoc
Group: Development/Java
Summary:          API documentation for %{name}
BuildArch: noarch

%description javadoc
This package contains %{summary}.

%prep
%setup -q -n %{name}
%patch0 -p1
%patch1 -p1

%mvn_file : %{name}

%pom_remove_plugin org.codehaus.mojo:cobertura-maven-plugin
%pom_add_dep net.sourceforge.cobertura:cobertura:any:test
sed -i "/<artifactId>spring</s/spring/&-core/" pom.xml
rm -f src/test/java/examples/SpringTest.java

# Replacement for bundled gdata-java-client
%pom_add_dep commons-codec:commons-codec

# remove bundled stuff
rm -rf target
rm -rf src/main/java/org/yaml/snakeyaml/external

# convert CR+LF to LF
sed -i 's/\r//g' LICENSE.txt

%build
%mvn_build %{!?fedora:-f}

%install
%mvn_install

%files -f .mfiles
%doc LICENSE.txt

%files javadoc -f .mfiles-javadoc
%doc LICENSE.txt

%changelog
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

