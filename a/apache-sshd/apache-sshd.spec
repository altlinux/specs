Name: apache-sshd
Version: 0.11.0
Summary: Apache SSHD
License: ASL 2.0
Url: http://mina.apache.org/sshd-project/
Packager: Igor Vlasenko <viy@altlinux.ru>
Provides: apache-sshd = 0.11.0-5.fc23
Provides: mvn(org.apache.sshd:sshd-core) = 0.11.0
Provides: mvn(org.apache.sshd:sshd-core:pom:) = 0.11.0
Provides: mvn(org.apache.sshd:sshd:pom:) = 0.11.0
Requires: java-headless
Requires: jpackage-utils
Requires: mvn(org.apache.mina:mina-core)

BuildArch: noarch
Group: Development/Java
Release: alt0.1jpp
Source: apache-sshd-0.11.0-5.fc23.cpio

%description
Apache SSHD is a 100% pure java library to support the SSH protocols on both
the client and server side.

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
* Thu Feb 04 2016 Igor Vlasenko <viy@altlinux.ru> 0.11.0-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

* Tue Aug 26 2014 Igor Vlasenko <viy@altlinux.ru> 0.9.0-alt1_2jpp7
- new release

* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 0.7.0-alt2_3jpp7
- new release

* Mon Jul 14 2014 Igor Vlasenko <viy@altlinux.ru> 0.7.0-alt2_1jpp7
- NMU rebuild to move poms and fragments

* Wed Sep 05 2012 Igor Vlasenko <viy@altlinux.ru> 0.7.0-alt1_1jpp7
- new release

