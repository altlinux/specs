Name: maven-enforcer-rules
Version: 1.4
Summary: Enforcer Rules
License: ASL 2.0
Url: http://maven.apache.org/enforcer
Epoch: 0
Packager: Igor Vlasenko <viy@altlinux.ru>
Provides: maven-enforcer-rules = 1.4-2.fc23
Provides: mvn(org.apache.maven.enforcer:enforcer-rules) = 1.4
Provides: mvn(org.apache.maven.enforcer:enforcer-rules:pom:) = 1.4
Requires: java-headless
Requires: jpackage-utils
Requires: mvn(commons-lang:commons-lang)
Requires: mvn(org.apache.maven.enforcer:enforcer-api)
Requires: mvn(org.apache.maven.shared:maven-common-artifact-filters)
Requires: mvn(org.apache.maven.shared:maven-dependency-tree)
Requires: mvn(org.apache.maven:maven-artifact:2.2.1)
Requires: mvn(org.apache.maven:maven-compat)
Requires: mvn(org.apache.maven:maven-core)
Requires: mvn(org.apache.maven:maven-plugin-api)
Requires: mvn(org.apache.maven:maven-project)
Requires: mvn(org.beanshell:bsh)
Requires: mvn(org.codehaus.plexus:plexus-i18n)
Requires: mvn(org.codehaus.plexus:plexus-utils)

BuildArch: noarch
Group: Development/Java
Release: alt0.1jpp
Source: maven-enforcer-rules-1.4-2.fc23.cpio

%description
This component contains the standard Enforcer Rules.

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

