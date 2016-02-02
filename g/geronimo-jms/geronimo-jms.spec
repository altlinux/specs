%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
%global spec_name geronimo-jms_1.1_spec

Name:		geronimo-jms
Version:	1.1.1
Release:	alt3_20jpp8
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
BuildRequires:  maven-local
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
%mvn_file  : %{name} %{spec_name} jms
%mvn_alias : javax.jms:jms
%mvn_build -f


%install
%mvn_install

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

%files -f .mfiles
%doc LICENSE.txt NOTICE.txt

#%_altdir/jms_1_1_api_geronimo-jms
#%_altdir/jms_api_geronimo-jms
%_altdir/jms_geronimo-jms
%exclude %{_javadir}*/jms.jar


%files javadoc -f .mfiles-javadoc
%doc LICENSE.txt NOTICE.txt


%changelog
* Tue Feb 02 2016 Igor Vlasenko <viy@altlinux.ru> 1.1.1-alt3_20jpp8
- new version

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 1.1.1-alt3_17jpp7
- new release

* Sat Aug 23 2014 Igor Vlasenko <viy@altlinux.ru> 1.1.1-alt3_16jpp7
- new release

* Thu Aug 21 2014 Igor Vlasenko <viy@altlinux.ru> 1.1.1-alt3_13jpp7
- added maven-local BR:

* Mon Jul 14 2014 Igor Vlasenko <viy@altlinux.ru> 1.1.1-alt2_13jpp7
- NMU rebuild to move poms and fragments

* Fri Aug 31 2012 Igor Vlasenko <viy@altlinux.ru> 1.1.1-alt1_13jpp7
- new version

