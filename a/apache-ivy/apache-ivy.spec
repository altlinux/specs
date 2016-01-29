Name: apache-ivy
Version: 2.4.0
Summary: Java-based dependency manager
License: ASL 2.0
Url: http://ant.apache.org/ivy
Epoch: 0
Packager: Igor Vlasenko <viy@altlinux.ru>
Provides: apache-ivy = 2.4.0-4.fc23
Provides: ivy = 2.4.0-4.fc23
Provides: mvn(jayasoft:ivy) = 2.4.0.local.20150617001712
Provides: mvn(jayasoft:ivy:pom:) = 2.4.0.local.20150617001712
Provides: mvn(jayasoft:ivy:xml:) = 2.4.0.local.20150617001712
Provides: mvn(org.apache.ivy:ivy) = 2.4.0.local.20150617001712
Provides: mvn(org.apache.ivy:ivy:pom:) = 2.4.0.local.20150617001712
Provides: mvn(org.apache.ivy:ivy:xml:) = 2.4.0.local.20150617001712
Requires: java-headless
Requires: jpackage-utils

BuildArch: noarch
Group: Development/Java
Release: alt0.1jpp
Source: apache-ivy-2.4.0-4.fc23.cpio

%description
Apache Ivy is a tool for managing (recording, tracking, resolving and
reporting) project dependencies.  It is designed as process agnostic and is
not tied to any methodology or structure. while available as a standalone
tool, Apache Ivy works particularly well with Apache Ant providing a number
of powerful Ant tasks ranging from dependency resolution to dependency
reporting and publication.

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
* Fri Jan 29 2016 Igor Vlasenko <viy@altlinux.ru> 0:2.4.0-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

* Fri Aug 01 2014 Igor Vlasenko <viy@altlinux.ru> 0:2.3.0-alt1_1jpp7
- new version

* Thu Sep 20 2012 Igor Vlasenko <viy@altlinux.ru> 0:2.2.0-alt3_5jpp7
- fc release

* Sat Sep 08 2012 Igor Vlasenko <viy@altlinux.ru> 0:2.2.0-alt3_1jpp6
- build with new commons-vfs2

* Tue Aug 28 2012 Igor Vlasenko <viy@altlinux.ru> 0:2.2.0-alt2_1jpp6
- fixed build

* Wed Sep 07 2011 Igor Vlasenko <viy@altlinux.ru> 0:2.2.0-alt1_1jpp6
- new version

* Mon Sep 20 2010 Igor Vlasenko <viy@altlinux.ru> 0:2.0.0-alt1_2jpp6
- new version

