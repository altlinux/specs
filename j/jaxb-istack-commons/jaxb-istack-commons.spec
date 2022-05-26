Group: Development/Java
BuildRequires: /proc rpm-build-java
BuildRequires: jpackage-default
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
# %%version is ahead of its definition. Predefining for rpm 4.0 compatibility.
%define version 3.0.12
%global commit 7ed1368ef26d2b4ef752b35ae33a98ec372ef3f8
%global _buildNumber %(c=%{commit}; echo ${c:0:7})
%global _scmBranch %{version}

Name:           jaxb-istack-commons
Version:        3.0.12
Release:        alt1_3jpp11
Summary:        iStack Common Utility Code
License:        BSD
URL:            https://github.com/eclipse-ee4j/jaxb-istack-commons
BuildArch:      noarch

Source0:        https://github.com/eclipse-ee4j/jaxb-istack-commons/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires:  maven-local
BuildRequires:  mvn(args4j:args4j)
BuildRequires:  mvn(jakarta.activation:jakarta.activation-api)
BuildRequires:  mvn(junit:junit)
BuildRequires:  mvn(org.apache.ant:ant)
BuildRequires:  mvn(org.apache.ant:ant-junit)
BuildRequires:  mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires:  mvn(org.apache.maven.plugin-tools:maven-plugin-annotations)
BuildRequires:  mvn(org.apache.maven.plugins:maven-failsafe-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-plugin-plugin)
BuildRequires:  mvn(org.apache.maven.resolver:maven-resolver-api)
BuildRequires:  mvn(org.apache.maven.resolver:maven-resolver-impl)
BuildRequires:  mvn(org.apache.maven:maven-artifact)
BuildRequires:  mvn(org.apache.maven:maven-core)
BuildRequires:  mvn(org.apache.maven:maven-model)
BuildRequires:  mvn(org.apache.maven:maven-plugin-api)
BuildRequires:  mvn(org.codehaus.mojo:build-helper-maven-plugin)
BuildRequires:  mvn(org.codehaus.plexus:plexus-utils)
BuildRequires:  mvn(org.glassfish.jaxb:codemodel)
BuildRequires:  mvn(org.testng:testng)
Source44: import.info

%description
Code shared between JAXP, JAXB, SAAJ, and JAX-WS projects.

%package -n istack-commons-maven-plugin
Group: Development/Java
Summary:        istack-commons Maven Mojo
%description -n istack-commons-maven-plugin
This package contains the istack-commons Maven Mojo.

%package -n import-properties-plugin
Group: Development/Java
Summary:        istack-commons import properties plugin
%description -n import-properties-plugin
This package contains the istack-commons import properties Maven Mojo.

%package -n istack-commons-runtime
Group: Development/Java
Summary:        istack-commons runtime
%description -n istack-commons-runtime
This package contains istack-commons runtime.

%package -n istack-commons-tools
Group: Development/Java
Summary:        istack-commons tools
%description -n istack-commons-tools
This package contains istack-commons tools.

%package -n istack-commons-buildtools
Group: Development/Java
Summary:        istack-commons buildtools
%description -n istack-commons-buildtools
This package contains istack-commons buildtools.

%package -n istack-commons-soimp
Group: Development/Java
Summary:        istack-commons soimp
%description -n istack-commons-soimp
This package contains istack-commons soimp.

%package -n istack-commons-test
Group: Development/Java
Summary:        istack-commons test
%description -n istack-commons-test
This package contains istack-commons test.

%prep
%setup -q


pushd istack-commons
# disable very verbose warnings
sed -i -e '/Xlint:all/d' pom.xml

# remove unnecessary dependency on parent POM
%pom_remove_parent

# remove unnecessary maven plugins
%pom_remove_plugin :buildnumber-maven-plugin
%pom_remove_plugin :glassfish-copyright-maven-plugin
%pom_remove_plugin :maven-enforcer-plugin
%pom_remove_plugin :maven-javadoc-plugin . test tools
%pom_remove_plugin :maven-source-plugin
%pom_remove_plugin :spotbugs-maven-plugin

%mvn_package :istack-commons __noinstall

# Compatibility
%mvn_alias :istack-commons-maven-plugin com.sun.istack:maven-istack-commons-plugin
popd

%build
pushd istack-commons
# - skip javadoc build due to https://github.com/fedora-java/xmvn/issues/58
# - ignore test
%mvn_build -f -j -s -- -Dmaven.compiler.source=1.8 -Dmaven.compiler.target=1.8 -Dmaven.compiler.release=8 -DscmBranch=%{_scmBranch} -DbuildNumber=%{_buildNumber}
popd

%install
pushd istack-commons
%mvn_install
popd

%files -n istack-commons-maven-plugin -f istack-commons/.mfiles-istack-commons-maven-plugin
%doc --no-dereference LICENSE.md NOTICE.md

%files -n import-properties-plugin -f istack-commons/.mfiles-import-properties-plugin
%doc --no-dereference LICENSE.md NOTICE.md

%files -n istack-commons-runtime -f istack-commons/.mfiles-istack-commons-runtime
%doc --no-dereference LICENSE.md NOTICE.md

%files -n istack-commons-tools -f istack-commons/.mfiles-istack-commons-tools
%doc --no-dereference LICENSE.md NOTICE.md

%files -n istack-commons-buildtools -f istack-commons/.mfiles-istack-commons-buildtools
%doc --no-dereference LICENSE.md NOTICE.md

%files -n istack-commons-test -f istack-commons/.mfiles-istack-commons-test
%doc --no-dereference LICENSE.md NOTICE.md

%files -n istack-commons-soimp -f istack-commons/.mfiles-istack-commons-soimp
%doc --no-dereference LICENSE.md NOTICE.md

%changelog
* Thu May 26 2022 Igor Vlasenko <viy@altlinux.org> 3.0.12-alt1_3jpp11
- new version

* Wed Aug 04 2021 Igor Vlasenko <viy@altlinux.org> 3.0.11-alt1_4jpp11
- update

* Fri Jun 04 2021 Igor Vlasenko <viy@altlinux.org> 3.0.11-alt1_3jpp11
- new version

