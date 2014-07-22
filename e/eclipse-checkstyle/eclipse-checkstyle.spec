# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-java
BuildRequires: unzip
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-compat
BuildRequires: rpm-build-java-osgi
%global eclipse_base %{_libdir}/eclipse
%global install_loc %{_datadir}/eclipse/dropins/checkstyle
%global cs_ver 5.1
%global eclipse_ver 3.5

Summary:   Checkstyle plugin for Eclipse
Name:      eclipse-checkstyle
Version:   5.1.0
Release:   alt1_8jpp7
License:   LGPLv2+
Group:     Development/Java
URL:       http://eclipse-cs.sourceforge.net
BuildArch: noarch

Source0: %{name}-%{version}.tar.xz
Source10: eclipse-eclipsecs-fetch-src.sh
Patch0:  itext-rtf-remove.patch
Patch1:  unpack-plugins.patch
Patch2:  remove-double-locking-check.patch

Requires: eclipse-platform >= 1:%{eclipse_ver}
Requires: eclipse-jdt
Requires: checkstyle >= 0:%{cs_ver}
Requires: antlr-tool
Requires: guava
Requires: apache-commons-beanutils
Requires: apache-commons-collections
Requires: apache-commons-io
Requires: apache-commons-lang
Requires: apache-commons-logging
Requires: dom4j

BuildRequires: jpackage-utils >= 0:1.5
BuildRequires: eclipse-pde >= 1:%{eclipse_ver}
BuildRequires: checkstyle >= 0:%{cs_ver}
BuildRequires: antlr-tool
BuildRequires: guava
BuildRequires: apache-commons-beanutils
BuildRequires: apache-commons-collections
BuildRequires: apache-commons-io
BuildRequires: apache-commons-lang
BuildRequires: apache-commons-logging
BuildRequires: jfreechart
BuildRequires: dom4j
Source44: import.info

%description
The Eclipse Checkstyle plugin integrates the Checkstyle Java code
auditor into the Eclipse IDE. The plugin provides real-time feedback
to the user about violations of rules that check for coding style and
possible error prone code constructs. 

%prep
%setup -q
%patch0 -R
%patch1
%patch2

find -name '*.class' -exec rm -f '{}' \;
find -name '*.jar' -exec rm -f '{}' \;

sed -i -e "s|checkstyle-all-5.1.jar|checkstyle.jar,antlr.jar,guava.jar,commons-beanutils.jar,commons-collections.jar,commons-logging.jar|g" \
  net.sf.eclipsecs.checkstyle/META-INF/MANIFEST.MF

ln -s $(build-classpath checkstyle) net.sf.eclipsecs.checkstyle/checkstyle.jar
ln -s $(build-classpath antlr) net.sf.eclipsecs.checkstyle/antlr.jar
ln -s $(build-classpath guava) net.sf.eclipsecs.checkstyle/guava.jar
ln -s $(build-classpath commons-beanutils) net.sf.eclipsecs.checkstyle/commons-beanutils.jar
ln -s $(build-classpath commons-collections) net.sf.eclipsecs.checkstyle/commons-collections.jar
ln -s $(build-classpath commons-logging) net.sf.eclipsecs.checkstyle/commons-logging.jar

ln -s %{_javadir}/commons-io.jar net.sf.eclipsecs.core/lib/commons-io-1.2.jar
ln -s %{_javadir}/commons-lang.jar net.sf.eclipsecs.core/lib/commons-lang-2.3.jar
ln -s %{_javadir}/dom4j.jar net.sf.eclipsecs.core/lib/dom4j-1.6.1.jar

ln -s %{_javadir}/jcommon.jar net.sf.eclipsecs.ui/lib/jcommon-1.0.9.jar
ln -s %{_javadir}/jfreechart/jfreechart.jar net.sf.eclipsecs.ui/lib/jfreechart-1.0.5.jar
ln -s %{_javadir}/itext.jar net.sf.eclipsecs.ui/lib/itext-2.0.1.jar

rm -fr net.sf.eclipsecs.ui/src/net/sf/eclipsecs/ui/stats/export/internal/RTFStatsExporter.java

%build
eclipse-pdebuild -f net.sf.eclipsecs

%install
install -d -m 755 $RPM_BUILD_ROOT%{install_loc}

unzip -q -o -d $RPM_BUILD_ROOT%{install_loc} \
 build/rpmBuild/net.sf.eclipsecs.zip

pushd $RPM_BUILD_ROOT%{install_loc}/eclipse/plugins
rm -fr net.sf.eclipsecs.checkstyle_0.0.0/*.jar
ln -s $(build-classpath checkstyle) net.sf.eclipsecs.checkstyle_0.0.0/checkstyle.jar
ln -s $(build-classpath guava) net.sf.eclipsecs.checkstyle_0.0.0/guava.jar
ln -s $(build-classpath antlr) net.sf.eclipsecs.checkstyle_0.0.0/antlr.jar
ln -s $(build-classpath commons-beanutils) net.sf.eclipsecs.checkstyle_0.0.0/commons-beanutils.jar
ln -s $(build-classpath commons-collections) net.sf.eclipsecs.checkstyle_0.0.0/commons-collections.jar
ln -s $(build-classpath commons-logging) net.sf.eclipsecs.checkstyle_0.0.0/commons-logging.jar

rm -fr net.sf.eclipsecs.core_0.0.0/lib/*.jar
ln -s %{_javadir}/commons-io.jar net.sf.eclipsecs.core_0.0.0/lib/commons-io-1.2.jar
ln -s %{_javadir}/commons-lang.jar net.sf.eclipsecs.core_0.0.0/lib/commons-lang-2.3.jar
ln -s %{_javadir}/dom4j.jar net.sf.eclipsecs.core_0.0.0/lib/dom4j-1.6.1.jar

rm -fr net.sf.eclipsecs.ui_0.0.0/lib/*.jar
ln -s %{_javadir}/jcommon.jar net.sf.eclipsecs.ui_0.0.0/lib/jcommon-1.0.9.jar
ln -s %{_javadir}/jfreechart/jfreechart.jar net.sf.eclipsecs.ui_0.0.0/lib/jfreechart-1.0.5.jar
ln -s %{_javadir}/itext.jar net.sf.eclipsecs.ui_0.0.0/lib/itext-2.0.1.jar
popd

%files
%doc net.sf.eclipsecs-feature/license.html
%{install_loc}

%changelog
* Tue Jul 22 2014 Igor Vlasenko <viy@altlinux.ru> 5.1.0-alt1_8jpp7
- update

* Fri Mar 26 2010 Igor Vlasenko <viy@altlinux.ru> 4.0.1-alt2_14jpp6
- rebuild with checkstyle 4.4

* Wed Jan 27 2010 Igor Vlasenko <viy@altlinux.ru> 4.0.1-alt1_14jpp6
- new version

* Sun Jan 04 2009 Igor Vlasenko <viy@altlinux.ru> 4.0.1-alt1_11jpp6
- new version

* Thu Jul 31 2008 Igor Vlasenko <viy@altlinux.ru> 4.0.1-alt1_10jpp6
- rebuild with eclipse 3.3.2

* Fri Nov 30 2007 Igor Vlasenko <viy@altlinux.ru> 4.0.1-alt1_9jpp5.0
- converted from JPackage by jppimport script

