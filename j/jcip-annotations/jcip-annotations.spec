Name: jcip-annotations
Version: 1
Summary: Java annotations for multithreaded software
License: CC-BY
Url: http://www.jcip.net/
Epoch: 1
Packager: Igor Vlasenko <viy@altlinux.ru>
Provides: jcip-annotations = 1-17.20060626.fc23
Provides: mvn(com.github.stephenc.jcip:jcip-annotations) = 1.0
Provides: mvn(com.github.stephenc.jcip:jcip-annotations:pom:) = 1.0
Provides: mvn(net.jcip:jcip-annotations) = 1.0
Provides: mvn(net.jcip:jcip-annotations:pom:) = 1.0
Requires: java-headless
Requires: java-headless
Requires: jpackage-utils
Requires: jpackage-utils

BuildArch: noarch
Group: Development/Java
Release: alt2jpp
Source: jcip-annotations-1-17.20060626.fc23.cpio

%description
This package provides class, field, and method level annotations for
describing thread-safety policies.  These annotations are relatively
unintrusive and are beneficial to both users and maintainers.  Users can see
immediately whether a class is thread-safe, and maintainers can see
immediately whether thread-safety guarantees must be preserved.  Annotations
are also useful to a third constituency: tools.  Static code-analysis tools
may be able to verify that the code complies with the contract indicated by
the annotation, such as verifying that a class annotated with @Immutable
actually is immutable.

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
* Sat Jan 23 2016 Igor Vlasenko <viy@altlinux.ru> 1:1-alt2jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 1:1-alt1_8.20060626jpp7
- new release

* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 1:1-alt1_7.20060626jpp7
- new release

* Sun Mar 17 2013 Igor Vlasenko <viy@altlinux.ru> 1:1-alt1_5.20060626jpp7
- fc update

* Sat Oct 23 2010 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt3_2jpp6
- added repolib

* Wed May 12 2010 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt3_1jpp5
- fixes for java6 support

* Sun Feb 21 2010 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt2_1jpp5
- use default jpp profile

* Sat Sep 06 2008 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt1_1jpp5
- converted from JPackage by jppimport script

