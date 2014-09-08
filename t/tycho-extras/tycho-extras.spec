Name: tycho-extras
Version: 0.18.0
Summary: Additional plugins for Tycho
License: EPL
Url: http://eclipse.org/tycho/
Packager: Igor Vlasenko <viy@altlinux.ru>
Provides: mvn(org.eclipse.tycho.extras:target-platform-validation-plugin)
Provides: mvn(org.eclipse.tycho.extras:tycho-buildtimestamp-jgit)
Provides: mvn(org.eclipse.tycho.extras:tycho-custom-bundle-plugin)
Provides: mvn(org.eclipse.tycho.extras:tycho-eclipserun-plugin)
Provides: mvn(org.eclipse.tycho.extras:tycho-extras)
Provides: mvn(org.eclipse.tycho.extras:tycho-p2-extras-plugin)
Provides: mvn(org.eclipse.tycho.extras:tycho-pack200)
Provides: mvn(org.eclipse.tycho.extras:tycho-pack200-impl)
Provides: mvn(org.eclipse.tycho.extras:tycho-pack200a-plugin)
Provides: mvn(org.eclipse.tycho.extras:tycho-pack200b-plugin)
Provides: mvn(org.eclipse.tycho.extras:tycho-source-feature-plugin)
Provides: mvn(org.eclipse.tycho.extras:tycho-sourceref-jgit)
Provides: mvn(org.eclipse.tycho.extras:tycho-version-bump-plugin)
Provides: mvn(org.eclipse.tycho:pack200)
Provides: mvn(org.eclipse.tycho:target-platform-validation-plugin)
Provides: mvn(org.eclipse.tycho:tycho-buildtimestamp-jgit)
Provides: mvn(org.eclipse.tycho:tycho-custom-bundle-plugin)
Provides: mvn(org.eclipse.tycho:tycho-eclipserun-plugin)
Provides: mvn(org.eclipse.tycho:tycho-extras)
Provides: mvn(org.eclipse.tycho:tycho-p2-extras-plugin)
Provides: mvn(org.eclipse.tycho:tycho-pack200-impl)
Provides: mvn(org.eclipse.tycho:tycho-pack200a-plugin)
Provides: mvn(org.eclipse.tycho:tycho-pack200b-plugin)
Provides: mvn(org.eclipse.tycho:tycho-source-feature-plugin)
Provides: mvn(org.eclipse.tycho:tycho-sourceref-jgit)
Provides: mvn(org.eclipse.tycho:tycho-version-bump-plugin)
Provides: mvn(org.sonatype.tycho:pack200)
Provides: mvn(org.sonatype.tycho:target-platform-validation-plugin)
Provides: mvn(org.sonatype.tycho:tycho-buildtimestamp-jgit)
Provides: mvn(org.sonatype.tycho:tycho-custom-bundle-plugin)
Provides: mvn(org.sonatype.tycho:tycho-eclipserun-plugin)
Provides: mvn(org.sonatype.tycho:tycho-extras)
Provides: mvn(org.sonatype.tycho:tycho-p2-extras-plugin)
Provides: mvn(org.sonatype.tycho:tycho-pack200-impl)
Provides: mvn(org.sonatype.tycho:tycho-pack200a-plugin)
Provides: mvn(org.sonatype.tycho:tycho-pack200b-plugin)
Provides: mvn(org.sonatype.tycho:tycho-source-feature-plugin)
Provides: mvn(org.sonatype.tycho:tycho-sourceref-jgit)
Provides: mvn(org.sonatype.tycho:tycho-version-bump-plugin)
Requires: java
Requires: jgit
Requires: jpackage-utils
Requires: tycho

BuildArch: noarch
Group: Development/Java
Release: alt0.1jpp
Source: tycho-extras-0.18.0-1.fc19.cpio

%description
A small set of plugins that work with Tycho to provide additional functionality
when building projects of an OSGi nature.

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
* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 0.18.0-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

* Thu Aug 07 2014 Igor Vlasenko <viy@altlinux.ru> 0.16.0-alt2_3jpp7
- rebuild with maven-local

* Mon Jul 21 2014 Igor Vlasenko <viy@altlinux.ru> 0.16.0-alt1_3jpp7
- update

* Wed Sep 05 2012 Igor Vlasenko <viy@altlinux.ru> 0.16.0-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

