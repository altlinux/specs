Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires: rpm-build-java
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%global debug_package %nil

%global commit f7d15412f9a95353ecfbc0a72211568fd2efe21a 
%global shortcommit %(c=%{commit}; echo ${c:0:7})

Name:          datanucleus-core
Version:       3.2.15
Release:       alt1_8jpp8
Summary:       DataNucleus Core
License:       ASL 2.0
URL:           http://www.datanucleus.org/%{name}
Source:        https://github.com/datanucleus/%{name}/archive/%{commit}/%{name}-%{commit}.tar.gz

BuildRequires: java-devel
BuildRequires: mvn(javax.time:time-api)
BuildRequires: mvn(javax.jdo:jdo-api)
BuildRequires: mvn(javax.transaction:jta)
BuildRequires: mvn(log4j:log4j)
BuildRequires: mvn(mx4j:mx4j)
BuildRequires: mvn(mx4j:mx4j-tools)
BuildRequires: mvn(org.apache.ant:ant)
BuildRequires: mvn(org.apache.geronimo.specs:geronimo-validation_1.0_spec)
BuildRequires: mvn(org.ow2.asm:asm)
BuildRequires: mvn(org.eclipse.osgi:org.eclipse.osgi)

# Test deps
BuildRequires: mvn(junit:junit)
BuildRequires: maven-local
BuildRequires: maven-install-plugin

# use Fedora base64 pkg
BuildRequires: mvn(biz.source_code:base64coder)

BuildRequires: datanucleus-maven-parent

BuildArch:     noarch
Source44: import.info

%description
DataNucleus Core provides the primary components
of a heterogeneous Java persistence solution. 
It supports persistence API's being layered on
top of the core functionality.

%package javadoc
Group: Development/Java
Summary:       Javadoc for %{name}
BuildArch: noarch

%description javadoc
This package contains javadoc for %{name}.

%prep
%setup -q -n %{name}-%{commit}

# just completely dump eclipse plugin support
# too dependent on system scope jars
rm src/java/org/datanucleus/plugin/EclipsePluginRegistry.java
%pom_remove_dep org.eclipse.core:org.eclipse.core.runtime.compatibility.auth
%pom_remove_dep org.eclipse.equinox:org.eclipse.equinox.registry
%pom_remove_dep org.eclipse.equinox:org.eclipse.equinox.common
%pom_remove_dep org.eclipse.equinox:org.eclipse.equinox.preferences
%pom_remove_dep org.eclipse.core:org.eclipse.core.runtime
%pom_remove_dep org.eclipse.core:org.eclipse.core.contenttype
%pom_remove_dep org.eclipse.core:org.eclipse.core.jobs

# Use system jvm apis
%pom_remove_dep javax.management:jmx
# Use system asm4 apis
rm -r src/java/org/datanucleus/asm
%pom_add_dep org.ow2.asm:asm
sed -i "s|org.datanucleus.asm|org.objectweb.asm|" $(find . -name "*.java")

%pom_xpath_inject "pom:project/pom:build/pom:plugins/pom:plugin[pom:artifactId = 'maven-bundle-plugin' ]/pom:configuration/pom:instructions" '
<Require-Bundle>org.eclipse.equinox.registry;resolution:=optional,org.eclipse.core.runtime;resolution:=optional</Require-Bundle>
<Bundle-Name>${project.name}</Bundle-Name>
<Bundle-Vendor>DataNucleus</Bundle-Vendor>
<Premain-Class>org.datanucleus.enhancer.DataNucleusClassFileTransformer</Premain-Class>
<Export-Package>org.datanucleus*;version="${project.version}"</Export-Package>'
%pom_xpath_inject "pom:project/pom:build/pom:plugins/pom:plugin[pom:artifactId = 'maven-bundle-plugin' ]" "
<executions>
  <execution>
    <id>bundle-manifest</id>
    <phase>process-classes</phase>
    <goals>
      <goal>manifest</goal>
    </goals>
  </execution>
</executions>"

# cache-api unavailable and used for an optional L2 pluggable cache
%pom_remove_dep javax.cache:cache-api
find -name 'JavaxCache*.java' -delete
sed -i".orig" "/javax.cache/d" plugin.xml

# swap out embedded base64 codec
find -name 'Base64.java' -delete
sed -i "s|org.datanucleus.util.Base64|biz.source_code.base64Coder.Base64Coder|" $(find . -name "*.java")
sed -i "s|\.Base64;|\.Base64Coder;|" $(find . -name "*.java")
sed -i "s|Base64\.|Base64Coder\.|" $(find . -name "*.java")
%pom_add_dep biz.source_code:base64coder

sed -i 's/\r//' META-INF/LICENSE.txt META-INF/NOTICE.txt META-INF/README.txt
cp -p META-INF/LICENSE.txt .
cp -p META-INF/NOTICE.txt .
cp -p META-INF/README.txt .

%build
%mvn_build -f

%install
%mvn_install

%files -f .mfiles
%doc LICENSE.txt NOTICE.txt

%files javadoc -f .mfiles-javadoc
%doc LICENSE.txt NOTICE.txt

%changelog
* Mon Feb 04 2019 Igor Vlasenko <viy@altlinux.ru> 3.2.15-alt1_8jpp8
- java update

* Fri May 25 2018 Igor Vlasenko <viy@altlinux.ru> 3.2.15-alt1_7jpp8
- new version

