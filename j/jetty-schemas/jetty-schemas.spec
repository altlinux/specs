Name: jetty-schemas
Version: 3.1
Summary: XML Schemas for Jetty
License: CDDL or GPLv2 with exceptions
Url: http://www.eclipse.org/jetty/
Packager: Igor Vlasenko <viy@altlinux.ru>
Provides: jetty-schemas = 3.1-4.fc23
Provides: mvn(org.eclipse.jetty.toolchain:jetty-schemas) = 3.1.M0
Provides: mvn(org.eclipse.jetty.toolchain:jetty-schemas:pom:) = 3.1.M0
Requires: java-headless
Requires: jpackage-utils

BuildArch: noarch
Group: Development/Java
Release: alt0.1jpp
Source: jetty-schemas-3.1-4.fc23.cpio

%description
XML Schemas for Jetty.

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
* Thu Feb 04 2016 Igor Vlasenko <viy@altlinux.ru> 3.1-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

