%filter_from_requires /^java-headless/d
Name: sisu-plexus
Version: 0.3.2
Summary: Sisu Plexus
License: EPL
Url: http://eclipse.org/sisu
Epoch: 1
Packager: Igor Vlasenko <viy@altlinux.ru>
Provides: mvn(org.eclipse.sisu:org.eclipse.sisu.plexus) = 0.3.2
Provides: mvn(org.eclipse.sisu:org.eclipse.sisu.plexus:pom:) = 0.3.2
Provides: mvn(org.eclipse.sisu:sisu-plexus:pom:) = 0.3.2
Provides: mvn(org.sonatype.sisu:sisu-inject-plexus) = 0.3.2
Provides: mvn(org.sonatype.sisu:sisu-inject-plexus:pom:) = 0.3.2
Provides: osgi(org.eclipse.sisu.plexus) = 0.3.2
Provides: sisu-plexus = 1:0.3.2-4.fc24
Requires: jpackage-utils
Requires: mvn(org.codehaus.plexus:plexus-classworlds)
Requires: mvn(org.codehaus.plexus:plexus-component-annotations)
Requires: mvn(org.codehaus.plexus:plexus-utils)
Requires: mvn(org.eclipse.sisu:org.eclipse.sisu.inject)

BuildArch: noarch
Group: Development/Java
Release: alt0.1jpp
Source: sisu-plexus-0.3.2-4.fc24.cpio

%description
This package contains Sisu Plexus.

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
* Thu Dec 15 2016 Igor Vlasenko <viy@altlinux.ru> 1:0.3.2-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

* Tue Jan 19 2016 Igor Vlasenko <viy@altlinux.ru> 1:0.3.1-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

