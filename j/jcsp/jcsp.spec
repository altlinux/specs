Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires: rpm-build-java
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
# %%version is ahead of its definition. Predefining for rpm 4.0 compatibility.
%define version 1.1
%global namedreltag -rc5
%global namedversion %{version}%{?namedreltag}
Name:          jcsp
Version:       1.1
Release:       alt1_0.8.rc5jpp8
Summary:       Communicating Sequential Processes for Java (JCSP)
License:       LGPLv2+
URL:           https://github.com/codehaus/jcsp
# sh jcsp-create-tarball.sh < VERSION-TAG >
Source0:       %{name}-%{namedversion}-clean.tar.xz
Source1:       %{name}-create-tarball.sh

BuildRequires: maven-local
BuildRequires: mvn(junit:junit)
BuildRequires: mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires: mvn(org.apache.felix:org.osgi.core)

BuildArch:     noarch
Source44: import.info

%description
JCSP (Communication Sequential Processes for Java) is a
library providing a concurrency model that is a combination
of ideas from Hoare's CSP and Milner's pi-calculus.

Communicating Sequential Processes (CSP) is a mathematical
theory for specifying and verifying complex patterns of
behavior arising from interactions between concurrent
objects.

JCSP provides a base range of CSP primitives plus a rich set of
extensions. Also included is a package providing CSP process
wrappers giving a channel interface to all Java AWT widgets
and graphics operations.  It is extensively (java/documented)
and includes much teaching.

JCSP is an alternative concurrency model to the threads and
mechanisms built into Java. It is also compatible with
it since it is implemented on top of it.

%package javadoc
Group: Development/Java
Summary:       Javadoc for %{name}
BuildArch: noarch

%description javadoc
This package contains javadoc for %{name}.

%prep
%setup -q -n %{name}-%{namedversion}

%pom_remove_plugin :cobertura-maven-plugin
%pom_remove_plugin :findbugs-maven-plugin
%pom_remove_plugin :jdepend-maven-plugin
%pom_remove_plugin :rat-maven-plugin
%pom_remove_plugin :taglist-maven-plugin

# remove wagon-webdav
%pom_xpath_remove "pom:project/pom:build/pom:extensions"
# fix resouce directory and filter these ones
%pom_xpath_inject "pom:project/pom:build" "
<resources>
  <resource>
    <directory>src</directory>
    <excludes>
      <exclude>**/*.java</exclude>
      <exclude>**/doc-files/**</exclude>
      <exclude>**/win32/*Services.txt</exclude>
      <exclude>**/package.html</exclude>
    </excludes>
  </resource>
</resources>"

%pom_xpath_remove "pom:project/pom:reporting/pom:plugins/pom:plugin[pom:artifactId='maven-javadoc-plugin']/pom:configuration/pom:excludePackageNames"

%pom_xpath_remove "pom:project/pom:build/pom:plugins/pom:plugin[pom:artifactId='maven-bundle-plugin']/pom:configuration/pom:instructions/pom:Export-Package"
%pom_xpath_inject "pom:project/pom:build/pom:plugins/pom:plugin[pom:artifactId='maven-bundle-plugin']/pom:configuration/pom:instructions" '
<Export-Package>org.jcsp.*;version="${project.version}"</Export-Package>'

sed -i 's|${name}|${project.name}|' pom.xml

sed -i "s|59 Temple Place, Suite 330, Boston, MA 02111-1307 USA|51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA|" pom.xml

for d in LICENCE README ; do
  iconv -f iso8859-1 -t utf-8 $d.txt > $d.txt.conv && mv -f $d.txt.conv $d.txt
  sed -i 's/\r//' $d.txt
done

rm -r src/org/jcsp/win32 \
 src/org/jcsp/net/remote/SpawnerServiceNT.java \
 src/org/jcsp/net/tcpip/TCPIPCNSServerNT.java

%mvn_file : %{name}

%build

%mvn_build -- -Dproject.build.sourceEncoding=UTF-8

%install
%mvn_install

%files -f .mfiles
%doc README.txt
%doc --no-dereference LICENCE.txt

%files javadoc -f .mfiles-javadoc
%doc --no-dereference LICENCE.txt

%changelog
* Thu Apr 19 2018 Igor Vlasenko <viy@altlinux.ru> 1.1-alt1_0.8.rc5jpp8
- java update

* Thu Nov 09 2017 Igor Vlasenko <viy@altlinux.ru> 1.1-alt1_0.7.rc5jpp8
- fc27 update

* Sun Oct 22 2017 Igor Vlasenko <viy@altlinux.ru> 1.1-alt1_0.6.rc5jpp8
- new jpp release

* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 1.1-alt1_0.5.rc5jpp8
- new fc release

* Mon Feb 01 2016 Igor Vlasenko <viy@altlinux.ru> 1.1-alt1_0.4.rc5jpp8
- new version

* Sat Jan 30 2016 Igor Vlasenko <viy@altlinux.ru> 1.1-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

