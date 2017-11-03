Name: xmvn-subst
Version: 3.0.0
Summary: XMvn Subst
License: ASL 2.0
Url: https://fedora-java.github.io/xmvn/
Packager: Igor Vlasenko <viy@altlinux.ru>
Provides: mvn(org.fedoraproject.xmvn:xmvn-subst) = 3.0.0
Provides: mvn(org.fedoraproject.xmvn:xmvn-subst:pom:) = 3.0.0
Provides: xmvn-subst = 3.0.0-6.fc27
Requires: /bin/bash
Requires: java-headless
Requires: javapackages-tools
Requires: mvn(com.beust:jcommander)
Requires: mvn(org.fedoraproject.xmvn:xmvn-api)
Requires: mvn(org.fedoraproject.xmvn:xmvn-core)

BuildArch: noarch
Group: Development/Java
Release: alt0.1jpp
Source: xmvn-subst-3.0.0-6.fc27.cpio

%description
This package provides XMvn Subst, which is a tool that can substitute
Maven artifact files with symbolic links to corresponding files in
artifact repository.

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
* Thu Nov 02 2017 Igor Vlasenko <viy@altlinux.ru> 3.0.0-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

