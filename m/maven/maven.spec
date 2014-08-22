Name: maven
Version: 3.0.5
Summary: Java project management and project comprehension tool
License: ASL 2.0
Url: http://maven.apache.org/
Epoch: 0
Packager: Igor Vlasenko <viy@altlinux.ru>
Provides: maven2
Requires: /bin/sh
Requires: java
Requires: jpackage-utils

BuildArch: noarch
Group: Development/Java
Release: alt0.1jpp
Source: maven-3.0.5-3.fc19.cpio

%description
Maven is a software project management and comprehension tool. Based on the
concept of a project object model (POM), Maven can manage a project's build,
reporting and documentation from a central piece of information.

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
touch %buildroot/etc/mavenrc

%files -f %name-list
/etc/mavenrc

%changelog
* Fri Aug 22 2014 Igor Vlasenko <viy@altlinux.ru> 0:3.0.5-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

%changelog
* Thu Aug 07 2014 Igor Vlasenko <viy@altlinux.ru> 0:3.0.4-alt7_21.3jpp7
- rebuild with maven-local

* Sat Jul 26 2014 Igor Vlasenko <viy@altlinux.ru> 0:3.0.4-alt6_21.3jpp7
- update

* Fri Jul 18 2014 Igor Vlasenko <viy@altlinux.ru> 0:3.0.4-alt5_21jpp7
- non-bootstrap build

* Fri Jul 18 2014 Igor Vlasenko <viy@altlinux.ru> 0:3.0.4-alt4jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

