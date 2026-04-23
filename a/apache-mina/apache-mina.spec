Name:           apache-mina
Version:        2.2.5
Release:        alt1

Summary:        Apache MINA
License:        Apache-2.0
Group:          Development/Java
URL:            http://mina.apache.org
VCS:            https://github.com/apache/mina

Source0:        %name-%version.tar

BuildRequires(pre):  maven-local
BuildRequires:  jpackage-default

BuildRequires:  mvn(org.apache:apache:pom:)
BuildRequires:  mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires:  mvn(org.slf4j:slf4j-reload4j)
BuildRequires:  mvn(org.easymock:easymock)
BuildRequires:  mvn(org.mockito:mockito-core)
BuildRequires:  mvn(ognl:ognl)

BuildArch:      noarch

%description
Apache MINA is a network application framework which helps users develop high
performance and high scalability network applications easily. It provides an
abstract event-driven asynchronous API over various transports such as TCP/IP
and UDP/IP via Java NIO.

%javadoc_package

%package -n     mina-core
Summary:        Apache MINA Core
Group:          Development/Java

%description -n mina-core
%summary.

%package -n     mina-filter-compression
Summary:        Apache MINA Compression Filter
Group:          Development/Java

%description -n mina-filter-compression
%summary.

%package -n     mina-http
Summary:        Apache MINA HTTP client and server codec
Group:          Development/Java

%description -n mina-http
%summary.

%package -n     mina-integration-beans
Summary:        Apache MINA JavaBeans Integration
Group:          Development/Java

%description -n mina-integration-beans
%summary.

%package -n     mina-integration-jmx
Summary:        Apache MINA JMX Integration
Group:          Development/Java

%description -n mina-integration-jmx
%summary.

%package -n     mina-integration-ognl
Summary:        Apache MINA OGNL Integration
Group:          Development/Java

%description -n mina-integration-ognl
%summary.

%package -n     mina-statemachine
Summary:        Apache MINA State Machine
Group:          Development/Java

%description -n mina-statemachine
%summary.

%prep
%setup

%pom_remove_plugin :cyclonedx-maven-plugin
%pom_remove_plugin :maven-enforcer-plugin
%pom_remove_plugin :maven-release-plugin
%pom_remove_plugin :maven-site-plugin

# requires Spring
%pom_disable_module mina-integration-xbean
%pom_disable_module mina-example

# requires pmd
%pom_disable_module mina-legal

# requires tomcat 10.0.27
%pom_disable_module mina-transport-apr

%build
# tests disabled due to fails with ports
%mvn_build -s -f

%install
%mvn_install

%files -f .mfiles-mina-parent
%doc LICENSE.txt NOTICE.txt

%files -n mina-core -f .mfiles-mina-core
%files -n mina-filter-compression -f .mfiles-mina-filter-compression
%files -n mina-http -f .mfiles-mina-http
%files -n mina-integration-beans -f .mfiles-mina-integration-beans
%files -n mina-integration-jmx -f .mfiles-mina-integration-jmx
%files -n mina-integration-ognl -f .mfiles-mina-integration-ognl
%files -n mina-statemachine -f .mfiles-mina-statemachine

%changelog
* Mon Apr 20 2026 Evgeniy Serov <scala@altlinux.org> 2.2.5-alt1
- Updated to 2.2.5.
- Returned to Sisyphus.

* Sat May 25 2019 Igor Vlasenko <viy@altlinux.ru> 2.0.9-alt1_10jpp8
- new version

* Tue Feb 05 2019 Igor Vlasenko <viy@altlinux.ru> 2.0.9-alt1_9jpp8
- fc29 update

* Sun Apr 15 2018 Igor Vlasenko <viy@altlinux.ru> 2.0.9-alt1_8jpp8
- java update

* Thu Nov 09 2017 Igor Vlasenko <viy@altlinux.ru> 2.0.9-alt1_7jpp8
- fc27 update

* Sun Oct 22 2017 Igor Vlasenko <viy@altlinux.ru> 2.0.9-alt1_6jpp8
- new jpp release

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

