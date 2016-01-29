Name: fasterxml-oss-parent
Version: 18e
Summary: FasterXML parent pom
License: ASL 2.0 and LGPLv2+
Url: http://fasterxml.com/
Packager: Igor Vlasenko <viy@altlinux.ru>
Provides: fasterxml-oss-parent = 18e-2.fc23
Provides: mvn(com.fasterxml:oss-parent:pom:) = 18
Requires: java-headless
Requires: jpackage-utils
Requires: mvn(org.apache.felix:maven-bundle-plugin)
Requires: mvn(org.apache.maven.plugins:maven-compiler-plugin)
Requires: mvn(org.apache.maven.plugins:maven-enforcer-plugin)
Requires: mvn(org.apache.maven.plugins:maven-jar-plugin)
Requires: mvn(org.apache.maven.plugins:maven-scm-plugin)
Requires: mvn(org.apache.maven.plugins:maven-site-plugin)
Requires: mvn(org.apache.maven.plugins:maven-surefire-plugin)
Requires: mvn(org.apache.maven.scm:maven-scm-manager-plexus)
Requires: mvn(org.apache.maven.scm:maven-scm-provider-gitexe)
Requires: mvn(org.codehaus.mojo:build-helper-maven-plugin)

BuildArch: noarch
Group: Development/Java
Release: alt0.1jpp
Source: fasterxml-oss-parent-18e-2.fc23.cpio

%description
FasterXML is the business behind the Woodstox streaming XML parser,
Jackson streaming JSON parser, the Aalto non-blocking XML parser, and
a growing family of utility libraries and extensions.

FasterXML offers consulting services for adoption, performance tuning,
and extension.

This package contains the parent pom file for FasterXML.com projects.

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
* Fri Jan 29 2016 Igor Vlasenko <viy@altlinux.ru> 18e-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 4-alt2_3jpp7
- new release

* Thu Feb 14 2013 Igor Vlasenko <viy@altlinux.ru> 4-alt2_1jpp7
- fixed maven1 dependency

* Mon Dec 24 2012 Igor Vlasenko <viy@altlinux.ru> 4-alt1_1jpp7
- use /var/lock/serial

