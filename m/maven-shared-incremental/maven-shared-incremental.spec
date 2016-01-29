Name: maven-shared-incremental
Version: 1.1
Summary: Maven Incremental Build support utilities
License: ASL 2.0
Url: http://maven.apache.org/shared/maven-shared-incremental/
Packager: Igor Vlasenko <viy@altlinux.ru>
Provides: maven-shared-incremental = 1.1-9.fc23
Provides: mvn(org.apache.maven.shared:maven-shared-incremental) = 1.1
Provides: mvn(org.apache.maven.shared:maven-shared-incremental:pom:) = 1.1
Requires: java-headless
Requires: jpackage-utils
Requires: mvn(org.apache.maven.shared:maven-shared-utils)
Requires: mvn(org.apache.maven:maven-core)
Requires: mvn(org.apache.maven:maven-plugin-api)
Requires: mvn(org.codehaus.plexus:plexus-component-annotations)

BuildArch: noarch
Group: Development/Java
Release: alt0.1jpp
Source: maven-shared-incremental-1.1-9.fc23.cpio

%description
Various utility classes and plexus components for supporting
incremental build functionality in maven plugins.

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
* Tue Jan 26 2016 Igor Vlasenko <viy@altlinux.ru> 1.1-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

* Mon Aug 25 2014 Igor Vlasenko <viy@altlinux.ru> 1.0-alt1_2jpp7
- new release

* Sat Aug 23 2014 Igor Vlasenko <viy@altlinux.ru> 1.0-alt0.2jpp
- rebuild to add provides

* Wed Aug 20 2014 Igor Vlasenko <viy@altlinux.ru> 1.0-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

