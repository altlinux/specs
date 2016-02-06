Name: tika
Version: 1.5
Summary: A content analysis toolkit
License: ASL 2.0
Url: http://tika.apache.org/
Packager: Igor Vlasenko <viy@altlinux.ru>
Provides: mvn(org.apache.tika:tika-core) = 1.5
Provides: mvn(org.apache.tika:tika-core:pom:) = 1.5
Provides: mvn(org.apache.tika:tika-parent:pom:) = 1.5
Provides: mvn(org.apache.tika:tika:pom:) = 1.5
Provides: tika = 1.5-6.fc23
Requires: java-headless
Requires: jpackage-utils

BuildArch: noarch
Group: Development/Java
Release: alt0.1jpp
Source: tika-1.5-6.fc23.cpio

%description
The Apache Tika toolkit detects and extracts meta-data and
structured text content from various documents using existing
parser libraries.

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
* Sat Feb 06 2016 Igor Vlasenko <viy@altlinux.ru> 1.5-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

