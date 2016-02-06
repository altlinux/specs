Name: jboss-servlet-2.5-api
Version: 1.0.1
Summary: Java Servlet 2.5 API
License: ASL 2.0 and W3C
Url: http://www.jboss.org
Packager: Igor Vlasenko <viy@altlinux.ru>
Provides: jboss-servlet-2.5-api = 1.0.1-8.fc22
Provides: mvn(org.jboss.spec.javax.servlet:jboss-servlet-api_2.5_spec) = 1.0.1.Final
Provides: mvn(org.jboss.spec.javax.servlet:jboss-servlet-api_2.5_spec:pom:) = 1.0.1.Final
Requires: java-headless
Requires: jpackage-utils
Requires: jpackage-utils

BuildArch: noarch
Group: Development/Java
Release: alt2jpp
Source: jboss-servlet-2.5-api-1.0.1-8.fc22.cpio

%description
The Java Servlet 2.5 API classes.

# sometimes commpress gets crazy (see maven-scm-javadoc for details)
%set_compress_method none
%prep
cpio -idmu --quiet --no-absolute-filenames < %{SOURCE0}

%build
cpio --list < %{SOURCE0} | sed -e 's,^\.,,' > %name-list

%install
mkdir -p $RPM_BUILD_ROOT
for i in usr var etc; do
[ -d $i ] && mv $i $RPM_BUILD_ROOT/
done


%files -f %name-list

%changelog
* Sat Feb 06 2016 Igor Vlasenko <viy@altlinux.ru> 1.0.1-alt2jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

* Fri Aug 01 2014 Igor Vlasenko <viy@altlinux.ru> 1.0.1-alt1_3jpp7
- new version

