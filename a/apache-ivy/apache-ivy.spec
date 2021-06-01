Epoch: 0
Group: Development/Java
BuildRequires: /proc rpm-build-java
BuildRequires: jpackage-11-compat
# fedora bcond_with macro
%define bcond_with() %{expand:%%{?_with_%{1}:%%global with_%{1} 1}}
%define bcond_without() %{expand:%%{!?_without_%{1}:%%global with_%{1} 1}}
# redefine altlinux specific with and without
%define with()         %{expand:%%{?with_%{1}:1}%%{!?with_%{1}:0}}
%define without()      %{expand:%%{?with_%{1}:0}%%{!?with_%{1}:1}}
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%bcond_with bouncycastle
%bcond_with ssh
%bcond_with vfs

Name:           apache-ivy
Version:        2.5.0
Release:        alt1_1jpp11
Summary:        Java-based dependency manager
License:        ASL 2.0

URL:            https://ant.apache.org/ivy
Source0:        https://www.apache.org/dist/ant/ivy/%{version}/%{name}-%{version}-src.tar.gz

BuildArch:      noarch

# Non-upstreamable.  Add /etc/ivy/ivysettings.xml at the end list of
# settings files Ivy tries to load.  This file will be used only as
# last resort, when no other setting files exist.
Patch0:         00-global-settings.patch

# Disable generating a code coverage report during build.
Patch1:         01-disable-jacoco-coverage-report.patch

BuildRequires:  ant
BuildRequires:  httpcomponents-client
BuildRequires:  ivy-local >= 4
BuildRequires:  jakarta-oro

%if %{with vfs}
BuildRequires:  apache-commons-vfs
%endif

%if %{with bouncycastle}
BuildRequires:  bouncycastle
BuildRequires:  bouncycastle-pg
%endif

%if %{with ssh}
BuildRequires:  jsch
BuildRequires:  jsch-agent-proxy-connector-factory
BuildRequires:  jsch-agent-proxy-core
BuildRequires:  jsch-agent-proxy-jsch
%endif

Provides:       ivy = %{version}-%{release}
Source44: import.info
AutoReqProv: yes,noosgi
Obsoletes: ivy < 2

%description
Apache Ivy is a tool for managing (recording, tracking, resolving and
reporting) project dependencies.  It is designed as process agnostic and is
not tied to any methodology or structure. while available as a standalone
tool, Apache Ivy works particularly well with Apache Ant providing a number
of powerful Ant tasks ranging from dependency resolution to dependency
reporting and publication.


%package javadoc
Group: Development/Java
Summary:        API Documentation for ivy
BuildArch: noarch

%description javadoc
JavaDoc documentation for %{name}


%prep
%setup -q
%patch0
%patch1 -p1

find -name '*.jar' -delete

# Don't hardcode sysconfdir path
sed -i 's:/etc/ivy/:%{_sysconfdir}/ivy/:' src/java/org/apache/ivy/ant/IvyAntSettings.java

%if %{without ssh}
%pom_remove_dep :jsch
%pom_remove_dep :jsch.agentproxy
%pom_remove_dep :jsch.agentproxy.connector-factory
%pom_remove_dep :jsch.agentproxy.jsch
rm -r src/java/org/apache/ivy/plugins/repository/{ssh,sftp}
rm src/java/org/apache/ivy/plugins/resolver/*{Ssh,SFTP}*.java
%endif

%if %{without bouncycastle}
%pom_remove_dep org.bouncycastle
rm src/java/org/apache/ivy/plugins/signer/bouncycastle/OpenPGPSignatureGenerator.java
%endif

%if %{without vfs}
# Remove dependency on commons-vfs
sed -i /commons-vfs/d ivy.xml
rm -rf src/java/org/apache/ivy/plugins/repository/vfs
rm -rf src/java/org/apache/ivy/plugins/resolver/VfsResolver.java
%endif

# Remove test dependencies
%pom_remove_dep :junit
%pom_remove_dep :hamcrest-core
%pom_remove_dep :hamcrest-library
%pom_remove_dep :ant-testutil
%pom_remove_dep :ant-launcher
%pom_remove_dep :ant-junit
%pom_remove_dep :ant-junit4
%pom_remove_dep :ant-contrib
%pom_remove_dep :xmlunit 

%mvn_alias : jayasoft:ivy
%mvn_file : %{name}/ivy ivy

# Remove prebuilt documentation
rm -rf asciidoc

# Publish artifacts through XMvn
sed -i /ivy:publish/s/local/xmvn/ build.xml

# girar noarch diff
sed -i -e s,yyyyMMddHHmmss,yyyyMMddHH, build.xml



%build
%ant -Dant.build.javac.source=1.8 -Dant.build.javac.target=1.8  \
    -Divy.mode=local \
    -Dtarget.ivy.bundle.version=%{version} \
    -Dtarget.ivy.bundle.version.qualifier= \
    -Dtarget.ivy.version=%{version} \
    jar javadoc publish-local


%install
%mvn_install -J build/reports/api

mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/ant.d
echo "apache-ivy/ivy" > $RPM_BUILD_ROOT%{_sysconfdir}/ant.d/%{name}


%files -f .mfiles
%doc --no-dereference LICENSE NOTICE
%doc README.adoc

%{_sysconfdir}/ant.d/%{name}

%files javadoc -f .mfiles-javadoc
%doc --no-dereference LICENSE NOTICE


%changelog
* Tue Jun 01 2021 Igor Vlasenko <viy@altlinux.org> 0:2.5.0-alt1_1jpp11
- new version

* Wed May 12 2021 Igor Vlasenko <viy@altlinux.org> 0:2.4.0-alt1_20jpp8
- fc update

* Sun May 09 2021 Igor Vlasenko <viy@altlinux.org> 0:2.4.0-alt1_18jpp8
- update

* Mon May 27 2019 Igor Vlasenko <viy@altlinux.ru> 0:2.4.0-alt1_16jpp8
- new version

* Fri Jun 01 2018 Igor Vlasenko <viy@altlinux.ru> 0:2.4.0-alt1_12jpp8
- java fc28+ update

* Wed May 09 2018 Igor Vlasenko <viy@altlinux.ru> 0:2.4.0-alt1_10jpp8
- java update

* Sat Nov 04 2017 Igor Vlasenko <viy@altlinux.ru> 0:2.4.0-alt1_9jpp8
- new fc release

* Mon Nov 28 2016 Igor Vlasenko <viy@altlinux.ru> 0:2.4.0-alt1_5jpp8
- new fc release

* Fri Feb 05 2016 Igor Vlasenko <viy@altlinux.ru> 0:2.4.0-alt1_4jpp8
- java 8 mass update

* Fri Jan 29 2016 Igor Vlasenko <viy@altlinux.ru> 0:2.4.0-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

* Fri Aug 01 2014 Igor Vlasenko <viy@altlinux.ru> 0:2.3.0-alt1_1jpp7
- new version

* Thu Sep 20 2012 Igor Vlasenko <viy@altlinux.ru> 0:2.2.0-alt3_5jpp7
- fc release

* Sat Sep 08 2012 Igor Vlasenko <viy@altlinux.ru> 0:2.2.0-alt3_1jpp6
- build with new commons-vfs2

* Tue Aug 28 2012 Igor Vlasenko <viy@altlinux.ru> 0:2.2.0-alt2_1jpp6
- fixed build

* Wed Sep 07 2011 Igor Vlasenko <viy@altlinux.ru> 0:2.2.0-alt1_1jpp6
- new version

* Mon Sep 20 2010 Igor Vlasenko <viy@altlinux.ru> 0:2.0.0-alt1_2jpp6
- new version

