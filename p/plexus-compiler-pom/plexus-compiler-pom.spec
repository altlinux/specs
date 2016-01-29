Name: plexus-compiler-pom
Version: 2.4
Summary: Maven POM files for plexus-compiler
License: MIT and ASL 2.0
Url: https://github.com/codehaus-plexus/plexus-compiler
Epoch: 0
Packager: Igor Vlasenko <viy@altlinux.ru>
Provides: mvn(org.codehaus.plexus:plexus-compiler:pom:) = 2.4
Provides: mvn(org.codehaus.plexus:plexus-compilers:pom:) = 2.4
Provides: plexus-compiler-pom = 0:2.4-3.fc23
Requires: java-headless
Requires: jpackage-utils
Requires: mvn(org.apache.maven.plugins:maven-gpg-plugin)
Requires: mvn(org.codehaus.plexus:plexus-compiler-api)
Requires: mvn(org.codehaus.plexus:plexus-component-metadata)
Requires: mvn(org.codehaus.plexus:plexus-components:pom:)

BuildArch: noarch
Group: Development/Java
Release: alt0.1jpp
Source: plexus-compiler-pom-2.4-3.fc23.cpio

%description
This package provides Maven POM files for plexus-compiler.

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
* Sat Jan 23 2016 Igor Vlasenko <viy@altlinux.ru> 0:2.4-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

* Tue Aug 26 2014 Igor Vlasenko <viy@altlinux.ru> 0:2.2-alt1_4jpp7
- new release

* Wed Aug 20 2014 Igor Vlasenko <viy@altlinux.ru> 0:2.2-alt1_0jpp7
- new version

* Thu Aug 07 2014 Igor Vlasenko <viy@altlinux.ru> 0:1.9.2-alt2_1jpp7.qa1
- rebuild with maven-local

* Mon Apr 22 2013 Repocop Q. A. Robot <repocop@altlinux.org> 0:1.9.2-alt1_1jpp7.qa1
- NMU (by repocop). See http://www.altlinux.org/Tools/Repocop
- applied repocop fixes:
  * beehive-log-dependency-needs-epoch-x86_64 for plexus-compiler

* Wed Feb 13 2013 Igor Vlasenko <viy@altlinux.ru> 0:1.9.2-alt1_1jpp7
- fc update

* Tue Sep 18 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.9.1-alt1_3jpp7
- new version

* Thu Aug 23 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.8.3-alt2_1jpp7
- applied repocop patches

* Fri Mar 30 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.8.3-alt1_1jpp7
- complete build

* Thu Mar 08 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.8.3-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

