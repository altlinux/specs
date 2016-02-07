Name: jetty8-client
Version: 8.1.17
Summary: Jetty asynchronous HTTP client
License: (ASL 2.0 or EPL) and MIT
Url: http://www.eclipse.org/jetty
Packager: Igor Vlasenko <viy@altlinux.ru>
Provides: jetty8-client = 8.1.17-1.fc23
Provides: mvn(org.eclipse.jetty:jetty-client:8.1) = 8.1.17.v20150415
Provides: mvn(org.eclipse.jetty:jetty-client:8.1.14.v20131031) = 8.1.17.v20150415
Provides: mvn(org.eclipse.jetty:jetty-client:8.1.17.v20150415) = 8.1.17.v20150415
Provides: mvn(org.eclipse.jetty:jetty-client:pom:8.1) = 8.1.17.v20150415
Provides: mvn(org.eclipse.jetty:jetty-client:pom:8.1.14.v20131031) = 8.1.17.v20150415
Provides: mvn(org.eclipse.jetty:jetty-client:pom:8.1.17.v20150415) = 8.1.17.v20150415
Requires: java-headless
Requires: jpackage-utils
Requires: mvn(org.eclipse.jetty:jetty-http:8.1.17.v20150415)

BuildArch: noarch
Group: Development/Java
Release: alt0.1jpp
Source: jetty8-client-8.1.17-1.fc23.cpio

%description
This package contains Jetty asynchronous HTTP client.

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
* Mon Feb 08 2016 Igor Vlasenko <viy@altlinux.ru> 8.1.17-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

