Name: aspectjweaver
Version: 1.8.4
Summary: Java byte-code weaving library
License: EPL
Url: http://eclipse.org/aspectj/
Epoch: 0
Packager: Igor Vlasenko <viy@altlinux.ru>
Provides: aspectjweaver = 1.8.4-3.fc23
Provides: mvn(aspectj:aspectjrt) = 1.8.4
Provides: mvn(aspectj:aspectjrt:pom:) = 1.8.4
Provides: mvn(org.aspectj:aspectjrt) = 1.8.4
Provides: mvn(org.aspectj:aspectjrt:pom:) = 1.8.4
Provides: mvn(org.aspectj:aspectjweaver) = 1.8.4
Provides: mvn(org.aspectj:aspectjweaver:pom:) = 1.8.4
Requires: java-headless
Requires: jpackage-utils
Requires: mvn(org.ow2.asm:asm)

BuildArch: noarch
Group: Development/Java
Release: alt0.1jpp
Source: aspectjweaver-1.8.4-3.fc23.cpio

%description
The AspectJ Weaver supports byte-code weaving for aspect-oriented
programming (AOP) in java.

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
* Sat Jan 23 2016 Igor Vlasenko <viy@altlinux.ru> 0:1.8.4-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

* Sat Jan 26 2013 Igor Vlasenko <viy@altlinux.ru> 0:1.6.12-alt4_1jpp6
- applied repocop patches

* Thu Oct 18 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.6.12-alt3_1jpp6
- merged aspectjweaver back

* Mon Oct 15 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.6.12-alt1_1jpp6
- new version

* Sat Oct 13 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.6.11-alt1_1jpp6
- new version

* Fri Oct 12 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.6.5-alt1_1jpp6
- new version

* Thu Sep 20 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.6.0-alt1_1jpp6
- new version

* Wed Sep 12 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.5.4-alt3_1jpp6
- build with saxon6

* Sat Sep 17 2011 Igor Vlasenko <viy@altlinux.ru> 0:1.5.4-alt2_1jpp6
- fixed build

* Wed Jan 26 2011 Igor Vlasenko <viy@altlinux.ru> 0:1.5.4-alt1_1jpp6
- new version

* Sun Feb 21 2010 Igor Vlasenko <viy@altlinux.ru> 0:1.5.3-alt3_2jpp5
- fixed build with eclipse 3.5

* Sun Jan 04 2009 Igor Vlasenko <viy@altlinux.ru> 0:1.5.3-alt2_2jpp5
- rebuild with eclipse 3.4

* Fri Dec 05 2008 Igor Vlasenko <viy@altlinux.ru> 0:1.5.3-alt1_2jpp5
- new version

