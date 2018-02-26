# BEGIN SourceDeps(oneline):
BuildRequires: unzip
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-compat
# Copyright (c) 2000-2009, JPackage Project
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions
# are met:
#
# 1. Redistributions of source code must retain the above copyright
#    notice, this list of conditions and the following disclaimer.
# 2. Redistributions in binary form must reproduce the above copyright
#    notice, this list of conditions and the following disclaimer in the
#    documentation and/or other materials provided with the
#    distribution.
# 3. Neither the name of the JPackage Project nor the names of its
#    contributors may be used to endorse or promote products derived
#    from this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
# "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
# LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR
# A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT
# OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
# SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT
# LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
# DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY
# THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
# (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
# OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
#

%define with()          %{expand:%%{?with_%{1}:1}%%{!?with_%{1}:0}}
%define without()       %{expand:%%{?with_%{1}:0}%%{!?with_%{1}:1}}
%define bcond_with()    %{expand:%%{?_with_%{1}:%%global with_%{1} 1}}
%define bcond_without() %{expand:%%{!?_without_%{1}:%%global with_%{1} 1}}


Name:           findbugs
Version:        1.3.9
Release:        alt1_5jpp6
Epoch:          0
Summary:        Bug Pattern Detector for Java
License:        LGPLv2+
URL:            http://findbugs.sourceforge.net/
Group:          Development/Java
Source0:        http://download.sourceforge.net/findbugs/findbugs-%{version}-source.zip
Source1:        findbugs-script
Source2:        findbugs-16x16.png
Source3:        findbugs-32x32.png
Source4:        findbugs-48x48.png
Source5:        findbugs.desktop
Source6:        http://repo1.maven.org/maven2/com/google/code/findbugs/findbugs/1.3.9/findbugs-1.3.9.pom
Source7:        http://repo1.maven.org/maven2/com/google/code/findbugs/annotations/1.3.9/annotations-1.3.9.pom
Source8:        http://repo1.maven.org/maven2/com/google/code/findbugs/findbugs-ant/1.3.9/findbugs-ant-1.3.9.pom
Source9:        http://repo1.maven.org/maven2/com/google/code/findbugs/bcel/1.3.9/bcel-1.3.9.pom
Source10:       http://repo1.maven.org/maven2/com/google/code/findbugs/jFormatString/1.3.9/jFormatString-1.3.9.pom
Source11:       http://repo1.maven.org/maven2/com/google/code/findbugs/jsr305/1.3.9/jsr305-1.3.9.pom
Patch0:         findbugs-build_xml.patch
Patch1:         findbugs-bcel.patch
Patch2:         findbugs-manifest.patch
Patch3:         findbugs-pom.patch
Requires(post): jpackage-utils >= 0:1.7.3
Requires(postun): jpackage-utils >= 0:1.7.3
Requires:       ant
Requires:       bcel5.3
Requires:       dom4j
Requires:       jakarta-commons-lang
Requires:       jaxen
Requires:       jcip-annotations
Requires:       jformatstring
Requires:       jpackage-utils >= 0:1.7.3
Requires:       jsr-305
BuildRequires:  ant >= 0:1.6.5
BuildRequires:  ant-nodeps
BuildRequires:  ant-junit
BuildRequires:  bcel5.3
BuildRequires:  desktop-file-utils
BuildRequires:  docbook-xsl >= 0:1.75.2
BuildRequires:  dom4j
BuildRequires:  jakarta-commons-lang
BuildRequires:  jaxen
BuildRequires:  jcip-annotations
BuildRequires:  jdepend
BuildRequires:  jformatstring
BuildRequires:  jpackage-utils >= 0:1.7.3
BuildRequires:  jsr-305
BuildRequires:  junit4
BuildRequires:  objectweb-asm >= 0:3.0
BuildRequires:  saxon >= 0:6.5.5
BuildArch:      noarch
Source44: import.info

%description
FindBugs is a program to find bugs in Java programs. It looks for 
instances of ``bug patterns''---code instances that are likely to be 
errors.

%package javadoc
Summary:        Javadoc for %{name}
Group:          Development/Documentation
Requires:       jpackage-utils
BuildArch: noarch

%description javadoc
%{summary}.

%package manual
Summary:        Documents for %{name}
Group:          Development/Documentation
BuildArch: noarch

%description manual
%{summary}.

%prep
%setup -q
%patch0 -p0 -b .sav0
%patch1 -p1 -b .sav1
%patch2 -p1 -b .sav2
%{__cp} %{SOURCE6} findbugs-1.3.9.pom
%patch3 -p0 -b .sav3

%{_bindir}/find -type f -name "*.bat" | %{_bindir}/xargs -t %{__rm}
%{_bindir}/find -type f -name "*.jar" | %{_bindir}/xargs -t %{__rm}
%{__rm} -r doc

%{__rm} src/java/edu/umd/cs/findbugs/gui/OSXAdapter.java
%{__rm} src/java5/edu/umd/cs/findbugs/gui2/OSXAdapter.java
%{__rm} -r src/java5/net/jcip/annotations

pushd lib
%{__ln_s} $(build-classpath ant) ant.jar
%{__ln_s} $(build-classpath bcel5.3) bcel.jar
%{__ln_s} $(build-classpath commons-lang) commons-lang.jar
%{__ln_s} $(build-classpath dom4j) dom4j.jar
%{__ln_s} $(build-classpath jaxen) jaxen.jar
%{__ln_s} $(build-classpath jcip-annotations) jcip-annotations.jar
%{__ln_s} $(build-classpath jdepend) jdepend-2.9.jar
%if %without bundled_jformatstring
%{__ln_s} $(build-classpath jformatstring) jFormatString.jar
%endif
%{__ln_s} $(build-classpath jsr-305) jsr305.jar
%{__ln_s} $(build-classpath junit4) junit.jar
%{__ln_s} $(build-classpath objectweb-asm/asm) asm.jar
%{__ln_s} $(build-classpath objectweb-asm/asm-analysis) asm-analysis.jar
%{__ln_s} $(build-classpath objectweb-asm/asm-commons) asm-commons.jar
%{__ln_s} $(build-classpath objectweb-asm/asm-tree) asm-tree.jar
%{__ln_s} $(build-classpath objectweb-asm/asm-util) asm-util.jar
%{__ln_s} $(build-classpath objectweb-asm/asm-xml) asm-xml.jar
popd

%if 0
# FIXME: setup is monolithic right now, as especially the ant task
# doesn't read the CLASSPATH
%{__perl} -p -i -e 's|^Class-Path:.*\n||g' etc/*.MF
%endif

%{__perl} -pi -e 's/\r$//g;' src/doc/manual_ja.xml

%{__unzip} -qq %{_javadir}/docbook-xsl-ns-resources.zip
# offline
sed -i -e s,http://findbugs.googlecode.com/svn/trunk/findbugs/etc/docbook/docbookx.dtd,`pwd`/etc/docbook/docbookx.dtd,g `grep -rl 'http://findbugs.googlecode.com/svn/trunk/findbugs/etc/docbook/docbookx.dtd' .`

%build
export CLASSPATH=
export OPT_JAR_LIST="`%{__cat} %{_sysconfdir}/ant.d/{junit,nodeps}`"
%{ant} -Dsaxon.home=%{_javadir} -Dfop.home=%{_javadir} -Dxsl.stylesheet.home=`pwd`/docbook dist

%install

%{__mkdir_p} %{buildroot}%{_javadir}/%{name}
%{__cp} -p lib/findbugs.jar %{buildroot}%{_javadir}/%{name}/findbugs-%{version}.jar
%{__cp} -p lib/findbugs-ant.jar %{buildroot}%{_javadir}/%{name}/findbugs-ant-%{version}.jar
%{__cp} -p lib/annotations.jar %{buildroot}%{_javadir}/%{name}/annotations-%{version}.jar
(cd %{buildroot}%{_javadir}/%{name} && for jar in *-%{version}*; do %{__ln_s} ${jar} ${jar/-%{version}/}; done)

pushd %{buildroot}%{_javadir}/%{name}
%{__ln_s} $(build-classpath ant) ant.jar
%{__ln_s} $(build-classpath bcel5.3) bcel.jar
%{__ln_s} $(build-classpath commons-lang) commons-lang.jar
%{__ln_s} $(build-classpath dom4j) dom4j.jar
%{__ln_s} $(build-classpath jaxen) jaxen.jar
%{__ln_s} $(build-classpath jcip-annotations) jcip-annotations.jar
%if %without bundled_jformatstring
%{__ln_s} $(build-classpath jformatstring) jFormatString.jar
%endif
%{__ln_s} $(build-classpath jsr-305) jsr305.jar
%{__ln_s} $(build-classpath objectweb-asm/asm) asm.jar
%{__ln_s} $(build-classpath objectweb-asm/asm-analysis) asm-analysis.jar
%{__ln_s} $(build-classpath objectweb-asm/asm-commons) asm-commons.jar
%{__ln_s} $(build-classpath objectweb-asm/asm-tree) asm-tree.jar
%{__ln_s} $(build-classpath objectweb-asm/asm-util) asm-util.jar
%{__ln_s} $(build-classpath objectweb-asm/asm-xml) asm-xml.jar
popd

%{__mkdir_p} %{buildroot}%{_sysconfdir}/ant.d
%{__cat} > %{buildroot}%{_sysconfdir}/ant.d/%{name} << EOF
findbugs/findbugs findbugs/findbugs-ant
EOF

%{__mkdir_p} %{buildroot}%{_datadir}/maven2/poms
%{__cp} -p findbugs-1.3.9.pom %{buildroot}%{_datadir}/maven2/poms/JPP.%{name}-findbugs.pom
%{__cp} -p %{SOURCE7} %{buildroot}%{_datadir}/maven2/poms/JPP.%{name}-annotations.pom
%{__cp} -p %{SOURCE8} %{buildroot}%{_datadir}/maven2/poms/JPP.%{name}-findbugs-ant.pom
%{__cp} -p %{SOURCE9} %{buildroot}%{_datadir}/maven2/poms/JPP.%{name}-bcel.pom
%{__cp} -p %{SOURCE10} %{buildroot}%{_datadir}/maven2/poms/JPP.%{name}-jFormatString.pom
%{__cp} -p %{SOURCE11} %{buildroot}%{_datadir}/maven2/poms/JPP.%{name}-jsr305.pom

%add_to_maven_depmap com.google.code.findbugs annotations %{version} JPP/%{name} annotations
%add_to_maven_depmap com.google.code.findbugs bcel %{version} JPP/%{name} bcel
%add_to_maven_depmap com.google.code.findbugs findbugs %{version} JPP/%{name} findbugs
%add_to_maven_depmap com.google.code.findbugs findbugs-ant %{version} JPP/%{name} findbugs-ant
%add_to_maven_depmap com.google.code.findbugs jFormatString %{version} JPP/%{name} jFormatString
%add_to_maven_depmap com.google.code.findbugs jsr305 %{version} JPP/%{name} jsr305

%add_to_maven_depmap net.sourceforge.findbugs annotations 1.3.2 JPP/%{name} annotations
%add_to_maven_depmap net.sourceforge.findbugs bcel 1.3.2 JPP/%{name} bcel
%add_to_maven_depmap net.sourceforge.findbugs findbugs 1.3.2 JPP/%{name} findbugs
%add_to_maven_depmap net.sourceforge.findbugs findbugs-ant 1.3.2 JPP/%{name} findbugs-ant
%add_to_maven_depmap net.sourceforge.findbugs jsr305 1.3.2 JPP/%{name} jsr305

%{__mkdir_p} %{buildroot}%{_bindir}
%{__cp} -p %{SOURCE1} %{buildroot}%{_bindir}/%{name}

%{__mkdir_p} %{buildroot}%{_javadocdir}/%{name}-%{version}
%{__cp} -pr web/api/* %{buildroot}%{_javadocdir}/%{name}-%{version}
%{__ln_s} %{name}-%{version} %{buildroot}%{_javadocdir}/%{name}

%{__mkdir_p} %{buildroot}%{_datadir}/applications
%{_bindir}/desktop-file-install --vendor jpackage --dir %{buildroot}%{_datadir}/applications %{SOURCE5}
%{__install} -D -p -m 644 %{SOURCE2} %{buildroot}%{_datadir}/icons/hicolor/16x16/apps/%{name}.png
%{__install} -D -p -m 644 %{SOURCE3} %{buildroot}%{_datadir}/icons/hicolor/32x32/apps/%{name}.png
%{__install} -D -p -m 644 %{SOURCE4} %{buildroot}%{_datadir}/icons/hicolor/48x48/apps/%{name}.png
%{__install} -D -p -m 644 %{SOURCE4} %{buildroot}%{_datadir}/pixmaps/%{name}.png

%{__mkdir_p} %{buildroot}%{_datadir}/%{name}-%{version}
%{__cp} -pr bin %{buildroot}%{_datadir}/%{name}-%{version}
%{__ln_s} %{_javadir}/%{name} %{buildroot}%{_datadir}/%{name}-%{version}/lib
%{__cp} -pr plugin %{buildroot}%{_datadir}/%{name}-%{version}
%{__mkdir_p} %{buildroot}%{_datadir}/%{name}-%{version}/src/xsl
%{__cp} -p src/xsl/*.xsl %{buildroot}%{_datadir}/%{name}-%{version}/src/xsl
%{__ln_s} %{_docdir}/%{name}-%{version} %{buildroot}%{_datadir}/%{name}-%{version}/doc
%{__ln_s} %{name}-%{version} %{buildroot}%{_datadir}/%{name}

%{__mkdir_p} %{buildroot}%{_docdir}/%{name}-%{version}
%{__cp} -pr src/doc/* %{buildroot}%{_docdir}/%{name}-%{version}
%{__ln_s} %{_javadocdir}/%{name}-%{version} %{buildroot}%{_docdir}/%{name}-%{version}/api

mkdir -p $RPM_BUILD_ROOT`dirname /etc/%name.conf`
touch $RPM_BUILD_ROOT/etc/%name.conf
# fix to report
sed -i -e 's,Categories=Development;X-JPackage;,Categories=X-JPackage;Java;Development;Debugger;,' $RPM_BUILD_ROOT%_desktopdir/*.desktop

%files
%doc LICENSE.txt README.txt design
%attr(0755,root,root) %{_bindir}/findbugs
%dir %{_datadir}/%{name}-%{version}
%dir %{_datadir}/%{name}-%{version}/lib
%dir %{_datadir}/%{name}-%{version}/plugin
%doc %{_datadir}/%{name}-%{version}/plugin/README
%dir %{_datadir}/%{name}-%{version}/bin
%dir %{_datadir}/%{name}-%{version}/bin/deprecated
%dir %{_datadir}/%{name}-%{version}/bin/experimental
%attr(0755,root,root) %{_datadir}/%{name}-%{version}/bin/addMessages
%attr(0755,root,root) %{_datadir}/%{name}-%{version}/bin/computeBugHistory
%attr(0755,root,root) %{_datadir}/%{name}-%{version}/bin/convertXmlToText
%attr(0755,root,root) %{_datadir}/%{name}-%{version}/bin/copyBuggySource
%attr(0755,root,root) %{_datadir}/%{name}-%{version}/bin/defectDensity
%attr(0755,root,root) %{_datadir}/%{name}-%{version}/bin/deprecated/bugHistory
%attr(0755,root,root) %{_datadir}/%{name}-%{version}/bin/deprecated/unionBugs
%attr(0755,root,root) %{_datadir}/%{name}-%{version}/bin/deprecated/unionResults
%attr(0755,root,root) %{_datadir}/%{name}-%{version}/bin/deprecated/updateBugs
%attr(0755,root,root) %{_datadir}/%{name}-%{version}/bin/experimental/churn
%attr(0755,root,root) %{_datadir}/%{name}-%{version}/bin/experimental/treemapVisualization
%attr(0755,root,root) %{_datadir}/%{name}-%{version}/bin/fbwrap
%attr(0755,root,root) %{_datadir}/%{name}-%{version}/bin/filterBugs
%attr(0755,root,root) %{_datadir}/%{name}-%{version}/bin/findbugs
%attr(0755,root,root) %{_datadir}/%{name}-%{version}/bin/findbugs2
%attr(0755,root,root) %{_datadir}/%{name}-%{version}/bin/findbugs-dbStats
%attr(0755,root,root) %{_datadir}/%{name}-%{version}/bin/findbugs-msv
%attr(0755,root,root) %{_datadir}/%{name}-%{version}/bin/listBugDatabaseInfo
%attr(0755,root,root) %{_datadir}/%{name}-%{version}/bin/mineBugHistory
%attr(0755,root,root) %{_datadir}/%{name}-%{version}/bin/printAppVersion
%attr(0755,root,root) %{_datadir}/%{name}-%{version}/bin/printClass
%attr(0755,root,root) %{_datadir}/%{name}-%{version}/bin/rejarForAnalysis
%attr(0755,root,root) %{_datadir}/%{name}-%{version}/bin/setBugDatabaseInfo
%attr(0755,root,root) %{_datadir}/%{name}-%{version}/bin/unionBugs
%attr(0755,root,root) %{_datadir}/%{name}-%{version}/bin/xpathFind
%dir %{_datadir}/%{name}-%{version}/doc
%dir %{_datadir}/%{name}-%{version}/src
%dir %{_datadir}/%{name}-%{version}/src/xsl
%{_datadir}/%{name}-%{version}/src/xsl/default.xsl
%{_datadir}/%{name}-%{version}/src/xsl/fancy-hist.xsl
%{_datadir}/%{name}-%{version}/src/xsl/fancy.xsl
%{_datadir}/%{name}-%{version}/src/xsl/plain.xsl
%{_datadir}/%{name}-%{version}/src/xsl/summary.xsl
%dir %{_datadir}/%{name}
%{_iconsdir}/hicolor/16x16/apps/findbugs.png
%{_iconsdir}/hicolor/32x32/apps/findbugs.png
%{_iconsdir}/hicolor/48x48/apps/findbugs.png
%dir %{_javadir}/%{name}
%{_javadir}/%{name}/annotations-%{version}.jar
%{_javadir}/%{name}/annotations.jar
%{_javadir}/%{name}/ant.jar
%{_javadir}/%{name}/asm-analysis.jar
%{_javadir}/%{name}/asm-commons.jar
%{_javadir}/%{name}/asm-tree.jar
%{_javadir}/%{name}/asm-util.jar
%{_javadir}/%{name}/asm-xml.jar
%{_javadir}/%{name}/asm.jar
%{_javadir}/%{name}/bcel.jar
%{_javadir}/%{name}/commons-lang.jar
%{_javadir}/%{name}/dom4j.jar
%{_javadir}/%{name}/findbugs-%{version}.jar
%{_javadir}/%{name}/findbugs-ant-%{version}.jar
%{_javadir}/%{name}/findbugs-ant.jar
%{_javadir}/%{name}/findbugs.jar
%{_javadir}/%{name}/jFormatString.jar
%{_javadir}/%{name}/jaxen.jar
%{_javadir}/%{name}/jcip-annotations.jar
%{_javadir}/%{name}/jsr305.jar
%{_datadir}/maven2/poms/JPP.%{name}-annotations.pom
%{_datadir}/maven2/poms/JPP.%{name}-findbugs-ant.pom
%{_datadir}/maven2/poms/JPP.%{name}-findbugs.pom
%{_datadir}/maven2/poms/JPP.%{name}-jFormatString.pom
%{_datadir}/maven2/poms/JPP.%{name}-bcel.pom
%{_datadir}/maven2/poms/JPP.%{name}-jsr305.pom
%{_mavendepmapfragdir}/%{name}
%{_sysconfdir}/ant.d/%{name}
%{_datadir}/applications/*%{name}.desktop
%{_datadir}/pixmaps/%{name}.png
%config(noreplace,missingok) /etc/%name.conf
#unpackaged directory: 
%dir %_datadir/%name-%version/bin/deprecated
%dir %_datadir/%name-%version/bin/experimental

%files javadoc
%{_javadocdir}/%{name}-%{version}
%{_javadocdir}/%{name}

%files manual
%doc %{_docdir}/%{name}-%{version}

%changelog
* Fri Feb 10 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.3.9-alt1_5jpp6
- new release

* Wed Feb 08 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.3.9-alt1_2jpp6
- new version

* Mon Nov 17 2008 Igor Vlasenko <viy@altlinux.ru> 0:1.3.4-alt2_2jpp5
- removed obsolete update_menus

