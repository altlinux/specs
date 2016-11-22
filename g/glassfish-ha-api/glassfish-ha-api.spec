Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
# END SourceDeps(oneline)
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
Name:          glassfish-ha-api
Version:       3.1.9
Release:       alt1_8jpp8
Summary:       High Availability APIs and SPI
License:       CDDL or GPLv2 with exceptions
URL:           http://glassfish.java.net/
# svn export https://svn.java.net/svn/glassfish~svn/tags/ha-api-3.1.9 glassfish-ha-api-3.1.9
# tar czf glassfish-ha-api-3.1.9-src-svn.tar.gz glassfish-ha-api-3.1.9
Source0:       %{name}-%{version}-src-svn.tar.gz
# wget -O glassfish-LICENSE.txt https://svn.java.net/svn/glassfish~svn/tags/legal-1.1/src/main/resources/META-INF/LICENSE.txt
# glassfish-ha-api package don't include the license file
Source1:       glassfish-LICENSE.txt

BuildRequires: maven-local
BuildRequires: mvn(junit:junit)
BuildRequires: mvn(net.java:jvnet-parent:pom:)
BuildRequires: mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires: mvn(org.glassfish.hk2:hk2-api)
BuildRequires: mvn(org.glassfish.hk2:osgiversion-maven-plugin)

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

# Remove support for hk2-jar
%pom_xpath_remove "pom:supportedProjectTypes"
%pom_remove_plugin org.glassfish.hk2:hk2-maven-plugin

%pom_xpath_set pom:packaging bundle
%pom_xpath_inject "pom:plugin[pom:artifactId ='maven-bundle-plugin']" "
<version>2.5.4</version>
<extensions>true</extensions>"

%pom_change_dep :hk2 :hk2-api

# META-INF/inhabitants/default contents ...not available without hk2
#class=org.glassfish.ha.store.impl.NoOpBackingStoreFactory,index=org.glassfish.ha.store.api.BackingStoreFactory:noop
#class=org.glassfish.ha.store.spi.ObjectInputStreamWithLoader

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
* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 3.1.9-alt1_8jpp8
- new fc release

* Sun Feb 07 2016 Igor Vlasenko <viy@altlinux.ru> 3.1.9-alt1_6jpp8
- java 8 mass update

* Wed Aug 27 2014 Igor Vlasenko <viy@altlinux.ru> 3.1.9-alt1_3jpp7
- new release

