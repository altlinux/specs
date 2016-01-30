Name: jsch-agent-proxy-pageant
Version: 0.0.8
Summary: Pageant connector for jsch-agent-proxy
License: BSD
Url: http://www.jcraft.com/jsch-agent-proxy/
Packager: Igor Vlasenko <viy@altlinux.ru>
Provides: jsch-agent-proxy-pageant = 0.0.8-2.fc23
Provides: mvn(com.jcraft:jsch.agentproxy.pageant) = 0.0.8
Provides: mvn(com.jcraft:jsch.agentproxy.pageant:pom:) = 0.0.8
Requires: java-headless
Requires: jpackage-utils
Requires: mvn(com.jcraft:jsch.agentproxy.core)
Requires: mvn(net.java.dev.jna:jna)
Requires: mvn(net.java.dev.jna:jna-platform)

BuildArch: noarch
Group: Development/Java
Release: alt0.1jpp
Source: jsch-agent-proxy-pageant-0.0.8-2.fc23.cpio

%description
Pageant connector for jsch-agent-proxy.

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
* Wed Jan 20 2016 Igor Vlasenko <viy@altlinux.ru> 0.0.8-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

