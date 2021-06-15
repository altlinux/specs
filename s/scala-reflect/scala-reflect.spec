
# sometimes commpress gets crazy (see maven-scm-javadoc for details)
%set_compress_method none

Name: scala-reflect
Version: 2.13.5
Summary: Scala reflection library
License: ASL 2.0 and BSD and MIT
Url: http://www.scala-lang.org/
Group: Development/Java
Release: alt0.1jpp

Packager: Igor Vlasenko <viy@altlinux.org>
Provides: mvn(org.scala-lang:scala-reflect) = 2.13.5
Provides: mvn(org.scala-lang:scala-reflect:pom:) = 2.13.5
Provides: osgi(org.scala-lang.scala-reflect) = 2.13.5
Requires: java-headless
Requires: javapackages-filesystem
Requires: mvn(org.scala-lang:scala-library)
Requires: scala-library

BuildArch: noarch
Source: scala-reflect-2.13.5-1.fc34.cpio


%description
Scala is a general purpose programming language designed to express
common programming patterns in a concise, elegant, and type-safe way.
It smoothly integrates features of object-oriented and functional
languages.  It is also fully interoperable with Java.

This package contains the reflection library for the Scala programming
language.

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
* Mon Jun 14 2021 Igor Vlasenko <viy@altlinux.org> 2.13.5-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

* Sun Jun 13 2021 Igor Vlasenko <viy@altlinux.org> 2.10.6-alt3_17jpp8
- use jline2

* Sat Feb 15 2020 Igor Vlasenko <viy@altlinux.ru> 2.10.6-alt2_17jpp8
- fc update

* Mon May 27 2019 Igor Vlasenko <viy@altlinux.ru> 2.10.6-alt2_15jpp8
- new version

* Tue May 08 2018 Igor Vlasenko <viy@altlinux.ru> 2.10.6-alt2_8jpp8
- java update

* Sat Nov 18 2017 Igor Vlasenko <viy@altlinux.ru> 2.10.6-alt2_3jpp8
- added BR: javapackages-local for javapackages 5

* Thu Nov 16 2017 Igor Vlasenko <viy@altlinux.ru> 2.10.6-alt1_3jpp8
- new version

* Sun Nov 05 2017 Igor Vlasenko <viy@altlinux.ru> 2.10.4-alt2_9jpp8
- updated dependencies

* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 2.10.4-alt1_9jpp8
- new fc release

* Tue Feb 02 2016 Igor Vlasenko <viy@altlinux.ru> 2.10.4-alt1_8jpp8
- new version

* Tue Feb 02 2016 Igor Vlasenko <viy@altlinux.ru> 2.10.4-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

