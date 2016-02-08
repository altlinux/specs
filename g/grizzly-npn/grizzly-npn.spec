Name: grizzly-npn
Version: 1.2
Summary: Grizzly Next Protocol Negotiation API
License: CDDL or GPLv2 with exceptions
Url: https://grizzly.java.net/spdy.html
Packager: Igor Vlasenko <viy@altlinux.ru>
Provides: grizzly-npn = 1.2-2.fc23
Provides: mvn(org.glassfish.grizzly:grizzly-npn-api) = 1.2
Provides: mvn(org.glassfish.grizzly:grizzly-npn-api:pom:) = 1.2
Provides: mvn(org.glassfish.grizzly:grizzly-npn:pom:) = 1.2
Requires: java-headless
Requires: jpackage-utils

BuildArch: noarch
Group: Development/Java
Release: alt0.1jpp
Source: grizzly-npn-1.2-2.fc23.cpio

%description
A pure Java implementation of the
Next Protocol Negotiation TLS Extension
for OpenJDK 7 or greater.

NPN allows the application layer to
negotiate which protocol to use over the
secure connection.

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

