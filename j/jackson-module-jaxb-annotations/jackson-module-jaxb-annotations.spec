Name: jackson-module-jaxb-annotations
Version: 2.5.0
Summary: JAXB annotations support for Jackson (2.x)
License: ASL 2.0
Url: http://wiki.fasterxml.com/JacksonJAXBAnnotations
Packager: Igor Vlasenko <viy@altlinux.ru>
Provides: jackson-module-jaxb-annotations = 2.5.0-2.fc23
Provides: jackson2-module-jaxb-annotations = 2.5.0-2.fc23
Provides: mvn(com.fasterxml.jackson.module:jackson-module-jaxb-annotations) = 2.5.0
Provides: mvn(com.fasterxml.jackson.module:jackson-module-jaxb-annotations:pom:) = 2.5.0
Requires: java-headless
Requires: jpackage-utils
Requires: mvn(com.fasterxml.jackson.core:jackson-core)
Requires: mvn(com.fasterxml.jackson.core:jackson-databind)

BuildArch: noarch
Group: Development/Java
Release: alt0.1jpp
Source: jackson-module-jaxb-annotations-2.5.0-2.fc23.cpio

%description
Support for using JAXB annotations as an alternative to
"native" Jackson annotations, for configuring data binding.

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
* Thu Jan 28 2016 Igor Vlasenko <viy@altlinux.ru> 2.5.0-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

