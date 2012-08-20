Name: gmaven
Version: 1.3
Summary: Groovy Maven Integration
License: ASL 2.0
Url: http://groovy.codehaus.org/GMaven
Epoch: 0
Packager: Igor Vlasenko <viy@altlinux.ru>
Requires: jpackage-utils
Requires: jpackage-utils
Requires: ant
Requires: codehaus-parent
Requires: gmaven-provider
Requires: sonatype-gossip
Requires: gshell
Requires: jakarta-commons-lang
Requires: jline
Requires: jpackage-utils
Requires: junit
Requires: maven-shared-file-management
Requires: maven-shared-reporting-impl
Requires: plexus-container-default
Requires: plexus-digest
Requires: plexus-utils
Requires: qdox
Requires: slf4j

BuildArch: noarch
Group: Development/Java
Release: alt4jpp
Source: gmaven-1.3-alt1_3jpp6.cpio

%description
GMaven provides integration of the Groovy language into Maven.
With GMaven you can:
* Build Groovy Projects
* Execute Groovy Code
* Run Groovy Tools
* Implement Maven Plugins
Advanced:
* Groovy Runtime
* Advanced Configuration

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
* Mon Aug 20 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.3-alt4jpp
- bootstrap jar pack to restore broken gmaven jars

%changelog
* Fri Jun 22 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.3-alt3_3jpp6
- dropped plexus-maven-plugin (unused)

* Thu Jun 21 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.3-alt2_3jpp6
- fixed build

* Wed Feb 08 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.3-alt1_3jpp6
- full version

* Wed Feb 08 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.3-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

