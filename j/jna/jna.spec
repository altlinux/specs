Name: jna
Version: 4.1.0
Summary: Pure Java access to native libraries
License: (LGPLv2 or ASL 2.0) and ASL 2.0
Url: https://github.com/twall/jna
Packager: Igor Vlasenko <viy@altlinux.ru>
Provides: jna = 4.1.0-9.fc23
Provides: mvn(net.java.dev.jna:jna) = 4.1.0.SNAPSHOT
Provides: mvn(net.java.dev.jna:jna:pom:) = 4.1.0.SNAPSHOT
Requires: java
Requires: java-headless
Requires: jpackage-utils
Requires: jpackage-utils
Requires: libffi

BuildArch: noarch
Group: Development/Java
Release: alt0.1jpp
Source: jna-4.1.0-9.fc23.cpio

%description
JNA provides Java programs easy access to native shared libraries
(DLLs on Windows) without writing anything but Java code. JNA's
design aims to provide native access in a natural way with a
minimum of effort. No boilerplate or generated code is required.
While some attention is paid to performance, correctness and ease
of use take priority.

# sometimes commpress gets crazy (see maven-scm-javadoc for details)
%set_compress_method none
%prep
cpio -idmu --quiet --no-absolute-filenames < %{SOURCE0}

%build
cpio --list < %{SOURCE0} | sed -e 's,^\.,,' | grep -v /usr/lib64 > %name-list

%install
mkdir -p $RPM_BUILD_ROOT
for i in usr var etc; do
[ -d $i ] && mv $i $RPM_BUILD_ROOT/
done

rm -rf %buildroot/usr/lib64

%files -f %name-list

%changelog
* Wed Jan 20 2016 Igor Vlasenko <viy@altlinux.ru> 4.1.0-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 3.5.2-alt1_2jpp7
- new release

* Fri Sep 05 2014 Igor Vlasenko <viy@altlinux.ru> 3.5.0-alt1_2jpp7
- new version

* Mon Jul 14 2014 Igor Vlasenko <viy@altlinux.ru> 3.4.0-alt2_5jpp7
- NMU rebuild to move poms and fragments

* Mon Aug 20 2012 Igor Vlasenko <viy@altlinux.ru> 3.4.0-alt1_5jpp7
- update to new release by jppimport

* Fri Sep 02 2011 Igor Vlasenko <viy@altlinux.ru> 3.2.7-alt1_12jpp6
- update to new release by jppimport

* Sun Aug 29 2010 Igor Vlasenko <viy@altlinux.ru> 3.2.4-alt2_3jpp5
- rebuild with new libffi

* Thu Apr 15 2010 Igor Vlasenko <viy@altlinux.ru> 3.2.4-alt1_3jpp5
- new version

* Mon Sep 15 2008 Igor Vlasenko <viy@altlinux.ru> 3.0.3-alt1_4jpp5
- jpp5 build

