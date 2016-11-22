Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
# END SourceDeps(oneline)
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
Name:          grizzly-npn
Version:       1.2
Release:       alt1_4jpp8
Summary:       Grizzly Next Protocol Negotiation API
License:       CDDL or GPLv2 with exceptions
URL:           https://grizzly.java.net/spdy.html
# git clone git://java.net/grizzly~npn
# (cd grizzly~npn && git archive --format=tar --prefix=grizzly-npn-1.2/ 1_2 | xz > ../grizzly-npn-1.2.tar.xz)
Source0:       %{name}-%{version}.tar.xz
# https://java.net/jira/browse/GRIZZLY-1770
# wget -O glassfish-LICENSE.txt https://svn.java.net/svn/glassfish~svn/tags/legal-1.1/src/main/resources/META-INF/LICENSE.txt
# grizzly-npn-api package don't include the license file
Source1:       glassfish-LICENSE.txt

BuildRequires: maven-local
BuildRequires: mvn(net.java:jvnet-parent:pom:)
BuildRequires: mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires: mvn(org.apache.maven.plugins:maven-enforcer-plugin)
BuildRequires: mvn(org.osgi:org.osgi.compendium)
BuildRequires: mvn(org.osgi:org.osgi.core)

BuildArch:     noarch
Source44: import.info

%description
A pure Java implementation of the
Next Protocol Negotiation TLS Extension
for OpenJDK 7 or greater.

NPN allows the application layer to
negotiate which protocol to use over the
secure connection.

%package bootstrap
Group: Development/Java
Summary:       Grizzly NPN Bootstrap

%description bootstrap
This package contains the JAR that
will be placed on the bootclasspath
in order for NPN to work.

%package osgi
Group: Development/Java
Summary:       Grizzly NPN OSGi

%description osgi
This empty module allows the bootclasspath classes in
org.glassfish.grizzly.npn to be available via the
OSGi classloading mechanisms.

Using GlassFish as an example:
- grizzly-npn-bootstrap.jar goes into the
  domain's bootclasspath (-Xbootclasspath/p:[PATH TO THE JAR])
- grizzly-npn-osgi and grizzly-spdy JARs go into the
  [PATH TO THE GlassFish 4 HOME]/modules directory.
 
%package javadoc
Group: Development/Java
Summary:       Javadoc for %{name}
BuildArch: noarch

%description javadoc
This package contains javadoc for %{name}.

%prep
%setup -q

cp -p %{SOURCE1} LICENSE.txt

sed -i "s,59 Temple Place,51 Franklin Street,;s,Suite 330,Fifth Floor,;s,02111-1307,02110-1301,"  $(find -name "*.java") LICENSE.txt

sed -i 's/\r//' LICENSE.txt

mkdir -p osgi/target/classes/META-INF
touch osgi/target/classes/META-INF/MANIFEST.MF

# use jvm jsse
rm -r bootstrap/src/main/java/sun/security/ssl/Alerts.java \
 bootstrap/src/main/java/sun/security/ssl/ClientHandshaker.java \
 bootstrap/src/main/java/sun/security/ssl/ExtensionType.java \
 bootstrap/src/main/java/sun/security/ssl/Handshaker.java \
 bootstrap/src/main/java/sun/security/ssl/HandshakeMessage.java \
 bootstrap/src/main/java/sun/security/ssl/HelloExtensions.java \
 bootstrap/src/main/java/sun/security/ssl/ServerHandshaker.java \
 bootstrap/src/main/java/sun/security/ssl/SSLEngineImpl.java

%pom_xpath_remove "pom:plugin[pom:artifactId = 'maven-bundle-plugin']/pom:configuration/pom:instructions/pom:Export-Package" bootstrap
%pom_xpath_inject "pom:plugin[pom:artifactId = 'maven-bundle-plugin']/pom:configuration/pom:instructions" "
<Export-Package>
    sun.security.ssl
</Export-Package>
<Import-Package>
    org.glassfish.grizzly.npn
</Import-Package>" bootstrap

%mvn_package :%{name} %{name}
%mvn_package :%{name}-api %{name}

%build

%mvn_build -s

%install
%mvn_install

%files -f .mfiles-%{name}
%doc LICENSE.txt

%files bootstrap -f .mfiles-%{name}-bootstrap
%doc LICENSE.txt

%files osgi -f .mfiles-%{name}-osgi
%doc LICENSE.txt

%files javadoc -f .mfiles-javadoc
%doc LICENSE.txt

%changelog
* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 1.2-alt1_4jpp8
- new fc release

* Wed Feb 10 2016 Igor Vlasenko <viy@altlinux.ru> 1.2-alt1_3jpp8
- java8 mass update

* Mon Feb 08 2016 Igor Vlasenko <viy@altlinux.ru> 1.2-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

