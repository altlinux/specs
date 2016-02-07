Group: Development/Java
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
Name:          glassfish-ha-api
Version:       3.1.9
Release:       alt1_6jpp8
Summary:       High Availability APIs and SPI
License:       CDDL or GPLv2 with exceptions
URL:           http://glassfish.java.net/
# svn export https://svn.java.net/svn/glassfish~svn/tags/ha-api-3.1.9 glassfish-ha-api-3.1.9
# tar czf glassfish-ha-api-3.1.9-src-svn.tar.gz glassfish-ha-api-3.1.9
Source0:       %{name}-%{version}-src-svn.tar.gz
# wget -O glassfish-LICENSE.txt https://svn.java.net/svn/glassfish~svn/tags/legal-1.1/src/main/resources/META-INF/LICENSE.txt
# glassfish-ha-api package don't include the license file
Source1:       glassfish-LICENSE.txt

BuildRequires: jvnet-parent
BuildRequires: glassfish-hk2-api
# test dep
BuildRequires: junit

BuildRequires: glassfish-hk2-maven-plugins
BuildRequires: maven-local
BuildRequires: maven-enforcer-plugin
BuildRequires: maven-install-plugin
BuildRequires: maven-plugin-bundle

BuildArch:     noarch
Source44: import.info

%description
GlassFish High Availability APIs and SPI.

%package javadoc
Group: Development/Java
Summary:       Javadoc for %{name}
BuildArch: noarch

%description javadoc
This package contains javadoc for %{name}.

%prep
%setup -q -n %{name}-%{version}

sed -i "s|<packaging>hk2-jar</packaging>|<packaging>jar</packaging>|" pom.xml

sed -i "s|<artifactId>hk2</artifactId>|<artifactId>hk2-api</artifactId>|" pom.xml

%pom_xpath_remove "pom:build/pom:plugins/pom:plugin[pom:artifactId ='maven-bundle-plugin']/pom:configuration"

%pom_remove_plugin org.glassfish.hk2:hk2-maven-plugin
%pom_add_plugin org.apache.maven.plugins:maven-jar-plugin . '
<configuration>
  <archive>
    <manifestFile>${project.build.outputDirectory}/META-INF/MANIFEST.MF</manifestFile>
  </archive>
</configuration>'

sed -i "s|<artifactId>hk2</artifactId>|<artifactId>hk2-api</artifactId>|" pom.xml

# META-INF/inhabitants/default contents ...not available without hk2
#class=org.glassfish.ha.store.impl.NoOpBackingStoreFactory,index=org.glassfish.ha.store.api.BackingStoreFactory:noop
#class=org.glassfish.ha.store.spi.ObjectInputStreamWithLoader

# in hk2 some modules require unavailable libraries. and i cant build ha-api as hk2-jar
#%%pom_xpath_remove "pom:project/pom:packaging"
#%%pom_xpath_inject "pom:project" "<packaging>jar</packaging>"

cp -p %{SOURCE1} LICENSE.txt
sed -i 's/\r//' LICENSE.txt

%mvn_file :ha-api %{name}

%build

%mvn_build

%install
%mvn_install

%files -f .mfiles
%doc LICENSE.txt

%files javadoc -f .mfiles-javadoc
%doc LICENSE.txt

%changelog
* Sun Feb 07 2016 Igor Vlasenko <viy@altlinux.ru> 3.1.9-alt1_6jpp8
- java 8 mass update

* Wed Aug 27 2014 Igor Vlasenko <viy@altlinux.ru> 3.1.9-alt1_3jpp7
- new release

