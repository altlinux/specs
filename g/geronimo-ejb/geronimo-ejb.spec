BuildRequires: geronimo-annotation geronimo-interceptor
BuildRequires: /proc
BuildRequires: jpackage-compat
%global spec_ver 3.1
%global spec_name geronimo-ejb_%{spec_ver}_spec

Name:             geronimo-ejb
Version:          1.0
Release:          alt2_7jpp7
Summary:          Java EE: EJB API v3.1
Group:            Development/Java
License:          ASL 2.0
URL:              http://geronimo.apache.org

Source0:          http://repo2.maven.org/maven2/org/apache/geronimo/specs/%{spec_name}/%{version}/%{spec_name}-%{version}-source-release.tar.gz
# Use parent pom files instead of unavailable 'genesis-java5-flava'
Patch1:           use_parent_pom.patch

BuildArch:        noarch

BuildRequires:    jpackage-utils
BuildRequires:    maven2 >= 2.2.1
BuildRequires:    geronimo-parent-poms
BuildRequires:    maven-resources-plugin
BuildRequires:    jta
BuildRequires:    interceptor_api
BuildRequires:    annotation_api
BuildRequires:    jaxrpc_api
BuildRequires:    geronimo-osgi-locator

Requires:         jta
Requires:         interceptor_api
Requires:         annotation_api
Requires:         jaxrpc_api
Requires:         geronimo-osgi-locator
Requires:         jpackage-utils

Provides:         ejb_api = %{spec_ver}
Source44: import.info

#Provides:       ejb = 0:3.1
#Provides:       ejb_api = 0:3.1
##Provides:       ejb_3_1_api = %{version}-%{release}

%description
Contains the Enterprise JavaBeans classes and interfaces that define the 
contracts between the enterprise bean and its clients and between the 
enterprise bean and the EJB container. 

%package javadoc
Group:            Development/Java
Summary:          Javadoc for %{name}
Requires:         jpackage-utils
BuildArch: noarch

%description javadoc
This package contains the API documentation for %{name}.


%prep
%setup -q -n %{spec_name}-%{version}
sed -i 's/\r//' LICENSE
%patch1 -p0

%build
mvn-rpmbuild install javadoc:javadoc

%install
# jars
install -d -m 0755 %{buildroot}%{_javadir}
install -m 644 target/%{spec_name}-%{version}.jar %{buildroot}%{_javadir}/%{name}.jar
ln -s %{name}.jar %{buildroot}%{_javadir}/ejb.jar

# poms
install -d -m 0755 %{buildroot}%{_mavenpomdir}
install -pm 644 pom.xml %{buildroot}%{_mavenpomdir}/JPP-%{name}.pom
%add_maven_depmap JPP-%{name}.pom %{name}.jar -a "org.apache.geronimo.specs:geronimo-ejb_2.1_spec,org.apache.geronimo.specs:geronimo-ejb_3.0_spec,javax.ejb:ejb"

# javadoc
install -d -m 0755 %{buildroot}%{_javadocdir}/%{name}
cp -pr target/site/api*/* %{buildroot}%{_javadocdir}/%{name}/

install -d $RPM_BUILD_ROOT/%_altdir; cat >$RPM_BUILD_ROOT/%_altdir/ejb_geronimo-ejb<<EOF
%{_javadir}/ejb.jar	%{_javadir}/geronimo-ejb.jar	30100
EOF
# install -d $RPM_BUILD_ROOT/%_altdir; cat >$RPM_BUILD_ROOT/%_altdir/ejb_api_geronimo-ejb<<EOF
# %{_javadir}/ejb_api.jar	%{_javadir}/geronimo-ejb.jar	30100
# EOF
# install -d $RPM_BUILD_ROOT/%_altdir; cat >$RPM_BUILD_ROOT/%_altdir/ejb_3_0_api_geronimo-ejb<<EOF
# %{_javadir}/ejb_3_0_api.jar	%{_javadir}/geronimo-ejb.jar	100
# EOF
# install -d $RPM_BUILD_ROOT/%_altdir; cat >$RPM_BUILD_ROOT/%_altdir/ejb_3_1_api_geronimo-ejb<<EOF
# %{_javadir}/ejb_3_1_api.jar	%{_javadir}/geronimo-ejb.jar	30100
# EOF


%files
%doc LICENSE
%{_javadir}/*
%{_mavenpomdir}/*
%{_mavendepmapfragdir}/*

#%_altdir/ejb_3_1_api_geronimo-ejb
#%_altdir/ejb_3_0_api_geronimo-ejb
#%_altdir/ejb_api_geronimo-ejb
%_altdir/ejb_geronimo-ejb
%exclude %{_javadir}*/ejb.jar


%files javadoc
%doc LICENSE
%{_javadocdir}/%{name}

%changelog
* Mon Jul 14 2014 Igor Vlasenko <viy@altlinux.ru> 1.0-alt2_7jpp7
- NMU rebuild to move poms and fragments

* Fri Aug 31 2012 Igor Vlasenko <viy@altlinux.ru> 1.0-alt1_7jpp7
- new version

