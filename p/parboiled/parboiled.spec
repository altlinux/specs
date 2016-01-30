Name: parboiled
Version: 1.1.6
Summary: Java/Scala library providing parsing of input text based on PEGs
License: ASL 2.0
Url: http://parboiled.org/
Packager: Igor Vlasenko <viy@altlinux.ru>
Provides: mvn(org.parboiled:parboiled-core) = 1.1.6
Provides: mvn(org.parboiled:parboiled-core:pom:) = 1.1.6
Provides: mvn(org.parboiled:parboiled-java) = 1.1.6
Provides: mvn(org.parboiled:parboiled-java:pom:) = 1.1.6
Provides: parboiled = 1.1.6-8.fc23
Requires: java-headless
Requires: jpackage-utils
Requires: mvn(org.ow2.asm:asm)
Requires: mvn(org.ow2.asm:asm-analysis)
Requires: mvn(org.ow2.asm:asm-tree)
Requires: mvn(org.ow2.asm:asm-util)

BuildArch: noarch
Group: Development/Java
Release: alt0.1jpp
Source: parboiled-1.1.6-8.fc23.cpio

%description
parboiled is a mixed Java/Scala library providing for lightweight and
easy-to-use, yet powerful and elegant parsing of arbitrary input text
based on Parsing expression grammars (PEGs). PEGs are an alternative to
context free grammars (CFGs) for formally specifying syntax, they
make a good replacement for regular expressions and generally have quite
a few advantages over the "traditional" way of building parser via CFGs.

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
* Mon Jan 25 2016 Igor Vlasenko <viy@altlinux.ru> 1.1.6-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 1.0.2-alt2_6jpp7
- new release

* Thu Aug 07 2014 Igor Vlasenko <viy@altlinux.ru> 1.0.2-alt2_3jpp7
- rebuild with maven-local

* Tue Mar 05 2013 Igor Vlasenko <viy@altlinux.ru> 1.0.2-alt1_3jpp7
- fc update

* Mon Sep 17 2012 Igor Vlasenko <viy@altlinux.ru> 1.0.2-alt1_2jpp7
- new version

