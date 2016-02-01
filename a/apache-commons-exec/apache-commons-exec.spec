Name: apache-commons-exec
Version: 1.3
Summary: Java library to reliably execute external processes from within the JVM
License: ASL 2.0
Url: http://commons.apache.org/exec/
Epoch: 0
Packager: Igor Vlasenko <viy@altlinux.ru>
Provides: apache-commons-exec = 1.3-3.fc23
Provides: mvn(org.apache.commons:commons-exec) = 1.3
Provides: mvn(org.apache.commons:commons-exec:pom:) = 1.3
Requires: java-headless
Requires: java-headless
Requires: jpackage-utils
Requires: jpackage-utils

BuildArch: noarch
Group: Development/Java
Release: alt0.1jpp
Source: apache-commons-exec-1.3-3.fc23.cpio

%description
Commons Exec is a library for dealing with external process execution and
environment management in Java.

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
* Mon Feb 01 2016 Igor Vlasenko <viy@altlinux.ru> 0:1.3-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

* Mon Aug 25 2014 Igor Vlasenko <viy@altlinux.ru> 0:1.1-alt1_8jpp7
- new version

* Wed Sep 19 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.1-alt1_6jpp7
- new version

* Mon Jan 10 2011 Igor Vlasenko <viy@altlinux.ru> 0:1.0.1-alt2_6jpp6
- excluded repolib from main package

* Sun Jan 02 2011 Igor Vlasenko <viy@altlinux.ru> 0:1.0.1-alt1_6jpp6
- renamed; new jpp version

