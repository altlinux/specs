Name: maven-wagon-http
Version: 2.9
Summary: http module for maven-wagon
License: ASL 2.0
Url: http://maven.apache.org/wagon
Epoch: 0
Packager: Igor Vlasenko <viy@altlinux.ru>
Provides: maven-wagon-http = 0:2.9-4.fc23
Provides: mvn(org.apache.maven.wagon:wagon-http) = 2.9
Provides: mvn(org.apache.maven.wagon:wagon-http::shaded:) = 2.9
Provides: mvn(org.apache.maven.wagon:wagon-http:pom:) = 2.9
Provides: mvn(org.apache.maven.wagon:wagon-http:pom:shaded:) = 2.9
Requires: java-headless
Requires: jpackage-utils
Requires: mvn(commons-logging:commons-logging)
Requires: mvn(org.apache.httpcomponents:httpclient)
Requires: mvn(org.apache.httpcomponents:httpcore)
Requires: mvn(org.apache.maven.wagon:wagon-http-shared)
Requires: mvn(org.apache.maven.wagon:wagon-provider-api)

BuildArch: noarch
Group: Development/Java
Release: alt0.1jpp
Source: maven-wagon-http-2.9-4.fc23.cpio

%description
http module for maven-wagon.

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
* Wed Jan 20 2016 Igor Vlasenko <viy@altlinux.ru> 0:2.9-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

