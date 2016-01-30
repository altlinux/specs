Name: glassfish-servlet-api
Version: 3.1.0
Summary: Java Servlet API
License: (CDDL or GPLv2 with exceptions) and ASL 2.0
Url: http://servlet-spec.java.net
Packager: Igor Vlasenko <viy@altlinux.ru>
Provides: glassfish-servlet-api = 3.1.0-9.fc23
Provides: mvn(javax.servlet:javax.servlet-api) = 3.1.0
Provides: mvn(javax.servlet:javax.servlet-api:pom:) = 3.1.0
Provides: mvn(javax.servlet:servlet-api) = 3.1.0
Provides: mvn(javax.servlet:servlet-api:pom:) = 3.1.0
Provides: mvn(org.apache.geronimo.specs:geronimo-servlet_3.0_spec) = 3.1.0
Provides: mvn(org.apache.geronimo.specs:geronimo-servlet_3.0_spec:pom:) = 3.1.0
Provides: mvn(org.eclipse.jetty.orbit:javax.servlet) = 3.1.0
Provides: mvn(org.eclipse.jetty.orbit:javax.servlet:pom:) = 3.1.0
Requires: java-headless
Requires: jpackage-utils

BuildArch: noarch
Group: Development/Java
Release: alt2jpp
Source: glassfish-servlet-api-3.1.0-9.fc23.cpio

%description
The javax.servlet package contains a number of classes
and interfaces that describe and define the contracts between
a servlet class and the runtime environment provided for
an instance of such a class by a conforming servlet container.

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
* Mon Jan 25 2016 Igor Vlasenko <viy@altlinux.ru> 3.1.0-alt2jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

* Wed Aug 27 2014 Igor Vlasenko <viy@altlinux.ru> 3.1.0-alt1_2jpp7
- new release

