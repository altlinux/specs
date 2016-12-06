Epoch: 0
Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
# END SourceDeps(oneline)
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
Name:           jmdns
Version:        3.4.1
Release:        alt1_10jpp8
Summary:        Java implementation of multi-cast DNS

# The project was originally developed under the GNU
# Lesser General Public License. It was later moved to Sourceforge
# and re-released under the Apache License, Version 2.0.
# See NOTICE.txt for more details
License:        ASL 2.0 and LGPLv2+
URL:            http://jmdns.sourceforge.net/
# sh create-tarball.sh
Source0:        %{name}-%{version}.tar.gz
Source1:        create-tarball.sh
# faster (unclean) shutdown, used by Jenkins
# https://github.com/jenkinsci/jmdns/commit/4d56e6f0f0c230b14f1353252ae3d42ff7a5b27c
Patch0:         0001-added-an-unclean-shut-down-that-s-a-whole-lot-faster.patch

BuildRequires:  maven-local
BuildRequires:  mvn(org.sonatype.oss:oss-parent:pom:)

BuildArch:      noarch
Source44: import.info

%description
JmDNS is a Java implementation of multi-cast DNS
and can be used for service registration and discovery
in local area networks. JmDNS is fully compatible
with Apple's Bonjour.

%package        javadoc
Group: Development/Documentation
Summary:        Javadoc for %{name}
BuildArch: noarch

%description javadoc
This package contains the API documentation for %{name}.


%prep
%setup -q -n %{name}-%{version}

%patch0 -p1

# Fix FSF address
sed -i "s,59 Temple Place,51 Franklin Street,;s,Suite 330,Fifth Floor,;s,02111-1307,02110-1301," \
  src/sample/java/samples/DiscoverServiceTypes.java LICENSE-LGPL.txt

chmod -x README.txt LICENSE-LGPL.txt
sed -i 's/\r//' LICENSE-LGPL.txt

%mvn_alias : "org.jenkins-ci:jmdns"

%build
# Tests are disabled because they try to use network
%mvn_build -f

%install
%mvn_install


%files -f .mfiles
%dir %{_javadir}/%{name}
%doc LICENSE LICENSE-LGPL.txt NOTICE.txt README.txt
%files javadoc -f .mfiles-javadoc
%doc LICENSE LICENSE-LGPL.txt NOTICE.txt README.txt


%changelog
* Tue Dec 06 2016 Igor Vlasenko <viy@altlinux.ru> 0:3.4.1-alt1_10jpp8
- new version

* Wed Oct 03 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt2_1jpp1.7
- added ant-junit BR:

* Mon Jun 04 2007 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt1_1jpp1.7
- converted from JPackage by jppimport script

