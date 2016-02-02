Name: tomcat-servlet-3.1-api
Version: 8.0.26
Summary: Apache Tomcat Servlet API implementation classes
License: ASL 2.0
Url: http://tomcat.apache.org/
Epoch: 1
Packager: Igor Vlasenko <viy@altlinux.ru>
Provides: mvn(org.apache.tomcat:tomcat-servlet-api) = 8.0.26
Provides: mvn(org.apache.tomcat:tomcat-servlet-api:pom:) = 8.0.26
Provides: servlet = 3.1
Provides: servlet3
Provides: servlet6
Provides: tomcat-servlet-3.1-api = 1:8.0.26-1.fc23
Requires: /bin/sh
Requires: /bin/sh
Requires: chkconfig
Requires: chkconfig
Requires: java-headless
Requires: jpackage-utils

BuildArch: noarch
Group: Development/Java
Release: alt0.1jpp
Source: tomcat-servlet-3.1-api-8.0.26-1.fc23.cpio
Obsoletes: tomcat-servlet-3.0-api < 8
Provides: tomcat-servlet-3.0-api = %version

%description
Apache Tomcat Servlet API implementation classes.

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
/usr/sbin/update-alternatives --install /usr/share/java/servlet.jar servlet \
    /usr/share/java/tomcat-servlet-3.1-api.jar 30000

%postun
if [ "$1" = "0" ]; then
    /usr/sbin/update-alternatives --remove servlet \
        /usr/share/java/tomcat-servlet-3.1-api.jar
fi


%files -f %name-list

%changelog
* Wed Feb 03 2016 Igor Vlasenko <viy@altlinux.ru> 1:8.0.26-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

