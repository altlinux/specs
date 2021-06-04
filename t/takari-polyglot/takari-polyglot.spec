Group: Development/Java
BuildRequires: /proc rpm-build-java
BuildRequires: jpackage-11-compat
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:          takari-polyglot
Version:       0.4.6
Release:       alt1_1jpp11
Summary:       Modules to enable Maven usage in other JVM languages
License:       EPL-1.0
URL:           https://github.com/takari/polyglot-maven
Source0:       https://github.com/takari/polyglot-maven/archive/polyglot-%{version}.tar.gz

BuildRequires:  maven-local
BuildRequires:  mvn(junit:junit)
BuildRequires:  mvn(org.apache.maven:maven-core)
BuildRequires:  mvn(org.apache.maven:maven-model)
BuildRequires:  mvn(org.apache.maven:maven-model-builder)
BuildRequires:  mvn(org.apache.maven:maven-parent:pom:)
BuildRequires:  mvn(org.apache.maven:maven-plugin-api)
BuildRequires:  mvn(org.apache.maven.plugins:maven-plugin-plugin)
BuildRequires:  mvn(org.apache.maven.plugin-tools:maven-plugin-annotations)
BuildRequires:  mvn(org.codehaus.plexus:plexus-component-annotations)
BuildRequires:  mvn(org.codehaus.plexus:plexus-component-metadata)
BuildRequires:  mvn(org.codehaus.plexus:plexus-utils)
BuildRequires:  mvn(org.eclipse.sisu:org.eclipse.sisu.plexus)
BuildRequires:  mvn(org.slf4j:slf4j-api)

BuildArch:     noarch

# Package was renamed upstream tesla -> takari F31
Provides:  tesla-polyglot = %{version}-%{release}
Obsoletes: tesla-polyglot < 0.4.4-3
Source44: import.info

%description
Polyglot for Maven is an experimental distribution of Maven
that allows the expression of a POM in something other than
XML. A couple of the dialects also have the capability to
write plugins inline: the Groovy, Ruby and Scala dialects
allow this.

%package atom
Group: Development/Java
Summary: Takari Polyglot :: Atom
# Package was renamed upstream tesla -> takari F31
Provides:  tesla-polyglot-atom = %{version}-%{release}
Obsoletes: tesla-polyglot-atom < 0.4.4-3

%description atom
Takari Polyglot :: Atom.

%package common
Group: Development/Java
Summary: Takari Polyglot :: Common
# Package was renamed upstream tesla -> takari F31
Provides:  tesla-polyglot-common = %{version}-%{release}
Obsoletes: tesla-polyglot-common < 0.4.4-3

# Obsoletes added for retired sub-packages in F31
Obsoletes: tesla-polyglot-groovy < 0.4.4-3
Obsoletes: tesla-polyglot-yaml < 0.4.4-3

%description common
Takari Polyglot :: Common.

%package xml
Group: Development/Java
Summary: Takari Polyglot :: XML
# Package was renamed upstream tesla -> takari F31
Provides:  tesla-polyglot-xml = %{version}-%{release}
Obsoletes: tesla-polyglot-xml < 0.4.4-3

%description xml
Takari Polyglot :: XML.

%package maven-plugin
Group: Development/Java
Summary: Takari Polyglot :: Maven Plugin
# Package was renamed upstream tesla -> takari F31
Provides:  tesla-polyglot-maven-plugin = %{version}-%{release}
Obsoletes: tesla-polyglot-maven-plugin < 0.4.4-3

%description maven-plugin
This package contains Takari Polyglot Maven Plugin.

%package translate-plugin
Group: Development/Java
Summary: Polyglot :: Translate Plugin
# Package was renamed upstream tesla -> takari F31
Provides:  tesla-polyglot-translate-plugin = %{version}-%{release}
Obsoletes: tesla-polyglot-translate-plugin < 0.4.4-3

%description translate-plugin
This package contains Polyglot Translate Plugin.

%package javadoc
Group: Development/Java
Summary: Javadoc for %{name}
# Package was renamed upstream tesla -> takari F31
Provides:  tesla-polyglot-javadoc = %{version}-%{release}
Obsoletes: tesla-polyglot-javadoc < 0.4.4-3
BuildArch: noarch

%description javadoc
This package contains javadoc for %{name}.

%prep
%setup -q -n polyglot-maven-polyglot-%{version}

find -name "*.class" -delete
find -name "*.jar" -delete

# Unecessary for RPM builds
%pom_remove_plugin ":maven-enforcer-plugin"

# Takari stack is unavailable, so build like an ordinary maven plugin project
%pom_remove_parent
%pom_xpath_remove "pom:packaging" polyglot-common polyglot-atom polyglot-xml
%pom_xpath_set "pom:packaging" "maven-plugin" polyglot-maven-plugin polyglot-translate-plugin
%pom_add_plugin org.apache.maven.plugins:maven-compiler-plugin:3.0 '
<configuration>
 <source>1.8</source>
 <target>1.8</target>
 <encoding>UTF-8</encoding>
</configuration>'
for p in maven-plugin translate-plugin; do
  %pom_add_plugin "org.apache.maven.plugins:maven-plugin-plugin" polyglot-${p} "
  <configuration>
    <skipErrorNoDescriptorsFound>true</skipErrorNoDescriptorsFound>
  </configuration>"
  %pom_xpath_inject "pom:dependency[pom:groupId = 'org.apache.maven']" "<version>3.3.1</version>" polyglot-${p}
done
%pom_xpath_inject "pom:project/pom:dependencies/pom:dependency[pom:groupId = 'org.apache.maven']" '<version>${mavenVersion}</version>'

# Unavailable build deps/tools
%pom_disable_module polyglot-clojure
%pom_disable_module polyglot-scala
%pom_remove_dep -r :polyglot-scala
%pom_disable_module polyglot-ruby
%pom_remove_dep -r :polyglot-ruby
%pom_disable_module polyglot-groovy
%pom_remove_dep -r :polyglot-groovy
%pom_disable_module polyglot-java
%pom_remove_dep -r :polyglot-java
%pom_disable_module polyglot-kotlin
%pom_remove_dep -r :polyglot-kotlin
%pom_disable_module polyglot-yaml
%pom_remove_dep -r :polyglot-yaml

# Test dep com.cedarsoftware:java-util:1.19.3 is missing from Fedora
sed -i '/DeepEquals/d' polyglot-xml/src/test/java/org/sonatype/maven/polyglot/xml/TestReaderComparedToDefault.java
%pom_remove_dep com.cedarsoftware:java-util polyglot-xml

# Back-compat aliases
%mvn_alias ':polyglot-{*}' io.tesla.polyglot:tesla-polyglot-@1

%build
%mvn_build -s -- -Dmaven.compiler.source=1.8 -Dmaven.compiler.target=1.8 -Dmaven.javadoc.source=1.8 -Dmaven.compiler.release=8 -Dproject.build.sourceEncoding=UTF-8

%install
%mvn_install

%files -f .mfiles-polyglot
%doc poms
%doc --no-dereference LICENSE.txt

%files atom -f .mfiles-polyglot-atom

%files common -f .mfiles-polyglot-common
%doc --no-dereference LICENSE.txt

%files xml -f .mfiles-polyglot-xml
%doc polyglot-xml/README.md

%files maven-plugin -f .mfiles-polyglot-maven-plugin

%files translate-plugin -f .mfiles-polyglot-translate-plugin

%files javadoc -f .mfiles-javadoc
%doc --no-dereference LICENSE.txt

%changelog
* Fri Jun 04 2021 Igor Vlasenko <viy@altlinux.org> 0.4.6-alt1_1jpp11
- new version

