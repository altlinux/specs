# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
# END SourceDeps(oneline)
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
# %%name or %%version is ahead of its definition. Predefining for rpm 4.0 compatibility.
%define name jboss-classfilewriter
%define version 1.0.5
%global namedreltag .Final
%global namedversion %{version}%{?namedreltag}

Name:             jboss-classfilewriter
Version:          1.0.5
Release:          alt1_8jpp8
Summary:          JBoss Class File Writer
Group:            Development/Other
License:          LGPLv2+
URL:              https://github.com/jbossas/jboss-classfilewriter

# git clone git://github.com/jbossas/jboss-classfilewriter.git
# cd jboss-classfilewriter/ && git archive --format=tar --prefix=jboss-classfilewriter-1.0.5.Final/ 1.0.5.Final | xz > jboss-classfilewriter-1.0.5.Final.tar.xz
Source0:          jboss-classfilewriter-%{namedversion}.tar.xz

BuildArch:        noarch

BuildRequires:    aether
BuildRequires:    maven-local
BuildRequires:    maven-surefire-provider-junit
BuildRequires:    junit
BuildRequires:    jboss-parent
Source44: import.info

%description
This package contains JBoss Class File Writer

%package javadoc
Summary:          Javadocs for %{name}
Group:            Development/Java
BuildArch: noarch

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q -n jboss-classfilewriter-%{namedversion}

%build
%mvn_build

%install
%mvn_install

%files -f .mfiles
%dir %{_javadir}/%{name}

%files javadoc -f .mfiles-javadoc

%changelog
* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 1.0.5-alt1_8jpp8
- new fc release

* Tue Feb 02 2016 Igor Vlasenko <viy@altlinux.ru> 1.0.5-alt1_7jpp8
- new version

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 1.0.5-alt1_3jpp7
- new release

* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 1.0.3-alt2_3jpp7
- new release

* Mon Jul 14 2014 Igor Vlasenko <viy@altlinux.ru> 1.0.3-alt2_1jpp7
- NMU rebuild to move poms and fragments

* Thu Sep 13 2012 Igor Vlasenko <viy@altlinux.ru> 1.0.3-alt1_1jpp7
- new version

