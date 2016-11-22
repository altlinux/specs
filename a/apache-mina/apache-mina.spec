Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
# END SourceDeps(oneline)
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
Name:           apache-mina
Version:        2.0.9
Release:        alt1_4jpp8
Summary:        Apache MINA
License:        ASL 2.0
URL:            http://mina.apache.org
Source0:        http://www.eu.apache.org/dist/mina/mina/%{version}/%{name}-%{version}-src.tar.gz

BuildRequires:  maven-local
BuildRequires:  mvn(com.jcraft:jzlib)
BuildRequires:  mvn(commons-lang:commons-lang)
BuildRequires:  mvn(org.apache:apache:pom:)
BuildRequires:  mvn(org.slf4j:slf4j-api)

BuildArch:      noarch
Source44: import.info

%description
Apache MINA is a network application framework which helps users develop high
performance and high scalability network applications easily. It provides an
abstract event-driven asynchronous API over various transports such as TCP/IP
and UDP/IP via Java NIO.


%package        mina-core
Group: Development/Java
Summary:        Apache MINA Core

%description    mina-core
This package contains Apache MINA Core module.

%package        mina-filter-compression
Group: Development/Java
Summary:        Apache MINA Compression Filter

%description    mina-filter-compression
This package contains Apache MINA Compression Filter module.

%package        mina-statemachine
Group: Development/Java
Summary:        Apache MINA State Machine

%description    mina-statemachine
This package contains Apache MINA State Machine module.

%package        mina-http
Group: Development/Java
Summary:        Apache MINA HTTP client and server codec

%description    mina-http
This package contains Apache MINA HTTP client and server codec.

%package        javadoc
Group: Development/Java
Summary:        API documentation for %{name}
BuildArch: noarch

%description javadoc
This package provides %{name}.

%prep
%setup -q

# In the tarball distributed by Apache the source code is inside the src
# directory, but our build tools expect the POM files in the current directory,
# so in order to simplify things we move everything to the top level before
# starting the build:
mv src/* .

# The modules use "bundle" packaging which doesn't work correctly with xmvn
# automatic dependency generation, in order to avoid that we change that to
# "jar":
sed -i \
    -e 's|<packaging>bundle</packaging>|<packaging>jar</packaging>|g' \
    -e 's|<type>bundle</type>|<type>jar</type>|g' \
    $(find . -name pom.xml)

# Disable the plugins that we don't need:
%pom_remove_plugin :maven-release-plugin
%pom_remove_plugin :maven-source-plugin
%pom_remove_plugin :maven-bundle-plugin
%pom_remove_plugin :maven-site-plugin

# Disable the modules that we can't currently build:
%pom_disable_module mina-legal
%pom_disable_module mina-transport-apr
%pom_disable_module mina-integration-beans
%pom_disable_module mina-integration-xbean
%pom_disable_module mina-integration-ognl
%pom_disable_module mina-integration-jmx
%pom_disable_module mina-example

%build
# The tests are disabled because they require EasyMock version 2 and we only
# have version 3:
%mvn_build -f -s

%install
%mvn_install

%files -f .mfiles-mina-parent
%doc LICENSE.txt NOTICE.txt

%files mina-core -f .mfiles-mina-core
%doc LICENSE.txt NOTICE.txt

%files mina-filter-compression -f .mfiles-mina-filter-compression

%files mina-statemachine -f .mfiles-mina-statemachine
%doc LICENSE.txt NOTICE.txt

%files mina-http -f .mfiles-mina-http

%files javadoc -f .mfiles-javadoc
%doc LICENSE.txt NOTICE.txt

%changelog
* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 2.0.9-alt1_4jpp8
- new fc release

* Tue Feb 02 2016 Igor Vlasenko <viy@altlinux.ru> 2.0.9-alt1_3jpp8
- new version

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 2.0.7-alt1_1jpp7
- new release

* Thu Aug 21 2014 Igor Vlasenko <viy@altlinux.ru> 2.0.4-alt3_6jpp7
- added BR: for xmvn

* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 2.0.4-alt2_6jpp7
- new release

* Mon Jul 14 2014 Igor Vlasenko <viy@altlinux.ru> 2.0.4-alt2_4jpp7
- NMU rebuild to move poms and fragments

* Wed Sep 05 2012 Igor Vlasenko <viy@altlinux.ru> 2.0.4-alt1_4jpp7
- new release

