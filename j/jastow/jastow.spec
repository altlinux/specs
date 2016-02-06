Name: jastow
Version: 1.0.0
Summary: Jasper fork
License: ASL 2.0
Url: https://github.com/undertow-io/jastow
Packager: Igor Vlasenko <viy@altlinux.ru>
Provides: jastow = 1.0.0-4.fc23
Provides: mvn(io.undertow.jastow:jastow) = 1.0.0.Final
Provides: mvn(io.undertow.jastow:jastow:pom:) = 1.0.0.Final
Requires: java-headless
Requires: jpackage-utils
#Requires: mvn(com.sun:tools)
#Requires: mvn(io.undertow:undertow-servlet)
Requires: mvn(org.jboss.logging:jboss-logging)

BuildArch: noarch
Group: Development/Java
Release: alt0.1jpp
Source: jastow-1.0.0-4.fc23.cpio

%description
The Jasper fork for Undertow.

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
* Sat Feb 06 2016 Igor Vlasenko <viy@altlinux.ru> 1.0.0-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

