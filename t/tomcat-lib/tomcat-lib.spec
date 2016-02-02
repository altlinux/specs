Name: tomcat-lib
Version: 8.0.26
Summary: Libraries needed to run the Tomcat Web container
License: ASL 2.0
Url: http://tomcat.apache.org/
Epoch: 1
Packager: Igor Vlasenko <viy@altlinux.ru>
Provides: mvn(org.apache.tomcat:tomcat-annotations-api) = 8.0.26
Provides: mvn(org.apache.tomcat:tomcat-annotations-api:pom:) = 8.0.26
Provides: mvn(org.apache.tomcat:tomcat-api) = 8.0.26
Provides: mvn(org.apache.tomcat:tomcat-api:pom:) = 8.0.26
Provides: mvn(org.apache.tomcat:tomcat-catalina) = 8.0.26
Provides: mvn(org.apache.tomcat:tomcat-catalina-ha) = 8.0.26
Provides: mvn(org.apache.tomcat:tomcat-catalina-ha:pom:) = 8.0.26
Provides: mvn(org.apache.tomcat:tomcat-catalina:pom:) = 8.0.26
Provides: mvn(org.apache.tomcat:tomcat-coyote) = 8.0.26
Provides: mvn(org.apache.tomcat:tomcat-coyote:pom:) = 8.0.26
Provides: mvn(org.apache.tomcat:tomcat-jasper) = 8.0.26
Provides: mvn(org.apache.tomcat:tomcat-jasper-el) = 8.0.26
Provides: mvn(org.apache.tomcat:tomcat-jasper-el:pom:) = 8.0.26
Provides: mvn(org.apache.tomcat:tomcat-jasper:pom:) = 8.0.26
Provides: mvn(org.apache.tomcat:tomcat-jdbc) = 8.0.26
Provides: mvn(org.apache.tomcat:tomcat-jdbc:pom:) = 8.0.26
Provides: mvn(org.apache.tomcat:tomcat-jni) = 8.0.26
Provides: mvn(org.apache.tomcat:tomcat-jni:pom:) = 8.0.26
Provides: mvn(org.apache.tomcat:tomcat-juli) = 8.0.26
Provides: mvn(org.apache.tomcat:tomcat-juli:pom:) = 8.0.26
Provides: mvn(org.apache.tomcat:tomcat-tribes) = 8.0.26
Provides: mvn(org.apache.tomcat:tomcat-tribes:pom:) = 8.0.26
Provides: mvn(org.apache.tomcat:tomcat-util) = 8.0.26
Provides: mvn(org.apache.tomcat:tomcat-util-scan) = 8.0.26
Provides: mvn(org.apache.tomcat:tomcat-util-scan:pom:) = 8.0.26
Provides: mvn(org.apache.tomcat:tomcat-util:pom:) = 8.0.26
Provides: tomcat-lib = 1:8.0.26-1.fc23
Requires: apache-commons-collections
Requires: apache-commons-dbcp
Requires: apache-commons-pool
Requires: coreutils
Requires: ecj
Requires: java-headless
Requires: jpackage-utils
Requires: tomcat-el-3.0-api
Requires: tomcat-jsp-2.3-api
Requires: tomcat-servlet-3.1-api
Provides: tomcat = 1:%version

BuildArch: noarch
Group: Development/Java
Release: alt0.1jpp
Source: tomcat-lib-8.0.26-1.fc23.cpio

%description
Libraries needed to run the Tomcat Web container.

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
* Wed Feb 03 2016 Igor Vlasenko <viy@altlinux.ru> 1:8.0.26-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

