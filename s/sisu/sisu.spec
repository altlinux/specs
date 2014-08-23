Epoch: 0
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-java
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-compat


Name:           sisu
Version:        2.3.0
Release:        alt1_8jpp7
Summary:        Sonatype dependency injection framework
Group:          Development/Java
License:        ASL 2.0 and EPL and MIT
URL:            http://github.com/sonatype/sisu

# git clone git://github.com/sonatype/%{name} ${name}-%{version}
# cd %{name}-%{version}
# git checkout %{name}-%{version}
# find ./ -name "*.jar" -delete
# find ./ -name "*.class" -delete
# cd ..
# tar czvf %{name}-%{version}.tar.gz %{name}-%{version}
Source0:        %{name}-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  jpackage-utils
BuildRequires:  maven-local >= 0.11.1

BuildRequires:  aopalliance
BuildRequires:  atinject
BuildRequires:  cdi-api
BuildRequires:  felix-framework
BuildRequires:  forge-parent
BuildRequires:  geronimo-specs
BuildRequires:  google-guice
BuildRequires:  junit
BuildRequires:  plexus-classworlds
BuildRequires:  plexus-containers-component-annotations
BuildRequires:  plexus-utils
BuildRequires:  geronimo-parent-poms
BuildRequires:  sisu
BuildRequires:  testng
BuildRequires:  weld-parent

Requires:       %{name}-bean = %{?epoch:%epoch:}%{version}-%{release}
Requires:       %{name}-bean-binders = %{?epoch:%epoch:}%{version}-%{release}
Requires:       %{name}-bean-containers = %{?epoch:%epoch:}%{version}-%{release}
Requires:       %{name}-bean-converters = %{?epoch:%epoch:}%{version}-%{release}
Requires:       %{name}-bean-inject = %{?epoch:%epoch:}%{version}-%{release}
Requires:       %{name}-bean-locators = %{?epoch:%epoch:}%{version}-%{release}
Requires:       %{name}-bean-reflect = %{?epoch:%epoch:}%{version}-%{release}
Requires:       %{name}-bean-scanners = %{?epoch:%epoch:}%{version}-%{release}
Requires:       %{name}-containers = %{?epoch:%epoch:}%{version}-%{release}
Requires:       %{name}-inject = %{?epoch:%epoch:}%{version}-%{release}
Requires:       %{name}-inject-bean = %{?epoch:%epoch:}%{version}-%{release}
Requires:       %{name}-inject-plexus = %{?epoch:%epoch:}%{version}-%{release}
Requires:       %{name}-osgi-registry = %{?epoch:%epoch:}%{version}-%{release}
Requires:       %{name}-parent = %{?epoch:%epoch:}%{version}-%{release}
Requires:       %{name}-plexus = %{?epoch:%epoch:}%{version}-%{release}
Requires:       %{name}-plexus-binders = %{?epoch:%epoch:}%{version}-%{release}
Requires:       %{name}-plexus-converters = %{?epoch:%epoch:}%{version}-%{release}
Requires:       %{name}-plexus-lifecycles = %{?epoch:%epoch:}%{version}-%{release}
Requires:       %{name}-plexus-locators = %{?epoch:%epoch:}%{version}-%{release}
Requires:       %{name}-plexus-metadata = %{?epoch:%epoch:}%{version}-%{release}
Requires:       %{name}-plexus-scanners = %{?epoch:%epoch:}%{version}-%{release}
Requires:       %{name}-plexus-shim = %{?epoch:%epoch:}%{version}-%{release}
Requires:       %{name}-registries = %{?epoch:%epoch:}%{version}-%{release}
Requires:       %{name}-spi-registry = %{?epoch:%epoch:}%{version}-%{release}
Source44: import.info
%filter_from_requires /^osgi\\(org\\.sonatype\\.sisu\\.guava\\)$/d

%description
Java dependency injection framework with backward support for plexus and bean
style dependency injection.

%package        parent
Group: Development/Java
Summary:        Sisu parent POM

%description    parent
This package contains %{summary}.

%package        containers
Group: Development/Java
Summary:        Sisu containers POM

%description    containers
This package contains %{summary}.

%package        bean
Group: Development/Java
Summary:        Sisu bean POM

%description    bean
This package contains %{summary}.

%package        plexus
Group: Development/Java
Summary:        Sisu Plexus POM

%description    plexus
This package contains %{summary}.

%package        registries
Group: Development/Java
Summary:        Sisu registries POM

%description    registries
This package contains %{summary}.

%package        inject
Group: Development/Java
Summary:        Sisu inject POM

%description    inject
This package contains %{summary}.

%package        bean-binders
Group: Development/Java
Summary:        Guice Bean Binders module for Sisu

%description    bean-binders
This package contains %{summary}.

%package        bean-containers
Group: Development/Java
Summary:        Guice Bean Containers module for Sisu

%description    bean-containers
This package contains %{summary}.

%package        bean-converters
Group: Development/Java
Summary:        Guice Bean Converters module for Sisu

%description    bean-converters
This package contains %{summary}.

%package        bean-inject
Group: Development/Java
Summary:        Guice Bean Inject module for Sisu

%description    bean-inject
This package contains %{summary}.

%package        bean-locators
Group: Development/Java
Summary:        Guice Bean Locators module for Sisu

%description    bean-locators
This package contains %{summary}.

%package        bean-reflect
Group: Development/Java
Summary:        Guice Bean Reflect module for Sisu

%description    bean-reflect
This package contains %{summary}.

%package        bean-scanners
Group: Development/Java
Summary:        Guice Bean Scanners module for Sisu

%description    bean-scanners
This package contains %{summary}.

%package        plexus-binders
Group: Development/Java
Summary:        Guice Plexus Binders module for Sisu

%description    plexus-binders
This package contains %{summary}.

%package        plexus-converters
Group: Development/Java
Summary:        Guice Plexus Converters module for Sisu

%description    plexus-converters
This package contains %{summary}.

%package        plexus-lifecycles
Group: Development/Java
Summary:        Guice Plexus Lifecycles module for Sisu

%description    plexus-lifecycles
This package contains %{summary}.

%package        plexus-locators
Group: Development/Java
Summary:        Guice Plexus Locators module for Sisu

%description    plexus-locators
This package contains %{summary}.

%package        plexus-metadata
Group: Development/Java
Summary:        Guice Plexus Metadata module for Sisu

%description    plexus-metadata
This package contains %{summary}.

%package        plexus-scanners
Group: Development/Java
Summary:        Guice Plexus Scanners module for Sisu

%description    plexus-scanners
This package contains %{summary}.

%package        plexus-shim
Group: Development/Java
Summary:        Guice Plexus Shim module for Sisu

%description    plexus-shim
This package contains %{summary}.

%package        inject-bean
Group: Development/Java
Summary:        Bean Inject bundle for Sisu

%description    inject-bean
This package contains %{summary}.

%package        inject-plexus
Group: Development/Java
Summary:        Plexus Inject bundle for Sisu

%description    inject-plexus
This package contains %{summary}.

%package        osgi-registry
Group: Development/Java
Summary:        OSGi registry for Sisu

%description    osgi-registry
This package contains %{summary}.

%package        spi-registry
Group: Development/Java
Summary:        SPI registry for Sisu

%description    spi-registry
This package contains %{summary}.

%package        javadoc
Summary:        API documentation for Sisu
Group:          Development/Java
BuildArch: noarch

%description    javadoc
This package contains %{summary}.

%prep
%setup -q

# Animal sniffer is only causing problems
%pom_remove_plugin :animal-sniffer-maven-plugin

# Don't generate auto-requires for optional dependencies
sed -i "s|<optional>true</optional>|<scope>provided</scope>|" \
    $(grep -l "<optional>" $(find sisu-inject -name pom.xml))

# Remove bundled objectweb-asm library
rm -rf ./sisu-inject/containers/guice-bean/guice-bean-scanners/src/main/java/org/sonatype/guice/bean/scanners/asm
%pom_add_dep asm:asm sisu-inject/containers/guice-bean/guice-bean-scanners
# sisu-inject-bean bundles classes from other modules, so it also needs asm
%pom_add_dep asm:asm sisu-inject/containers/guice-bean/sisu-inject-bean

# Fix namespace of imported asm classes
sed -i 's/org.sonatype.guice.bean.scanners.asm/org.objectweb.asm/g' \
    sisu-inject/containers/guice-plexus/guice-plexus-scanners/src/{main,test}/java/org/sonatype/guice/plexus/scanners/*.java \
    sisu-inject/containers/guice-bean/guice-bean-scanners/src/{main,test}/java/org/sonatype/guice/bean/scanners/*.java \

# Fix plexus bundling
sed -i -e '/provide these APIs as a convenience/,+2d' \
    sisu-inject/containers/guice-bean/sisu-inject-bean/pom.xml
%pom_add_dep javax.inject:javax.inject sisu-inject/containers/guice-bean/sisu-inject-bean
%pom_add_dep javax.enterprise:cdi-api sisu-inject/containers/guice-bean/sisu-inject-bean

# add backward compatible location
cp sisu-inject/containers/guice-plexus/guice-plexus-lifecycles/src/main/java/org/sonatype/guice/plexus/lifecycles/*java \
   sisu-inject/containers/guice-plexus/guice-plexus-lifecycles/src/main/java/org/codehaus/plexus/
sed -i 's/org.sonatype.guice.plexus.lifecycles/org.codehaus.plexus/' \
       sisu-inject/containers/guice-plexus/guice-plexus-lifecycles/src/main/java/org/codehaus/plexus/*java

# Dependency not available
%pom_disable_module sisu-eclipse-registry sisu-inject/registries

%pom_remove_plugin :maven-surefire-plugin sisu-inject/containers/guice-bean/guice-bean-containers
%pom_remove_plugin :maven-clean-plugin sisu-inject/containers/guice-plexus/guice-plexus-binders
%pom_remove_plugin :maven-dependency-plugin sisu-inject/containers/guice-plexus/guice-plexus-binders

%build
%mvn_package ":{sisu,guice}-{*}" @2
%mvn_build -s -f

%install
%mvn_install

%files
%doc LICENSE-ASL.txt LICENSE-EPL.txt
%dir %{_javadir}/%{name}

%files parent            -f .mfiles-parent
%files containers        -f .mfiles-containers
%files bean              -f .mfiles-bean
%files plexus            -f .mfiles-plexus
%files registries        -f .mfiles-registries
%files inject            -f .mfiles-inject
%files bean-binders      -f .mfiles-bean-binders
%files bean-containers   -f .mfiles-bean-containers
%files bean-converters   -f .mfiles-bean-converters
%files bean-inject       -f .mfiles-bean-inject
%files bean-locators     -f .mfiles-bean-locators
%files bean-reflect      -f .mfiles-bean-reflect
%files bean-scanners     -f .mfiles-bean-scanners
%files plexus-binders    -f .mfiles-plexus-binders
%files plexus-converters -f .mfiles-plexus-converters
%files plexus-lifecycles -f .mfiles-plexus-lifecycles
%files plexus-locators   -f .mfiles-plexus-locators
%files plexus-metadata   -f .mfiles-plexus-metadata
%files plexus-scanners   -f .mfiles-plexus-scanners
%files plexus-shim       -f .mfiles-plexus-shim
%files inject-bean       -f .mfiles-inject-bean
%files inject-plexus     -f .mfiles-inject-plexus
%files osgi-registry     -f .mfiles-osgi-registry
%files spi-registry      -f .mfiles-spi-registry

%files javadoc -f .mfiles-javadoc
%doc LICENSE-ASL.txt LICENSE-EPL.txt


%changelog
* Sat Aug 23 2014 Igor Vlasenko <viy@altlinux.ru> 0:2.3.0-alt1_8jpp7
- new version

* Fri Aug 22 2014 Igor Vlasenko <viy@altlinux.ru> 0:2.2.3-alt4_6jpp7
- added BR: for xmvn

* Thu Aug 07 2014 Igor Vlasenko <viy@altlinux.ru> 0:2.2.3-alt3_6jpp7
- rebuild with maven-local

* Mon Jul 14 2014 Igor Vlasenko <viy@altlinux.ru> 0:2.2.3-alt2_6jpp7
- NMU rebuild to move poms and fragments

* Fri Aug 24 2012 Igor Vlasenko <viy@altlinux.ru> 0:2.2.3-alt1_6jpp7
- complete build

* Wed Mar 07 2012 Igor Vlasenko <viy@altlinux.ru> 0:2.2.3-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

