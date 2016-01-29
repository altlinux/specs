Name: maven-dependency-tree
Version: 2.2
Summary: Maven dependency tree artifact
License: ASL 2.0
Url: http://maven.apache.org/
Packager: Igor Vlasenko <viy@altlinux.ru>
Provides: maven-dependency-tree = 2.2-2.fc23
Provides: maven-shared-dependency-tree = 2.2-2.fc23
Provides: mvn(org.apache.maven.shared:maven-dependency-tree) = 2.2
Provides: mvn(org.apache.maven.shared:maven-dependency-tree:pom:) = 2.2
Requires: java-headless
Requires: jpackage-utils
Requires: mvn(org.codehaus.plexus:plexus-component-annotations)
Requires: mvn(org.eclipse.aether:aether-api)
Requires: mvn(org.eclipse.aether:aether-util)

BuildArch: noarch
Group: Development/Java
Release: alt0.1jpp
Source: maven-dependency-tree-2.2-2.fc23.cpio

%description
Apache Maven dependency tree artifact. Originally part of maven-shared.

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
* Wed Jan 20 2016 Igor Vlasenko <viy@altlinux.ru> 2.2-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

* Mon Aug 25 2014 Igor Vlasenko <viy@altlinux.ru> 2.0-alt2_4jpp7
- new release

* Thu Aug 07 2014 Igor Vlasenko <viy@altlinux.ru> 2.0-alt2_1jpp7
- rebuild with maven-local

* Mon Jul 21 2014 Igor Vlasenko <viy@altlinux.ru> 2.0-alt1_1jpp7
- update

