Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires: rpm-build-java
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
# %%version is ahead of its definition. Predefining for rpm 4.0 compatibility.
%define version 8.0.7
%global namedreltag .Final
%global namedversion %{version}%{?namedreltag}
%global jdkreltag 8u72

Name:          openjdk-orb
Version:       8.0.7
Release:       alt1_6jpp8
Summary:       A downstream fork of OpenJDK's ORB implementation
# 2 file without license headers https://github.com/jboss/openjdk-orb/issues/2
License:       GPLv2 with exceptions
URL:           https://github.com/jboss/openjdk-orb/
Source0:       https://github.com/jboss/openjdk-orb/archive/%{name}-%{namedversion}.tar.gz

BuildRequires: maven-local
BuildRequires: mvn(org.apache.maven.plugins:maven-enforcer-plugin)
BuildRequires: mvn(org.codehaus.mojo:build-helper-maven-plugin)
BuildRequires: mvn(org.codehaus.mojo:exec-maven-plugin)
BuildRequires: mvn(org.codehaus.mojo:idlj-maven-plugin)
BuildRequires: mvn(org.jacorb:jacorb-idl-compiler)
BuildRequires: mvn(org.jboss:jboss-parent:pom:)
BuildRequires: mvn(org.jboss.jandex:jandex-maven-plugin)
BuildRequires: mvn(org.jboss.spec.javax.transaction:jboss-transaction-api_1.2_spec)

Provides:      bundled(com.sun.corba.se.impl) = %{jdkreltag}
Provides:      bundled(com.sun.corba.se.internal) = %{jdkreltag}
Provides:      bundled(com.sun.corba.se.org.omg.CORBA) = %{jdkreltag}
Provides:      bundled(com.sun.corba.se.pept) = %{jdkreltag}
Provides:      bundled(com.sun.corba.se.spi) = %{jdkreltag}
Provides:      bundled(com.sun.org.omg.CORBA) = %{jdkreltag}
Provides:      bundled(com.sun.org.omg.SendingContext) = %{jdkreltag}
Provides:      bundled(com.sun.tools.corba.se.idl) = %{jdkreltag}
Provides:      bundled(javax.activity) = %{jdkreltag}
Provides:      bundled(javax.rmi.CORBA) = %{jdkreltag}
Provides:      bundled(org.omg.CORBA) = %{jdkreltag}
Provides:      bundled(org.omg.CORBA_2_3) = %{jdkreltag}
Provides:      bundled(org.omg.CosNaming) = %{jdkreltag}
Provides:      bundled(org.omg.Dynamic) = %{jdkreltag}
Provides:      bundled(org.omg.DynamicAny) = %{jdkreltag}
Provides:      bundled(org.omg.IOP) = %{jdkreltag}
Provides:      bundled(org.omg.Messaging) = %{jdkreltag}
Provides:      bundled(org.omg.PortableInterceptor) = %{jdkreltag}
Provides:      bundled(org.omg.PortableServer) = %{jdkreltag}
Provides:      bundled(org.omg.SendingContext) = %{jdkreltag}
Provides:      bundled(org.omg.stub) = %{jdkreltag}
Provides:      bundled(sun.corba) = %{jdkreltag}

BuildArch:     noarch
Source44: import.info

%description
JBoss repackaging of the OpenJDK ORB.

%package javadoc
Group: Development/Java
Summary:       Javadoc for %{name}
BuildArch: noarch

%description javadoc
This package contains javadoc for %{name}.

%prep
%setup -q -n %{name}-%{name}-%{namedversion}
# https://github.com/jboss/openjdk-orb/issues/3
sed -i "s,59 Temple Place,51 Franklin Street,;s,Suite 330,Fifth Floor,;s,02111-1307,02110-1301," LICENSE

%build

%mvn_build

%install
%mvn_install

%files -f .mfiles
%doc README
%doc --no-dereference ASSEMBLY_EXCEPTION LICENSE THIRD_PARTY_README

%files javadoc -f .mfiles-javadoc
%doc --no-dereference ASSEMBLY_EXCEPTION LICENSE THIRD_PARTY_README

%changelog
* Sun May 26 2019 Igor Vlasenko <viy@altlinux.ru> 8.0.7-alt1_6jpp8
- new version

* Thu May 31 2018 Igor Vlasenko <viy@altlinux.ru> 8.0.7-alt1_4jpp8
- java update

* Wed May 30 2018 Igor Vlasenko <viy@altlinux.ru> 8.0.7-alt1_3jpp8
- new version

