Name: tomcat-el-3.0-api
Version: 8.0.26
Summary: Expression Language v3.0 API
License: ASL 2.0
Url: http://tomcat.apache.org/
Epoch: 1
Packager: Igor Vlasenko <viy@altlinux.ru>
Provides: el_api = 3.0
Provides: mvn(org.apache.tomcat:tomcat-el-api) = 8.0.26
Provides: mvn(org.apache.tomcat:tomcat-el-api:pom:) = 8.0.26
Provides: mvn(org.eclipse.jetty.orbit:javax.el) = 8.0.26
Provides: mvn(org.eclipse.jetty.orbit:javax.el:pom:) = 8.0.26
Provides: tomcat-el-3.0-api = 1:8.0.26-1.fc23
Requires: /bin/sh
Requires: /bin/sh
Requires: chkconfig
Requires: chkconfig
Requires: java-headless
Requires: jpackage-utils

BuildArch: noarch
Group: Development/Java
Release: alt0.1jpp
Source: tomcat-el-3.0-api-8.0.26-1.fc23.cpio
Obsoletes: tomcat-el-2.2-api < 8
Provides: tomcat-el-2.2-api = %version

%description
Expression Language 3.0.

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
/usr/sbin/update-alternatives --install /usr/share/java/elspec.jar elspec \
   /usr/share/java/tomcat-el-3.0-api.jar 20300

%postun
if [ "$1" = "0" ]; then
    /usr/sbin/update-alternatives --remove elspec \
        /usr/share/java/tomcat-el-3.0-api.jar
fi


%files -f %name-list

%changelog
* Wed Feb 03 2016 Igor Vlasenko <viy@altlinux.ru> 1:8.0.26-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

