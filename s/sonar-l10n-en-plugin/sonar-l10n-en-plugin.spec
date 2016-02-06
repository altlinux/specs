Name: sonar-l10n-en-plugin
Version: 3.2
Summary: L10n-en-plugin module for sonar
License: LGPLv3+
Url: http://www.sonarqube.org
Packager: Igor Vlasenko <viy@altlinux.ru>
Provides: mvn(org.codehaus.sonar.plugins:sonar-l10n-en-plugin) = 3.2
Provides: mvn(org.codehaus.sonar.plugins:sonar-l10n-en-plugin:pom:) = 3.2
Provides: sonar-l10n-en-plugin = 3.2-5.fc23
Requires: java-headless
Requires: jpackage-utils
Requires: mvn(com.google.code.findbugs:jsr305)

BuildArch: noarch
Group: Development/Java
Release: alt0.1jpp
Source: sonar-l10n-en-plugin-3.2-5.fc23.cpio

%description
L10n-en-plugin module for sonar.

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
* Sat Feb 06 2016 Igor Vlasenko <viy@altlinux.ru> 3.2-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

