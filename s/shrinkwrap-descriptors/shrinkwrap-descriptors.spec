Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-java
# END SourceDeps(oneline)
%filter_from_requires /^java-headless/d
BuildRequires: /proc jdepend
BuildRequires: jpackage-generic-compat
# %%name or %%version is ahead of its definition. Predefining for rpm 4.0 compatibility.
%define name shrinkwrap-descriptors
%define version 2.0.0
%global namedreltag -alpha-2
%global namedversion %{version}%{?namedreltag}


Name:          shrinkwrap-descriptors
Version:       2.0.0
Release:       alt3_0.11.alpha2jpp8
Summary:       ShrinkWrap subproject for creating Archive Descriptors
License:       ASL 2.0
Url:           http://www.jboss.org/shrinkwrap/

# git clone https://github.com/shrinkwrap/descriptors.git shrinkwrap-descriptors-2.0.0-alpha-2
# cd shrinkwrap-descriptors-2.0.0-alpha-2 && git archive --format=tar --prefix=shrinkwrap-descriptors-2.0.0-alpha-2/ 2.0.0-alpha-2 | xz > ../shrinkwrap-descriptors-2.0.0-alpha-2.tar.xz
Source0:       %{name}-%{namedversion}.tar.xz

# saxon-dom is built in saxon in Fedora
Patch0:        %{name}-saxon-dom.patch

BuildArch:     noarch

BuildRequires: jboss-parent
BuildRequires: apiviz
BuildRequires: junit
BuildRequires: maven-local
BuildRequires: maven-checkstyle-plugin
BuildRequires: maven-compiler-plugin
BuildRequires: maven-enforcer-plugin
BuildRequires: maven-install-plugin
BuildRequires: maven-jar-plugin
BuildRequires: maven-javadoc-plugin
BuildRequires: maven-resources-plugin
BuildRequires: maven-source-plugin
BuildRequires: maven-surefire-plugin
BuildRequires: maven-surefire-provider-junit
BuildRequires: maven-plugin-build-helper

BuildRequires: apache-commons-lang3
BuildRequires: saxon
BuildRequires: codemodel
BuildRequires: glassfish-dtd-parser
BuildRequires: xmlunit
Source44: import.info

%description
ShrinkWrap subproject for creating Archive Descriptors

%package javadoc
Group: Development/Java
Summary:       Javadoc for %{name}
BuildArch: noarch

%description javadoc
This package contains javadoc for %{name}.

%prep
%setup -q -n %{name}-%{namedversion}
%patch0 -p1

# Do not build test module, which is only for tests
sed -i "s|<module>test</module>|<!--module>test</module-->|" pom.xml

%build

export JAVA5_HOME=%{_jvmdir}/java
%mvn_build

%install
%mvn_install

%files -f .mfiles
%dir %{_javadir}/%{name}

%files javadoc -f .mfiles-javadoc

%changelog
* Sat Feb 06 2016 Igor Vlasenko <viy@altlinux.ru> 2.0.0-alt3_0.11.alpha2jpp8
- java 8 mass update

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 2.0.0-alt3_0.7.alpha2jpp7
- new release

* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 2.0.0-alt3_0.4.alpha2jpp7
- new release

* Fri Jul 18 2014 Igor Vlasenko <viy@altlinux.ru> 2.0.0-alt3_0.2.alpha2jpp7
- fixed build

* Mon Jul 14 2014 Igor Vlasenko <viy@altlinux.ru> 2.0.0-alt2_0.2.alpha2jpp7
- NMU rebuild to move poms and fragments

* Wed Sep 12 2012 Igor Vlasenko <viy@altlinux.ru> 2.0.0-alt1_0.2.alpha2jpp7
- new version

