Name: sisu-plexus
Version: 0.3.1
Summary: Sisu Plexus
License: EPL
Url: http://eclipse.org/sisu
Epoch: 1
Packager: Igor Vlasenko <viy@altlinux.ru>
Provides: mvn(org.eclipse.sisu:org.eclipse.sisu.plexus) = 0.3.1
Provides: mvn(org.eclipse.sisu:org.eclipse.sisu.plexus:pom:) = 0.3.1
Provides: mvn(org.eclipse.sisu:sisu-plexus:pom:) = 0.3.1
Provides: sisu-plexus = 1:0.3.1-2.fc23
Requires: java-headless
Requires: jpackage-utils
Requires: mvn(org.codehaus.plexus:plexus-classworlds)
Requires: mvn(org.codehaus.plexus:plexus-component-annotations)
Requires: mvn(org.codehaus.plexus:plexus-utils)
Requires: mvn(org.eclipse.sisu:org.eclipse.sisu.inject)

BuildArch: noarch
Group: Development/Java
Release: alt0.1jpp
Source: sisu-plexus-0.3.1-2.fc23.cpio

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
* Tue Jan 19 2016 Igor Vlasenko <viy@altlinux.ru> 1:0.3.1-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

