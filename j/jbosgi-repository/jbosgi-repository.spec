# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-java
BuildRequires: maven
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-compat
# %%name or %%version is ahead of its definition. Predefining for rpm 4.0 compatibility.
%define name jbosgi-repository
%define version 1.0.5
%global namedreltag .Final
%global namedversion %{version}%{?namedreltag}

Name:             jbosgi-repository
Version:          1.0.5
Release:          alt2_6jpp7
Summary:          JBossOSGi Repository
Group:            Development/Java
License:          LGPLv2+
URL:              http://community.jboss.org/wiki/JBossOSGi

# git clone git://github.com/jbosgi/jbosgi-repository.git
# cd jbosgi-repository/ && git archive --format=tar --prefix=jbosgi-repository-1.0.5.Final/ 1.0.5.Final | xz > jbosgi-repository-1.0.5.Final.tar.xz
Source0:          jbosgi-repository-%{namedversion}.tar.xz

# Not needed, causes compilation errors
Patch0:           0001-Drop-osgi.enterprise-dependency.patch
# We don't have test classes available to compile it
Patch1:           0002-Disable-itests-module.patch
Patch2:           fix_metadata.patch

BuildArch:        noarch

BuildRequires:    jpackage-utils
BuildRequires:    maven-local
BuildRequires:    maven-compiler-plugin
BuildRequires:    maven-install-plugin
BuildRequires:    maven-jar-plugin
BuildRequires:    maven-javadoc-plugin
BuildRequires:    maven-surefire-provider-junit4
BuildRequires:    jbosgi-parent
BuildRequires:    arquillian-core
BuildRequires:    arquillian-osgi
BuildRequires:    jboss-logmanager
BuildRequires:    jbosgi-resolver
BuildRequires:    jbosgi-framework
BuildRequires:    shrinkwrap
BuildRequires:    shrinkwrap-resolver
BuildRequires:    felix-osgi-core
BuildRequires:    junit
BuildRequires:    mockito

Requires:         jpackage-utils
Requires:         arquillian-core
Requires:         arquillian-osgi
Requires:         jboss-logmanager
Requires:         jbosgi-resolver
Requires:         jbosgi-framework
Requires:         shrinkwrap
Requires:         shrinkwrap-resolver
Requires:         felix-osgi-core
Source44: import.info

%description
This package contains the JBoss OSGi Repository.

%package javadoc
Summary:          Javadocs for %{name}
Group:            Development/Java
Requires:         jpackage-utils
BuildArch: noarch

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q -n jbosgi-repository-%{namedversion}

find -name '*.class' -exec rm -f '{}' \;
find -name '*.dll' -exec rm -f '{}' \;

%patch0 -p1
%patch1 -p1
%patch2

%build
# We need to use Maven3 explicitly because otherwise Maven2 classes are used...
# Bundle tests fail
mvn-rpmbuild -Dmaven.test.skip=true -Dmaven.local.depmap.file=%{_mavendepmapfragdir}/maven install javadoc:aggregate

%install
install -d -m 755 $RPM_BUILD_ROOT%{_javadir}/%{name}
install -d -m 755 $RPM_BUILD_ROOT%{_mavenpomdir}
install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}

for m in api core ; do
  # JAR
  install -pm 644 ${m}/target/jbosgi-repository-${m}-%{namedversion}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/%{name}-${m}.jar
  # POM
  install -pm 644 ${m}/pom.xml $RPM_BUILD_ROOT%{_mavenpomdir}/JPP.%{name}-%{name}-${m}.pom
  # DEPMAP
  %add_maven_depmap JPP.%{name}-%{name}-${m}.pom %{name}/%{name}-${m}.jar
done

# JAR
install -pm 644 bundle/target/jbosgi-repository-%{namedversion}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/%{name}.jar
install -pm 644 plugins/shrinkwrap/target/jbosgi-repository-plugin-shrinkwrap-%{namedversion}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/%{name}-plugin-shrinkwrap.jar

# POM
install -pm 644 bundle/pom.xml $RPM_BUILD_ROOT%{_mavenpomdir}/JPP.%{name}-%{name}.pom
install -pm 644 plugins/shrinkwrap/pom.xml $RPM_BUILD_ROOT%{_mavenpomdir}/JPP.%{name}-%{name}-plugin-shrinkwrap.pom
install -pm 644 plugins/pom.xml $RPM_BUILD_ROOT%{_mavenpomdir}/JPP.%{name}-%{name}-plugins.pom
install -pm 644 pom.xml $RPM_BUILD_ROOT%{_mavenpomdir}/JPP.%{name}-%{name}-parent.pom

# DEPMAP
%add_maven_depmap JPP.%{name}-%{name}.pom %{name}/%{name}.jar
%add_maven_depmap JPP.%{name}-%{name}-plugin-shrinkwrap.pom %{name}/%{name}-plugin-shrinkwrap.jar
%add_maven_depmap JPP.%{name}-%{name}-plugins.pom
%add_maven_depmap JPP.%{name}-%{name}-parent.pom

# APIDOCS
cp -rp target/site/apidocs/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}

%files
%{_mavenpomdir}/*
%{_mavendepmapfragdir}/*
%{_javadir}/*

%files javadoc
%{_javadocdir}/%{name}

%changelog
* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 1.0.5-alt2_6jpp7
- new release

* Mon Jul 14 2014 Igor Vlasenko <viy@altlinux.ru> 1.0.5-alt2_4jpp7
- NMU rebuild to move poms and fragments

* Thu Sep 13 2012 Igor Vlasenko <viy@altlinux.ru> 1.0.5-alt1_4jpp7
- new version

