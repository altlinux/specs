Name: aether
Version: 1.13.1
Summary: Sonatype library to resolve, install and deploy artifacts the Maven way
License: EPL or ASL 2.0
Url: https://docs.sonatype.org/display/AETHER/Home
Packager: Igor Vlasenko <viy@altlinux.ru>
Requires: async-http-client
Requires: java
Requires: jboss-parent

BuildArch: noarch
Group: Development/Java
Release: alt0.1jpp
Source: aether-1.13.1-1.fc17.cpio

%description
Aether is standalone library to resolve, install and deploy artifacts
the Maven way developed by Sonatype

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
* Wed Mar 07 2012 Igor Vlasenko <viy@altlinux.ru> 1.13.1-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

