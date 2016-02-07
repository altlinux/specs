Name: glassfish-gmbal
Version: 3.2.0
Summary: GlassFish MBean Annotation Library
License: CDDL or GPLv2 with exceptions
Url: http://java.net/projects/gmbal/pages/Home
Packager: Igor Vlasenko <viy@altlinux.ru>
Provides: glassfish-gmbal = 3.2.0-0.8.b003.fc23
Provides: mvn(org.glassfish.gmbal:gmbal) = 3.2.0.b003
Provides: mvn(org.glassfish.gmbal:gmbal-api-only) = 3.2.0.b003
Provides: mvn(org.glassfish.gmbal:gmbal-api-only:pom:) = 3.2.0.b003
Provides: mvn(org.glassfish.gmbal:gmbal:pom:) = 3.2.0.b003
Requires: java-headless
Requires: jpackage-utils
Requires: mvn(org.glassfish.external:management-api)
Requires: mvn(org.glassfish.pfl:pfl-basic)
Requires: mvn(org.glassfish.pfl:pfl-basic-tools)
Requires: mvn(org.glassfish.pfl:pfl-tf)
Requires: mvn(org.glassfish.pfl:pfl-tf-tools)

BuildArch: noarch
Group: Development/Java
Release: alt2jpp
Source: glassfish-gmbal-3.2.0-0.8.b003.fc23.cpio

%description
The GlassFish MBean Annotation Library (gmbal, pronounced "Gumball")
is a library for using annotations to create Open MBeans. There is similar
functionality in JSR 255 for JDK 7, but gmbal only requires JDK 5. Gmbal
also supports JSR 77 ObjectNames and the GlassFish Version 3 AMX
requirements for MBeans. AS a consequence, gmbal-enabled classes
will be fully manageable in GlassFish v3 using the standard GlassFish
v3 admin tools, while still being manageable with generic MBean tools
when not run under GlassFish v3.

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
* Sun Feb 07 2016 Igor Vlasenko <viy@altlinux.ru> 3.2.0-alt2jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

* Wed Aug 27 2014 Igor Vlasenko <viy@altlinux.ru> 3.2.0-alt1_0.3.b003jpp7
- new release

