Name: grizzly-npn-osgi
Version: 1.2
Summary: Grizzly NPN OSGi
License: CDDL or GPLv2 with exceptions
Url: https://grizzly.java.net/spdy.html
Packager: Igor Vlasenko <viy@altlinux.ru>
Provides: grizzly-npn-osgi = 1.2-2.fc23
Provides: mvn(org.glassfish.grizzly:grizzly-npn-osgi) = 1.2
Provides: mvn(org.glassfish.grizzly:grizzly-npn-osgi:pom:) = 1.2
Requires: java-headless
Requires: jpackage-utils

BuildArch: noarch
Group: Development/Java
Release: alt0.1jpp
Source: grizzly-npn-osgi-1.2-2.fc23.cpio

%description
This empty module allows the bootclasspath classes in
org.glassfish.grizzly.npn to be available via the
OSGi classloading mechanisms.

Using GlassFish as an example:
- grizzly-npn-bootstrap.jar goes into the
  domain's bootclasspath (-Xbootclasspath/p:[PATH TO THE JAR])
- grizzly-npn-osgi and grizzly-spdy JARs go into the
  [PATH TO THE GlassFish 4 HOME]/modules directory.

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

