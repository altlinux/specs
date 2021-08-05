Group: Development/Java
BuildRequires: /proc rpm-build-java
BuildRequires: jpackage-default
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:          nom-tam-fits
Version:       1.15.2
Release:       alt1_8jpp11
Summary:       Java library for reading and writing FITS files
License:       Public Domain
URL:           http://nom-tam-fits.github.io/nom-tam-fits/
Source0:       https://github.com/nom-tam-fits/nom-tam-fits/archive/%{name}-%{version}.tar.gz
Patch0:        0001-Skip-tests-if-we-cannot-download-images.patch

BuildRequires: maven-local
BuildRequires: mvn(junit:junit)
BuildRequires: mvn(org.apache.commons:commons-compress)
BuildRequires: mvn(org.codehaus.mojo:exec-maven-plugin)

# retired in Fedora:
# BuildRequires: mvn(org.openjdk.jmh:jmh-core)
# BuildRequires: mvn(org.openjdk.jmh:jmh-generator-annprocess)

BuildArch:     noarch
Source44: import.info

%description
FITS (Flexible Image Transport System) is the standard data format in
astronomy used for the transport, analysis, and archival storage of
scientific data sets.

This library provides efficient I/O for FITS images and binary
tables. All basic FITS formats and GZIP compressed files are
supported.

%package javadoc
Group: Development/Java
Summary:       Javadoc for %{name}
BuildArch: noarch

%description javadoc
This package contains javadoc for %{name}.

%prep
%setup -q -n %{name}-%{name}-%{version}
%patch0 -p1

rm -r src/main/fpack

# remove unnecessary dependency on parent POM
%pom_remove_parent

# com.github.stephenc.wagon:wagon-gitsite:0.5
%pom_xpath_remove pom:build/pom:extensions
# Disable classpath in MANIFEST file
%pom_xpath_set pom:addClasspath false

# Unwanted tasks
%pom_remove_plugin :jacoco-maven-plugin
%pom_remove_plugin :maven-assembly-plugin
%pom_remove_plugin :maven-deploy-plugin
%pom_remove_plugin :maven-gpg-plugin
%pom_remove_plugin :maven-javadoc-plugin
%pom_remove_plugin :maven-release-plugin
%pom_remove_plugin :maven-source-plugin

# Not available plugins
%pom_remove_plugin com.googlecode.maven-java-formatter-plugin:maven-java-formatter-plugin
%pom_remove_plugin org.codehaus.mojo:findbugs-maven-plugin
%pom_remove_plugin org.codehaus.mojo:license-maven-plugin
%pom_remove_plugin org.eluder.coveralls:coveralls-maven-plugin
%pom_remove_plugin org.tinyjee.dim:doxia-include-macro
%pom_remove_plugin :maven-pdf-plugin
# Use doxia-include-macro
%pom_remove_plugin :maven-site-plugin

# Not available test dep com.nanohttpd:nanohttpd-webserver:2.1.1
%pom_remove_dep :nanohttpd-webserver
# rm src/test/java/nom/tam/fits/test/CompressTest.java
# Error occurred during initialization of VM
# Could not reserve enough space for 2097152KB object heap
%pom_xpath_remove pom:argLine
# rm src/test/java/nom/tam/fits/compression/ReadWriteProvidedCompressedImageTest.java
# UnsupportedOperationException: could not get blackbox image from anywhere (use web connection)
# rm src/test/java/nom/tam/fits/test/UserProvidedTest.java

# https://bugzilla.redhat.com/show_bug.cgi?id=1736095
%pom_remove_plugin :maven-checkstyle-plugin

%pom_remove_plugin :maven-compiler-plugin
%pom_add_plugin org.apache.maven.plugins:maven-compiler-plugin  . "
<executions>
  <execution>
    <id>default-compile</id>
    <phase>compile</phase>
    <configuration>
      <source>1.8</source>
      <target>1.8</target>
    </configuration>
    <goals>
      <goal>compile</goal>
    </goals>
  </execution>
  <execution>
    <id>default-testCompile</id>
    <phase>test-compile</phase>
    <configuration>
      <testExcludes>
        <exclude>**/CompressTest.*</exclude>
        <exclude>**/ReadWriteProvidedCompressedImageTest.*</exclude>
        <exclude>**/UserProvidedTest.*</exclude>
      </testExcludes>
    </configuration>
    <goals>
      <goal>testCompile</goal>
    </goals>
  </execution>
</executions>"

# retired in Fedora
%pom_remove_dep org.openjdk.jmh:
rm src/test/java/nom/tam/manual/intergration/FitsBenchmark.java

# Retired in Fedora; not required for build
%pom_remove_dep com.google.code.findbugs:annotations
sed -i 's/.*SuppressFBWarnings.*//' $(fgrep -lr SuppressFBWarnings src/main/java)

%mvn_file :%{name} %{name} fits

%build
%mvn_build -- -Dmaven.compiler.source=1.8 -Dmaven.compiler.target=1.8 -Dmaven.javadoc.source=1.8 -Dmaven.compiler.release=8

%install
%mvn_install

%files -f .mfiles
%doc target/NOTE.* README.md
%doc --no-dereference src/license/publicdomain/license.txt

%files javadoc -f .mfiles-javadoc
%doc --no-dereference src/license/publicdomain/license.txt

%changelog
* Wed Aug 04 2021 Igor Vlasenko <viy@altlinux.org> 1.15.2-alt1_8jpp11
- update

* Fri Jun 04 2021 Igor Vlasenko <viy@altlinux.org> 1.15.2-alt1_6jpp11
- new version

