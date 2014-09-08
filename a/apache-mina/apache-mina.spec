# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-java
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-compat
Name: apache-mina
Version: 2.0.7
Release: alt1_1jpp7
Summary: Apache MINA
Group: Development/Java
License: ASL 2.0
URL: http://mina.apache.org
Source0: http://mina.apache.org/dyn/closer.cgi/mina/%{version}/%{name}-%{version}-src.tar.gz
BuildArch: noarch

BuildRequires: maven-local

BuildRequires: apache-commons-lang
BuildRequires: easymock
BuildRequires: maven-compiler-plugin
BuildRequires: maven-jar-plugin
BuildRequires: maven-javadoc-plugin
BuildRequires: maven-resources-plugin
BuildRequires: maven-shared
BuildRequires: maven-site-plugin
BuildRequires: maven-surefire-plugin
Source44: import.info


%description
Apache MINA is a network application framework which helps users develop high
performance and high scalability network applications easily. It provides an
abstract event-driven asynchronous API over various transports such as TCP/IP
and UDP/IP via Java NIO.


%package javadoc
Summary: API documentation for %{name}
Group: Development/Java
BuildArch: noarch


%description javadoc
This package provides %{name}.


%prep

# Extract the source:
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
%mvn_build -f


%install
%mvn_install


%files -f .mfiles
%dir %{_javadir}/%{name}
%doc LICENSE.txt
%doc NOTICE.txt


%files javadoc -f .mfiles-javadoc
%doc LICENSE.txt
%doc NOTICE.txt


%changelog
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

