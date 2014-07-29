# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-java
BuildRequires: maven
# END SourceDeps(oneline)
BuildRequires: geronimo-saaj
BuildRequires: /proc
BuildRequires: jpackage-compat
%global spec_ver 1.1
%global spec_name geronimo-jaxrpc_%{spec_ver}_spec

Name:             geronimo-jaxrpc
Version:          2.1
Release:          alt2_11jpp7
Summary:          Java EE: Java API for XML Remote Procedure Call v1.1
Group:            Development/Java
License:          ASL 2.0 and W3C

URL:              http://geronimo.apache.org/
Source0:          http://repo2.maven.org/maven2/org/apache/geronimo/specs/%{spec_name}/%{version}/%{spec_name}-%{version}-source-release.tar.gz
Source1:          %{name}.depmap
# Use parent pom files instead of unavailable 'genesis-java5-flava'
Patch1:           use_parent_pom.patch
BuildArch:        noarch

BuildRequires:    jpackage-utils
BuildRequires:    maven-local
BuildRequires:    geronimo-parent-poms
BuildRequires:    maven-resources-plugin
BuildRequires:    saaj_api
BuildRequires:    geronimo-osgi-locator
BuildRequires:    tomcat-servlet-3.0-api
BuildRequires:    maven-surefire-provider-junit

Requires:         jpackage-utils
Requires:         saaj_api
Requires:         geronimo-osgi-locator
Requires:         servlet >= 2.5

Provides:         jaxrpc_api = %{spec_ver}
Source44: import.info

#Provides:       jaxrpc = 0:1.1
#Provides:       jaxrpc_1_1_api = %{version}-%{release}
#Provides:       jaxrpc_api = 0:1.1

%description
This package contains the core JAX-RPC APIs for the client programming model. 

%package javadoc
Group:            Development/Java
Summary:          Javadoc for %{name}
Requires:         jpackage-utils
BuildArch: noarch

%description javadoc
This package contains the API documentation for %{name}.


%prep
%setup -q -n %{spec_name}-%{version}
iconv -f iso8859-1 -t utf-8 LICENSE > LICENSE.conv && mv -f LICENSE.conv LICENSE
sed -i 's/\r//' LICENSE NOTICE
%patch1 -p0

%build
mvn-rpmbuild \
        -Dmaven.local.depmap.file="%{SOURCE1}" \
        install javadoc:javadoc

%install
# jars
install -d -m 0755 %{buildroot}%{_javadir}
install -m 644 target/%{spec_name}-%{version}.jar %{buildroot}%{_javadir}/%{name}.jar
ln -s %{name}.jar %{buildroot}%{_javadir}/jaxrpc.jar

# poms
install -d -m 0755 %{buildroot}%{_mavenpomdir}
install -pm 644 pom.xml %{buildroot}%{_mavenpomdir}/JPP-%{name}.pom
%add_maven_depmap -a javax.xml:jaxrpc-api

# javadoc
install -d -m 0755 %{buildroot}%{_javadocdir}/%{name}
cp -pr target/site/api*/* %{buildroot}%{_javadocdir}/%{name}/

install -d $RPM_BUILD_ROOT/%_altdir; cat >$RPM_BUILD_ROOT/%_altdir/jaxrpc_geronimo-jaxrpc<<EOF
%{_javadir}/jaxrpc.jar	%{_javadir}/geronimo-jaxrpc.jar	10000
EOF
#install -d $RPM_BUILD_ROOT/%_altdir; cat >$RPM_BUILD_ROOT/%_altdir/jaxrpc_api_geronimo-jaxrpc<<EOF
#%{_javadir}/jaxrpc_api.jar	%{_javadir}/geronimo-jaxrpc.jar	10000
#EOF
#install -d $RPM_BUILD_ROOT/%_altdir; cat >$RPM_BUILD_ROOT/%_altdir/jaxrpc_1_1_api_geronimo-jaxrpc<<EOF
#%{_javadir}/jaxrpc_1_1_api.jar	%{_javadir}/geronimo-jaxrpc.jar	10000
#EOF


%files
%doc LICENSE NOTICE
%{_javadir}/*
%{_mavenpomdir}/*
%{_mavendepmapfragdir}/*

#%_altdir/jaxrpc_1_1_api_geronimo-jaxrpc
#%_altdir/jaxrpc_api_geronimo-jaxrpc
%_altdir/jaxrpc_geronimo-jaxrpc
%exclude %{_javadir}*/jaxrpc.jar


%files javadoc
%doc LICENSE NOTICE
%{_javadocdir}/%{name}

%changelog
* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 2.1-alt2_11jpp7
- new release

* Mon Jul 14 2014 Igor Vlasenko <viy@altlinux.ru> 2.1-alt2_9jpp7
- NMU rebuild to move poms and fragments

* Fri Aug 31 2012 Igor Vlasenko <viy@altlinux.ru> 2.1-alt1_9jpp7
- new version

