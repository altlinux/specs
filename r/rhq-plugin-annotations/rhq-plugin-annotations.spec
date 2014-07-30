# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-java
BuildRequires: maven
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-compat
Name:             rhq-plugin-annotations
Version:          3.0.4
Release:          alt2_5jpp7
Summary:          RHQ plugin annotations
Group:            Development/Java
License:          GPL and LGPLv2+
URL:              http://rhq-project.org

# git clone git://git.fedorahosted.org/rhq/rhq.git
# git checkout rhq-pluginGen-3.0.4
# cd rhq/modules/helpers/
# tar cafJ rhq-plugin-annotations-3.0.4.tar.xz pluginAnnotations
Source0:          rhq-plugin-annotations-%{version}.tar.xz
Patch0:           rhq-plugin-annotations-%{version}-pom.patch

BuildArch:        noarch

BuildRequires:    jpackage-utils
BuildRequires:    maven-local
BuildRequires:    maven-compiler-plugin
BuildRequires:    maven-install-plugin
BuildRequires:    maven-jar-plugin
BuildRequires:    maven-javadoc-plugin

Requires:         jpackage-utils
Source44: import.info

%description
Annotations to help generate RHQ plugin descriptors

%package javadoc
Summary:          Javadocs for %{name}
Group:            Development/Java
Requires:         jpackage-utils
BuildArch: noarch

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q -n pluginAnnotations
%patch0 -p1

%build
mvn-rpmbuild -Dproject.build.sourceEncoding=iso8859-1  install javadoc:aggregate

%install
install -d -m 755 $RPM_BUILD_ROOT%{_javadir}
install -d -m 755 $RPM_BUILD_ROOT%{_mavenpomdir}
install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}

# JAR
install -pm 644 target/rhq-pluginAnnotations-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}.jar

# POM
install -pm 644 pom.xml $RPM_BUILD_ROOT%{_mavenpomdir}/JPP-%{name}.pom

# DEPMAP
%add_maven_depmap JPP-%{name}.pom %{name}.jar

# APIDOCS
cp -rp target/site/apidocs/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}

%files
%{_mavenpomdir}/*
%{_mavendepmapfragdir}/*
%{_javadir}/*

%files javadoc
%{_javadocdir}/%{name}

%changelog
* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 3.0.4-alt2_5jpp7
- new release

* Mon Jul 14 2014 Igor Vlasenko <viy@altlinux.ru> 3.0.4-alt2_3jpp7
- NMU rebuild to move poms and fragments

* Thu Sep 13 2012 Igor Vlasenko <viy@altlinux.ru> 3.0.4-alt1_3jpp7
- new version

