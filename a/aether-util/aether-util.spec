Name: aether-util
Version: 1.0.2
Summary: Aether utilities
License: EPL
Url: http://eclipse.org/aether
Epoch: 1
Packager: Igor Vlasenko <viy@altlinux.ru>
Provides: aether-util = 1:1.0.2-2.fc23
Provides: mvn(org.eclipse.aether:aether-util) = 1.0.2.v20150114
Provides: mvn(org.eclipse.aether:aether-util:pom:) = 1.0.2.v20150114
Requires: java-headless
Requires: jpackage-utils
Requires: mvn(org.eclipse.aether:aether-api)

BuildArch: noarch
Group: Development/Java
Release: alt0.1jpp
Source: aether-util-1.0.2-2.fc23.cpio

%description
Aether is a standalone library to resolve, install and deploy
artifacts the Maven way.  This package provides a collection of
utility classes to ease usage of Aether repository system.

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
* Tue Jan 19 2016 Igor Vlasenko <viy@altlinux.ru> 1:1.0.2-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

