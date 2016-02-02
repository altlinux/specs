Name: joda-convert
Version: 1.7
Summary: Java library for conversion to and from standard string formats
License: ASL 2.0
Url: https://github.com/JodaOrg/joda-convert/
Packager: Igor Vlasenko <viy@altlinux.ru>
Provides: joda-convert = 1.7-2.fc23
Provides: mvn(org.joda:joda-convert) = 1.7
Provides: mvn(org.joda:joda-convert:pom:) = 1.7
Requires: java-headless
Requires: jpackage-utils

BuildArch: noarch
Group: Development/Java
Release: alt0.1jpp
Source: joda-convert-1.7-2.fc23.cpio

%description
Java library to enable conversion to and from standard string formats.

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
* Tue Feb 02 2016 Igor Vlasenko <viy@altlinux.ru> 1.7-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 1.3.1-alt1_2jpp7
- new release

* Fri Aug 01 2014 Igor Vlasenko <viy@altlinux.ru> 1.3-alt1_1jpp7
- new version

* Mon Jul 14 2014 Igor Vlasenko <viy@altlinux.ru> 1.2-alt2_3jpp7
- NMU rebuild to move poms and fragments

* Mon Sep 17 2012 Igor Vlasenko <viy@altlinux.ru> 1.2-alt1_3jpp7
- new version

