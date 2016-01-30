Name: plexus-sec-dispatcher
Version: 1.4
Summary: Plexus Security Dispatcher Component
License: ASL 2.0
Url: https://github.com/codehaus-plexus/plexus-sec-dispatcher
Packager: Igor Vlasenko <viy@altlinux.ru>
Provides: mvn(org.sonatype.plexus:plexus-sec-dispatcher) = 1.4
Provides: mvn(org.sonatype.plexus:plexus-sec-dispatcher:pom:) = 1.4
Provides: plexus-sec-dispatcher = 1.4-20.fc23
Requires: java-headless
Requires: jpackage-utils
Requires: mvn(org.codehaus.plexus:plexus-utils)
Requires: mvn(org.sonatype.plexus:plexus-cipher)

BuildArch: noarch
Group: Development/Java
Release: alt3jpp
Source: plexus-sec-dispatcher-1.4-20.fc23.cpio

%description
Plexus Security Dispatcher Component

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
* Fri Jan 22 2016 Igor Vlasenko <viy@altlinux.ru> 1.4-alt3jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 1.4-alt2_11jpp7
- new release

* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 1.4-alt2_10jpp7
- new release

* Mon Jul 14 2014 Igor Vlasenko <viy@altlinux.ru> 1.4-alt2_7jpp7
- NMU rebuild to move poms and fragments

* Mon Aug 13 2012 Igor Vlasenko <viy@altlinux.ru> 1.4-alt1_7jpp7
- fixed build

* Fri Mar 30 2012 Igor Vlasenko <viy@altlinux.ru> 1.4-alt1_4jpp7
- complete build

* Wed Mar 07 2012 Igor Vlasenko <viy@altlinux.ru> 1.4-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

