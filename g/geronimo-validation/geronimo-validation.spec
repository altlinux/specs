BuildRequires: /proc
BuildRequires: jpackage-compat
%global spec_ver 1.0
%global spec_name geronimo-validation_%{spec_ver}_spec

Name:           geronimo-validation
Version:        1.1
Release:        alt2_5jpp7
Summary:        Geronimo implementation of JSR 303
Group:          Development/Java
License:        ASL 2.0
URL:            http://apache.org/
# svn export https://svn.apache.org/repos/asf/geronimo/specs/tags/geronimo-validation_1.0_spec-1.1/
# tar caf geronimo-validation_1.0_spec-1.1.tar.xz geronimo-validation_1.0_spec-1.1
Source0:        %{spec_name}-%{version}.tar.xz
Patch0:         %{name}-build.patch
BuildArch:      noarch

BuildRequires:  jpackage-utils
BuildRequires:  maven
BuildRequires:  maven-surefire-plugin
BuildRequires:  maven-surefire-provider-junit
BuildRequires:  geronimo-parent-poms
BuildRequires:  geronimo-osgi-support
Requires:       jpackage-utils
Source44: import.info

%description
This is the Geronimo implementation of JSR-303, the Bean
Validation API specification.

%package javadoc
Group: Development/Java
Summary:        Javadoc for %{name}
Requires:       jpackage-utils
BuildArch: noarch

%description javadoc
Javadoc for %{name}.

%prep
%setup -q -n %{spec_name}-%{version}
%patch0 -p1

%build
mvn-rpmbuild install javadoc:aggregate

%install
install -d -m 0755 $RPM_BUILD_ROOT%{_javadir}
install -pm 0644 target/%{spec_name}-%{version}.jar \
  $RPM_BUILD_ROOT%{_javadir}/%{name}.jar
install -d -m 0755 $RPM_BUILD_ROOT%{_mavenpomdir}
install -pm 0644 pom.xml \
        $RPM_BUILD_ROOT%{_mavenpomdir}/JPP-%{name}.pom 
install -d -m 0755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}
cp -rp target/site/apidocs $RPM_BUILD_ROOT%{_javadocdir}/%{name}/

%add_maven_depmap JPP-%{name}.pom %{name}.jar -a javax.validation:validation-api

%files
%doc LICENSE NOTICE
%{_mavenpomdir}/JPP-%{name}.pom
%{_mavendepmapfragdir}/%{name}
%{_javadir}/%{name}.jar

%files javadoc
%doc LICENSE NOTICE
%{_javadocdir}/%{name}

%changelog
* Mon Jul 14 2014 Igor Vlasenko <viy@altlinux.ru> 1.1-alt2_5jpp7
- NMU rebuild to move poms and fragments

* Fri Aug 31 2012 Igor Vlasenko <viy@altlinux.ru> 1.1-alt1_5jpp7
- new version

