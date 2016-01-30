Name: aether-impl
Version: 1.0.2
Summary: Implementation of Aether repository system
License: EPL
Url: http://eclipse.org/aether
Epoch: 1
Packager: Igor Vlasenko <viy@altlinux.ru>
Provides: aether-impl = 1:1.0.2-2.fc23
Provides: mvn(org.eclipse.aether:aether-impl) = 1.0.2.v20150114
Provides: mvn(org.eclipse.aether:aether-impl:pom:) = 1.0.2.v20150114
Requires: java-headless
Requires: jpackage-utils
Requires: mvn(org.eclipse.aether:aether-api)
Requires: mvn(org.eclipse.aether:aether-spi)
Requires: mvn(org.eclipse.aether:aether-util)

BuildArch: noarch
Group: Development/Java
Release: alt0.1jpp
Source: aether-impl-1.0.2-2.fc23.cpio

%description
Aether is a standalone library to resolve, install and deploy
artifacts the Maven way.  This package provides implementation of
Aether repository system.

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
* Wed Jan 20 2016 Igor Vlasenko <viy@altlinux.ru> 1:1.0.2-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

