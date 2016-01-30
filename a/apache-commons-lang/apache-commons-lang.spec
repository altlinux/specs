Provides: jakarta-commons-lang
Name: apache-commons-lang
Version: 2.6
Summary: Provides a host of helper utilities for the java.lang API
License: ASL 2.0
Url: http://commons.apache.org/lang
Epoch: 0
Packager: Igor Vlasenko <viy@altlinux.ru>
Provides: apache-commons-lang = 2.6-17.fc23
Provides: mvn(commons-lang:commons-lang) = 2.6
Provides: mvn(commons-lang:commons-lang:pom:) = 2.6
Provides: mvn(lang:lang) = 2.6
Provides: mvn(lang:lang:pom:) = 2.6
Provides: mvn(org.apache.commons:commons-lang) = 2.6
Provides: mvn(org.apache.commons:commons-lang:pom:) = 2.6
Requires: java-headless
Requires: jpackage-utils

BuildArch: noarch
Group: Development/Java
Release: alt4jpp
Source: apache-commons-lang-2.6-17.fc23.cpio

%description
The standard Java libraries fail to provide enough methods for
manipulation of its core classes. The Commons Lang Component provides
these extra methods.
The Commons Lang Component provides a host of helper utilities for the
java.lang API, notably String manipulation methods, basic numerical
methods, object reflection, creation and serialization, and System
properties. Additionally it contains an inheritable enum type, an
exception structure that supports multiple types of nested-Exceptions
and a series of utilities dedicated to help with building methods, such
as hashCode, toString and equals.

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
* Fri Jan 22 2016 Igor Vlasenko <viy@altlinux.ru> 0:2.6-alt4jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 0:2.6-alt3_13jpp7
- new release

* Sat Aug 23 2014 Igor Vlasenko <viy@altlinux.ru> 0:2.6-alt3_12jpp7
- new release

* Thu Aug 07 2014 Igor Vlasenko <viy@altlinux.ru> 0:2.6-alt3_7jpp7
- rebuild with maven-local

* Mon Jul 14 2014 Igor Vlasenko <viy@altlinux.ru> 0:2.6-alt2_7jpp7
- NMU rebuild to move poms and fragments

* Wed Sep 05 2012 Igor Vlasenko <viy@altlinux.ru> 0:2.6-alt1_7jpp7
- new version

* Mon Mar 26 2012 Igor Vlasenko <viy@altlinux.ru> 0:2.4-alt3_7jpp6
- restored javadoc

* Sat Mar 24 2012 Igor Vlasenko <viy@altlinux.ru> 0:2.4-alt2_7jpp6
- fixed build

* Wed Jan 05 2011 Igor Vlasenko <viy@altlinux.ru> 0:2.4-alt1_7jpp6
- renamed

