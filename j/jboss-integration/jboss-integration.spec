Epoch: 0
Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
# END SourceDeps(oneline)
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
# %%name or %%version is ahead of its definition. Predefining for rpm 4.0 compatibility.
%define name jboss-integration
%define version 6.0.0
%global namedreltag .CR1
%global namedversion %{version}%{?namedreltag}

Name:             jboss-integration
Version:          6.0.0
Release:          alt1_0.5.CR1jpp8
Summary:          JBoss Integration
License:          LGPLv2+
URL:              http://www.jboss.org

# svn export http://anonsvn.jboss.org/repos/jbossas/projects/integration/tags/6.0.0.CR1/ jboss-integration-6.0.0.CR1
# tar -zcvf jboss-integration-6.0.0.CR1.tar.gz jboss-integration-6.0.0.CR1
Source0:          jboss-integration-%{namedversion}.tar.gz

BuildArch:        noarch

BuildRequires:    jacorb
BuildRequires:    maven-local
BuildRequires:    maven-compiler-plugin
BuildRequires:    maven-enforcer-plugin
BuildRequires:    maven-install-plugin
BuildRequires:    maven-jar-plugin
BuildRequires:    maven-javadoc-plugin
BuildRequires:    jboss-transaction-1.1-api
Source44: import.info

%description
The JBoss integration classes

%package javadoc
Group: Development/Documentation
Summary:          Javadocs for %{name}
BuildArch: noarch

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q -n jboss-integration-%{namedversion}

# Not needed
%pom_disable_module jboss-classloading-spi
%pom_disable_module jboss-deployment-spi
%pom_disable_module jboss-transaction-spi
%pom_disable_module jboss-scanning-spi
%pom_disable_module jboss-annotations-spi
%pom_disable_module jboss-jca-spi
%pom_disable_module build

%pom_remove_dep "org.jboss.javaee:jboss-transaction-api" jboss-corba-ots-spi/pom.xml
%pom_add_dep "org.jboss.spec.javax.transaction:jboss-transaction-api_1.1_spec" jboss-corba-ots-spi/pom.xml

sed -i "s,59 Temple Place,51 Franklin Street,;s,Suite 330,Fifth Floor,;s,02111-1307,02110-1301," build/lgpl.txt

%build
%mvn_build

%install
%mvn_install

%files -f .mfiles
%dir %{_javadir}/%{name}
%doc build/lgpl.txt

%files javadoc -f .mfiles-javadoc
%doc build/lgpl.txt

%changelog
* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 0:6.0.0-alt1_0.5.CR1jpp8
- new fc release

* Fri Feb 05 2016 Igor Vlasenko <viy@altlinux.ru> 0:6.0.0-alt1_0.4.CR1jpp8
- java 8 mass update

* Fri Sep 03 2010 Igor Vlasenko <viy@altlinux.ru> 0:5.1.0-alt1_4jpp6
- new version

