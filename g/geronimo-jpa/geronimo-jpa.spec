BuildRequires: /proc
BuildRequires: jpackage-compat
%global spec_ver 3.0
%global spec_name geronimo-jpa_%{spec_ver}_spec

Name:           geronimo-jpa
Version:        1.1.1
Release:        alt2_8jpp7
Summary:        Java persistence API implementation

Group:          Development/Java
License:        ASL 2.0
URL:            http://geronimo.apache.org/
# Unfortunately no source release was created in
# http://repo2.maven.org/maven2/org/apache/geronimo/specs/geronimo-jpa_3.0_spec/1.1.1/
# so we do:
# svn export http://svn.apache.org/repos/asf/geronimo/specs/tags/geronimo-jpa_3.0_spec-1.1.1
# tar caf geronimo-jpa_3.0_spec-1.1.1.tar.xz geronimo-jpa_3.0_spec-1.1.1
Source0:       %{spec_name}-%{version}.tar.xz

BuildArch:     noarch

# This pulls in all of the required java and maven stuff
BuildRequires:  geronimo-parent-poms
BuildRequires:  maven-resources-plugin

Provides:       jpa_api = %{spec_ver}
Source44: import.info

#Provides:       jpa_3_0_api = %{version}-%{release}
#Provides:       jpa_api = 0:3.0



%description
The Java Persistence API is a new programming model under EJB 3.0
specification (JSR220) for the management of persistence and
object/relational mapping with Java EE and Java SE. Geronimo JPA is
one implementation of this specification.


%package javadoc
Summary:   API documentation for %{name}
Group:     Development/Java
Requires:  jpackage-utils
BuildArch: noarch

%description javadoc
%{summary}.

%prep
%setup -q -n %{spec_name}-%{version}

%build
mvn-rpmbuild install javadoc:javadoc


%install
install -d -m 755 $RPM_BUILD_ROOT%{_javadir}

install -m 644 target/%{spec_name}-%{version}.jar \
  $RPM_BUILD_ROOT%{_javadir}/%{name}.jar

# Also provide compat symlinks
pushd $RPM_BUILD_ROOT%{_javadir}
ln -sf %{name}.jar %{spec_name}-%{version}.jar
ln -sf %{name}.jar jpa.jar
popd

install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}
cp -pr target/site/apidocs/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}

install -d -m 755 $RPM_BUILD_ROOT%{_mavenpomdir}
install -pm 644 pom.xml $RPM_BUILD_ROOT/%{_mavenpomdir}/JPP-%{name}.pom

%add_maven_depmap JPP-%{name}.pom %{name}.jar -a 'javax.persistence:persistence-api'

#install -d $RPM_BUILD_ROOT/%_altdir; cat >$RPM_BUILD_ROOT/%_altdir/jpa_api_geronimo-jpa<<EOF
#%{_javadir}/jpa_api.jar	%{_javadir}/geronimo-jpa.jar	30100
#EOF
#install -d $RPM_BUILD_ROOT/%_altdir; cat >$RPM_BUILD_ROOT/%_altdir/jpa_3_0_api_geronimo-jpa<<EOF
#%{_javadir}/jpa_3_0_api.jar	%{_javadir}/geronimo-jpa.jar	30100
#EOF


%pre javadoc
[ $1 -gt 1 ] && [ -L %{_javadocdir}/%{name} ] && \
rm -rf $(readlink -f %{_javadocdir}/%{name}) %{_javadocdir}/%{name} || :

%files
%doc LICENSE.txt NOTICE.txt
%{_javadir}/*.jar
%{_mavenpomdir}/JPP-%{name}.pom
%{_mavendepmapfragdir}/%{name}

#%_altdir/jpa_3_0_api_geronimo-jpa
#%_altdir/jpa_api_geronimo-jpa


%files javadoc
%doc LICENSE.txt NOTICE.txt
%{_javadocdir}/%{name}



%changelog
* Mon Jul 14 2014 Igor Vlasenko <viy@altlinux.ru> 1.1.1-alt2_8jpp7
- NMU rebuild to move poms and fragments

* Thu Aug 30 2012 Igor Vlasenko <viy@altlinux.ru> 1.1.1-alt1_8jpp7
- new version

