Name: snappy-java
Version: 1.0.5
Summary: Fast compressor/decompresser
License: ASL 2.0
Url: http://xerial.org/snappy-java/
Packager: Igor Vlasenko <viy@altlinux.ru>
Provides: mvn(org.xerial.snappy:snappy-java) = 1.0.5
Provides: mvn(org.xerial.snappy:snappy-java:pom:) = 1.0.5
Provides: snappy-java = 1.0.5-5.fc23
Requires: java-headless
Requires: jpackage-utils
Requires: libsnappy

BuildArch: noarch
Group: Development/Java
Release: alt0.1jpp
Source: snappy-java-1.0.5-5.fc23.cpio

%description
A Java port of the snappy, a fast compresser/decompresser written in C++.

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
* Fri Jan 22 2016 Igor Vlasenko <viy@altlinux.ru> 1.0.5-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

* Mon Sep 15 2014 Igor Vlasenko <viy@altlinux.ru> 1.0.4.1-alt3_5jpp7
- fixed build

* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 1.0.4.1-alt2_5jpp7
- new release

* Mon Jul 14 2014 Igor Vlasenko <viy@altlinux.ru> 1.0.4.1-alt2_3jpp7
- NMU rebuild to move poms and fragments

* Thu Sep 13 2012 Igor Vlasenko <viy@altlinux.ru> 1.0.4.1-alt1_3jpp7
- new version

