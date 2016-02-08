Name: grizzly-npn-bootstrap
Version: 1.2
Summary: Grizzly NPN Bootstrap
License: CDDL or GPLv2 with exceptions
Url: https://grizzly.java.net/spdy.html
Packager: Igor Vlasenko <viy@altlinux.ru>
Provides: grizzly-npn-bootstrap = 1.2-2.fc23
Provides: mvn(org.glassfish.grizzly:grizzly-npn-bootstrap) = 1.2
Provides: mvn(org.glassfish.grizzly:grizzly-npn-bootstrap:pom:) = 1.2
Requires: java-headless
Requires: jpackage-utils
Requires: mvn(org.glassfish.grizzly:grizzly-npn-api)

BuildArch: noarch
Group: Development/Java
Release: alt0.1jpp
Source: grizzly-npn-bootstrap-1.2-2.fc23.cpio

%description
This package contains the JAR that
will be placed on the bootclasspath
in order for NPN to work.

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
* Mon Feb 08 2016 Igor Vlasenko <viy@altlinux.ru> 1.2-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

