Name: jboss-websocket-1.1-api
Version: 1.1.0
Summary: JSR-356: Java WebSocket 1.1 API
License: CDDL or GPLv2 with exceptions
Url: https://github.com/jboss/jboss-websocket-api_spec
Packager: Igor Vlasenko <viy@altlinux.ru>
Provides: jboss-websocket-1.1-api = 1.1.0-2.fc23
Provides: mvn(org.jboss.spec.javax.websocket:jboss-websocket-api_1.1_spec) = 1.1.0.Final
Provides: mvn(org.jboss.spec.javax.websocket:jboss-websocket-api_1.1_spec:pom:) = 1.1.0.Final
Requires: java-headless
Requires: jpackage-utils
Requires: mvn(com.sun:tools)

BuildArch: noarch
Group: Development/Java
Release: alt0.1jpp
Source: jboss-websocket-1.1-api-1.1.0-2.fc23.cpio

%description
The JSR-356: Java WebSocket 1.1 API classes.

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
* Thu Feb 04 2016 Igor Vlasenko <viy@altlinux.ru> 1.1.0-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

