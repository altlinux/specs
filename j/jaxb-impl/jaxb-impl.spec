
# sometimes commpress gets crazy (see maven-scm-javadoc for details)
%set_compress_method none

Name: jaxb-impl
Version: 2.3.3
Summary: Old JAXB Runtime
License: BSD
Url: https://github.com/eclipse-ee4j/jaxb-ri
Group: Development/Java
Release: alt0.1jpp

Packager: Igor Vlasenko <viy@altlinux.org>
Provides: mvn(com.sun.xml.bind:jaxb-impl) = 2.3.3
Provides: mvn(com.sun.xml.bind:jaxb-impl:pom:) = 2.3.3
Provides: osgi(com.sun.xml.bind.jaxb-impl) = 2.3.3
Requires: java-headless
Requires: javapackages-filesystem
Requires: mvn(com.sun.activation:jakarta.activation)
Requires: mvn(jakarta.xml.bind:jakarta.xml.bind-api)

BuildArch: noarch
Source: jaxb-impl-2.3.3-6.fc34.cpio


%description
Old JAXB Runtime module. Contains sources required for runtime processing.
Standalone bundle suitable for use in OSGi runtimes.

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
* Sat Jun 05 2021 Igor Vlasenko <viy@altlinux.org> 2.3.3-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

