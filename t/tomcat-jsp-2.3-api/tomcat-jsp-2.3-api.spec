Name: tomcat-jsp-2.3-api
Version: 8.0.26
Summary: Apache Tomcat JSP API implementation classes
License: ASL 2.0
Url: http://tomcat.apache.org/
Epoch: 1
Packager: Igor Vlasenko <viy@altlinux.ru>
Provides: jsp = 2.3
Provides: mvn(org.apache.tomcat:tomcat-jsp-api) = 8.0.26
Provides: mvn(org.apache.tomcat:tomcat-jsp-api:pom:) = 8.0.26
Provides: mvn(org.eclipse.jetty.orbit:javax.servlet.jsp) = 8.0.26
Provides: mvn(org.eclipse.jetty.orbit:javax.servlet.jsp:pom:) = 8.0.26
Provides: tomcat-jsp-2.3-api = 1:8.0.26-1.fc23
Requires: /bin/sh
Requires: /bin/sh
Requires: chkconfig
Requires: chkconfig
Requires: java-headless
Requires: jpackage-utils
Requires: tomcat-el-3.0-api
Requires: tomcat-servlet-3.1-api

BuildArch: noarch
Group: Development/Java
Release: alt0.1jpp
Source: tomcat-jsp-2.3-api-8.0.26-1.fc23.cpio
Obsoletes: tomcat-jsp-2.2-api < 8
Provides: tomcat-jsp-2.2-api = %version

%description
Apache Tomcat JSP API implementation classes.

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

%post
/usr/sbin/update-alternatives --install /usr/share/java/jsp.jar jsp \
    /usr/share/java/tomcat-jsp-2.3-api.jar 20200

%postun
if [ "$1" = "0" ]; then
    /usr/sbin/update-alternatives --remove jsp \
        /usr/share/java/tomcat-jsp-2.3-api.jar
fi


%files -f %name-list

%changelog
* Wed Feb 03 2016 Igor Vlasenko <viy@altlinux.ru> 1:8.0.26-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

