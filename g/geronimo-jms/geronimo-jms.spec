BuildRequires: /proc
BuildRequires: jpackage-compat
%global spec_name geronimo-jms_1.1_spec

Name:		geronimo-jms
Version:	1.1.1
Release:	alt2_13jpp7
Summary:	J2EE JMS v1.1 API

Group:		Development/Java
License:	ASL 2.0
URL:		http://geronimo.apache.org/
# svn export http://svn.apache.org/repos/asf/geronimo/specs/tags/%{spec_name}-%{version}/
Source0:	%{spec_name}-%{version}.tar.bz
# Remove unavailable dependencies
Patch0:		geronimo-jms-1.1-api-remove-mockobjects.patch

BuildArch:	noarch

# This pulls in almost all of the required java and maven stuff
BuildRequires:	geronimo-parent-poms
BuildRequires:	maven-resources-plugin

# Ensure a smooth transition from geronimo-specs
Provides:	jms = %{version}-%{release}
Obsoletes:	geronimo-specs <= 1.0-3.3
Obsoletes:	geronimo-specs-compat <= 1.0-3.3
Source44: import.info

#Provides:       jms_1_1_api = %{version}-%{release}
#Provides:       jms_api = 0:1.1
# drop the following asap
#Provides:       jms = 0:1.1

%description
The Java Message Service (JMS) API is a messaging standard that allows
application components based on the Java 2 Platform, Enterprise Edition
(J2EE) to create, send, receive, and read messages. It enables distributed
communication that is loosely coupled, reliable, and asynchronous.

%package javadoc
Summary:	API documentation for %{name}
Group:		Development/Java
Requires:	jpackage-utils >= 0:1.7.5
BuildArch:	noarch

%description javadoc
%{summary}.

%prep
%setup -q -n %{spec_name}-%{version}
%patch0 -p1


%build
mvn-rpmbuild \
	-Dmaven.test.skip=true \
	install javadoc:javadoc


%install
install -d -m 755 $RPM_BUILD_ROOT%{_javadir}

install -m 644 target/%{spec_name}-%{version}.jar \
  $RPM_BUILD_ROOT%{_javadir}/%{name}.jar

# Also provide compat symlinks
pushd $RPM_BUILD_ROOT%{_javadir}
ln -sf %{name}.jar %{spec_name}.jar
ln -sf %{name}.jar jms.jar
popd

install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}

install -d -m 755 $RPM_BUILD_ROOT%{_mavenpomdir}
install -pm 644 pom.xml $RPM_BUILD_ROOT/%{_mavenpomdir}/JPP-%{name}.pom

%add_maven_depmap JPP-%{name}.pom %{name}.jar -a "javax.jms:jms"

install -d $RPM_BUILD_ROOT/%_altdir; cat >$RPM_BUILD_ROOT/%_altdir/jms_geronimo-jms<<EOF
%{_javadir}/jms.jar	%{_javadir}/geronimo-jms.jar	10200
EOF
#install -d $RPM_BUILD_ROOT/%_altdir; cat >$RPM_BUILD_ROOT/%_altdir/jms_api_geronimo-jms<<EOF
#%{_javadir}/jms_api.jar	%{_javadir}/geronimo-jms.jar	10200
#EOF
#install -d $RPM_BUILD_ROOT/%_altdir; cat >$RPM_BUILD_ROOT/%_altdir/jms_1_1_api_geronimo-jms<<EOF
#%{_javadir}/jms_1_1_api.jar	%{_javadir}/geronimo-jms.jar	10200
#EOF


%pre javadoc
[ $1 -gt 1 ] && [ -L %{_javadocdir}/%{name} ] && \
rm -rf $(readlink -f %{_javadocdir}/%{name}) %{_javadocdir}/%{name} || :

%files
%doc LICENSE.txt NOTICE.txt
%{_javadir}/%{name}.jar
%{_javadir}/%{spec_name}.jar
%{_javadir}/jms.jar
%{_mavendepmapfragdir}/%{name}
%{_mavenpomdir}/JPP-%{name}.pom

#%_altdir/jms_1_1_api_geronimo-jms
#%_altdir/jms_api_geronimo-jms
%_altdir/jms_geronimo-jms
%exclude %{_javadir}*/jms.jar


%files javadoc
%doc LICENSE.txt NOTICE.txt
%{_javadocdir}/%{name}


%changelog
* Mon Jul 14 2014 Igor Vlasenko <viy@altlinux.ru> 1.1.1-alt2_13jpp7
- NMU rebuild to move poms and fragments

* Fri Aug 31 2012 Igor Vlasenko <viy@altlinux.ru> 1.1.1-alt1_13jpp7
- new version

