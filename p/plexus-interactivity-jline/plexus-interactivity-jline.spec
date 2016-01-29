Name: plexus-interactivity-jline
Version: 1.0
Summary: jline module for plexus-interactivity
License: MIT
Url: https://github.com/codehaus-plexus/plexus-interactivity
Epoch: 0
Packager: Igor Vlasenko <viy@altlinux.ru>
Provides: mvn(org.codehaus.plexus:plexus-interactivity-jline) = 1.0.alpha.6
Provides: mvn(org.codehaus.plexus:plexus-interactivity-jline:pom:) = 1.0.alpha.6
Provides: plexus-interactivity-jline = 0:1.0-0.21.alpha6.fc23
Requires: java-headless
Requires: jpackage-utils
Requires: mvn(jline:jline)
Requires: mvn(org.codehaus.plexus:plexus-interactivity-api)

BuildArch: noarch
Group: Development/Java
Release: alt5jpp
Source: plexus-interactivity-jline-1.0-0.21.alpha6.fc23.cpio

%description
jline module for plexus-interactivity.

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
* Tue Jan 26 2016 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt5jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt4_0.11.alpha6jpp7
- new release

* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt4_0.10.alpha6jpp7
- new release

* Tue Mar 19 2013 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt4_0.7.alpha6jpp7
- fc update

* Fri Feb 25 2011 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt3_0.a6.1jpp6
- new version

* Tue Feb 22 2011 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt3_0.a5.6jpp5
- fixed build

* Sun Feb 21 2010 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt2_0.a5.6jpp5
- new jpackage release

* Wed Nov 14 2007 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt2_0.a5.5jpp1.7
- build with maven2

* Wed Jun 13 2007 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt1_0.a5.5jpp1.7
- updated to new jpackage release

* Mon May 07 2007 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt1_0.a5.4jpp1.7
- converted from JPackage by jppimport script

* Sun Dec 04 2005 Vladimir Lettiev <crux@altlinux.ru> 1.0-alt0.1.alpha5
- Rebuild for ALTLinux Sisyphus
- spec cleanup

* Mon Nov 07 2005 Ralph Apel <r.apel at r-apel.de> - 0:1.0-0.a5.1jpp
- First JPackage build

