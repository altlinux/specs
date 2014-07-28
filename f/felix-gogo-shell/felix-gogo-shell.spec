# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-java
BuildRequires: maven
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-compat
# %%name or %%version is ahead of its definition. Predefining for rpm 4.0 compatibility.
%define name felix-gogo-shell
%define version 0.10.0
%global project   felix
%global bundle    org.apache.felix.gogo.shell

%{!?scl:%global pkg_name %{name}}
%{?scl:%scl_package %{project}-gogo-shell}

Name:             %{?scl_prefix}%{project}-gogo-shell
Version:          0.10.0
Release:          alt2_7jpp7
Summary:          Community OSGi R4 Service Platform Implementation - Basic Commands
Group:            Development/Java
License:          ASL 2.0
URL:              http://felix.apache.org/site/apache-felix-gogo.html

Source0:          http://mirror.catn.com/pub/apache//felix/org.apache.felix.gogo.shell-0.10.0-project.tar.gz
  
# Changed GroupID from osgi to felix
Patch0:           %{pkg_name}-groupid.patch

Patch1:           ignoreActivatorException.patch

BuildArch:        noarch

BuildRequires:    jpackage-utils
BuildRequires:    maven-local
BuildRequires:    maven-plugin-bundle
BuildRequires:    maven-surefire-provider-junit4
BuildRequires:    %{?scl_prefix}felix-gogo-parent
BuildRequires:    %{?scl_prefix}felix-gogo-runtime
BuildRequires:    felix-osgi-compendium
%{?scl:BuildRequires:	  %{?scl_prefix}build}

Requires:         jpackage-utils
%{?scl:Requires: %scl_runtime}
Source44: import.info

%description
Apache Felix is a community effort to implement the OSGi R4 Service Platform
and other interesting OSGi-related technologies under the Apache license. The
OSGi specifications originally targeted embedded devices and home services
gateways, but they are ideally suited for any project interested in the
principles of modularity, component-orientation, and/or service-orientation.
OSGi technology combines aspects of these aforementioned principles to define a
dynamic service deployment framework that is amenable to remote management.

%package javadoc
Group:            Development/Java
Summary:          Javadoc for %{pkg_name}
Requires:         jpackage-utils
BuildArch: noarch

%description javadoc
This package contains the API documentation for %{pkg_name}.

%prep
%setup -q -n %{bundle}-%{version}
%patch0 -p1 -F3
%patch1

%build
%{?scl:%scl_maven_opts}
mvn-rpmbuild install javadoc:aggregate 

%install
# jars
install -d -m 0755 %{buildroot}%{_javadir}/%{project}
install -pm 644 target/%{bundle}-%{version}.jar %{buildroot}%{_javadir}/%{project}/%{bundle}.jar

# pom
install -d -m 755 %{buildroot}%{_mavenpomdir}
install -pm 644 pom.xml %{buildroot}%{_mavenpomdir}/JPP.%{project}-%{bundle}.pom
%add_maven_depmap JPP.%{project}-%{bundle}.pom %{project}/%{bundle}.jar

# javadoc
install -d -m 0755 %{buildroot}%{_javadocdir}/%{pkg_name}
cp -pr target/site/api*/* %{buildroot}%{_javadocdir}/%{pkg_name}


%files
%doc DEPENDENCIES LICENSE NOTICE
%{_javadir}/*
%{_mavenpomdir}/JPP.%{project}-%{bundle}.pom
%{_mavendepmapfragdir}/%{name}

%files javadoc
%doc LICENSE
%{_javadocdir}/%{pkg_name}

%changelog
* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 0.10.0-alt2_7jpp7
- new release

* Mon Jul 14 2014 Igor Vlasenko <viy@altlinux.ru> 0.10.0-alt2_4jpp7
- NMU rebuild to move poms and fragments

* Fri Aug 24 2012 Igor Vlasenko <viy@altlinux.ru> 0.10.0-alt1_4jpp7
- new release

