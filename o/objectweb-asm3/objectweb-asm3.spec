Provides: /etc/java/objectweb-asm3.conf
Name: objectweb-asm3
Version: 3.3.1
Summary: Java bytecode manipulation and analysis framework
License: BSD
Url: http://asm.ow2.org/
Packager: Igor Vlasenko <viy@altlinux.ru>
Provides: mvn(asm:asm) = 3.3.1
Provides: mvn(asm:asm-all) = 3.3.1
Provides: mvn(asm:asm-all-distroshaded) = 3.3.1
Provides: mvn(asm:asm-all-distroshaded:pom:) = 3.3.1
Provides: mvn(asm:asm-all:pom:) = 3.3.1
Provides: mvn(asm:asm-analysis) = 3.3.1
Provides: mvn(asm:asm-analysis-distroshaded) = 3.3.1
Provides: mvn(asm:asm-analysis-distroshaded:pom:) = 3.3.1
Provides: mvn(asm:asm-analysis:pom:) = 3.3.1
Provides: mvn(asm:asm-commons) = 3.3.1
Provides: mvn(asm:asm-commons-distroshaded) = 3.3.1
Provides: mvn(asm:asm-commons-distroshaded:pom:) = 3.3.1
Provides: mvn(asm:asm-commons:pom:) = 3.3.1
Provides: mvn(asm:asm-distroshaded) = 3.3.1
Provides: mvn(asm:asm-distroshaded:pom:) = 3.3.1
Provides: mvn(asm:asm-parent:pom:) = 3.3.1
Provides: mvn(asm:asm-tree) = 3.3.1
Provides: mvn(asm:asm-tree-distroshaded) = 3.3.1
Provides: mvn(asm:asm-tree-distroshaded:pom:) = 3.3.1
Provides: mvn(asm:asm-tree:pom:) = 3.3.1
Provides: mvn(asm:asm-util) = 3.3.1
Provides: mvn(asm:asm-util-distroshaded) = 3.3.1
Provides: mvn(asm:asm-util-distroshaded:pom:) = 3.3.1
Provides: mvn(asm:asm-util:pom:) = 3.3.1
Provides: mvn(asm:asm-xml) = 3.3.1
Provides: mvn(asm:asm-xml-distroshaded) = 3.3.1
Provides: mvn(asm:asm-xml-distroshaded:pom:) = 3.3.1
Provides: mvn(asm:asm-xml:pom:) = 3.3.1
Provides: mvn(asm:asm:pom:) = 3.3.1
Provides: objectweb-asm3 = 3.3.1-12.fc23
Requires: /bin/bash
Requires: java-headless
Requires: jpackage-utils

BuildArch: noarch
Group: Development/Java
Release: alt0.1jpp
Source: objectweb-asm3-3.3.1-12.fc23.cpio

%description
ASM is an all purpose Java bytecode manipulation and analysis
framework.  It can be used to modify existing classes or dynamically
generate classes, directly in binary form.  Provided common
transformations and analysis algorithms allow to easily assemble
custom complex transformations and code analysis tools.

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
* Thu Jan 28 2016 Igor Vlasenko <viy@altlinux.ru> 3.3.1-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

