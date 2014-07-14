BuildRequires: /proc
BuildRequires: jpackage-compat
%global spec_name geronimo-jta_1.1_spec

Name:		geronimo-jta
Version:	1.1.1
Release:	alt2_10jpp7
Summary:	J2EE JTA v1.1 API

Group:		Development/Java
License:	ASL 2.0
URL:		http://geronimo.apache.org/
# svn export http://svn.apache.org/repos/asf/geronimo/specs/tags/%{spec_name}-%{version}/
Source0:	%{spec_name}-%{version}.tar.bz

BuildArch:	noarch

# This pulls in almost all of the required java and maven stuff
BuildRequires:	geronimo-parent-poms
BuildRequires:	maven-resources-plugin

# Ensure a smooth transition from geronimo-specs
Provides:	jta = %{version}-%{release}
Obsoletes:	geronimo-specs <= 1.0-3.3
Obsoletes:	geronimo-specs-compat <= 1.0-3.3
Source44: import.info

#Provides:       jta_1_1_api = %{version}-%{release}
#Provides:       jta_api = 0:1.1
# drop asap
#Provides:       jta = 0:1.1

%description
Java Transaction API (JTA) specifies standard Java interfaces between a
transaction manager and the parties involved in a distributed transaction
system: the resource manager, the application server, and the transactional
applications.

%package javadoc
Summary:	API documentation for %{name}
Group:		Development/Java
Requires:	jpackage-utils >= 0:1.7.5
BuildArch:	noarch

%description javadoc
%{summary}.

%prep
%setup -q -n %{spec_name}-%{version}


%build
mvn-rpmbuild -Dmaven.test.skip=true \
	         install javadoc:javadoc


%install

install -d -m 755 $RPM_BUILD_ROOT%{_javadir}

install -m 644 target/%{spec_name}-%{version}.jar \
  $RPM_BUILD_ROOT%{_javadir}/%{name}.jar

# Also provide compat symlinks
pushd $RPM_BUILD_ROOT%{_javadir}
ln -sf %{name}.jar %{spec_name}.jar
ln -sf %{name}.jar jta.jar
popd

install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}
cp -pr target/site/apidocs/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}

install -d -m 755 $RPM_BUILD_ROOT%{_mavenpomdir}
install -pm 644 pom.xml $RPM_BUILD_ROOT/%{_mavenpomdir}/JPP-%{name}.pom

%add_maven_depmap JPP-%{name}.pom %{name}.jar -a "javax.transaction:jta"

install -d $RPM_BUILD_ROOT/%_altdir; cat >$RPM_BUILD_ROOT/%_altdir/jta_geronimo-jta<<EOF
%{_javadir}/jta.jar	%{_javadir}/geronimo-jta.jar	10200
EOF
#install -d $RPM_BUILD_ROOT/%_altdir; cat >$RPM_BUILD_ROOT/%_altdir/jta_api_geronimo-jta<<EOF
#%{_javadir}/jta_api.jar	%{_javadir}/geronimo-jta.jar	10200
#EOF
#install -d $RPM_BUILD_ROOT/%_altdir; cat >$RPM_BUILD_ROOT/%_altdir/jta_1_1_api_geronimo-jta<<EOF
#%{_javadir}/jta_1_1_api.jar	%{_javadir}/geronimo-jta.jar	10200
#EOF


%pre javadoc
[ $1 -gt 1 ] && [ -L %{_javadocdir}/%{name} ] && \
rm -rf $(readlink -f %{_javadocdir}/%{name}) %{_javadocdir}/%{name} || :

%files
%doc LICENSE.txt NOTICE.txt
%{_javadir}/%{name}.jar
%{_javadir}/%{spec_name}.jar
%{_javadir}/jta.jar
%{_mavendepmapfragdir}/%{name}
%{_mavenpomdir}/JPP-%{name}.pom

#%_altdir/jta_1_1_api_geronimo-jta
#%_altdir/jta_api_geronimo-jta
%_altdir/jta_geronimo-jta


%files javadoc
%doc LICENSE.txt NOTICE.txt
%{_javadocdir}/%{name}


%changelog
* Mon Jul 14 2014 Igor Vlasenko <viy@altlinux.ru> 1.1.1-alt2_10jpp7
- NMU rebuild to move poms and fragments

* Fri Aug 31 2012 Igor Vlasenko <viy@altlinux.ru> 1.1.1-alt1_10jpp7
- new version

