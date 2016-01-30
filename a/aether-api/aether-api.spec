Name: aether-api
Version: 1.0.2
Summary: Aether API
License: EPL
Url: http://eclipse.org/aether
Epoch: 1
Packager: Igor Vlasenko <viy@altlinux.ru>
Provides: aether-api = 1:1.0.2-2.fc23
Provides: mvn(org.eclipse.aether:aether-api) = 1.0.2.v20150114
Provides: mvn(org.eclipse.aether:aether-api:pom:) = 1.0.2.v20150114
Requires: java-headless
Requires: jpackage-utils

BuildArch: noarch
Group: Development/Java
Release: alt0.1jpp
Source: aether-api-1.0.2-2.fc23.cpio

%description
Aether is a standalone library to resolve, install and deploy
artifacts the Maven way.  This package provides application
programming interface for Aether repository system.

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

pushd %buildroot/usr/share/java/aether
	ln -s aether-api.jar api.jar
	ln -s aether-util.jar util.jar
popd

%files -f %name-list
/usr/share/java/aether/api.jar
/usr/share/java/aether/util.jar

%changelog
* Tue Jan 19 2016 Igor Vlasenko <viy@altlinux.ru> 1:1.0.2-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

