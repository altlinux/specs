Epoch: 0
Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
# END SourceDeps(oneline)
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
# %%name or %%version is ahead of its definition. Predefining for rpm 4.0 compatibility.
%define name jboss-remoting
%define version 4.0.3
%global namedreltag .Final
%global namedversion %{version}%{?namedreltag}

Name:             jboss-remoting
Version:          4.0.3
Release:          alt1_4jpp8
Summary:          JBoss Remoting
License:          LGPLv2+
URL:              http://www.jboss.org/jbossremoting

# git clone git://github.com/jboss-remoting/jboss-remoting.git
# cd jboss-remoting && git checkout 4.0.3.Final && git checkout-index -f -a --prefix=jboss-remoting-4.0.3.Final/
# rm jboss-remoting-4.0.3.Final/src/test/resources/test-content.bin
# tar -cJf jboss-remoting-4.0.3.Final-CLEAN.tar.xz jboss-remoting-4.0.3.Final
Source0:          jboss-remoting-%{namedversion}-CLEAN.tar.xz

BuildArch:        noarch

BuildRequires:    maven-local
BuildRequires:    mvn(jdepend:jdepend)
BuildRequires:    mvn(junit:junit)
BuildRequires:    mvn(org.jboss:jboss-parent:pom:)
BuildRequires:    mvn(org.jboss.apiviz:apiviz)
BuildRequires:    mvn(org.jboss.logging:jboss-logging)
BuildRequires:    mvn(org.jboss.logging:jboss-logging-processor)
BuildRequires:    mvn(org.jboss.xnio:xnio-api)
BuildRequires:    mvn(org.jboss.xnio:xnio-nio)
Source44: import.info

%description
The purpose of JBoss Remoting is to provide a general purpose framework
for symmetric and asymmetric communication over a network. It supports
various modes of interaction, including invocations, one way messaging,
and asynchronous callbacks.

%package javadoc
Group: Development/Java
Summary:          Javadoc for %{name}
BuildArch: noarch

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q -n jboss-remoting-%{namedversion}

%build
# Skipped test because of removing binary content from test dir which is required to run them
%mvn_build -f

%install
%mvn_install

%files -f .mfiles
%doc COPYING.txt

%files javadoc -f .mfiles-javadoc
%doc COPYING.txt

%changelog
* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 0:4.0.3-alt1_4jpp8
- new fc release

* Sat Feb 06 2016 Igor Vlasenko <viy@altlinux.ru> 0:4.0.3-alt1_2jpp8
- java 8 mass update

* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 0:3.2.4-alt2_4jpp7
- new release

* Mon Jul 14 2014 Igor Vlasenko <viy@altlinux.ru> 0:3.2.4-alt2_2jpp7
- NMU rebuild to move poms and fragments

* Fri Sep 07 2012 Igor Vlasenko <viy@altlinux.ru> 0:3.2.4-alt1_2jpp7
- new version

* Mon Jan 16 2012 Igor Vlasenko <viy@altlinux.ru> 0:2.5.1-alt2_4jpp6
- hack: built w/o jdk6 support for jboss/jbossas 4 support

* Sat Jan 14 2012 Igor Vlasenko <viy@altlinux.ru> 0:2.5.1-alt1_4jpp6
- converted from JPackage by jppimport script

* Sat Mar 06 2010 Igor Vlasenko <viy@altlinux.ru> 0:2.2.2-alt1_3.SP8.1jpp5
- new version

* Fri Mar 05 2010 Igor Vlasenko <viy@altlinux.ru> 0:2.2.2-alt0.1jpp
- bootstrap for jbossas

