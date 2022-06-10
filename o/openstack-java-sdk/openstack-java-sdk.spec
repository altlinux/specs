Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
# END SourceDeps(oneline)
BuildRequires: /proc rpm-build-java
BuildRequires: jpackage-default
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
# % global git_hash git10597f7

Name:           openstack-java-sdk
Version:        3.2.9
Release:        alt1_9jpp11
Summary:        OpenStack Java SDK

License:        ASL 2.0
URL:            https://github.com/woorea/%{name}
Source0:        https://github.com/woorea/%{name}/archive/%{name}-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  jpackage-utils >= 0:1.7.3
BuildRequires:  jackson-annotations >= 2.9.0
BuildRequires:  jackson-core >= 2.9.0
BuildRequires:  jackson-databind >= 2.9.0
BuildRequires:  jackson-jaxrs-json-provider >= 2.9.0
BuildRequires:  maven-local
BuildRequires:  junit
BuildRequires:  mvn(org.apache.httpcomponents:httpclient) >= 4.5.0
BuildRequires:  mvn(org.jboss.resteasy:resteasy-jaxrs)

Requires:  jackson-annotations >= 2.9.0
Requires:  jackson-core >= 2.9.0
Requires:  jackson-databind >= 2.9.0
Requires:  jackson-jaxrs-json-provider >= 2.9.0
Source44: import.info

%description
OpenStack client implementation in Java.

%package javadoc
Group: Development/Java
Summary:        API documentation for %{name}
BuildArch: noarch

%description javadoc
This package provides %{summary}.

%package -n openstack-java-client
Group: Development/Java
Summary:        OpenStack Java Client

%description -n openstack-java-client
This package contains the %{summary}.


%package -n openstack-java-resteasy-connector
Group: Development/Java
Summary:        OpenStack Java RESTEasy Connector

%description -n openstack-java-resteasy-connector
This package contains the %{summary}.
Requires:  mvn(org.apache.httpcomponents:httpclient) >= 4.5.0


%package -n openstack-java-ceilometer-client
Group: Development/Java
Summary:        OpenStack Java Ceilometer Client

%description -n openstack-java-ceilometer-client
This package contains the %{summary}.


%package -n openstack-java-ceilometer-model
Group: Development/Java
Summary:        OpenStack Java Ceilometer Model

%description -n openstack-java-ceilometer-model
This package contains the %{summary}.


%package -n openstack-java-glance-client
Group: Development/Java
Summary:        OpenStack Java Glance Client

%description -n openstack-java-glance-client
This package contains the %{summary}.


%package -n openstack-java-glance-model
Group: Development/Java
Summary:        OpenStack Java Glance Model

%description -n openstack-java-glance-model
This package contains the %{summary}.


%package -n openstack-java-cinder-client
Group: Development/Java
Summary:        OpenStack Java Cinder Client

%description -n openstack-java-cinder-client
This package contains the %{summary}.


%package -n openstack-java-cinder-model
Group: Development/Java
Summary:        OpenStack Java Cinder Model

%description -n openstack-java-cinder-model
This package contains the %{summary}.


%package -n openstack-java-keystone-client
Group: Development/Java
Summary:        OpenStack Java Keystone Client

%description -n openstack-java-keystone-client
This package contains the %{summary}.


%package -n openstack-java-keystone-model
Group: Development/Java
Summary:        OpenStack Java Keystone Model

%description -n openstack-java-keystone-model
This package contains the %{summary}.


%package -n openstack-java-nova-client
Group: Development/Java
Summary:        OpenStack Java Nova Client

%description -n openstack-java-nova-client
This package contains the %{summary}.


%package -n openstack-java-nova-model
Group: Development/Java
Summary:        OpenStack Java Nova Model

%description -n openstack-java-nova-model
This package contains the %{summary}.


%package -n openstack-java-quantum-client
Group: Development/Java
Summary:        OpenStack Java Quantum Client

%description -n openstack-java-quantum-client
This package contains the %{summary}.


%package -n openstack-java-quantum-model
Group: Development/Java
Summary:        OpenStack Java Quantum Model

%description -n openstack-java-quantum-model
This package contains the %{summary}.


%package -n openstack-java-swift-client
Group: Development/Java
Summary:        OpenStack Java Swift Client

%description -n openstack-java-swift-client
This package contains the %{summary}.


%package -n openstack-java-swift-model
Group: Development/Java
Summary:        OpenStack Java Swift Model

%description -n openstack-java-swift-model
This package contains the %{summary}.


%package -n openstack-java-heat-client
Group: Development/Java
Summary:        OpenStack Java Heat Client

%description -n openstack-java-heat-client
This package contains the %{summary}.


%package -n openstack-java-heat-model
Group: Development/Java
Summary:        OpenStack Java Heat Model

%description -n openstack-java-heat-model
This package contains the %{summary}.


%prep
%setup -q -n %{name}-%{name}-%{version}

# remove unnecessary dependency on parent POM
%pom_remove_parent

%mvn_package ":{openstack-java-sdk,openstack-client-connectors}" __noinstall


%build
%mvn_build -s -- -Dmaven.compiler.source=1.8 -Dmaven.compiler.target=1.8 -Dmaven.javadoc.source=1.8 -Dmaven.compiler.release=8 -P "!console,!examples,!jersey2,!jersey,resteasy" -DskipTests


%install
%mvn_install

%files javadoc -f .mfiles-javadoc

%files -n openstack-java-client -f .mfiles-openstack-client
%doc --no-dereference LICENSE.txt
%doc README.textile
%dir %{_javadir}/%{name}

%files -n openstack-java-resteasy-connector -f .mfiles-resteasy-connector
%doc LICENSE.txt README.textile
%dir %{_javadir}/%{name}

%files -n openstack-java-ceilometer-client -f .mfiles-ceilometer-client
%doc --no-dereference LICENSE.txt
%doc README.textile

%files -n openstack-java-ceilometer-model -f .mfiles-ceilometer-model
%doc --no-dereference LICENSE.txt
%doc README.textile
%dir %{_javadir}/%{name}

%files -n openstack-java-glance-client -f .mfiles-glance-client
%doc --no-dereference LICENSE.txt
%doc README.textile

%files -n openstack-java-glance-model -f .mfiles-glance-model
%doc --no-dereference LICENSE.txt
%doc README.textile
%dir %{_javadir}/%{name}

%files -n openstack-java-cinder-client -f .mfiles-cinder-client
%doc --no-dereference LICENSE.txt
%doc README.textile

%files -n openstack-java-cinder-model -f .mfiles-cinder-model
%doc --no-dereference LICENSE.txt
%doc README.textile
%dir %{_javadir}/%{name}

%files -n openstack-java-keystone-client -f .mfiles-keystone-client
%doc --no-dereference LICENSE.txt
%doc README.textile

%files -n openstack-java-keystone-model -f .mfiles-keystone-model
%doc --no-dereference LICENSE.txt
%doc README.textile
%dir %{_javadir}/%{name}

%files -n openstack-java-nova-client -f .mfiles-nova-client
%doc --no-dereference LICENSE.txt
%doc README.textile

%files -n openstack-java-nova-model -f .mfiles-nova-model
%doc --no-dereference LICENSE.txt
%doc README.textile
%dir %{_javadir}/%{name}

%files -n openstack-java-quantum-client -f .mfiles-quantum-client
%doc --no-dereference LICENSE.txt
%doc README.textile

%files -n openstack-java-quantum-model -f .mfiles-quantum-model
%doc --no-dereference LICENSE.txt
%doc README.textile
%dir %{_javadir}/%{name}

%files -n openstack-java-swift-client -f .mfiles-swift-client
%doc --no-dereference LICENSE.txt
%doc README.textile

%files -n openstack-java-swift-model -f .mfiles-swift-model
%doc --no-dereference LICENSE.txt
%doc README.textile
%dir %{_javadir}/%{name}

%files -n openstack-java-heat-client -f .mfiles-heat-client
%doc --no-dereference LICENSE.txt
%doc README.textile

%files -n openstack-java-heat-model -f .mfiles-heat-model
%doc --no-dereference LICENSE.txt
%doc README.textile
%dir %{_javadir}/%{name}

%changelog
* Fri Jun 10 2022 Igor Vlasenko <viy@altlinux.org> 3.2.9-alt1_9jpp11
- update

* Fri Jun 04 2021 Igor Vlasenko <viy@altlinux.org> 3.2.9-alt1_7jpp11
- new version

