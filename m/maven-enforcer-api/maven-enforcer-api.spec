Name: maven-enforcer-api
Version: 1.4
Summary: Enforcer API
License: ASL 2.0
Url: http://maven.apache.org/enforcer
Epoch: 0
Packager: Igor Vlasenko <viy@altlinux.ru>
Provides: maven-enforcer-api = 1.4-2.fc23
Provides: mvn(org.apache.maven.enforcer:enforcer-api) = 1.4
Provides: mvn(org.apache.maven.enforcer:enforcer-api:pom:) = 1.4
Requires: java-headless
Requires: jpackage-utils
Requires: mvn(org.apache.maven:maven-plugin-api)
Requires: mvn(org.codehaus.plexus:plexus-container-default)

BuildArch: noarch
Group: Development/Java
Release: alt0.1jpp
Source: maven-enforcer-api-1.4-2.fc23.cpio

%description
This component provides the generic interfaces needed to
implement custom rules for the maven-enforcer-plugin.

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
* Wed Jan 20 2016 Igor Vlasenko <viy@altlinux.ru> 0:1.4-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

