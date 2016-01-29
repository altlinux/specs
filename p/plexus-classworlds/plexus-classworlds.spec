Name: plexus-classworlds
Version: 2.5.2
Summary: Plexus Classworlds Classloader Framework
License: ASL 2.0 and Plexus
Url: https://github.com/codehaus-plexus/plexus-classworlds
Epoch: 0
Packager: Igor Vlasenko <viy@altlinux.ru>
Provides: mvn(classworlds:classworlds) = 2.5.2
Provides: mvn(classworlds:classworlds:pom:) = 2.5.2
Provides: mvn(org.codehaus.plexus:plexus-classworlds) = 2.5.2
Provides: mvn(org.codehaus.plexus:plexus-classworlds:pom:) = 2.5.2
Provides: plexus-classworlds = 2.5.2-3.fc23
Requires: java-headless
Requires: jpackage-utils

BuildArch: noarch
Group: Development/Java
Release: alt0.1jpp
Source: plexus-classworlds-2.5.2-3.fc23.cpio

%description
Classworlds is a framework for container developers
who require complex manipulation of Java's ClassLoaders.
Java's native ClassLoader mechanisms and classes can cause
much headache and confusion for certain types of
application developers. Projects which involve dynamic
loading of components or otherwise represent a 'container'
can benefit from the classloading control provided by
classworlds.

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
* Tue Jan 19 2016 Igor Vlasenko <viy@altlinux.ru> 0:2.5.2-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

* Fri Aug 01 2014 Igor Vlasenko <viy@altlinux.ru> 0:2.4.2-alt1_4jpp7
- new version

* Mon Jul 14 2014 Igor Vlasenko <viy@altlinux.ru> 0:2.4-alt2_7jpp7
- NMU rebuild to move poms and fragments

* Mon Aug 27 2012 Igor Vlasenko <viy@altlinux.ru> 0:2.4-alt1_7jpp7
- new release

* Fri Mar 30 2012 Igor Vlasenko <viy@altlinux.ru> 0:2.4-alt1_3jpp7
- complete build

* Thu Mar 08 2012 Igor Vlasenko <viy@altlinux.ru> 0:2.4-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

