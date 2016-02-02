Provides: /usr/share/java/aqute-bnd.jar
Provides: /etc/java/aqute-bnd.conf
Name: aqute-bnd
Version: 2.4.1
Summary: BND Tool
License: ASL 2.0
Url: http://www.aqute.biz/Bnd/Bnd
Packager: Igor Vlasenko <viy@altlinux.ru>
Provides: aqute-bnd = 2.4.1-2.fc23
Provides: mvn(biz.aQute.bnd:biz.aQute.bnd) = 2.4.1
Provides: mvn(biz.aQute.bnd:biz.aQute.bnd:pom:) = 2.4.1
Provides: mvn(biz.aQute.bnd:bnd) = 2.4.1
Provides: mvn(biz.aQute.bnd:bnd:pom:) = 2.4.1
Provides: mvn(biz.aQute:bnd) = 2.4.1
Provides: mvn(biz.aQute:bnd:pom:) = 2.4.1
Requires: /bin/bash
Requires: java-headless
Requires: jpackage-utils
Requires: mvn(ant:ant)
Requires: mvn(biz.aQute.bnd:biz.aQute.bndlib)
Requires: mvn(org.eclipse.osgi:org.eclipse.osgi)
Requires: mvn(org.eclipse.osgi:org.eclipse.osgi.services)

BuildArch: noarch
Group: Development/Java
Release: alt0.2jpp
Source: aqute-bnd-2.4.1-2.fc23.cpio

%description
The bnd tool helps you create and diagnose OSGi bundles.
The key functions are:
- Show the manifest and JAR contents of a bundle
- Wrap a JAR so that it becomes a bundle
- Create a Bundle from a specification and a class path
- Verify the validity of the manifest entries
The tool is capable of acting as:
- Command line tool
- File format
- Directives
- Use of macros

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
#pushd %buildroot/usr/share/java
#ln -s aqute-bnd/biz.aQute.bnd.jar aqute-bnd.jar
#popd

%files -f %name-list
#/usr/share/java/aqute-bnd.jar

%changelog
* Tue Feb 02 2016 Igor Vlasenko <viy@altlinux.ru> 2.4.1-alt0.2jpp
- removed compatibility symlink

* Fri Jan 22 2016 Igor Vlasenko <viy@altlinux.ru> 2.4.1-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

* Fri Sep 05 2014 Igor Vlasenko <viy@altlinux.ru> 0.0.363-alt2_14jpp7
- new release

* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 0.0.363-alt2_8jpp7
- new release

* Mon Jul 14 2014 Igor Vlasenko <viy@altlinux.ru> 0.0.363-alt2_7jpp7
- NMU rebuild to move poms and fragments

* Fri Aug 24 2012 Igor Vlasenko <viy@altlinux.ru> 0.0.363-alt1_7jpp7
- complete build

* Thu Mar 08 2012 Igor Vlasenko <viy@altlinux.ru> 0.0.363-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

