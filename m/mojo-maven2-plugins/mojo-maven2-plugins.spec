BuildRequires: geronimo-jpa-3.0-api javacc3 sun-ws-metadata-2.0-api sun-annotation-1.0-api
BuildRequires: /proc
BuildRequires: jpackage-compat
# Copyright (c) 2000-2011, JPackage Project
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

%define gcj_support 0

%define repo_dir    m2_repo/repository

%define antlr_namedversion 2.2-SNAPSHOT
%define antlr_include 1
%define appassembler_namedversion 1.0-SNAPSHOT
%define appassembler_include 1
%define aspectj_namedversion 1.1-SNAPSHOT
%define aspectj_include 1
%define axistools_namedversion 1.2-SNAPSHOT
%define axistools_include 1
%define build_helper_namedversion 1.5
%define build_helper_include 1
%define buildnumber_namedversion 1.0-beta-2-SNAPSHOT
%define buildnumber_include 1
%define castor_namedversion 2.0-SNAPSHOT
%define castor_include 1
%define clirr_namedversion 2.3-SNAPSHOT
%define clirr_include 1
%define cobertura_namedversion 2.3-SNAPSHOT
%define cobertura_include 1
%define commons_attributes_namedversion 1.1-SNAPSHOT
%define commons_attributes_include 1
%define dbunit_namedversion 1.0-beta-2-SNAPSHOT
%define dbunit_include 1
%define docbook_namedversion 1.0.0-alpha-2-SNAPSHOT
%define docbook_include 1
%define exec_namedversion 1.1-beta-2-SNAPSHOT
%define exec_include 1
%define findbugs_namedversion 2.3.1
%define findbugs_include 1

#%%define groovy_namedversion 1.0-beta-3 SEE gmaven
%define groovy_include 0

%define hibernate2_namedversion 1.0-alpha-1-SNAPSHOT
%define hibernate2_include 1
%define hibernate3_namedversion 2.2-SNAPSHOT
%define hibernate3_include 0
%define idlj_namedversion 1.1-SNAPSHOT
%define idlj_include 1
%define jalopy_namedversion 1.0-alpha-2-SNAPSHOT
%define jalopy_include 1
%define jasperreports_namedversion 1.0-beta-2-SNAPSHOT
%define jasperreports_include 1
%define javacc_namedversion 2.5-SNAPSHOT
%define javacc_include 1
%define javancss_namedversion 2.0-beta-3-SNAPSHOT
%define javancss_include 1
%define jaxb2_namedversion 1.3-SNAPSHOT
%define jaxb2_include 1
%define jboss_namedversion 1.3.2-SNAPSHOT
%define jboss_include 1
%define jboss_packaging_namedversion 2.0-SNAPSHOT
%define jboss_packaging_include 1
%define jdepend_namedversion 2.0-SNAPSHOT
%define jdepend_include 1
%define jdiff_namedversion 0.1-SNAPSHOT
%define jdiff_include 1
%define jpox_namedversion 1.1.8-SNAPSHOT
%define jpox_include 1
%define jruby_namedversion 1.0-beta-5-SNAPSHOT
%define jruby_include 1
%define jruby_stdlib_namedversion 1.8.5
%define jruby_stdlib_include 1
%define jspc_namedversion 2.0-alpha-3
%define jspc_include 1
%define keytool_namedversion 1.1-beta-1-SNAPSHOT
%define keytool_include 1
%define l10n_namedversion 1.0-alpha-2-SNAPSHOT
%define l10n_include 1
%define wagon_cifs_namedversion 1.0-alpha-1-SNAPSHOT
%define wagon_cifs_include 0

#%%define mojo_archetypes_namedversion 1.0-SNAPSHOT
%define mojo_archetypes_include 0
#%%define mojo_archetypes_netbeans_namedversion 1.1-SNAPSHOT
%define mojo_archetypes_netbeans_include 0

%define native_namedversion 1.0-alpha-3-SNAPSHOT
%define native_include 1
%define minijar_namedversion 1.0-alpha-3
%define minijar_include 1

%define appbundler_namedversion 1.0-SNAPSHOT
%define appbundler_include 1
%define appfuse_namedversion 2.0.0-SNAPSHOT
%define appfuse_include 1
%define apt_namedversion 1.0-alpha-3-SNAPSHOT
%define apt_include 1
%define batik_namedversion 1.0-SNAPSHOT
%define batik_include 1
%define cis_namedversion 1.0-alpha-1-SNAPSHOT
%define cis_include 1
%define cruisecontrol_namedversion 1.0-SNAPSHOT
%define cruisecontrol_include 1
%define dashboard_namedversion 1.0-SNAPSHOT
%define dashboard_include 0
%define deb_namedversion 1.0-SNAPSHOT
%define deb_include 1
%define delicious_namedversion 1.0-alpha-1-SNAPSHOT
%define delicious_include 1
%define ejbdoclet_namedversion 1.0-beta-1-SNAPSHOT
%define ejbdoclet_include 1
%define emma_namedversion 1.0-SNAPSHOT
%define emma_include 1
%define fileutils_namedversion 1.0-SNAPSHOT
%define fileutils_include 1
%define fit_namedversion 2.0-beta-4-SNAPSHOT
%define fit_include 1
%define freemarker_namedversion 0.0.4-alpha-1-SNAPSHOT
%define freemarker_include 1
%define ganalytics_namedversion 1.0-SNAPSHOT
%define ganalytics_include 1
%define graphing_namedversion 0.1-SNAPSHOT
%define graphing_include 1
%define hibernatedoclet_namedversion 1.0-beta-1-SNAPSHOT
%define hibernatedoclet_include 1
%define ibatis_namedversion 1.0-alpha-1-SNAPSHOT
%define ibatis_include 0
%define j2me_namedversion 0.1.0-alpha-SNAPSHOT
%define j2me_include 1
%define jardiff_namedversion 1.0-SNAPSHOT
%define jardiff_include 1
%define jaxws_namedversion 1.0-beta-1-SNAPSHOT
%define jaxws_include 1
#
%define jellyapi_namedversion 2.0-SNAPSHOT
%define jellyapi_include 0
%define jellymojo_namedversion 1.0
%define jellymojo_include 0
#
%define jettybin_namedversion 0.1-SNAPSHOT
%define jettybin_include 1
%define jetty_namedversion 1.0.0-alpha-1-SNAPSHOT
%define jetty_include 1
#%%define legaltools_namedversion 1.0-alpha-1-SNAPSHOT
%define legaltools_include 0
%define mant_namedversion 1.0-beta-2-SNAPSHOT
%define mant_include 1
#%%define mojo_was5_plugin_namedversion 1.1.3
%define mojo_was5_plugin_include 0
%define mojo_was_plugin_anttasks_namedversion 1.1
%define mojo_was_plugin_anttasks_include 1
%define buildinfo_namedversion 1.0-SNAPSHOT
%define buildinfo_include 1
%define changes_namedversion 2.0-SNAPSHOT
%define changes_include 1
%define diagram_maker_namedversion 0.1-SNAPSHOT
%define diagram_maker_include 1
%define diagrams_namedversion 1.0-SNAPSHOT
%define diagrams_include 1
%define hsqldb_namedversion 1.0-SNAPSHOT
%define hsqldb_include 1
%define springbeandoc_namedversion 1.0.8-SNAPSHOT
%define springbeandoc_include 1
#%%define testing_simple_namedversion 1.0-SNAPSHOT
%define testing_simple_include 0
%define pomtools_namedversion 1.0-SNAPSHOT
%define pomtools_include 1
%define properties_namedversion 1.0-SNAPSHOT
%define properties_include 1
%define push_namedversion 1.0-alpha-1-SNAPSHOT
%define push_include 1
%define retroweaver_namedversion 1.0-SNAPSHOT
%define retroweaver_include 1
#%%define rspec_namedversion 1.0-SNAPSHOT
%define rspec_include 0
%define rubyscript_namedversion 1.0-beta-1-SNAPSHOT
%define rubyscript_include 0
%define runtime_builder_namedversion 0.1-SNAPSHOT
%define runtime_builder_include 1
%define script_namedversion 1.0-SNAPSHOT
%define script_include 1
%define shade_namedversion 1.0-alpha-11-SNAPSHOT
%define shade_include 1
%define shell_namedversion 1.0-SNAPSHOT
%define shell_include 1
%define springdoclet_namedversion 1.0-beta-1
%define springdoclet_include 1
%define visibroker_namedversion 1.0-alpha-1-SNAPSHOT
%define visibroker_include 1
%define wagon_namedversion 1.0-SNAPSHOT
%define wagon_include 1
%define webdoclet_namedversion 1.0-beta-1
%define webdoclet_include 1
%define xfire_namedversion 1.0-SNAPSHOT
%define xfire_include 0
%define xjc_namedversion 1.0-beta-2-SNAPSHOT
%define xjc_include 1
%define xsltc_namedversion 1.0-SNAPSHOT
%define xsltc_include 1

%define native2ascii_namedversion 1.0-alpha-2-SNAPSHOT
%define native2ascii_include 1
%define netbeans_freeform_namedversion 2.1-SNAPSHOT
%define netbeans_freeform_include 1
%define openjpa_namedversion 1.1-alpha-SNAPSHOT
%define openjpa_include 1
%define osxappbundle_namedversion 1.0-alpha-2-SNAPSHOT
%define osxappbundle_include 1
%define ounce_namedversion 1.1-SNAPSHOT
%define ounce_include 1
#%%define pde_namedversion 1.0-alpha-2-SNAPSHOT
%define pde_include 0
%define plugin_support_namedversion 1.0-alpha-2-SNAPSHOT
%define plugin_support_include 1
%define retrotranslator_namedversion 1.0-beta-1-SNAPSHOT
%define retrotranslator_include 1
%define rat_namedversion 1.0-alpha-4-SNAPSHOT
%define rat_include 1
%define rmic_namedversion 1.0-SNAPSHOT
%define rmic_include 1
%define rpm_namedversion 2.0-beta-2-SNAPSHOT
%define rpm_include 1
%define sablecc_namedversion 2.3-SNAPSHOT
%define sablecc_include 1
%define selenium_namedversion 1.0-beta-3-SNAPSHOT
%define selenium_include 1
%define shitty_namedversion 1.0-alpha-2-SNAPSHOT
%define shitty_include 1
%define smc_namedversion 1.0-alpha-2-SNAPSHOT
%define smc_include 1
%define solaris_namedversion 1.0-alpha-2-SNAPSHOT
%define solaris_include 1
%define sql_namedversion 1.1-SNAPSHOT
%define sql_include 1
%define sysdeo_tomcat_namedversion 1.1-SNAPSHOT
%define sysdeo_tomcat_include 1
%define taglist_namedversion 2.3-SNAPSHOT
%define taglist_include 1
%define tomcat_namedversion 1.0-alpha-2-SNAPSHOT
%define tomcat_include 1
%define pack200_anttasks_namedversion 1.2-SNAPSHOT
%define pack200_anttasks_include 1
%define webstart_namedversion 1.0-beta-1-SNAPSHOT
%define webstart_include 1
%define webstart_servlet_namedversion 1.0-6.0.02_ea_b02.1-SNAPSHOT
%define webstart_servlet_include 1
%define wsdl2java_namedversion 0.4-SNAPSHOT
%define wsdl2java_include 1
%define xdoclet_namedversion 1.0-beta-1-SNAPSHOT
%define xdoclet_include 0
%define xmlbeans_namedversion 2.3.2-SNAPSHOT
%define xmlbeans_include 1
%define xml_namedversion 1.0-beta-3-SNAPSHOT
%define xml_include 1
%define xslt_namedversion 1.1-SNAPSHOT
%define xslt_include 1
#
%define RHAT 0
%if %{RHAT}
# NEW %define appfuse_include 0
%define appfuse_include 0
%define aspectj_include 0
%define clirr_include 0
# NEW %define cobertura_include 0
%define cobertura_include 0
# NEW %define commons_attributes_include 0
%define commons_attributes_include 0
# NEW %define dashboard_include 0
%define dashboard_include 0
# NEW %define dbunit_include 0
%define dbunit_include 0
# NEW %define diagram_maker_include 0
%define diagram_maker_include 0
# NEW %define findbugs_include 0
%define findbugs_include 0
%define fit_include 0
%define graphing_include 0
%define hibernate2_include 0
# NEW %define hibernate3_include 0
%define hibernate3_include 0
%define ibatis_include 0
# NEW %define jalopy_include 0
%define jalopy_include 0
# NEW %define jardiff_include 0
%define jardiff_include 0
%define javancss_include 0
# NEW %define jaxb2_include 0
%define jaxb2_include 0
# NEW %define jaxws_include 0
%define jaxws_include 0
# NEW %define jdepend_include 0
%define jdepend_include 0
%define jetty_include 0
%define jpox_include 0
%define jruby_include 0
%define jruby_stdlib_include 0
# NEW %define jspc_include 0
%define jspc_include 0
%define minijar_include 0
%define openjpa_include 0
%define osxappbundle_include 0
%define rat_include 0
%define retrotranslator_include 0
%define sablecc_include 0
%define selenium_include 0
# NEW %define shitty_include 0
%define shitty_include 0
%define smc_include 0
%define springbeandoc_include 0
%define xfire_include 0
# NEW %define xjc_include 0
%define xjc_include 0
# NEW %define xmlbeans_include 0
%define xmlbeans_include 0
%endif

Name:           mojo-maven2-plugins
Version:        17
Release:        alt20_8jpp6
Epoch:          0
Summary:        Maven2 plugin set from mojo.codehaus.org
License:        ASL, MIT, GPL, LGPL
Group:          Development/Java
URL:            http://mojo.codehaus.org
Source0:    mojo-maven2-plugins-17.tar.gz
# svn export http://svn.codehaus.org/mojo/tags/mojo-17/ mojo-maven2-plugins-17
Source1:    mojo12-pom.xml
Source2:    %{name}-jpp-depmap.xml
Source3:    mojo-maven2-plugins-settings.xml
#Source4:    apache-jar-resource-bundle-1.3.jar
Source5:    minijar-maven-plugin-1.0-alpha-3.tar.gz
Source6:    mojo-maven2-plugins-sandbox-4.tar.gz
# svn export http://svn.codehaus.org/mojo/tags/mojo-sandbox-4/ mojo-maven2-plugins-sandbox-4
Source7:    wrapper-delta-pack-3.2.3.tar.gz
Source8:    cobertura-maven-plugin-bootstrap-pom.xml
Source9:    jspc-2.0-alpha-3.tgz
# svn export http://svn.codehaus.org/mojo/tags/jspc-2.0-alpha-3/
# tar czf jspc-2.0-alpha-3.tgz jspc-2.0-alpha-3/
Source10:   build-helper-maven-plugin-1.5.tgz
# svn export http://svn.codehaus.org/mojo/tags/build-helper-maven-plugin-1.5/
# tar czf build-helper-maven-plugin-1.5.tgz build-helper-maven-plugin-1.5/
Source11:   findbugs-maven-plugin-2.3.1.tgz
# svn export http://svn.codehaus.org/mojo/tags/findbugs-maven-plugin-2.3.1/
# tar czf findbugs-maven-plugin-2.3.1.tgz findbugs-maven-plugin-2.3.1/
Source12:   http://repo1.maven.org/maven2/org/codehaus/mojo/mojo-parent/23/mojo-parent-23.pom


Patch0:     mojo-maven2-plugins-16-AjcReportMojo.patch
Patch1:     mojo-maven2-plugins-16-docbook-pom_xml.patch
#Patch2:     mojo-maven2-plugins-17-FindbugsXdocSink.patch
Patch3:     mojo-maven2-plugins-17-jspc-pom.patch
Patch4:     mojo-maven2-plugins-16-minijar-temp-pom.patch
Patch5:     mojo-maven2-plugins-16-mojo-sandbox-batik-pom.patch
Patch6:     mojo-maven2-plugins-16-mojo-sandbox-deb-pom.patch
Patch7:     mojo-maven2-plugins-16-mojo-sandbox-diagrams-plugin-pom.patch
Patch8:     mojo-maven2-plugins-16-mojo-sandbox-diagram-connector-classes-pom.patch
Patch9:     mojo-maven2-plugins-16-mojo-sandbox-graph-api-pom.patch
Patch10:    mojo-maven2-plugins-17-shitty-maven-plugin-ScriptLogger.patch
Patch11:    mojo-maven2-plugins-17-mojo-sandbox-pom.patch
Patch12:    mojo-maven2-plugins-16-mojo-sandbox-push-pom.patch
Patch13:    mojo-maven2-plugins-16-mojo-sandbox-runtime-mdo.patch
Patch14:    mojo-maven2-plugins-16-mojo-sandbox-runtime-pom.patch
Patch15:    mojo-maven2-plugins-16-mojo-sandbox-runtime-RuntimeMojo.patch
Patch16:    mojo-maven2-plugins-16-mojo-sandbox-shade-pom.patch
Patch17:    mojo-maven2-plugins-17-pom.patch
Patch18:    mojo-maven2-plugins-17-retrotranslator-pom.patch
Patch19:    mojo-maven2-plugins-16-taglist-TagListReport.patch
Patch20:    mojo-maven2-plugins-16-taglist-ReportGenerator.patch
Patch21:    mojo-maven2-plugins-17-cobertura-CoberturaReportMojo.patch
Patch22:    mojo-maven2-plugins-javancss-NcssReportMojo.patch
Patch23:    mojo-maven2-plugins-jdepend-JDependMojo.patch
Patch24:    mojo-maven2-plugins-jdepend-ReportGenerator.patch
Patch25:    mojo-maven2-plugins-jdiff-JDiffMojo.patch
Patch26:    mojo-maven2-plugins-17-selenium-pom.patch
Patch27:    mojo-maven2-plugins-16-jspc-maven-plugin-pom.patch
Patch28:    mojo-maven2-plugins-17-shitty-pom.patch
Patch29:    mojo-maven2-plugins-hibernate2-pom.patch
Patch30:    mojo-maven2-plugins-hibernate3-jdk15-pom.patch
Patch31:    mojo-maven2-plugins-hibernate3-jdk15-JPAComponentConfiguration.patch
Patch32:    mojo-maven2-plugins-16-mojo-sandbox-emma-EmmaReportMojo.patch
Patch33:    mojo-maven2-plugins-16-mojo-sandbox-cis-pom.patch
Patch34:    mojo-maven2-plugins-buildinfo-plugin-mdo.patch
Patch35:    mojo-maven2-plugins-16-antlr-AntlrHtmlReport.patch
Patch36:    mojo-maven2-plugins-16-dbunit-pom.patch
Patch37:    mojo-maven2-plugins-17-pomtools-maven-plugin-mdo.patch
Patch38:    mojo-maven2-plugins-16-smc-SmcReportMojo.patch
Patch39:    mojo-maven2-plugins-16-mojo-sandbox-appfuse-pom.patch
Patch40:    mojo-maven2-plugins-16-mojo-sandbox-appfuse-JDBCConfigurationUtility.patch
Patch41:    mojo-maven2-plugins-16-mojo-sandbox-dashboard-pom.patch
Patch42:    mojo-maven2-plugins-16-mojo-sandbox-dashboard-DashBoardReportMojo.patch
Patch43:    mojo-maven2-plugins-16-mojo-sandbox-dashboard-DashBoardReportGenerator.patch
Patch44:    mojo-maven2-plugins-16-mojo-sandbox-dashboard-DashBoardHistoricReportGenerator.patch
Patch45:    mojo-maven2-plugins-17-mojo-sandbox-dashboard-AbstractDashBoardGenerator.patch
Patch46:    mojo-maven2-plugins-16-mojo-sandbox-dashboard-DashBoardMultiReportGenerator.patch
Patch47:    mojo-maven2-plugins-16-mojo-sandbox-JardiffReportMojo.patch
Patch48:    mojo-maven2-plugins-17-findbugs-FindBugsMojo.patch
Patch49:    mojo-maven2-plugins-17-findbugs-FindbugsViolationCheckMojo.patch
#Patch50:    mojo-maven2-plugins-16-mojo-sandbox-rubyscript-parent-pom.patch
#Patch51:    mojo-maven2-plugins-16-mojo-sandbox-archetype-rubyscript-pom.patch
Patch52:    mojo-maven2-plugins-16-mojo-sandbox-was-pom.patch
Patch53:    mojo-maven2-plugins-16-mojo-sandbox-visibroker-pom.patch
Patch54:    mojo-maven2-plugins-16-mojo-sandbox-xsltc-pom.patch
Patch55:    mojo-maven2-plugins-16-mojo-sandbox-diagram-connector-classes-DescriptionParserTest.patch
Patch56:    mojo-maven2-plugins-16-mojo-sandbox-diagram-connector-classes-ClassNodesRepositoryTest.patch
Patch57:    mojo-maven2-plugins-16-mojo-sandbox-fileutils-pom.patch
Patch58:    mojo-maven2-plugins-16-mojo-sandbox-ibatis-pom.patch
Patch59:    mojo-maven2-plugins-16-mojo-sandbox-jaxws-pom.patch
Patch60:    mojo-maven2-plugins-16-mojo-sandbox-jettybin-pom.patch
Patch61:    mojo-maven2-plugins-16-mojo-sandbox-jetty-pom.patch
Patch62:    mojo-maven2-plugins-16-mojo-sandbox-script-pom.patch
Patch63:    mojo-maven2-plugins-16-mojo-sandbox-diagrams-gui-pom.patch
Patch64:    mojo-maven2-plugins-16-mojo-sandbox-diagram-connector-api-pom.patch
Patch65:    mojo-maven2-plugins-16-mojo-sandbox-diagram-connector-dependencies-pom.patch
Patch66:    mojo-maven2-plugins-16-mojo-sandbox-diagram-connector-classes-PackageUtilsTest.patch
Patch67:    mojo-maven2-plugins-appassembler-booter-pom.patch
Patch68:    mojo-maven2-plugins-17-findbugs-pom.patch
Patch69:    mojo-maven2-plugins-17-l10n-pom.patch
Patch70:    mojo-maven2-plugins-17-was6-pom.patch
Patch71:    mojo-maven2-plugins-17-webstart-JarSignMojoConfig.patch
Patch72:    mojo-maven2-plugins-17-xml-pom.patch
Patch73:    mojo-maven2-plugins-17-xml-java5-TransformMojo.patch
Patch74:    mojo-maven2-plugins-17-mojo-sandbox-batik-RasterizeMojo.patch
Patch75:    mojo-maven2-plugins-16-mojo-sandbox-dashboard-DashBoardMaven1ReportGenerator.patch
Patch76:    mojo-maven2-plugins-17-buildnumber-BuildMojo.patch
Patch77:    mojo-maven2-plugins-17-ounce-ReportMojo.patch
Patch78:    mojo-maven2-plugins-17-rat-pom.patch
Patch79:    mojo-maven2-plugins-17-rat-RatReportMojo.patch
Patch80:    mojo-maven2-plugins-17-mojo-sandbox-shade-DefaultShader.patch
Patch81:    mojo-maven2-plugins-hibernate3-pom.patch
Patch82:    mojo-maven2-plugins-NcssExecuter.patch
Patch83:    mojo-maven2-plugins-JarUnsignMojo.patch
Patch84:    mojo-maven2-plugins-TimeChartRenderer.patch
Patch85:    mojo-maven2-plugins-DashBoardUtils.patch
Patch86:    mojo-maven2-plugins-delicious-pom.patch
Patch87:    mojo-maven2-plugins-17-xfire-pom.patch
Patch88:    mojo-maven2-plugins-17-antlr-pom.patch
Patch89:    mojo-maven2-plugins-17-appassembler-model-pom.patch
Patch90:    mojo-maven2-plugins-17-pde-maven-plugin-pom.patch
Patch91:    mojo-maven2-plugins-17-netbeans-freeform-maven-plugin-pom.patch
Patch92:    mojo-maven2-plugins-17-nbm-maven-plugin-pom.patch
Patch93:    mojo-maven2-plugins-17-maven-buildinfo-plugin-pom.patch
Patch94:    mojo-maven2-plugins-17-pomtools-maven-plugin-pom.patch
Patch95:    mojo-maven2-plugins-17-wagon-cifs-CifsWagon.patch


Patch101:   mojo-maven2-plugins-17-RHAT-pom.patch
Patch102:   mojo-maven2-plugins-17-RHAT-sandbox-pom.patch
Patch103:   mojo-maven2-plugins-17-RHAT-native-pom.patch
Patch104:   mojo-maven2-plugins-17-RHAT-ounce-pom.patch
Patch105:   mojo-maven2-plugins-17-RHAT-sandbox-xsltc-pom.patch


%if %{gcj_support}
BuildRequires:    gnu-crypto
BuildRequires:          java-gcj-compat-devel
Requires(post):         java-gcj-compat
Requires(postun):       java-gcj-compat
%endif
%if ! %{gcj_support}
BuildArch:      noarch
%endif

%if %{RHAT}
BuildRequires:  jpackage-utils
%else
BuildRequires:  jpackage-utils >= 0:1.7.5
%endif
BuildRequires:    maven2 >= 0:2.0.8
BuildRequires:    maven2-plugin-antrun
BuildRequires:    maven2-plugin-assembly
BuildRequires:    maven2-plugin-clean
BuildRequires:    maven2-plugin-compiler
BuildRequires:    maven2-plugin-dependency
BuildRequires:    maven2-plugin-deploy
BuildRequires:    maven2-plugin-docck
BuildRequires:    maven2-plugin-eclipse
BuildRequires:    maven2-plugin-enforcer
BuildRequires:    maven2-plugin-idea
BuildRequires:    maven2-plugin-install
BuildRequires:    maven2-plugin-invoker
BuildRequires:    maven2-plugin-jar
BuildRequires:    maven2-plugin-javadoc
BuildRequires:    maven2-plugin-one
BuildRequires:    maven2-plugin-plugin
BuildRequires:    maven2-plugin-remote-resources
BuildRequires:    maven2-plugin-resources
BuildRequires:    maven2-plugin-site
BuildRequires:    maven2-plugin-war
BuildRequires:    maven-doxia
BuildRequires:    maven-embedder
BuildRequires:    maven-jxr
BuildRequires:    maven-plugin-tools
BuildRequires:    maven-release
BuildRequires:    maven-scm
BuildRequires:    maven-shared-archiver
BuildRequires:    maven-shared-dependency-tree
BuildRequires:    maven-shared-downloader
%if ! %{RHAT}
BuildRequires:    maven-shared-enforcer-rule-api
%endif
BuildRequires:    maven-shared-file-management
BuildRequires:    maven-shared-osgi
BuildRequires:    maven-shared-plugin-tools-api
BuildRequires:    maven-shared-plugin-tools-java
BuildRequires:    maven-shared-plugin-testing-harness
BuildRequires:    maven-shared-plugin-testing-tools
BuildRequires:    maven-shared-reporting-impl
BuildRequires:    maven-surefire-plugin
%if ! %{RHAT}
BuildRequires:    maven-surefire-report-plugin
%endif
BuildRequires:    maven-wagon
BuildRequires:    apache-jar-resource-bundle
BuildRequires:    easymock
BuildRequires:    plexus-maven-plugin
BuildRequires:    modello
BuildRequires:    modello-maven-plugin
BuildRequires:    geronimo-genesis
BuildRequires:    geronimo-jta-1.0.1B-api

Requires:       jpackage-utils >= 0:1.7.5
Obsoletes:      mojo-maven2-plugin-changes < 0:16
Obsoletes:      mojo-maven2-plugin-dependency < 0:16
Obsoletes:      mojo-maven2-plugin-jxr < 0:16
Obsoletes:      mojo-maven2-archetypeng < 0:17-2
Source44: import.info
Patch50: mojo-maven2-plugins-17-alt-maven-wagon-a7-support.patch

%description
The Mojo project allows a bunch of people not necessarily 
involved with the Maven project to come along and build 
some plugins. 
Maven plugins may also be developed here because they are 
not compatible with the Apache license. Plugin authors may 
choose to use other licenses (BSD, GPL, MPL ...) to license 
their work or may be forced to because of the nature of the 
plugin and its dependencies. These plugin authors are 
responsible for working with their plugins license but the 
mailing lists are a great place to get help if people get 
confused on what can or can not be done within the mojo project. 


%if %{antlr_include}
%package -n mojo-maven2-plugin-antlr
Summary:     Antlr plugin from %{name}
Group:       Development/Java
Requires:    %{name} = 0:%{version}-%{release}
BuildRequires:    maven2 >= 0:2.0.8
BuildRequires:    maven-shared-plugin-testing-harness
BuildRequires:    maven-shared-reporting-impl
BuildRequires:    maven-wagon
BuildRequires:    modello-maven-plugin
BuildRequires:    antlr
BuildRequires:    plexus-i18n
BuildRequires:    plexus-utils
Requires:    maven2 >= 0:2.0.8
Requires:    maven-shared-reporting-impl
Requires:    maven-wagon
Requires:    antlr
Requires:    plexus-i18n
Requires:    plexus-utils
Provides: maven2-plugin-antlr = 2.0.4

%description -n mojo-maven2-plugin-antlr
%{summary}.
%endif

%if %{appassembler_include}
%package -n mojo-maven2-plugin-appassembler
Summary:     App assembler plugin and support from %{name}
Group:       Development/Java
Requires:    %{name} = 0:%{version}-%{release}
BuildRequires:    maven2 >= 0:2.0.8
BuildRequires:    maven-wagon
BuildRequires:    plexus-container-default
BuildRequires:    plexus-maven-plugin
BuildRequires:    plexus-utils
Requires:    maven2 >= 0:2.0.8
Requires:    maven-wagon
Requires:    plexus-container-default
Requires:    plexus-utils

%description -n mojo-maven2-plugin-appassembler
%{summary}.
%endif

%if %{appbundler_include}
%package -n mojo-maven2-plugin-appbundler
Summary:     App bundler plugin from %{name}
Group:       Development/Java
Requires:    %{name} = 0:%{version}-%{release}
BuildRequires:    maven2 >= 0:2.0.8
BuildRequires:    maven-shared-archiver
BuildRequires:    plexus-archiver
BuildRequires:    plexus-velocity
Requires:    maven2 >= 0:2.0.8
Requires:    maven-shared-archiver
Requires:    plexus-archiver
Requires:    plexus-velocity

%description -n mojo-maven2-plugin-appbundler
%{summary}.
%endif

%if %{appfuse_include}
%package -n mojo-maven2-plugin-appfuse
Summary:     App fuse plugin from %{name}
Group:       Development/Java
Requires:    %{name} = 0:%{version}-%{release}
BuildRequires:    maven2 >= 0:2.0.8
BuildRequires:    ant
BuildRequires:    jakarta-commons-logging
BuildRequires:    hibernate3
BuildRequires:    hibernate3-tools
BuildRequires:    mysql-connector-java
Requires:    maven2 >= 0:2.0.8
Requires:    ant
Requires:    jakarta-commons-logging
Requires:    hibernate3
Requires:    hibernate3-tools

%description -n mojo-maven2-plugin-appfuse
%{summary}.
%endif

%if %{apt_include}
%package -n mojo-maven2-plugin-apt
Summary:     Apt plugin from %{name}
Group:       Development/Java
Requires:    %{name} = 0:%{version}-%{release}
BuildRequires:    maven2 >= 0:2.0.8
BuildRequires:    plexus-compiler
Requires:    maven2 >= 0:2.0.8
Requires:    plexus-compiler

%description -n mojo-maven2-plugin-apt
%{summary}.
%endif

%if %{aspectj_include}
%package -n mojo-maven2-plugin-aspectj
Summary:     Aspectj plugin from %{name}
Group:       Development/Java
Requires:    %{name} = 0:%{version}-%{release}
BuildRequires:    maven2 >= 0:2.0.8
BuildRequires:    maven-embedder
BuildRequires:    maven-shared-reporting-impl
BuildRequires:    maven-surefire-plugin
BuildRequires:    aspectj >= 0:1.5.3
BuildRequires:    junit
Requires:    maven2 >= 0:2.0.8
Requires:    maven-embedder
Requires:    maven-shared-reporting-impl
Requires:    aspectj >= 0:1.5.3

%description -n mojo-maven2-plugin-aspectj
%{summary}.
%endif

%if %{axistools_include}
%package -n mojo-maven2-plugin-axistools
Summary:     Axistools plugin from %{name}
Group:       Development/Java
Requires:    %{name} = 0:%{version}-%{release}
BuildRequires:    maven2 >= 0:2.0.8
BuildRequires:    axis >= 0:1.4
BuildRequires:    jakarta-commons-discovery
BuildRequires:    jakarta-commons-logging
BuildRequires:    plexus-compiler
BuildRequires:    plexus-utils
BuildRequires:    wsdl4j
Requires:    maven2 >= 0:2.0.8
Requires:    axis >= 0:1.4
Requires:    jakarta-commons-discovery
Requires:    jakarta-commons-logging
Requires:    plexus-compiler
Requires:    plexus-utils
Requires:    wsdl4j

%description -n mojo-maven2-plugin-axistools
%{summary}.
%endif

%if %{batik_include}
%package -n mojo-maven2-plugin-batik
Summary:     Batik plugin from %{name}
Group:       Development/Java
Requires:    %{name} = 0:%{version}-%{release}
BuildRequires:    maven2 >= 0:2.0.8
BuildRequires:    xmlgraphics-batik
BuildRequires:    xmlgraphics-batik-rasterizer
BuildRequires:    plexus-utils
Requires:    maven2 >= 0:2.0.8
Requires:    xmlgraphics-batik
Requires:    xmlgraphics-batik-rasterizer
Requires:    plexus-utils

%description -n mojo-maven2-plugin-batik
%{summary}.
%endif

%if %{build_helper_include}
%package -n mojo-maven2-plugin-build-helper
Summary:     Build Helper plugin from %{name}
Group:       Development/Java
Requires:    %{name} = 0:%{version}-%{release}
BuildRequires:    maven2 >= 0:2.0.8
BuildRequires:    plexus-containers-component-javadoc
BuildRequires:    plexus-utils
Requires:    maven2 >= 0:2.0.8
Requires:    plexus-containers-component-javadoc
Requires:    plexus-utils

%description -n mojo-maven2-plugin-build-helper
%{summary}.
%endif

%if %{buildinfo_include}
%package -n mojo-maven2-plugin-buildinfo
Summary:     Buildinfo plugin from %{name}
Group:       Development/Java
Requires:    %{name} = 0:%{version}-%{release}
BuildRequires:    maven2 >= 0:2.0.8
BuildRequires:    maven-shared-plugin-tools-ant
BuildRequires:    modello-maven-plugin
BuildRequires:    ant >= 0:1.7.1
BuildRequires:    plexus-utils
Requires:    maven2 >= 0:2.0.8
Requires:    ant >= 0:1.7.1
Requires:    plexus-utils

%description -n mojo-maven2-plugin-buildinfo
%{summary}.
%endif

%if %{buildnumber_include}
%package -n mojo-maven2-plugin-buildnumber
Summary:     Buildnumber plugin from %{name}
Group:       Development/Java
Requires:    %{name} = 0:%{version}-%{release}
BuildRequires:    maven2 >= 0:2.0.8
BuildRequires:    maven-release
BuildRequires:    maven-scm
BuildRequires:    maven-shared-archiver
BuildRequires:    maven-surefire-plugin
Requires:    maven2 >= 0:2.0.8
Requires:    maven-shared-archiver
Requires:    maven-scm

%description -n mojo-maven2-plugin-buildnumber
%{summary}.
%endif

%if %{castor_include}
%package -n mojo-maven2-plugin-castor
Summary:     Castor plugin from %{name}
Group:       Development/Java
Requires:    %{name} = 0:%{version}-%{release}
BuildRequires:    maven2 >= 0:2.0.8
BuildRequires:    maven-shared-plugin-testing-harness
BuildRequires:    castor
BuildRequires:    jakarta-commons-io
BuildRequires:    jakarta-commons-logging
BuildRequires:    plexus-compiler
BuildRequires:    plexus-utils
BuildRequires:    velocity
Requires:    maven2 >= 0:2.0.8
Requires:    castor
Requires:    jakarta-commons-io
Requires:    jakarta-commons-logging
Requires:    plexus-compiler
Requires:    plexus-utils
Requires:    velocity

%description -n mojo-maven2-plugin-castor
%{summary}.
%endif

%if %{changes_include}
%package -n mojo-maven2-changes
Summary:     Changes support from %{name}
Group:       Development/Java
Requires:    %{name} = 0:%{version}-%{release}
BuildRequires:    maven2 >= 0:2.0.8
BuildRequires:    plexus-utils
Requires:    maven2 >= 0:2.0.8
Requires:    plexus-utils

%description -n mojo-maven2-changes
%{summary}.
%endif

%if %{cis_include}
%package -n mojo-maven2-plugin-cis
Summary:     CIS plugin from %{name}
Group:       Development/Java
Requires:    %{name} = 0:%{version}-%{release}
BuildRequires:    maven2 >= 0:2.0.8
BuildRequires:    maven2-plugin-war
BuildRequires:    maven-shared-dependency-tree
Requires:    maven2 >= 0:2.0.8
Requires:    maven2-plugin-war
Requires:    maven-shared-dependency-tree

%description -n mojo-maven2-plugin-cis
%{summary}.
%endif

%if %{clirr_include}
%package -n mojo-maven2-plugin-clirr
Summary:     Clirr plugin from %{name}
Group:       Development/Java
Requires:    %{name} = 0:%{version}-%{release}
BuildRequires:    maven2 >= 0:2.0.8
BuildRequires:    maven-shared-reporting-impl
BuildRequires:    clirr
BuildRequires:    maven-doxia
BuildRequires:    plexus-i18n
Requires:    maven2 >= 0:2.0.8
Requires:    maven-shared-reporting-impl
Requires:    clirr
Requires:    maven-doxia
Requires:    plexus-i18n

%description -n mojo-maven2-plugin-clirr
%{summary}.
%endif

%if %{cobertura_include}
%package -n mojo-maven2-plugin-cobertura
Summary:     Cobertura plugin from %{name}
Group:       Development/Java
Requires:    %{name} = 0:%{version}-%{release}
BuildRequires:    maven2 >= 0:2.0.8
BuildRequires:    maven-shared-plugin-testing-harness
BuildRequires:    maven-shared-reporting-impl
BuildRequires:    cobertura >= 0:1.9
BuildRequires:    gnu-getopt
BuildRequires:    httpunit
BuildRequires:    junit
BuildRequires:    plexus-container-default
BuildRequires:    plexus-utils
Requires:    maven2 >= 0:2.0.8
Requires:    maven-shared-reporting-impl
Requires:    cobertura >= 0:1.9
Requires:    gnu-getopt
Requires:    plexus-container-default
Requires:    plexus-utils

%description -n mojo-maven2-plugin-cobertura
%{summary}.
%endif

%if %{commons_attributes_include}
%package -n mojo-maven2-plugin-commons-attributes
Summary:     Commons Attributes plugin from %{name}
Group:       Development/Java
Requires:    %{name} = 0:%{version}-%{release}
BuildRequires:    maven2 >= 0:2.0.8
BuildRequires:    ant
BuildRequires:    jakarta-commons-attributes
BuildRequires:    jakarta-commons-collections
BuildRequires:    plexus-container-default
BuildRequires:    plexus-utils
#BuildRequires:    qdox15
BuildRequires:    qdox
BuildRequires:    xjavadoc
Requires:    maven2 >= 0:2.0.8
Requires:    ant
Requires:    jakarta-commons-attributes
Requires:    jakarta-commons-collections
Requires:    plexus-container-default
Requires:    plexus-utils
#Requires:    qdox15
Requires:    qdox
Requires:    xjavadoc

%description -n mojo-maven2-plugin-commons-attributes
%{summary}.
%endif

%if %{cruisecontrol_include}
%package -n mojo-maven2-plugin-cruisecontrol
Summary:     Cruisecontrol plugin from %{name}
Group:       Development/Java
Requires:    %{name} = 0:%{version}-%{release}
BuildRequires:    maven2 >= 0:2.0.8
BuildRequires:    junit
BuildRequires:    plexus-compiler
Requires:    maven2 >= 0:2.0.8
Requires:    plexus-compiler

%description -n mojo-maven2-plugin-cruisecontrol
%{summary}.
%endif

%if %{dashboard_include}
%package -n mojo-maven2-plugin-dashboard
Summary:     Dashboard plugin from %{name}
Group:       Development/Java
Requires:    %{name} = 0:%{version}-%{release}
BuildRequires:    maven2 >= 0:2.0.8
BuildRequires:    maven-surefire-plugin
BuildRequires:    maven-surefire-report-plugin
BuildRequires:    maven-shared-reporting-impl
BuildRequires:    plexus-maven-plugin
BuildRequires:    cobertura
BuildRequires:    hibernate3
BuildRequires:    jcommon
BuildRequires:    jfreechart
BuildRequires:    jta_1_0_1B_api
BuildRequires:    log4j
BuildRequires:    plexus-resources
BuildRequires:    plexus-utils
BuildRequires:    xalan-j2
BuildRequires:    xerces-j2
BuildRequires:    xstream
Requires:    maven2 >= 0:2.0.8
Requires:    maven-surefire-report-plugin
Requires:    maven-shared-reporting-impl
Requires:    mojo-maven2-plugin-jdepend
Requires:    cobertura
Requires:    hibernate3
Requires:    jcommon
Requires:    jfreechart
Requires:    jta_1_0_1B_api
Requires:    log4j
Requires:    plexus-resources
Requires:    plexus-utils
Requires:    xalan-j2
Requires:    xerces-j2
Requires:    xstream

%description -n mojo-maven2-plugin-dashboard
%{summary}.
%endif

%if %{dbunit_include}
%package -n mojo-maven2-plugin-dbunit
Summary:     DbUnit plugin from %{name}
Group:       Development/Java
Requires:    %{name} = 0:%{version}-%{release}
BuildRequires:    maven2 >= 0:2.0.8
BuildRequires:    ant >= 0:1.7.1
BuildRequires:    dbunit >= 0:2.2
BuildRequires:    hsqldb
BuildRequires:    junit
Requires:    maven2 >= 0:2.0.8
Requires:    ant >= 0:1.7.1
Requires:    dbunit >= 0:2.2

%description -n mojo-maven2-plugin-dbunit
%{summary}.
%endif

%if %{deb_include}
%package -n mojo-maven2-plugin-deb
Summary:     DEB plugin from %{name}
Group:       Development/Java
Requires:    %{name} = 0:%{version}-%{release}
BuildRequires:    maven2 >= 0:2.0.8
BuildRequires:    maven-embedder
Requires:    maven2 >= 0:2.0.8

%description -n mojo-maven2-plugin-deb
%{summary}.
%endif

%if %{delicious_include}
%package -n mojo-maven2-plugin-delicious
Summary:     Delicious plugin from %{name}
Group:       Development/Java
Requires:    %{name} = 0:%{version}-%{release}
BuildRequires:    maven2 >= 0:2.0.8
BuildRequires:    jakarta-commons-codec
BuildRequires:    jakarta-commons-httpclient
BuildRequires:    jakarta-commons-logging
BuildRequires:    junit
Requires:    maven2 >= 0:2.0.8
Requires:    jakarta-commons-codec
Requires:    jakarta-commons-httpclient
Requires:    jakarta-commons-logging

%description -n mojo-maven2-plugin-delicious
%{summary}.
%endif

%if %{diagram_maker_include}
%package -n mojo-maven2-diagram-maker
Summary:     Diagram Maker plugin and support from %{name}
Group:       Development/Java
Requires:    %{name} = 0:%{version}-%{release}
BuildRequires:    maven2 >= 0:2.0.8
BuildRequires:    maven-shared-dependency-tree
BuildRequires:    junit
BuildRequires:    objectweb-asm
BuildRequires:    plexus-classworlds
BuildRequires:    plexus-containers-component-api
BuildRequires:    plexus-containers-container-default
BuildRequires:    plexus-container-default
BuildRequires:    plexus-utils
BuildRequires:    xpp3
BuildRequires:    xstream
Requires:    maven2 >= 0:2.0.8
Requires:    maven-shared-dependency-tree
Requires:    objectweb-asm
Requires:    plexus-containers-component-api
Requires:    plexus-containers-container-default
Requires:    plexus-container-default
Requires:    plexus-utils
Requires:    xstream

%description -n mojo-maven2-diagram-maker
%{summary}.
%endif

%if %{docbook_include}
%package -n mojo-maven2-plugin-docbook
Summary:     DocBook plugin from %{name}
Group:       Development/Java
Requires:    %{name} = 0:%{version}-%{release}
BuildRequires:    maven2 >= 0:2.0.8
BuildRequires:    docbook-xsl-java-xalan
BuildRequires:    jakarta-commons-logging
BuildRequires:    junit
BuildRequires:    plexus-compiler
BuildRequires:    plexus-utils
BuildRequires:    xalan-j2
BuildRequires:    xerces-j2
BuildRequires:    xml-commons-resolver12
BuildRequires:    xmlgraphics-fop
Requires:    maven2 >= 0:2.0.8
Requires:    docbook-xsl-java-xalan
Requires:    jakarta-commons-logging
Requires:    plexus-compiler
Requires:    plexus-utils
Requires:    xalan-j2
Requires:    xerces-j2
Requires:    xml-commons-resolver12
Requires:    xmlgraphics-fop

%description -n mojo-maven2-plugin-docbook
%{summary}.
%endif

%if %{ejbdoclet_include}
%package -n mojo-maven2-plugin-ejbdoclet
Summary:     EJB doclet plugin from %{name}
Group:       Development/Java
Requires:    %{name} = 0:%{version}-%{release}
BuildRequires:    maven2 >= 0:2.0.8
#BuildRequires:    mojo-maven2-plugin-mant
BuildRequires:    jakarta-commons-collections
BuildRequires:    jakarta-commons-logging
BuildRequires:    jboss4-j2ee
BuildRequires:    junit
BuildRequires:    servlet_2_3_api
BuildRequires:    xdoclet
BuildRequires:    xjavadoc
Requires:    maven2 >= 0:2.0.8
Requires:    mojo-maven2-plugin-mant
Requires:    jakarta-commons-collections
Requires:    jakarta-commons-logging
Requires:    jboss4-j2ee
Requires:    servlet_2_3_api
Requires:    xdoclet
Requires:    xjavadoc

%description -n mojo-maven2-plugin-ejbdoclet
%{summary}.
%endif

%if %{emma_include}
%package -n mojo-maven2-plugin-emma
Summary:     Emma plugin from %{name}
Group:       Development/Java
Requires:    %{name} = 0:%{version}-%{release}
BuildRequires:    maven2 >= 0:2.0.8
BuildRequires:    emma
Requires:    maven2 >= 0:2.0.8
Requires:    emma

%description -n mojo-maven2-plugin-emma
%{summary}.
%endif

%if %{exec_include}
%package -n mojo-maven2-plugin-exec
Summary:     Exec plugin from %{name}
Group:       Development/Java
Requires:    %{name} = 0:%{version}-%{release}
BuildRequires:    maven2 >= 0:2.0.8
BuildRequires:    maven-shared-plugin-testing-harness
BuildRequires:    plexus-container-default
BuildRequires:    plexus-utils
Requires:    maven2 >= 0:2.0.8
Requires:    plexus-container-default
Requires:    plexus-utils

%description -n mojo-maven2-plugin-exec
%{summary}.
%endif

%if %{fileutils_include}
%package -n mojo-maven2-plugin-fileutils
Summary:     Fileutils plugin from %{name}
Group:       Development/Java
Requires:    %{name} = 0:%{version}-%{release}
BuildRequires:    maven2 >= 0:2.0.8
BuildRequires:    maven-shared-plugin-testing-harness
BuildRequires:    plexus-utils
Requires:    maven2 >= 0:2.0.8
Requires:    plexus-utils

%description -n mojo-maven2-plugin-fileutils
%{summary}.
%endif

%if %{findbugs_include}
%package -n mojo-maven2-plugin-findbugs
Summary:     Findbugs plugin from %{name}
Group:       Development/Java
Requires:    %{name} = 0:%{version}-%{release}
BuildRequires:    dom4j
BuildRequires:    jgoodies-looks
BuildRequires:    gmaven
BuildRequires:    gmaven-runtime-1.6
BuildRequires:    groovy16
BuildRequires:    maven2 >= 0:2.0.8
BuildRequires:    maven-shared-reporting-impl
BuildRequires:    maven-doxia
BuildRequires:    findbugs
Requires:    maven2 >= 0:2.0.8
Requires:    maven-shared-reporting-impl
Requires:    maven-doxia
Requires:    findbugs
Requires:    jgoodies-looks
Requires: mojo-parent

%description -n mojo-maven2-plugin-findbugs
%{summary}.
%endif

%if %{fit_include}
%package -n mojo-maven2-plugin-fit
Summary:     FIT plugin from %{name}
Group:       Development/Java
Requires:    %{name} = 0:%{version}-%{release}
BuildRequires:    maven2 >= 0:2.0.8
BuildRequires:    ant
BuildRequires:    fit >= 0:1.1
BuildRequires:    junit
Requires:    maven2 >= 0:2.0.8
Requires:    ant
Requires:    fit >= 0:1.1

%description -n mojo-maven2-plugin-fit
%{summary}.
%endif

%if %{freemarker_include}
%package -n mojo-maven2-plugin-freemarker
Summary:     Freemarker plugin from %{name}
Group:       Development/Java
Requires:    %{name} = 0:%{version}-%{release}
BuildRequires:    maven2 >= 0:2.0.8
BuildRequires:    maven2-plugin-docck
BuildRequires:    maven-shared-plugin-testing-harness
BuildRequires:    dom4j
BuildRequires:    freemarker >= 0:2.3.6
BuildRequires:    junit
BuildRequires:    plexus-utils
Requires:    maven2 >= 0:2.0.8
Requires:    dom4j
Requires:    freemarker >= 0:2.3.6
Requires:    plexus-utils

%description -n mojo-maven2-plugin-freemarker
%{summary}.
%endif

%if %{ganalytics_include}
%package -n mojo-maven2-plugin-ganalytics
Summary:     Ganalytics plugin from %{name}
Group:       Development/Java
Requires:    %{name} = 0:%{version}-%{release}
BuildRequires:    maven2 >= 0:2.0.8
BuildRequires:    plexus-utils
Requires:    maven2 >= 0:2.0.8
Requires:    plexus-utils

%description -n mojo-maven2-plugin-ganalytics
%{summary}.
%endif

%if %{graphing_include}
%package -n mojo-maven2-plugin-graphing
Summary:     Graphing plugin from %{name}
Group:       Development/Java
Requires:    %{name} = 0:%{version}-%{release}
BuildRequires:    jakarta-commons-lang
BuildRequires:    jung
BuildRequires:    junit
BuildRequires:    maven2 >= 0:2.0.8
BuildRequires:    maven-shared-reporting-impl
BuildRequires:    plexus-utils
Requires:    jakarta-commons-lang
Requires:    jung
Requires:    maven2 >= 0:2.0.8
Requires:    maven-shared-reporting-impl
Requires:    plexus-utils

%description -n mojo-maven2-plugin-graphing
%{summary}.
%endif

%if %{hibernate2_include}
%package -n mojo-maven2-plugin-hibernate2
Summary:     Hibernate2 plugin from %{name}
Group:       Development/Java
Requires:    %{name} = 0:%{version}-%{release}
BuildRequires:    maven2 >= 0:2.0.8
BuildRequires:    dom4j
BuildRequires:    hibernate2
BuildRequires:    hibernate2-tools
Requires:    maven2 >= 0:2.0.8
Requires:    dom4j
Requires:    hibernate2
Requires:    hibernate2-tools

%description -n mojo-maven2-plugin-hibernate2
%{summary}.
%endif

%if %{hibernate3_include}
%package -n mojo-maven2-hibernate3
Summary:     Hibernate3 plugin and support from %{name}
Group:       Development/Java
Requires:    %{name} = 0:%{version}-%{release}
BuildRequires:    maven2 >= 0:2.0.8
BuildRequires:    maven-shared-plugin-testing-harness
BuildRequires:    maven-shared-reporting-impl
BuildRequires:    hibernate3-annotations
BuildRequires:    hibernate3-entitymanager
BuildRequires:    hibernate3-tools
BuildRequires:    hsqldb
BuildRequires:    javassist
BuildRequires:    jboss4-common
BuildRequires:    jpa_1_0B_api
BuildRequires:    jta_1_0_1B_api
BuildRequires:    log4j
BuildRequires:    plexus-utils
Requires:    maven2 >= 0:2.0.8
Requires:    hibernate3-annotations
Requires:    hibernate3-entitymanager
Requires:    hibernate3-tools
Requires:    javassist
Requires:    jboss4-common
Requires:    jpa_1_0B_api
Requires:    jta_1_0_1B_api
Requires:    log4j
Requires:    plexus-utils

%description -n mojo-maven2-hibernate3
%{summary}.
%endif

%if %{hibernatedoclet_include}
%package -n mojo-maven2-plugin-hibernatedoclet
Summary:     Hibernate doclet plugin from %{name}
Group:       Development/Java
Requires:    %{name} = 0:%{version}-%{release}
BuildRequires:    maven2 >= 0:2.0.8
#BuildRequires:    mojo-maven2-plugin-mant
BuildRequires:    jakarta-commons-collections
BuildRequires:    jakarta-commons-logging
BuildRequires:    jboss4-j2ee
BuildRequires:    junit
BuildRequires:    servlet_2_3_api
BuildRequires:    xdoclet
BuildRequires:    xjavadoc
Requires:    maven2 >= 0:2.0.8
Requires:    mojo-maven2-plugin-mant
Requires:    jakarta-commons-collections
Requires:    jakarta-commons-logging
Requires:    jboss4-j2ee
Requires:    servlet_2_3_api
Requires:    xdoclet
Requires:    xjavadoc

%description -n mojo-maven2-plugin-hibernatedoclet
%{summary}.
%endif

%if %{hsqldb_include}
%package -n mojo-maven2-plugin-hsqldb
Summary:     Hsqldb doclet plugin from %{name}
Group:       Development/Java
Requires:    %{name} = 0:%{version}-%{release}
BuildRequires:    maven2 >= 0:2.0.8
BuildRequires:    maven-shared-plugin-testing-harness
BuildRequires:    hsqldb
BuildRequires:    junit
BuildRequires:    plexus-archiver
BuildRequires:    plexus-utils
Requires:    maven2 >= 0:2.0.8
Requires:    hsqldb
Requires:    plexus-archiver
Requires:    plexus-utils

%description -n mojo-maven2-plugin-hsqldb
%{summary}.
%endif

%if %{ibatis_include}
%package -n mojo-maven2-plugin-ibatis
Summary:     Ibatis plugin from %{name}
Group:       Development/Java
Requires:    %{name} = 0:%{version}-%{release}
BuildRequires:    maven2 >= 0:2.0.8
BuildRequires:    apache-ibatis2-ibator-core
BuildRequires:    hsqldb
Requires:    maven2 >= 0:2.0.8
Requires:    apache-ibatis2-ibator-core
Requires:    hsqldb

%description -n mojo-maven2-plugin-ibatis
%{summary}.
%endif

%if %{idlj_include}
%package -n mojo-maven2-plugin-idlj
Summary:     IDLJ plugin from %{name}
Group:       Development/Java
Requires:    %{name} = 0:%{version}-%{release}
BuildRequires:    maven2 >= 0:2.0.8
BuildRequires:    plexus-compiler
BuildRequires:    plexus-utils
Requires:    maven2 >= 0:2.0.8
Requires:    plexus-compiler
Requires:    plexus-utils

%description -n mojo-maven2-plugin-idlj
%{summary}.
%endif

%if %{j2me_include}
%package -n mojo-maven2-plugin-j2me
Summary:     J2ME plugin from %{name}
Group:       Development/Java
Requires:    %{name} = 0:%{version}-%{release}
BuildRequires:    maven2 >= 0:2.0.8
BuildRequires:    junit
Requires:    maven2 >= 0:2.0.8

%description -n mojo-maven2-plugin-j2me
%{summary}.
%endif

%if %{jalopy_include}
%package -n mojo-maven2-plugin-jalopy
Summary:     Jalopy plugin from %{name}
Group:       Development/Java
Requires:    %{name} = 0:%{version}-%{release}
BuildRequires:    maven2 >= 0:2.0.8
BuildRequires:    maven-shared-plugin-testing-harness
BuildRequires:    aelfred
BuildRequires:    jalopy
BuildRequires:    jdom
BuildRequires:    junit
BuildRequires:    log4j
BuildRequires:    oro
BuildRequires:    plexus-utils
BuildRequires:    xml-commons-jaxp-1.3-apis
Requires:    maven2 >= 0:2.0.8
Requires:    aelfred
Requires:    jalopy
Requires:    jdom
Requires:    log4j
Requires:    oro
Requires:    plexus-utils
Requires:    xml-commons-jaxp-1.3-apis

%description -n mojo-maven2-plugin-jalopy
%{summary}.
%endif

%if %{jardiff_include}
%package -n mojo-maven2-plugin-jardiff
Summary:     Jar diff plugin from %{name}
Group:       Development/Java
Requires:    %{name} = 0:%{version}-%{release}
BuildRequires:    maven2 >= 0:2.0.8
BuildRequires:    maven-shared-reporting-impl
BuildRequires:    jardiff
Requires:    maven2 >= 0:2.0.8
Requires:    maven-shared-reporting-impl
Requires:    jardiff

%description -n mojo-maven2-plugin-jardiff
%{summary}.
%endif

%if %{jasperreports_include}
%package -n mojo-maven2-plugin-jasperreports
Summary:     Jasperreports plugin from %{name}
Group:       Development/Java
Requires:    %{name} = 0:%{version}-%{release}
BuildRequires:    maven2 >= 0:2.0.8
BuildRequires:    jasperreports2
BuildRequires:    plexus-compiler
Requires:    maven2 >= 0:2.0.8
Requires:    jasperreports2
Requires:    plexus-compiler

%description -n mojo-maven2-plugin-jasperreports
%{summary}.
%endif

%if %{javacc_include}
%package -n mojo-maven2-plugin-javacc
Summary:     JavaCC plugin from %{name}
Group:       Development/Java
Requires:    %{name} = 0:%{version}-%{release}
BuildRequires:    maven2 >= 0:2.0.8
BuildRequires:    maven-doxia
BuildRequires:    maven-shared-reporting-impl
BuildRequires:    javacc >= 0:4.0
BuildRequires:    jtb >= 0:1.3.2
BuildRequires:    junit
BuildRequires:    plexus-compiler
BuildRequires:    plexus-utils
Requires:    maven2 >= 0:2.0.8
Requires:    javacc >= 0:4.0
Requires:    jtb >= 0:1.3.2
Requires:    plexus-compiler
Requires:    plexus-utils

%description -n mojo-maven2-plugin-javacc
%{summary}.
%endif

%if %{javancss_include}
%package -n mojo-maven2-plugin-javancss
Summary:     JavaNCSS plugin from %{name}
Group:       Development/Java
Requires:    %{name} = 0:%{version}-%{release}
BuildRequires:    easymock
BuildRequires:    maven2 >= 0:2.0.8
BuildRequires:    maven-shared-reporting-impl
BuildRequires:    dom4j
BuildRequires:    javancss
BuildRequires:    javahelp2
BuildRequires:    jaxen
Requires:    maven2 >= 0:2.0.8
Requires:    maven-shared-reporting-impl
Requires:    dom4j
Requires:    javancss
Requires:    javahelp2
Requires:    jaxen

%description -n mojo-maven2-plugin-javancss
%{summary}.
%endif

%if %{jaxb2_include}
%package -n mojo-maven2-plugin-jaxb2
Summary:     JAXB 2 plugin from %{name}
Group:       Development/Java
Requires:    %{name} = 0:%{version}-%{release}
BuildRequires:    maven2 >= 0:2.0.8
BuildRequires:    maven-shared-plugin-testing-harness
BuildRequires:    junit
BuildRequires:    sun-jaxb-2.1-impl
Requires:    maven2 >= 0:2.0.8
Requires:    jaxb_2_1_api
Requires:    sun-jaxb-2.1-impl

%description -n mojo-maven2-plugin-jaxb2
%{summary}.
%endif

%if %{jaxws_include}
%package -n mojo-maven2-plugin-jaxws
Summary:     JAXWS plugin from %{name}
Group:       Development/Java
Requires:    %{name} = 0:%{version}-%{release}
BuildRequires:    maven2 >= 0:2.0.8
BuildRequires:    jaxws_2_1_api
BuildRequires:    sun-jaxws-2.1-impl
BuildRequires:    sun-saaj-1.3-impl
Requires:    maven2 >= 0:2.0.8
Requires:    jaxws_2_1_api
Requires:    sun-jaxws-2.1-impl
Requires:    sun-saaj-1.3-impl

%description -n mojo-maven2-plugin-jaxws
%{summary}.
%endif

%if %{jboss_include}
%package -n mojo-maven2-plugin-jboss
Summary:     JBoss plugin from %{name}
Group:       Development/Java
Requires:    %{name} = 0:%{version}-%{release}
BuildRequires:    maven2 >= 0:2.0.8
BuildRequires:    jakarta-commons-codec
BuildRequires:    jakarta-commons-lang
BuildRequires:    jboss4-jmx
BuildRequires:    plexus-utils
BuildRequires:    velocity
Requires:    maven2 >= 0:2.0.8
Requires:    jakarta-commons-codec
Requires:    jakarta-commons-lang
Requires:    jboss4-jmx
Requires:    plexus-utils
Requires:    velocity

%description -n mojo-maven2-plugin-jboss
%{summary}.
%endif

%if %{jboss_packaging_include}
%package -n mojo-maven2-plugin-jboss-packaging
Summary:     JBoss packaging plugin from %{name}
Group:       Development/Java
Requires:    %{name} = 0:%{version}-%{release}
BuildRequires:    maven2 >= 0:2.0.8
BuildRequires:    maven-shared-archiver
BuildRequires:    plexus-utils
Requires:    maven2 >= 0:2.0.8
Requires:    maven-shared-archiver
Requires:    plexus-utils

%description -n mojo-maven2-plugin-jboss-packaging
%{summary}.
%endif

%if %{jdepend_include}
%package -n mojo-maven2-plugin-jdepend
Summary:     JDepend plugin from %{name}
Group:       Development/Java
Requires:    %{name} = 0:%{version}-%{release}
BuildRequires:    maven2 >= 0:2.0.8
BuildRequires:    maven-shared-reporting-impl
BuildRequires:    jdepend >= 0:2.9.1
Requires:    maven2 >= 0:2.0.8
Requires:    maven-shared-reporting-impl
Requires:    jdepend >= 0:2.9.1

%description -n mojo-maven2-plugin-jdepend
%{summary}.
%endif

%if %{jdiff_include}
%package -n mojo-maven2-plugin-jdiff
Summary:     JDiff plugin from %{name}
Group:       Development/Java
Requires:    %{name} = 0:%{version}-%{release}
BuildRequires:    maven2 >= 0:2.0.8
BuildRequires:    maven-doxia
BuildRequires:    maven-scm
BuildRequires:    maven-shared-reporting-impl
BuildRequires:    jakarta-commons-lang
BuildRequires:    jdiff >= 0:1.0.9
BuildRequires:    plexus-utils
BuildRequires:    xerces-j2
Requires:    maven2 >= 0:2.0.8
Requires:    maven-doxia
Requires:    maven-scm
Requires:    maven-shared-reporting-impl
Requires:    jakarta-commons-lang
Requires:    jdiff >= 0:1.0.9
Requires:    plexus-utils
Requires:    xerces-j2

%description -n mojo-maven2-plugin-jdiff
%{summary}.
%endif

%if %{jellyapi_include}
%package -n mojo-maven2-plugin-jellyapi
Summary:     Jelly Plugin API from %{name}
Group:       Development/Java
Requires:    %{name} = 0:%{version}-%{release}
BuildRequires:    maven2 >= 0:2.0.8
BuildRequires:    dom4j
BuildRequires:    jakarta-commons-jelly
Requires:    maven2 >= 0:2.0.8
Requires:    dom4j
Requires:    jakarta-commons-jelly

%description -n mojo-maven2-plugin-jellyapi
%{summary}.
%endif

%if %{jellymojo_include}
%package -n mojo-maven2-archetype-jellymojo
Summary:     Jelly mojo archetype from %{name}
Group:       Development/Java
Requires:    %{name} = 0:%{version}-%{release}
BuildRequires:    maven2 >= 0:2.0.8
Requires:    maven2 >= 0:2.0.8

%description -n mojo-maven2-archetype-jellymojo
%{summary}.
%endif

%if %{jetty_include}
%package -n mojo-maven2-plugin-jetty
Summary:     Jetty plugin from %{name}
Group:       Development/Java
Requires:    %{name} = 0:%{version}-%{release}
BuildRequires:    maven2 >= 0:2.0.8
BuildRequires:    ecj
BuildRequires:    jakarta-commons-el
BuildRequires:    jakarta-commons-logging
BuildRequires:    jetty5
BuildRequires:    tomcat5-jasper
BuildRequires:    tomcat5-servlet-2.4-api
BuildRequires:    tomcat5-jsp-2.0-api
BuildRequires:    xerces-j2
BuildRequires:    xml-commons-jaxp-1.3-apis
Requires:    maven2 >= 0:2.0.8
Requires:    ecj
Requires:    jakarta-commons-el
Requires:    jakarta-commons-logging
Requires:    jetty5
Requires:    tomcat5-jasper
Requires:    tomcat5-servlet-2.4-api
Requires:    tomcat5-jsp-2.0-api
Requires:    xerces-j2
Requires:    xml-commons-jaxp-1.3-apis

%description -n mojo-maven2-plugin-jetty
%{summary}.
%endif

%if %{jettybin_include}
%package -n mojo-maven2-plugin-jettybin
Summary:     Jetty bin plugin from %{name}
Group:       Development/Java
Requires:    %{name} = 0:%{version}-%{release}
BuildRequires:    maven2 >= 0:2.0.8
BuildRequires:    maven-shared-archiver
BuildRequires:    junit
BuildRequires:    plexus-digest
Requires:    maven2 >= 0:2.0.8
Requires:    maven-shared-archiver
Requires:    plexus-digest

%description -n mojo-maven2-plugin-jettybin
%{summary}.
%endif

%if %{jpox_include}
%package -n mojo-maven2-plugin-jpox
Summary:     JPOX plugin from %{name}
Group:       Development/Java
Requires:    %{name} = 0:%{version}-%{release}
BuildRequires:    maven2 >= 0:2.0.8
BuildRequires:    jpox-core
BuildRequires:    jpox-enhancer
BuildRequires:    plexus-container-default
BuildRequires:    plexus-utils
Requires:    maven2 >= 0:2.0.8
Requires:    jpox-core
Requires:    jpox-enhancer
Requires:    plexus-container-default
Requires:    plexus-utils

%description -n mojo-maven2-plugin-jpox
%{summary}.
%endif

%if %{jruby_include}
%package -n mojo-maven2-jruby
Summary:     JRuby plugin and support from %{name}
Group:       Development/Java
Requires:    %{name} = 0:%{version}-%{release}
BuildRequires:    maven2 >= 0:2.0.8
BuildRequires:    maven-shared-plugin-tools-api
BuildRequires:    plexus-jruby-factory
Requires:    maven2 >= 0:2.0.8
Requires:    maven-shared-plugin-tools-api
Requires:    plexus-jruby-factory

%description -n mojo-maven2-jruby
%{summary}.
%endif

%if %{jspc_include}
%package -n mojo-maven2-plugin-jspc
Summary:     Jspc plugin and api from %{name}
Group:       Development/Java
Requires:    %{name} = 0:%{version}-%{release}
BuildRequires:    maven2 >= 0:2.0.8
BuildRequires:    maven-shared-file-management
BuildRequires:    gmaven
BuildRequires:    jakarta-commons-lang
Requires:    maven2 >= 0:2.0.8
Requires:    maven-shared-file-management
Requires:    gmaven
Requires:    jakarta-commons-lang

%description -n mojo-maven2-plugin-jspc
%{summary}.
%endif

%if %{jspc_include}
%package -n mojo-maven2-jspc-compiler-tomcat5
Summary:     Jspc5 compiler from %{name}
Group:       Development/Java
Requires:    %{name} = 0:%{version}-%{release}
BuildRequires:    ecj
BuildRequires:    tomcat5
BuildRequires:    tomcat5-jasper
BuildRequires:    tomcat5-jsp-2.0-api
BuildRequires:    tomcat5-servlet-2.4-api
Requires:    mojo-maven2-plugin-jspc = 0:%{version}-%{release}
Requires:    ecj
Requires:    tomcat5
Requires:    tomcat5-jasper
Requires:    tomcat5-jsp-2.0-api
Requires:    tomcat5-servlet-2.4-api

%description -n mojo-maven2-jspc-compiler-tomcat5
%{summary}.
%endif

%if %{jspc_include}
%package -n mojo-maven2-jspc-compiler-tomcat6
Summary:     Jspc6 compiler from %{name}
Group:       Development/Java
Requires:    %{name} = 0:%{version}-%{release}
BuildRequires:    maven2 >= 0:2.0.8
BuildRequires:    annotation_1_0_api
BuildRequires:    ecj
BuildRequires:    el_1_0_api
BuildRequires:    tomcat6-lib
BuildRequires:    tomcat6
BuildRequires:    tomcat6-jsp-2.1-api
BuildRequires:    tomcat6-servlet-2.5-api
Requires:    maven2 >= 0:2.0.8
Requires:    annotation_1_0_api
Requires:    ecj
Requires:    el_1_0_api
Requires:    tomcat6-lib
Requires:    tomcat6
Requires:    tomcat6-jsp-2.1-api
Requires:    tomcat6-servlet-2.5-api

%description -n mojo-maven2-jspc-compiler-tomcat6
%{summary}.
%endif

#%package -n mojo-maven2-plugin-jxr
#Summary:     JXR plugin from %{name}
#Group:       Development/Java
#Requires:    %{name} = 0:%{version}-%{release}
#Requires:    maven2 >= 0:2.0.8
#Requires:    maven-jxr
#
#%description -n mojo-maven2-plugin-jxr
#%{summary}.

%if %{wagon_cifs_include}
%package -n mojo-maven2-wagon-cifs
Summary:     CIFS wagon extension from %{name}
Group:       Development/Java
Requires:    %{name} = 0:%{version}-%{release}
BuildRequires:    maven2 >= 0:2.0.8
BuildRequires:    maven-wagon
BuildRequires:    jcifs >= 0:1.2.9
BuildRequires:    plexus-utils
Requires:    maven2 >= 0:2.0.8
Requires:    maven-wagon
Requires:    jcifs >= 0:1.2.9
Requires:    plexus-utils

%description -n mojo-maven2-wagon-cifs
%{summary}.
%endif

%if %{keytool_include}
%package -n mojo-maven2-plugin-keytool
Summary:     Keytool plugin from %{name}
Group:       Development/Java
Requires:    %{name} = 0:%{version}-%{release}
BuildRequires:    maven2 >= 0:2.0.8
BuildRequires:    jakarta-commons-lang
BuildRequires:    plexus-utils
Requires:    maven2 >= 0:2.0.8
Requires:    jakarta-commons-lang
Requires:    plexus-utils

%description -n mojo-maven2-plugin-keytool
%{summary}.
%endif

%if %{mojo_archetypes_include}
%package -n mojo-maven2-archetypes
Summary:     Archetypes from %{name}
Group:       Development/Java
Requires:    %{name} = 0:%{version}-%{release}
BuildRequires:    maven2 >= 0:2.0.8
Requires:    maven2 >= 0:2.0.8

%description -n mojo-maven2-archetypes
%{summary}.
%endif

#%if %{legaltools_include}
#%package -n mojo-maven2-plugin-legaltools
#Summary:     Legal tools plugin from %{name}
#Group:       Development/Java
#Requires:    %{name} = 0:%{version}-%{release}
#Requires:    maven2 >= 0:2.0.8
#Requires:    maven-shared-file-management
#Requires:    mojo-maven2-groovy
#
#%description -n mojo-maven2-plugin-legaltools
#%{summary}.
#%endif

%if %{l10n_include}
%package -n mojo-maven2-plugin-l10n
Summary:     Localization plugin from %{name}
Group:       Development/Java
Requires:    %{name} = 0:%{version}-%{release}
BuildRequires:    maven2 >= 0:2.0.8
BuildRequires:    maven-doxia
BuildRequires:    maven-shared-reporting-impl
BuildRequires:    plexus-utils
Requires:    maven2 >= 0:2.0.8
Requires:    maven-shared-reporting-impl
Requires:    plexus-utils

%description -n mojo-maven2-plugin-l10n
%{summary}.
%endif

%if %{mant_include}
%package -n mojo-maven2-plugin-mant
Summary:     Mant plugin from %{name}
Group:       Development/Java
Requires:    %{name} = 0:%{version}-%{release}
BuildRequires:    maven2 >= 0:2.0.8
BuildRequires:    ant >= 0:1.7.1
BuildRequires:    dom4j
BuildRequires:    junit
BuildRequires:    xerces-j2
BuildRequires:    xml-commons-jaxp-1.3-apis
Requires:    maven2 >= 0:2.0.8
Requires:    ant >= 0:1.7.1
Requires:    dom4j
Requires:    xerces-j2
Requires:    xml-commons-jaxp-1.3-apis

%description -n mojo-maven2-plugin-mant
%{summary}.
%endif

%if %{mojo_was_plugin_anttasks_include}
%package -n mojo-maven2-was
Summary:     WAS plugin and support from %{name}
Group:       Development/Java
Requires:    %{name} = 0:%{version}-%{release}
Requires:    maven2 >= 0:2.0.8
Requires:    maven-embedder
Requires:    ant >= 0:1.7.1

%description -n mojo-maven2-was
%{summary}.
%endif

%if %{minijar_include}
%package -n mojo-maven2-plugin-minijar
Summary:     Minijar plugin from %{name}
Group:       Development/Java
Requires:    %{name} = 0:%{version}-%{release}
BuildRequires:    maven2 >= 0:2.0.8
BuildRequires:    jakarta-commons-io
BuildRequires:    plexus-utils
BuildRequires:    vafer-dependency
Requires:    maven2 >= 0:2.0.8
Requires:    jakarta-commons-io
Requires:    plexus-utils
Requires:    vafer-dependency

%description -n mojo-maven2-plugin-minijar
%{summary}.
%endif

%if %{native_include}
%package -n mojo-maven2-natives
Summary:     Native plugin and support from %{name}
Group:       Development/Java
Requires:    %{name} = 0:%{version}-%{release}
BuildRequires:    maven2 >= 0:2.0.8
BuildRequires:    maven-shared-plugin-testing-harness
BuildRequires:    bcel
BuildRequires:    plexus-container-default
BuildRequires:    plexus-utils
Requires:    maven2 >= 0:2.0.8
Requires:    bcel
Requires:    plexus-container-default
Requires:    plexus-utils

%description -n mojo-maven2-natives
%{summary}.
%endif

%if %{native2ascii_include}
%package -n mojo-maven2-plugin-native2ascii
Summary:     Native2ascii plugin from %{name}
Group:       Development/Java
Requires:    %{name} = 0:%{version}-%{release}
BuildRequires:    maven2 >= 0:2.0.8
BuildRequires:    ant
BuildRequires:    ant-nodeps
Requires:    maven2 >= 0:2.0.8
Requires:    ant
Requires:    ant-nodeps

%description -n mojo-maven2-plugin-native2ascii
%{summary}.
%endif

%if %{netbeans_freeform_include}
%package -n mojo-maven2-plugin-netbeans-freeform
Summary:     Netbeans Freeform plugin from %{name}
Group:       Development/Java
Requires:    %{name} = 0:%{version}-%{release}
BuildRequires:    maven2 >= 0:2.0.8
BuildRequires:    plexus-utils
Requires:    maven2 >= 0:2.0.8
Requires:    plexus-utils

%description -n mojo-maven2-plugin-netbeans-freeform
%{summary}.
%endif

%if %{openjpa_include}
%package -n mojo-maven2-plugin-openjpa
Summary:     OpenJPA plugin from %{name}
Group:       Development/Java
Requires:    %{name} = 0:%{version}-%{release}
BuildRequires:    maven2 >= 0:2.0.8
BuildRequires:    maven-shared-plugin-testing-harness
BuildRequires:    maven-shared-plugin-testing-tools
BuildRequires:    maven-shared-test-tools
BuildRequires:    geronimo-jms-1.1-api
BuildRequires:    openjpa
BuildRequires:    plexus-container-default
BuildRequires:    plexus-utils
Requires:    maven2 >= 0:2.0.8
Requires:    openjpa
Requires:    plexus-container-default
Requires:    plexus-utils

%description -n mojo-maven2-plugin-openjpa
%{summary}.
%endif

%if %{osxappbundle_include}
%package -n mojo-maven2-plugin-osxappbundle
Summary:     OS/X Appbundle plugin from %{name}
Group:       Development/Java
Requires:    %{name} = 0:%{version}-%{release}
BuildRequires:    maven2 >= 0:2.0.8
BuildRequires:    maven-shared-archiver
BuildRequires:    plexus-archiver
BuildRequires:    plexus-mainclass-finder
BuildRequires:    plexus-velocity
Requires:    maven2 >= 0:2.0.8
Requires:    maven-shared-archiver
Requires:    plexus-archiver
Requires:    plexus-mainclass-finder
Requires:    plexus-velocity

%description -n mojo-maven2-plugin-osxappbundle
%{summary}.
%endif

%if %{ounce_include}
%package -n mojo-maven2-plugin-ounce
Summary:     Ounce plugin from %{name}
Group:       Development/Java
Requires:    %{name} = 0:%{version}-%{release}
BuildRequires:    maven2 >= 0:2.0.8
BuildRequires:    maven-shared-plugin-testing-harness
BuildRequires:    maven-shared-plugin-testing-tools
BuildRequires:    maven-shared-reporting-impl
BuildRequires:    maven-shared-test-tools
BuildRequires:    maven-surefire-plugin
BuildRequires:    plexus-container-default
BuildRequires:    plexus-io
BuildRequires:    plexus-maven-plugin
BuildRequires:    plexus-utils
BuildRequires:    xerces-j2
BuildRequires:    xstream
Requires:    maven2 >= 0:2.0.8
Requires:    maven-shared-reporting-impl
Requires:    plexus-io
Requires:    plexus-container-default
Requires:    plexus-utils
Requires:    xerces-j2
Requires:    xstream

%description -n mojo-maven2-plugin-ounce
%{summary}.
%endif

#%if %{pde_include}
#%package -n mojo-maven2-plugin-pde
#Summary:     PDE plugin from %{name}
#Group:       Development/Java
#Requires:    %{name} = 0:%{version}-%{release}
#Requires:    maven2 >= 0:2.0.8
#Requires:    maven-shared-osgi
#Requires:    aqute-bndlib
#Requires:    eclipse-pde
#Requires:    eclipse-platform
#Requires:    eclipse-rcp
#Requires:    jakarta-commons-configuration
#Requires:    jakarta-commons-lang
#Requires:    plexus-utils

#%description -n mojo-maven2-plugin-pde
#%{summary}.
#%endif

%if %{plugin_support_include}
%package -n mojo-maven2-support
Summary:     Support lib from %{name}
Group:       Development/Java
Requires:    %{name} = 0:%{version}-%{release}
BuildRequires:    maven2 >= 0:2.0.8
BuildRequires:    ant >= 0:1.7.1
BuildRequires:    jakarta-commons-jexl
BuildRequires:    jakarta-commons-lang
BuildRequires:    jakarta-commons-logging
Requires:    maven2 >= 0:2.0.8
Requires:    ant >= 0:1.7.1
Requires:    jakarta-commons-jexl
Requires:    jakarta-commons-lang
Requires:    jakarta-commons-logging

%description -n mojo-maven2-support
%{summary}.
%endif

%if %{pomtools_include}
%package -n mojo-maven2-plugin-pomtools
Summary:     POM tools plugin from %{name}
Group:       Development/Java
Requires:    %{name} = 0:%{version}-%{release}
BuildRequires:    maven2 >= 0:2.0.8
BuildRequires:    jakarta-commons-beanutils
BuildRequires:    jakarta-commons-lang
BuildRequires:    plexus-interactivity
Requires:    maven2 >= 0:2.0.8
Requires:    jakarta-commons-beanutils
Requires:    jakarta-commons-lang
Requires:    plexus-interactivity

%description -n mojo-maven2-plugin-pomtools
%{summary}.
%endif

%if %{properties_include}
%package -n mojo-maven2-plugin-properties
Summary:     Properties plugin from %{name}
Group:       Development/Java
Requires:    %{name} = 0:%{version}-%{release}
BuildRequires:    maven2 >= 0:2.0.8
BuildRequires:    junit
Requires:    maven2 >= 0:2.0.8

%description -n mojo-maven2-plugin-properties
%{summary}.
%endif

%if %{push_include}
%package -n mojo-maven2-plugin-push
Summary:     Push plugin from %{name}
Group:       Development/Java
Requires:    %{name} = 0:%{version}-%{release}
BuildRequires:    maven2 >= 0:2.0.8
BuildRequires:    maven-wagon
Requires:    maven2 >= 0:2.0.8
Requires:    maven-wagon

%description -n mojo-maven2-plugin-push
%{summary}.
%endif

%if %{rat_include}
%package -n mojo-maven2-plugin-rat
Summary:     Rat plugin from %{name}
Group:       Development/Java
Requires:    %{name} = 0:%{version}-%{release}
BuildRequires:    maven2 >= 0:2.0.8
BuildRequires:    maven-doxia
BuildRequires:    maven-shared-plugin-testing-harness
BuildRequires:    maven-shared-reporting-impl
BuildRequires:    junit
BuildRequires:    plexus-utils
BuildRequires:    rat-lib
Requires:    maven2 >= 0:2.0.8
Requires:    plexus-utils
Requires:    rat-lib

%description -n mojo-maven2-plugin-rat
%{summary}.
%endif

%if %{retroweaver_include}
%package -n mojo-maven2-plugin-retroweaver
Summary:     Retroweaver plugin from %{name}
Group:       Development/Java
Requires:    %{name} = 0:%{version}-%{release}
BuildRequires:    maven2 >= 0:2.0.8
BuildRequires:    junit
Requires:    maven2 >= 0:2.0.8

%description -n mojo-maven2-plugin-retroweaver
%{summary}.
%endif

%if %{retrotranslator_include}
%package -n mojo-maven2-plugin-retrotranslator
Summary:     Retrotranslator plugin from %{name}
Group:       Development/Java
Requires:    %{name} = 0:%{version}-%{release}
BuildRequires:    maven2 >= 0:2.0.8
BuildRequires:    maven-shared-archiver
BuildRequires:    maven-shared-file-management
BuildRequires:    gmaven
BuildRequires:    jakarta-commons-lang
BuildRequires:    retrotranslator >= 0:1.2.1
Requires:    maven2 >= 0:2.0.8
Requires:    maven-shared-archiver
Requires:    maven-shared-file-management
Requires:    gmaven
Requires:    jakarta-commons-lang
Requires:    retrotranslator >= 0:1.2.1

%description -n mojo-maven2-plugin-retrotranslator
%{summary}.
%endif

%if %{rmic_include}
%package -n mojo-maven2-plugin-rmic
Summary:     Rmic plugin from %{name}
Group:       Development/Java
Requires:    %{name} = 0:%{version}-%{release}
BuildRequires:    maven2 >= 0:2.0.8
BuildRequires:    plexus-archiver
BuildRequires:    plexus-container-default
Requires:    maven2 >= 0:2.0.8
Requires:    plexus-archiver
Requires:    plexus-container-default

%description -n mojo-maven2-plugin-rmic
%{summary}.
%endif

%if %{rpm_include}
%package -n mojo-maven2-plugin-rpm
Summary:     RPM plugin from %{name}
Group:       Development/Java
Requires:    %{name} = 0:%{version}-%{release}
BuildRequires:    maven2 >= 0:2.0.8
BuildRequires:    plexus-archiver
BuildRequires:    plexus-container-default
BuildRequires:    plexus-utils
Requires:    maven2 >= 0:2.0.8
Requires:    plexus-archiver
Requires:    plexus-container-default
Requires:    plexus-utils

%description -n mojo-maven2-plugin-rpm
%{summary}.
%endif

#%if %{rspec_include}
#%package -n mojo-maven2-plugin-rspec
#Summary:     Rspec plugin from %{name}
#Group:       Development/Java
#Requires:    %{name} = 0:%{version}-%{release}
#Requires:    maven2 >= 0:2.0.8
#Requires:    jruby
#
#%description -n mojo-maven2-plugin-rspec
#%{summary}.
#%endif

%if %{rubyscript_include}
%package -n mojo-maven2-archetype-rubyscript
Summary:     Rubyscript archetype from %{name}
Group:       Development/Java
Requires:    %{name} = 0:%{version}-%{release}
BuildRequires:    maven2 >= 0:2.0.8
Requires:    maven2 >= 0:2.0.8

%description -n mojo-maven2-archetype-rubyscript
%{summary}.
%endif

%if %{runtime_builder_include}
%package -n mojo-maven2-plugin-runtime-builder
Summary:     Runtime builder plugin from %{name}
Group:       Development/Java
Requires:    %{name} = 0:%{version}-%{release}
BuildRequires:    maven2 >= 0:2.0.8
BuildRequires:    maven-shared-archiver
BuildRequires:    maven-wagon
BuildRequires:    classworlds
BuildRequires:    plexus-appserver
BuildRequires:    plexus-archiver
BuildRequires:    plexus-compiler
BuildRequires:    plexus-utils
BuildRequires:    plexus-velocity
BuildRequires:    velocity
Requires:    maven2 >= 0:2.0.8
Requires:    maven-shared-archiver
Requires:    maven-wagon
Requires:    classworlds
Requires:    plexus-appserver
Requires:    plexus-archiver
Requires:    plexus-compiler
Requires:    plexus-utils
Requires:    plexus-velocity
Requires:    velocity

%description -n mojo-maven2-plugin-runtime-builder
%{summary}.
%endif

%if %{sablecc_include}
%package -n mojo-maven2-plugin-sablecc
Summary:     Sablecc plugin from %{name}
Group:       Development/Java
Requires:    %{name} = 0:%{version}-%{release}
BuildRequires:    maven2 >= 0:2.0.8
BuildRequires:    plexus-compiler
BuildRequires:    plexus-utils
BuildRequires:    sablecc
Requires:    maven2 >= 0:2.0.8
Requires:    plexus-compiler
Requires:    plexus-utils
Requires:    sablecc

%description -n mojo-maven2-plugin-sablecc
%{summary}.
%endif

%if %{script_include}
%package -n mojo-maven2-plugin-script
Summary:     Script plugin from %{name}
Group:       Development/Java
Requires:    %{name} = 0:%{version}-%{release}
BuildRequires:    maven2 >= 0:2.0.8
#BuildRequires:    bsf >= 0:2.4.0
BuildRequires:    bsf
Requires:    maven2 >= 0:2.0.8
#Requires:    bsf >= 0:2.4.0
Requires:    bsf

%description -n mojo-maven2-plugin-script
%{summary}.
%endif

%if %{selenium_include}
%package -n mojo-maven2-plugin-selenium
Summary:     Selenium plugin from %{name}
Group:       Development/Java
Requires:    %{name} = 0:%{version}-%{release}
BuildRequires:    maven2 >= 0:2.0.8
BuildRequires:    maven-surefire-plugin
BuildRequires:    maven-release
BuildRequires:    bouncycastle
BuildRequires:    gmaven
BuildRequires:    jakarta-commons-lang
BuildRequires:    log4j
BuildRequires:    openqa-selenium-core >= 0.8.3
BuildRequires:    openqa-selenium-rc-java-client-driver >= 0:0.9.2
BuildRequires:    openqa-selenium-rc-server >= 0:0.9.2
BuildRequires:    openqa-selenium-rc-server-coreless >= 0:0.9.2
Requires:    maven2 >= 0:2.0.8
Requires:    bouncycastle
Requires:    gmaven
Requires:    jakarta-commons-lang
Requires:    log4j
Requires:    openqa-selenium-core >= 0.8.3
Requires:    openqa-selenium-rc-java-client-driver >= 0:0.9.2
Requires:    openqa-selenium-rc-server >= 0:0.9.2
Requires:    openqa-selenium-rc-server-coreless >= 0:0.9.2

%description -n mojo-maven2-plugin-selenium
%{summary}.
%endif

%if %{shade_include}
%package -n mojo-maven2-plugin-shade
Summary:     Shade testing plugin from %{name}
Group:       Development/Java
Requires:    %{name} = 0:%{version}-%{release}
BuildRequires:    maven2 >= 0:2.0.8
BuildRequires:    jdom
BuildRequires:    junit
BuildRequires:    objectweb-asm >= 0:3.0
BuildRequires:    plexus-utils
Requires:    maven2 >= 0:2.0.8
Requires:    jdom
Requires:    objectweb-asm >= 0:3.0
Requires:    plexus-utils

%description -n mojo-maven2-plugin-shade
%{summary}.
%endif

%if %{shell_include}
%package -n mojo-maven2-plugin-shell
Summary:     Shell testing plugin from %{name}
Group:       Development/Java
Requires:    %{name} = 0:%{version}-%{release}
BuildRequires:    maven2 >= 0:2.0.8
BuildRequires:    plexus-utils
Requires:    maven2 >= 0:2.0.8
Requires:    plexus-utils

%description -n mojo-maven2-plugin-shell
%{summary}.
%endif

%if %{shitty_include}
%package -n mojo-maven2-plugin-shitty
Summary:     Shitty testing plugin from %{name}
Group:       Development/Java
Requires:    %{name} = 0:%{version}-%{release}
BuildRequires:    maven2 >= 0:2.0.8
BuildRequires:    maven-shared-file-management
BuildRequires:    gmaven
BuildRequires:    backport-util-concurrent
BuildRequires:    jakarta-commons-lang
BuildRequires:    jline
BuildRequires:    plexus-digest
BuildRequires:    plexus-utils
Requires:    maven2 >= 0:2.0.8
Requires:    maven-shared-file-management
Requires:    gmaven
Requires:    backport-util-concurrent
Requires:    jakarta-commons-lang
Requires:    jline
Requires:    plexus-digest
Requires:    plexus-utils

%description -n mojo-maven2-plugin-shitty
%{summary}.
%endif

%if %{testing_simple_include}
%package -n mojo-maven2-plugin-simple
Summary:     Simple testing plugin from %{name}
Group:       Development/Java
Requires:    %{name} = 0:%{version}-%{release}
BuildRequires:    maven2 >= 0:2.0.8
Requires:    maven2 >= 0:2.0.8

%description -n mojo-maven2-plugin-simple
%{summary}.
%endif

%if %{smc_include}
%package -n mojo-maven2-plugin-smc
Summary:     State machine compiler plugin from %{name}
Group:       Development/Java
Requires:    %{name} = 0:%{version}-%{release}
BuildRequires:    maven2 >= 0:2.0.8
BuildRequires:    maven-shared-reporting-impl
BuildRequires:    jakarta-commons-lang
BuildRequires:    plexus-utils
BuildRequires:    jsmc >= 0:5.0
Requires:    maven2 >= 0:2.0.8
Requires:    maven-shared-reporting-impl
Requires:    jakarta-commons-lang
Requires:    plexus-utils
Requires:    jsmc >= 0:5.0

%description -n mojo-maven2-plugin-smc
%{summary}.
%endif

%if %{springbeandoc_include}
%package -n mojo-maven2-plugin-springbeandoc
Summary:     Spring Beandoc plugin from %{name}
Group:       Development/Java
Requires:    %{name} = 0:%{version}-%{release}
BuildRequires:    maven2 >= 0:2.0.8
BuildRequires:    maven-shared-reporting-impl
BuildRequires:    jakarta-commons-collections
BuildRequires:    jakarta-commons-logging
BuildRequires:    jdom
BuildRequires:    junit
BuildRequires:    spring2-beans
BuildRequires:    spring2-core
BuildRequires:    spring-beandoc
Requires:    maven2 >= 0:2.0.8
Requires:    maven-shared-reporting-impl
Requires:    jakarta-commons-collections
Requires:    jakarta-commons-logging
Requires:    jdom
Requires:    spring2-beans
Requires:    spring2-core
Requires:    spring-beandoc

%description -n mojo-maven2-plugin-springbeandoc
%{summary}.
%endif

%if %{springdoclet_include}
%package -n mojo-maven2-plugin-springdoclet
Summary:     Spring doclet plugin from %{name}
Group:       Development/Java
Requires:    %{name} = 0:%{version}-%{release}
BuildRequires:    maven2 >= 0:2.0.8
BuildRequires:    jakarta-commons-collections
BuildRequires:    jakarta-commons-logging
BuildRequires:    jboss4-j2ee
BuildRequires:    junit
BuildRequires:    servlet_2_3_api
BuildRequires:    xdoclet
BuildRequires:    xjavadoc
Requires:    maven2 >= 0:2.0.8
Requires:    mojo-maven2-plugin-mant
Requires:    jakarta-commons-collections
Requires:    jakarta-commons-logging
Requires:    jboss4-j2ee
Requires:    servlet_2_3_api
Requires:    xdoclet
Requires:    xjavadoc

%description -n mojo-maven2-plugin-springdoclet
%{summary}.
%endif

%if %{sql_include}
%package -n mojo-maven2-plugin-sql
Summary:     SQL plugin from %{name}
Group:       Development/Java
Requires:    %{name} = 0:%{version}-%{release}
BuildRequires:    maven2 >= 0:2.0.8
BuildRequires:    axion
BuildRequires:    javacc3
BuildRequires:    junit
Requires:    maven2 >= 0:2.0.8

%description -n mojo-maven2-plugin-sql
%{summary}.
%endif

%if %{sysdeo_tomcat_include}
%package -n mojo-maven2-plugin-sysdeo-tomcat
Summary:     Sysdeo Tomcat plugin from %{name}
Group:       Development/Java
Requires:    %{name} = 0:%{version}-%{release}
BuildRequires:    maven2 >= 0:2.0.8
BuildRequires:    freemarker >= 0:2.3.6
BuildRequires:    jakarta-commons-codec
BuildRequires:    jakarta-commons-io
Requires:    maven2 >= 0:2.0.8
Requires:    freemarker >= 0:2.3.6
Requires:    jakarta-commons-codec
Requires:    jakarta-commons-io

%description -n mojo-maven2-plugin-sysdeo-tomcat
%{summary}.
%endif

%if %{taglist_include}
%package -n mojo-maven2-plugin-taglist
Summary:     Taglist plugin from %{name}
Group:       Development/Java
Requires:    %{name} = 0:%{version}-%{release}
BuildRequires:    maven2 >= 0:2.0.8
BuildRequires:    maven-shared-reporting-impl
Requires:    maven2 >= 0:2.0.8
Requires:    maven-shared-reporting-impl

%description -n mojo-maven2-plugin-taglist
%{summary}.
%endif

%if %{tomcat_include}
%package -n mojo-maven2-plugin-tomcat
Summary:     Tomcat plugin from %{name}
Group:       Development/Java
Requires:    %{name} = 0:%{version}-%{release}
BuildRequires:    maven2 >= 0:2.0.8
BuildRequires:    ecj
BuildRequires:    jakarta-commons-codec
BuildRequires:    jakarta-commons-logging
BuildRequires:    plexus-utils
BuildRequires:    tomcat5
BuildRequires:    tomcat5-common-lib
BuildRequires:    tomcat5-jasper
BuildRequires:    tomcat5-jsp-2.0-api
BuildRequires:    tomcat5-server-lib
BuildRequires:    tomcat5-servlet-2.4-api
Requires:    maven2 >= 0:2.0.8
Requires:    ecj
Requires:    jakarta-commons-codec
Requires:    jakarta-commons-logging
Requires:    plexus-utils
Requires:    tomcat5
Requires:    tomcat5-common-lib
Requires:    tomcat5-jasper
Requires:    tomcat5-jsp-2.0-api
Requires:    tomcat5-server-lib
Requires:    tomcat5-servlet-2.4-api

%description -n mojo-maven2-plugin-tomcat
%{summary}.
%endif

%if %{visibroker_include}
%package -n mojo-maven2-plugin-visibroker
Summary:     Visibroker plugin from %{name}
Group:       Development/Java
Requires:    %{name} = 0:%{version}-%{release}
BuildRequires:    maven2 >= 0:2.0.8
Requires:    maven2 >= 0:2.0.8
Requires:    mojo-maven2-natives

%description -n mojo-maven2-plugin-visibroker
%{summary}.
%endif

%if %{wagon_include}
%package -n mojo-maven2-plugin-wagon
Summary:     Wagon plugin from %{name}
Group:       Development/Java
Requires:    %{name} = 0:%{version}-%{release}
BuildRequires:    maven2 >= 0:2.0.8
BuildRequires:    maven-shared-plugin-testing-harness
BuildRequires:    maven-wagon
BuildRequires:    plexus-container-default
BuildRequires:    plexus-utils
Requires:    maven2 >= 0:2.0.8
Requires:    maven-wagon
Requires:    plexus-container-default
Requires:    plexus-utils

%description -n mojo-maven2-plugin-wagon
%{summary}.
%endif

%if %{webdoclet_include}
%package -n mojo-maven2-plugin-webdoclet
Summary:     Web doclet plugin from %{name}
Group:       Development/Java
Requires:    %{name} = 0:%{version}-%{release}
BuildRequires:    maven2 >= 0:2.0.8
BuildRequires:    jakarta-commons-collections
BuildRequires:    jakarta-commons-logging
BuildRequires:    jboss4-j2ee
BuildRequires:    junit
BuildRequires:    servlet_2_3_api
BuildRequires:    xdoclet
BuildRequires:    xjavadoc
Requires:    maven2 >= 0:2.0.8
Requires:    mojo-maven2-plugin-mant
Requires:    jakarta-commons-collections
Requires:    jakarta-commons-logging
Requires:    jboss4-j2ee
Requires:    servlet_2_3_api
Requires:    xdoclet
Requires:    xjavadoc

%description -n mojo-maven2-plugin-webdoclet
%{summary}.
%endif

%if %{webstart_include}
%package -n mojo-maven2-plugin-webstart
Summary:     Webstart plugin and support from %{name}
Group:       Development/Java
Requires:    %{name} = 0:%{version}-%{release}
BuildRequires:    maven2 >= 0:2.0.8
BuildRequires:    maven2-plugin-jar
BuildRequires:    maven2-plugin-plugin
BuildRequires:    maven-embedder
BuildRequires:    maven-shared-plugin-testing-harness
BuildRequires:    maven-shared-plugin-tools-java
BuildRequires:    maven-shared-reporting-impl
BuildRequires:    ant
BuildRequires:    jakarta-commons-lang
BuildRequires:    junit
BuildRequires:    plexus-utils
BuildRequires:    servlet_api
BuildRequires:    velocity
BuildRequires:    xmlunit
Requires:    maven2 >= 0:2.0.8
Requires:    maven2-plugin-jar
Requires:    maven2-plugin-plugin
Requires:    maven-shared-plugin-tools-java
Requires:    maven-shared-reporting-impl
Requires:    mojo-maven2-plugin-keytool
Requires:    ant
Requires:    jakarta-commons-lang
Requires:    plexus-utils
Requires:    servlet_api
Requires:    velocity

%description -n mojo-maven2-plugin-webstart
%{summary}.
%endif

%if %{wsdl2java_include}
%package -n mojo-maven2-plugin-wsdl2java
Summary:     WSDL2Java plugin from %{name}
Group:       Development/Java
Requires:    %{name} = 0:%{version}-%{release}
BuildRequires:    maven2 >= 0:2.0.8
BuildRequires:    axis >= 0:1.4
BuildRequires:    jakarta-commons-discovery
BuildRequires:    jakarta-commons-logging
BuildRequires:    plexus-compiler
BuildRequires:    plexus-utils
BuildRequires:    wsdl4j >= 0:1.5.1
Requires:    maven2 >= 0:2.0.8
Requires:    axis >= 0:1.4
Requires:    jakarta-commons-discovery
Requires:    jakarta-commons-logging
Requires:    plexus-compiler
Requires:    plexus-utils
Requires:    wsdl4j >= 0:1.5.1

%description -n mojo-maven2-plugin-wsdl2java
%{summary}.
%endif

%if %{xdoclet_include}
%package -n mojo-maven2-plugin-xdoclet
Summary:     XDoclet plugin from %{name}
Group:       Development/Java
Requires:    %{name} = 0:%{version}-%{release}
BuildRequires:    maven2 >= 0:2.0.8
BuildRequires:    maven2-plugin-antrun
BuildRequires:    jakarta-commons-collections
BuildRequires:    jakarta-commons-logging
BuildRequires:    jboss4-j2ee
BuildRequires:    servlet_2_3_api
BuildRequires:    xdoclet
BuildRequires:    xjavadoc
Requires:    maven2 >= 0:2.0.8
Requires:    maven2-plugin-antrun
Requires:    jakarta-commons-collections
Requires:    jakarta-commons-logging
Requires:    jboss4-j2ee
Requires:    servlet_2_3_api
Requires:    xdoclet
Requires:    xjavadoc

%description -n mojo-maven2-plugin-xdoclet
%{summary}.
%endif

%if %{xfire_include}
%package -n mojo-maven2-plugin-xfire
Summary:     XFire plugin from %{name}
Group:       Development/Java
Requires:    %{name} = 0:%{version}-%{release}
BuildRequires:    maven2 >= 0:2.0.8
BuildRequires:    glassfish-javamail >= 0:1.4
BuildRequires:    log4j
BuildRequires:    servlet_2_3_api
BuildRequires:    xfire-generator
Requires:    maven2 >= 0:2.0.8
Requires:    javamail_1_4_api
Requires:    log4j
Requires:    servlet_2_3_api
Requires:    xfire-generator

%description -n mojo-maven2-plugin-xfire
%{summary}.
%endif

%if %{xjc_include}
%package -n mojo-maven2-plugin-xjc
Summary:     XJC (JAXB 1) plugin from %{name}
Group:       Development/Java
Requires:    %{name} = 0:%{version}-%{release}
BuildRequires:    maven2 >= 0:2.0.8
BuildRequires:    jaxb_1_0_api
BuildRequires:    junit
BuildRequires:    sun-jaxb-1.0-impl
Requires:    maven2 >= 0:2.0.8
Requires:    mojo-maven2-plugin-mant
Requires:    jaxb_1_0_api
Requires:    sun-jaxb-1.0-impl

%description -n mojo-maven2-plugin-xjc
%{summary}.
%endif

%if %{xmlbeans_include}
%package -n mojo-maven2-plugin-xmlbeans
Summary:     XmlBeans plugin from %{name}
Group:       Development/Java
Requires:    %{name} = 0:%{version}-%{release}
BuildRequires:    maven2 >= 0:2.0.8
BuildRequires:    classworlds
BuildRequires:    junit
BuildRequires:    maven-wagon
BuildRequires:    plexus-container-artifact
BuildRequires:    plexus-container-default
BuildRequires:    plexus-utils
BuildRequires:    xml-commons-resolver12
BuildRequires:    xmlbeans
Requires:    maven2 >= 0:2.0.8
Requires:    maven-wagon
Requires:    plexus-container-default
Requires:    plexus-utils
Requires:    xml-commons-resolver12
Requires:    xmlbeans

%description -n mojo-maven2-plugin-xmlbeans
%{summary}.
%endif

%if %{xml_include}
%package -n mojo-maven2-plugin-xml
Summary:     Xml plugin from %{name}
Group:       Development/Java
Requires:    %{name} = 0:%{version}-%{release}
BuildRequires:    maven2 >= 0:2.0.8
BuildRequires:    maven-shared-plugin-testing-harness
BuildRequires:    plexus-io
BuildRequires:    plexus-resources
BuildRequires:    plexus-utils
BuildRequires:    saxon8
BuildRequires:    xalan-j2
BuildRequires:    xerces-j2
BuildRequires:    xml-commons-jaxp-1.3-apis
BuildRequires:    xml-commons-resolver11
Requires:    maven2 >= 0:2.0.8
Requires:    plexus-io
Requires:    plexus-resources
Requires:    plexus-utils
Requires:    xerces-j2
Requires:    xml-commons-jaxp-1.3-apis
Requires:    xml-commons-resolver11

%description -n mojo-maven2-plugin-xml
%{summary}.
%endif

%if %{xslt_include}
%package -n mojo-maven2-plugin-xslt
Summary:     Xslt plugin from %{name}
Group:       Development/Java
Requires:    %{name} = 0:%{version}-%{release}
BuildRequires:    maven2 >= 0:2.0.8
BuildRequires:    junit
BuildRequires:    plexus-utils
Requires:    maven2 >= 0:2.0.8
Requires:    plexus-utils

%description -n mojo-maven2-plugin-xslt
%{summary}.
%endif

%if %{xsltc_include}
%package -n mojo-maven2-plugin-xsltc
Summary:     Xsltc plugin from %{name}
Group:       Development/Java
Requires:    %{name} = 0:%{version}-%{release}
BuildRequires:    maven2 >= 0:2.0.8
BuildRequires:    bcel
BuildRequires:    xalan-j2
BuildRequires:    xalan-j2-xsltc
BuildRequires:    xerces-j2
BuildRequires:    xml-commons-jaxp-1.3-apis
Requires:    maven2 >= 0:2.0.8
Requires:    bcel
Requires:    xalan-j2
Requires:    xalan-j2-xsltc
Requires:    xerces-j2
Requires:    xml-commons-jaxp-1.3-apis

%description -n mojo-maven2-plugin-xsltc
%{summary}.
%endif

%if %{solaris_include}
%package -n mojo-maven2-solaris
Summary:     Solaris module from %{name}
Group:       Development/Java
Requires:    %{name} = 0:%{version}-%{release}
BuildRequires:    maven2 >= 0:2.0.8
Requires:    maven2 >= 0:2.0.8

%description -n mojo-maven2-solaris
%{summary}.
%endif

%package javadoc
Summary:        Javadoc for %{name}
Group:          Development/Documentation
BuildArch: noarch

%description javadoc
Javadoc for %{name}.

%prep
%setup -q 
gzip -dc %{SOURCE6} | tar xf -
mv mojo-maven2-plugins-sandbox-4/ mojo-sandbox

rm -rf minijar-maven-plugin
gzip -dc %{SOURCE5} | tar xf -
mv minijar-maven-plugin-1.0-alpha-3 minijar-maven-plugin

rm -rf jspc
gzip -dc %{SOURCE9} | tar xf -
mv jspc-2.0-alpha-3 jspc

rm -rf build-helper-maven-plugin
gzip -dc %{SOURCE10} | tar xf -
mv build-helper-maven-plugin-1.5 build-helper-maven-plugin

rm -rf findbugs-maven-plugin
gzip -dc %{SOURCE11} | tar xf -
mv findbugs-maven-plugin-2.3.1 findbugs-maven-plugin

cp %{SOURCE3} maven2-settings.xml
sed -i -e "s|<url>__JPP_URL_PLACEHOLDER__</url>|<url>file://`pwd`/m2_repo/repository</url>|g" maven2-settings.xml
sed -i -e "s|<url>__JAVADIR_PLACEHOLDER__</url>|<url>file://`pwd`/external_repo</url>|g" maven2-settings.xml
sed -i -e "s|<url>__MAVENREPO_DIR_PLACEHOLDER__</url>|<url>file://`pwd`/m2_repo/repository</url>|g" maven2-settings.xml
mkdir external_repo
ln -s %{_javadir} external_repo/JPP

# drop these: no future
rm -rf mojo-archetypes
rm -rf mojo-sandbox/maven-archetypeng
rm -rf mojo-sandbox/jelly-maven-tools
rm -rf mojo-sandbox/rubyscript-maven-tools
rm shitty-maven-plugin/src/main/groovy/org/codehaus/mojo/shitty/Test*.groovy
for g in $(find . -name "*.groovy"); do
    sed -i -e 's|org\.codehaus\.groovy\.maven\.mojo\.GroovyMojo|org.codehaus.gmaven.mojo.GroovyMojo|' $g
done

%patch0 -b .sav0
%patch1 -b .sav1
#%patch2 -b .sav2
%patch3 -b .sav3
%patch4 -b .sav4
%patch5 -b .sav5
%patch6 -b .sav6
%patch7 -b .sav7
%patch8 -b .sav8
%patch9 -b .sav9
%patch10 -b .sav10
%patch11 -b .sav11
%patch12 -b .sav12
%patch13 -b .sav13
%patch14 -b .sav14
%patch15 -b .sav15
%patch16 -b .sav16
%patch17 -b .sav17
%patch18 -b .sav18
%patch19 -b .sav19
%patch20 -b .sav20
%patch21 -b .sav21
%patch22 -b .sav22
%patch23 -b .sav23
%patch24 -b .sav24
%patch25 -b .sav25
%patch26 -b .sav26
%patch27 -b .sav27
%patch28 -b .sav28
%patch29 -b .sav29
%patch30 -b .sav30
%patch31 -b .sav31
%patch32 -b .sav32
%patch33 -b .sav33
%patch34 -b .sav34
%patch35 -b .sav35
%patch36 -b .sav36
%patch37 -b .sav37
%patch38 -b .sav38
%patch39 -b .sav39
%patch40 -b .sav40
%patch41 -b .sav41
%patch42 -b .sav42
%patch43 -b .sav43
%patch44 -b .sav44
%patch45 -b .sav45
%patch46 -b .sav46
%patch47 -b .sav47
%patch48 -b .sav48
%patch49 -b .sav49
#%patch50 -b .sav50
#%patch51 -b .sav51
%patch52 -b .sav52
%patch53 -b .sav53
%patch54 -b .sav54
%patch55 -b .sav55
%patch56 -b .sav56
%patch57 -b .sav57
%patch58 -b .sav58
%patch59 -b .sav59
%patch60 -b .sav60
%patch61 -b .sav61
%patch62 -b .sav62
%patch63 -b .sav63
%patch64 -b .sav64
%patch65 -b .sav65
%patch66 -b .sav66
%patch67 -b .sav67
%patch68 -b .sav68
%patch69 -b .sav69
%patch70 -b .sav70
%patch71 -b .sav71
%patch72 -b .sav72
%patch73 -b .sav73
%patch74 -b .sav74
%patch75 -b .sav75
%patch76 -b .sav76
%patch77 -b .sav77
%patch78 -b .sav78
%patch79 -b .sav79
%patch80 -b .sav80
%patch81 -b .sav81
%patch82 -b .sav82
%patch83 -b .sav83
%patch84 -b .sav84
%patch85 -b .sav85
%patch86 -b .sav86
%patch87 -b .sav87
%patch88 -b .sav88
%patch89 -b .sav89
%patch90 -b .sav90
%patch91 -b .sav91
%patch92 -b .sav92
%patch93 -b .sav93
%patch94 -b .sav94
%patch95 -b .sav95

%if %{RHAT}
%patch101 -b .sav101
%patch102 -b .sav102
%patch103 -b .sav103
%patch104 -b .sav104
%patch105 -b .sav105
%endif
%patch50 -p0

sed -i 's,<module>dashboard-maven-plugin</module>,<!--2.0.8 nocompile<module>dashboard-maven-plugin</module>-->,' mojo-sandbox/pom.xml

sed -i 's,<module>wagon-cifs</module>,<!--tmp nocompile<module>wagon-cifs</module>-->,' maven-extensions/pom.xml

sed -i 's,<module>ibatis-maven-plugin</module>,<!--tmp nocompile<module>ibatis-maven-plugin</module>-->,' mojo-sandbox/pom.xml

sed -i 's,<module>xfire-maven-plugin</module>,<!--tmp nocompile<module>xfire-maven-plugin</module>-->,' mojo-sandbox/pom.xml

%build
export MAVEN_OPTS="-Xmx640m -XX:MaxPermSize=256m"
export MAVEN_REPO_LOCAL=`pwd`/%{repo_dir}
#mkdir -p $MAVEN_REPO_LOCAL/org.apache/
#cp %{SOURCE4} $MAVEN_REPO_LOCAL/org.apache/apache-jar-resource-bundle.jar
mkdir -p $MAVEN_REPO_LOCAL/JPP/maven2/default_poms/
mkdir -p $MAVEN_REPO_LOCAL/JPP/
ln -sf $(build-classpath docbook-xsl-xalan) $MAVEN_REPO_LOCAL/JPP/docbook-xsl-xalan.zip

mkdir -p $MAVEN_REPO_LOCAL/JPP/maven2/poms/
ln -sf $(pwd)/mojo-sandbox/pom.xml \
    $MAVEN_REPO_LOCAL/JPP/maven2/poms/JPP.mojo-mojo-sandbox.pom
mkdir -p $MAVEN_REPO_LOCAL/org/codehaus/mojo/mojo-sandbox/2/
ln -sf $(pwd)/mojo-sandbox/pom.xml \
    $MAVEN_REPO_LOCAL/org/codehaus/mojo/mojo-sandbox/2/mojo-sandbox-2.pom
mkdir -p $MAVEN_REPO_LOCAL/org/codehaus/mojo/mojo-sandbox/2-SNAPSHOT/
ln -sf $(pwd)/mojo-sandbox/pom.xml \
    $MAVEN_REPO_LOCAL/org/codehaus/mojo/mojo-sandbox/2-SNAPSHOT/mojo-sandbox-2-SNAPSHOT.pom
mkdir -p $MAVEN_REPO_LOCAL/org/codehaus/mojo/mojo-sandbox/3/
ln -sf $(pwd)/mojo-sandbox/pom.xml \
    $MAVEN_REPO_LOCAL/org/codehaus/mojo/mojo-sandbox/3/mojo-sandbox-3.pom
mkdir -p $MAVEN_REPO_LOCAL/org/codehaus/mojo/mojo-sandbox/3-SNAPSHOT/
ln -sf $(pwd)/mojo-sandbox/pom.xml \
    $MAVEN_REPO_LOCAL/org/codehaus/mojo/mojo-sandbox/3-SNAPSHOT/mojo-sandbox-3-SNAPSHOT.pom
mkdir -p $MAVEN_REPO_LOCAL/org/codehaus/mojo/mojo-sandbox/4/
ln -sf $(pwd)/mojo-sandbox/pom.xml \
    $MAVEN_REPO_LOCAL/org/codehaus/mojo/mojo-sandbox/4/mojo-sandbox-4.pom
mkdir -p $MAVEN_REPO_LOCAL/org/codehaus/mojo/mojo-sandbox/4-SNAPSHOT/
ln -sf $(pwd)/mojo-sandbox/pom.xml \
    $MAVEN_REPO_LOCAL/org/codehaus/mojo/mojo-sandbox/4-SNAPSHOT/mojo-sandbox-4-SNAPSHOT.pom


mkdir -p $MAVEN_REPO_LOCAL/org/codehaus/mojo/keytool-maven-plugin/1.0/
ln -sf $(pwd)/keytool-maven-plugin/target/keytool-maven-plugin-%{keytool_namedversion}.jar \
     $MAVEN_REPO_LOCAL/org/codehaus/mojo/keytool-maven-plugin/1.0/keytool-maven-plugin-1.0.jar

mkdir -p $MAVEN_REPO_LOCAL/org/codehaus/mojo/jruby-stdlib/1.8.5/
ln -sf $(pwd)/jruby-stdlib/target/jruby-stdlib-%{jruby_stdlib_namedversion}.jar \
    $MAVEN_REPO_LOCAL/org/codehaus/mojo/jruby-stdlib/1.8.5/jruby-stdlib-1.8.5.jar

mkdir -p $MAVEN_REPO_LOCAL/org/codehaus/mojo/sandbox/maven-diagram-maker/prefuse/prefuse/beta-20070723-SNAPSHOT/
ln -sf $(pwd)/mojo-sandbox/maven-diagram-maker/libs/prefuse-beta-20070723-SNAPSHOT.jar \
    $MAVEN_REPO_LOCAL/org/codehaus/mojo/sandbox/maven-diagram-maker/prefuse/prefuse/beta-20070723-SNAPSHOT/prefuse-beta-20070723-SNAPSHOT.jar

mkdir -p $MAVEN_REPO_LOCAL/tanukisoft/wrapper-delta-pack/3.2.3/
cp %{SOURCE7} $MAVEN_REPO_LOCAL/tanukisoft/wrapper-delta-pack/3.2.3/wrapper-delta-pack-3.2.3.tar.gz

mkdir -p $MAVEN_REPO_LOCAL/org/codehaus/mojo/mojo-parent/22/
cp %{SOURCE12} $MAVEN_REPO_LOCAL/org/codehaus/mojo/mojo-parent/22/mojo-parent-22.pom
mkdir -p $MAVEN_REPO_LOCAL/org/codehaus/mojo/mojo-parent/23/
cp %{SOURCE12} $MAVEN_REPO_LOCAL/org/codehaus/mojo/mojo-parent/23/mojo-parent-23.pom

export SETTINGS=$(pwd)/maven2-settings.xml

%if ! %{RHAT}
pushd cobertura-maven-plugin
cp pom.xml pom.xml.save
cp %{SOURCE8} pom.xml
mvn-jpp -Dmaven.compile.target=1.5 -Dmaven.javadoc.source=1.5  -e \
    -s ${SETTINGS} \
    -Dmaven.repo.local=$MAVEN_REPO_LOCAL \
    -Dmaven.test.failure.ignore=true \
    -Dmaven2.jpp.depmap.file=%{SOURCE2} \
    install

mvn-jpp -Dmaven.compile.target=1.5 -Dmaven.javadoc.source=1.5  -e \
    -s ${SETTINGS} \
    -Dmaven.repo.local=$MAVEN_REPO_LOCAL \
    -Dmaven.test.failure.ignore=true \
    -Dmaven2.jpp.depmap.file=%{SOURCE2} \
    javadoc:javadoc

cp pom.xml.save pom.xml
mkdir -p $MAVEN_REPO_LOCAL/JPP/maven2/default_poms/
cp pom.xml $MAVEN_REPO_LOCAL/JPP/maven2/default_poms/JPP.mojo-cobertura-maven-plugin.pom
popd
pushd jruby-stdlib
mvn-jpp -Dmaven.compile.target=1.5 -Dmaven.javadoc.source=1.5  -e \
    -s ${SETTINGS} \
    -Dmaven.repo.local=$MAVEN_REPO_LOCAL \
    -Dmaven.test.failure.ignore=true \
    -Dmaven2.jpp.depmap.file=%{SOURCE2} \
    jar:jar
popd
%endif

mvn-jpp -e \
    -s ${SETTINGS} \
    -Dmaven.repo.local=$MAVEN_REPO_LOCAL \
    -Dmaven.test.failure.ignore=true \
    -Dmaven2.jpp.depmap.file=%{SOURCE2} \
    install:install-file -DgroupId=org.eclipse.jdt.core.compiler -DartifactId=ecj -Dversion=3.3.1 -Dpackaging=jar -Dfile=$(build-classpath ecj)

mvn-jpp -e \
    -s ${SETTINGS} \
    -Dmaven.repo.local=$MAVEN_REPO_LOCAL \
    -Dmaven.test.failure.ignore=true \
    -Dmaven2.jpp.depmap.file=%{SOURCE2} \
    install:install-file -DgroupId=easymock -DartifactId=easymock -Dversion=1.1 -Dpackaging=jar -Dfile=$(build-classpath easymock)

pushd docbook-maven-plugin
mvn-jpp -Dmaven.compile.target=1.5 -Dmaven.javadoc.source=1.5  -e \
    -s ${SETTINGS} \
    -Dmaven.repo.local=$MAVEN_REPO_LOCAL \
    -Dmaven.test.failure.ignore=true \
    -Dmaven2.jpp.depmap.file=%{SOURCE2} \
    install
popd

pushd taglist-maven-plugin
mvn-jpp -Dmaven.compile.target=1.5 -Dmaven.javadoc.source=1.5  -e \
    -s ${SETTINGS} \
    -Dmaven.repo.local=$MAVEN_REPO_LOCAL \
    -Dmaven.test.failure.ignore=true \
    -Dmaven2.jpp.depmap.file=%{SOURCE2} \
    install javadoc:javadoc
popd

mvn-jpp -Dmaven.compile.target=1.5 -Dmaven.javadoc.source=1.5  -e \
    -s ${SETTINGS} \
    -Dmaven.test.skip=true \
    -Dmaven.repo.local=$MAVEN_REPO_LOCAL \
    -Dmaven.test.failure.ignore=true \
    -Dmaven2.jpp.depmap.file=%{SOURCE2} \
    install javadoc:javadoc

%install

# jars and poms
install -d -m 755 $RPM_BUILD_ROOT%{_javadir}/mojo
install -d -m 755 $RPM_BUILD_ROOT%{_datadir}/maven2/poms

install -m 644 pom.xml $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.mojo-mojo.pom
%add_to_maven_depmap org.codehaus.mojo mojo %{version} JPP/mojo mojo
install -m 644 mojo-sandbox/pom.xml $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.mojo-mojo-sandbox.pom
%add_to_maven_depmap org.codehaus.mojo mojo-sandbox %{version} JPP/mojo mojo-sandbox
# explicit: too many variants and versionless symlinks

%if %{antlr_include}
ver=$(echo %{antlr_namedversion} | sed -e 's/-SNAPSHOT//')
nam=antlr-maven-plugin
install -m 644 ${nam}/target/${nam}-%{antlr_namedversion}.jar \
               $RPM_BUILD_ROOT%{_javadir}/mojo/${nam}-${ver}.jar
ln -sf ${nam}-${ver}.jar $RPM_BUILD_ROOT%{_javadir}/mojo/${nam}.jar
install -m 644 ${nam}/pom.xml $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.mojo-${nam}.pom
%add_to_maven_depmap org.codehaus.mojo ${nam} ${ver} JPP/mojo ${nam}
%endif

%if %{appassembler_include}
ver=$(echo %{appassembler_namedversion} | sed -e 's/-SNAPSHOT//')
install -m 644 appassembler/pom.xml $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.mojo-appassembler.pom
%add_to_maven_depmap org.codehaus.mojo appassembler ${ver} JPP/mojo appassembler
nam=appassembler-booter
install -m 644 appassembler/${nam}/target/${nam}-%{appassembler_namedversion}.jar \
               $RPM_BUILD_ROOT%{_javadir}/mojo/${nam}-${ver}.jar
ln -sf ${nam}-${ver}.jar $RPM_BUILD_ROOT%{_javadir}/mojo/${nam}.jar
install -m 644 appassembler/${nam}/pom.xml $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.mojo-${nam}.pom
%add_to_maven_depmap org.codehaus.mojo ${nam} ${ver} JPP/mojo ${nam}
nam=appassembler-maven-plugin
install -m 644 appassembler/${nam}/target/${nam}-%{appassembler_namedversion}.jar \
               $RPM_BUILD_ROOT%{_javadir}/mojo/${nam}-${ver}.jar
ln -sf ${nam}-${ver}.jar $RPM_BUILD_ROOT%{_javadir}/mojo/${nam}.jar
install -m 644 appassembler/${nam}/pom.xml $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.mojo-${nam}.pom
%add_to_maven_depmap org.codehaus.mojo ${nam} ${ver} JPP/mojo ${nam}
nam=appassembler-model
install -m 644 appassembler/${nam}/target/${nam}-%{appassembler_namedversion}.jar \
               $RPM_BUILD_ROOT%{_javadir}/mojo/${nam}-${ver}.jar
ln -sf ${nam}-${ver}.jar $RPM_BUILD_ROOT%{_javadir}/mojo/${nam}.jar
install -m 644 appassembler/${nam}/pom.xml $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.mojo-${nam}.pom
%add_to_maven_depmap org.codehaus.mojo ${nam} ${ver} JPP/mojo ${nam}
%endif

%if %{aspectj_include}
ver=$(echo %{aspectj_namedversion} | sed -e 's/-SNAPSHOT//')
nam=aspectj-maven-plugin
install -m 644 ${nam}/target/${nam}-%{aspectj_namedversion}.jar \
               $RPM_BUILD_ROOT%{_javadir}/mojo/${nam}-${ver}.jar
ln -sf ${nam}-${ver}.jar $RPM_BUILD_ROOT%{_javadir}/mojo/${nam}.jar
install -m 644 ${nam}/pom.xml $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.mojo-${nam}.pom
%add_to_maven_depmap org.codehaus.mojo ${nam} ${ver} JPP/mojo ${nam}
%endif

%if %{axistools_include}
ver=$(echo %{axistools_namedversion} | sed -e 's/-SNAPSHOT//')
nam=axistools-maven-plugin
install -m 644 ${nam}/target/${nam}-%{axistools_namedversion}.jar \
               $RPM_BUILD_ROOT%{_javadir}/mojo/${nam}-${ver}.jar
ln -sf ${nam}-${ver}.jar $RPM_BUILD_ROOT%{_javadir}/mojo/${nam}.jar
install -m 644 ${nam}/pom.xml $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.mojo-${nam}.pom
%add_to_maven_depmap org.codehaus.mojo ${nam} ${ver} JPP/mojo ${nam}
%endif

%if %{build_helper_include}
ver=$(echo %{build_helper_namedversion} | sed -e 's/-SNAPSHOT//')
nam=build-helper-maven-plugin
install -m 644 ${nam}/target/${nam}-%{build_helper_namedversion}.jar \
               $RPM_BUILD_ROOT%{_javadir}/mojo/${nam}-${ver}.jar
ln -sf ${nam}-${ver}.jar $RPM_BUILD_ROOT%{_javadir}/mojo/${nam}.jar
install -m 644 ${nam}/pom.xml $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.mojo-${nam}.pom
%add_to_maven_depmap org.codehaus.mojo ${nam} ${ver} JPP/mojo ${nam}
%endif

%if %{buildnumber_include}
ver=$(echo %{buildnumber_namedversion} | sed -e 's/-SNAPSHOT//')
nam=buildnumber-maven-plugin
install -m 644 ${nam}/target/${nam}-%{buildnumber_namedversion}.jar \
               $RPM_BUILD_ROOT%{_javadir}/mojo/${nam}-${ver}.jar
ln -sf ${nam}-${ver}.jar $RPM_BUILD_ROOT%{_javadir}/mojo/${nam}.jar
install -m 644 ${nam}/pom.xml $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.mojo-${nam}.pom
%add_to_maven_depmap org.codehaus.mojo ${nam} ${ver} JPP/mojo ${nam}
%endif

%if %{castor_include}
ver=$(echo %{castor_namedversion} | sed -e 's/-SNAPSHOT//')
nam=castor-maven-plugin
install -m 644 ${nam}/target/${nam}-%{castor_namedversion}.jar \
               $RPM_BUILD_ROOT%{_javadir}/mojo/${nam}-${ver}.jar
ln -sf ${nam}-${ver}.jar $RPM_BUILD_ROOT%{_javadir}/mojo/${nam}.jar
install -m 644 ${nam}/pom.xml $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.mojo-${nam}.pom
%add_to_maven_depmap org.codehaus.mojo ${nam} ${ver} JPP/mojo ${nam}
%endif

%if %{clirr_include}
ver=$(echo %{clirr_namedversion} | sed -e 's/-SNAPSHOT//')
nam=clirr-maven-plugin
install -m 644 ${nam}/target/${nam}-%{clirr_namedversion}.jar \
               $RPM_BUILD_ROOT%{_javadir}/mojo/${nam}-${ver}.jar
ln -sf ${nam}-${ver}.jar $RPM_BUILD_ROOT%{_javadir}/mojo/${nam}.jar
install -m 644 ${nam}/pom.xml $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.mojo-${nam}.pom
%add_to_maven_depmap org.codehaus.mojo ${nam} ${ver} JPP/mojo ${nam}
%endif

%if %{cobertura_include}
ver=$(echo %{cobertura_namedversion} | sed -e 's/-SNAPSHOT//')
nam=cobertura-maven-plugin
install -m 644 ${nam}/target/${nam}-%{cobertura_namedversion}.jar \
               $RPM_BUILD_ROOT%{_javadir}/mojo/${nam}-${ver}.jar
ln -sf ${nam}-${ver}.jar $RPM_BUILD_ROOT%{_javadir}/mojo/${nam}.jar
install -m 644 ${nam}/pom.xml $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.mojo-${nam}.pom
%add_to_maven_depmap org.codehaus.mojo ${nam} ${ver} JPP/mojo ${nam}
%endif

%if %{commons_attributes_include}
ver=$(echo %{commons_attributes_namedversion} | sed -e 's/-SNAPSHOT//')
nam=commons-attributes-maven-plugin
install -m 644 ${nam}/target/${nam}-%{commons_attributes_namedversion}.jar \
               $RPM_BUILD_ROOT%{_javadir}/mojo/${nam}-${ver}.jar
ln -sf ${nam}-${ver}.jar $RPM_BUILD_ROOT%{_javadir}/mojo/${nam}.jar
install -m 644 ${nam}/pom.xml $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.mojo-${nam}.pom
%add_to_maven_depmap org.codehaus.mojo ${nam} ${ver} JPP/mojo ${nam}
%endif

%if %{dbunit_include}
ver=$(echo %{dbunit_namedversion} | sed -e 's/-SNAPSHOT//')
nam=dbunit-maven-plugin
install -m 644 ${nam}/target/${nam}-%{dbunit_namedversion}.jar \
               $RPM_BUILD_ROOT%{_javadir}/mojo/${nam}-${ver}.jar
ln -sf ${nam}-${ver}.jar $RPM_BUILD_ROOT%{_javadir}/mojo/${nam}.jar
install -m 644 ${nam}/pom.xml $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.mojo-${nam}.pom
%add_to_maven_depmap org.codehaus.mojo ${nam} ${ver} JPP/mojo ${nam}
%endif

%if %{docbook_include}
ver=$(echo %{docbook_namedversion} | sed -e 's/-SNAPSHOT//')
nam=docbook-maven-plugin
install -m 644 ${nam}/target/${nam}-%{docbook_namedversion}.jar \
               $RPM_BUILD_ROOT%{_javadir}/mojo/${nam}-${ver}.jar
ln -sf ${nam}-${ver}.jar $RPM_BUILD_ROOT%{_javadir}/mojo/${nam}.jar
install -m 644 ${nam}/pom.xml $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.mojo-${nam}.pom
%add_to_maven_depmap org.codehaus.mojo ${nam} ${ver} JPP/mojo ${nam}
%endif

%if %{exec_include}
ver=$(echo %{exec_namedversion} | sed -e 's/-SNAPSHOT//')
nam=exec-maven-plugin
install -m 644 ${nam}/target/${nam}-%{exec_namedversion}.jar \
               $RPM_BUILD_ROOT%{_javadir}/mojo/${nam}-${ver}.jar
ln -sf ${nam}-${ver}.jar $RPM_BUILD_ROOT%{_javadir}/mojo/${nam}.jar
install -m 644 ${nam}/pom.xml $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.mojo-${nam}.pom
%add_to_maven_depmap org.codehaus.mojo ${nam} ${ver} JPP/mojo ${nam}
%endif

%if %{findbugs_include}
ver=$(echo %{findbugs_namedversion} | sed -e 's/-SNAPSHOT//')
nam=findbugs-maven-plugin
install -m 644 ${nam}/target/${nam}-%{findbugs_namedversion}.jar \
               $RPM_BUILD_ROOT%{_javadir}/mojo/${nam}-${ver}.jar
ln -sf ${nam}-${ver}.jar $RPM_BUILD_ROOT%{_javadir}/mojo/${nam}.jar
install -m 644 ${nam}/pom.xml $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.mojo-${nam}.pom
%add_to_maven_depmap org.codehaus.mojo ${nam} ${ver} JPP/mojo ${nam}
%endif

%if %{hibernate2_include}
ver=$(echo %{hibernate2_namedversion} | sed -e 's/-SNAPSHOT//')
nam=hibernate2-maven-plugin
install -m 644 ${nam}/target/${nam}-%{hibernate2_namedversion}.jar \
               $RPM_BUILD_ROOT%{_javadir}/mojo/${nam}-${ver}.jar
ln -sf ${nam}-${ver}.jar $RPM_BUILD_ROOT%{_javadir}/mojo/${nam}.jar
install -m 644 ${nam}/pom.xml $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.mojo-${nam}.pom
%add_to_maven_depmap org.codehaus.mojo ${nam} ${ver} JPP/mojo ${nam}
%endif

%if %{hibernate3_include}
ver=$(echo %{hibernate3_namedversion} | sed -e 's/-SNAPSHOT//')
install -m 644 hibernate3/pom.xml $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.mojo-hibernate3.pom
%add_to_maven_depmap org.codehaus.mojo.hibernate3 maven-hibernate3 ${ver} JPP/mojo hibernate3
install -m 644 hibernate3/maven-hibernate3-components/pom.xml $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.mojo-maven-hibernate3-components.pom
%add_to_maven_depmap org.codehaus.mojo.hibernate3 maven-hibernate3-components ${ver} JPP/mojo maven-hibernate3-components

nam=hibernate3-maven-plugin
install -m 644 hibernate3/${nam}/target/${nam}-%{hibernate3_namedversion}.jar \
               $RPM_BUILD_ROOT%{_javadir}/mojo/${nam}-${ver}.jar
ln -sf ${nam}-${ver}.jar $RPM_BUILD_ROOT%{_javadir}/mojo/${nam}.jar
install -m 644 hibernate3/${nam}/pom.xml $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.mojo-${nam}.pom
%add_to_maven_depmap org.codehaus.mojo.hibernate3 ${nam} ${ver} JPP/mojo ${nam}
nam=maven-hibernate3-api
install -m 644 hibernate3/${nam}/target/${nam}-%{hibernate3_namedversion}.jar \
               $RPM_BUILD_ROOT%{_javadir}/mojo/${nam}-${ver}.jar
ln -sf ${nam}-${ver}.jar $RPM_BUILD_ROOT%{_javadir}/mojo/${nam}.jar
install -m 644 hibernate3/${nam}/pom.xml $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.mojo-${nam}.pom
%add_to_maven_depmap org.codehaus.mojo.hibernate3 ${nam} ${ver} JPP/mojo ${nam}
nam=maven-hibernate3-jdk14
install -m 644 hibernate3/maven-hibernate3-components/${nam}/target/${nam}-%{hibernate3_namedversion}.jar \
               $RPM_BUILD_ROOT%{_javadir}/mojo/${nam}-${ver}.jar
ln -sf ${nam}-${ver}.jar $RPM_BUILD_ROOT%{_javadir}/mojo/${nam}.jar
install -m 644 hibernate3/maven-hibernate3-components/${nam}/pom.xml $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.mojo-${nam}.pom
%add_to_maven_depmap org.codehaus.mojo.hibernate3 ${nam} ${ver} JPP/mojo ${nam}
nam=maven-hibernate3-jdk15
install -m 644 hibernate3/maven-hibernate3-components/${nam}/target/${nam}-%{hibernate3_namedversion}.jar \
               $RPM_BUILD_ROOT%{_javadir}/mojo/${nam}-${ver}.jar
ln -sf ${nam}-${ver}.jar $RPM_BUILD_ROOT%{_javadir}/mojo/${nam}.jar
install -m 644 hibernate3/maven-hibernate3-components/${nam}/pom.xml $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.mojo-${nam}.pom
%add_to_maven_depmap org.codehaus.mojo.hibernate3 ${nam} ${ver} JPP/mojo ${nam}
%endif

%if %{idlj_include}
ver=$(echo %{idlj_namedversion} | sed -e 's/-SNAPSHOT//')
nam=idlj-maven-plugin
install -m 644 ${nam}/target/${nam}-%{idlj_namedversion}.jar \
               $RPM_BUILD_ROOT%{_javadir}/mojo/${nam}-${ver}.jar
ln -sf ${nam}-${ver}.jar $RPM_BUILD_ROOT%{_javadir}/mojo/${nam}.jar
install -m 644 ${nam}/pom.xml $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.mojo-${nam}.pom
%add_to_maven_depmap org.codehaus.mojo ${nam} ${ver} JPP/mojo ${nam}
%endif

%if %{jalopy_include}
ver=$(echo %{jalopy_namedversion} | sed -e 's/-SNAPSHOT//')
nam=jalopy-maven-plugin
install -m 644 ${nam}/target/${nam}-%{jalopy_namedversion}.jar \
               $RPM_BUILD_ROOT%{_javadir}/mojo/${nam}-${ver}.jar
ln -sf ${nam}-${ver}.jar $RPM_BUILD_ROOT%{_javadir}/mojo/${nam}.jar
install -m 644 ${nam}/pom.xml $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.mojo-${nam}.pom
%add_to_maven_depmap org.codehaus.mojo ${nam} ${ver} JPP/mojo ${nam}
%endif

%if %{javacc_include}
ver=$(echo %{javacc_namedversion} | sed -e 's/-SNAPSHOT//')
nam=javacc-maven-plugin
install -m 644 ${nam}/target/${nam}-%{javacc_namedversion}.jar \
               $RPM_BUILD_ROOT%{_javadir}/mojo/${nam}-${ver}.jar
ln -sf ${nam}-${ver}.jar $RPM_BUILD_ROOT%{_javadir}/mojo/${nam}.jar
install -m 644 ${nam}/pom.xml $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.mojo-${nam}.pom
%add_to_maven_depmap org.codehaus.mojo ${nam} ${ver} JPP/mojo ${nam}
%endif

%if %{javancss_include}
ver=$(echo %{javancss_namedversion} | sed -e 's/-SNAPSHOT//')
nam=javancss-maven-plugin
install -m 644 ${nam}/target/${nam}-%{javancss_namedversion}.jar \
               $RPM_BUILD_ROOT%{_javadir}/mojo/${nam}-${ver}.jar
ln -sf ${nam}-${ver}.jar $RPM_BUILD_ROOT%{_javadir}/mojo/${nam}.jar
install -m 644 ${nam}/pom.xml $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.mojo-${nam}.pom
%add_to_maven_depmap org.codehaus.mojo ${nam} ${ver} JPP/mojo ${nam}
%endif

%if %{jaxb2_include}
ver=$(echo %{jaxb2_namedversion} | sed -e 's/-SNAPSHOT//')
nam=jaxb2-maven-plugin
install -m 644 ${nam}/target/${nam}-%{jaxb2_namedversion}.jar \
               $RPM_BUILD_ROOT%{_javadir}/mojo/${nam}-${ver}.jar
ln -sf ${nam}-${ver}.jar $RPM_BUILD_ROOT%{_javadir}/mojo/${nam}.jar
install -m 644 ${nam}/pom.xml $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.mojo-${nam}.pom
%add_to_maven_depmap org.codehaus.mojo ${nam} ${ver} JPP/mojo ${nam}
%endif

%if %{jboss_include}
ver=$(echo %{jboss_namedversion} | sed -e 's/-SNAPSHOT//')
nam=jboss-maven-plugin
install -m 644 ${nam}/target/${nam}-%{jboss_namedversion}.jar \
               $RPM_BUILD_ROOT%{_javadir}/mojo/${nam}-${ver}.jar
ln -sf ${nam}-${ver}.jar $RPM_BUILD_ROOT%{_javadir}/mojo/${nam}.jar
install -m 644 ${nam}/pom.xml $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.mojo-${nam}.pom
%add_to_maven_depmap org.codehaus.mojo ${nam} ${ver} JPP/mojo ${nam}
%endif

%if %{jdepend_include}
ver=$(echo %{jdepend_namedversion} | sed -e 's/-SNAPSHOT//')
nam=jdepend-maven-plugin
install -m 644 ${nam}/target/${nam}-%{jdepend_namedversion}.jar \
               $RPM_BUILD_ROOT%{_javadir}/mojo/${nam}-${ver}.jar
ln -sf ${nam}-${ver}.jar $RPM_BUILD_ROOT%{_javadir}/mojo/${nam}.jar
install -m 644 ${nam}/pom.xml $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.mojo-${nam}.pom
%add_to_maven_depmap org.codehaus.mojo ${nam} ${ver} JPP/mojo ${nam}
%endif

%if %{jdiff_include}
ver=$(echo %{jdiff_namedversion} | sed -e 's/-SNAPSHOT//')
nam=jdiff-maven-plugin
install -m 644 ${nam}/target/${nam}-%{jdiff_namedversion}.jar \
               $RPM_BUILD_ROOT%{_javadir}/mojo/${nam}-${ver}.jar
ln -sf ${nam}-${ver}.jar $RPM_BUILD_ROOT%{_javadir}/mojo/${nam}.jar
install -m 644 ${nam}/pom.xml $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.mojo-${nam}.pom
%add_to_maven_depmap org.codehaus.mojo ${nam} ${ver} JPP/mojo ${nam}
%endif

%if %{jpox_include}
ver=$(echo %{jpox_namedversion} | sed -e 's/-SNAPSHOT//')
nam=jpox-maven-plugin
install -m 644 ${nam}/target/${nam}-%{jpox_namedversion}.jar \
               $RPM_BUILD_ROOT%{_javadir}/mojo/${nam}-${ver}.jar
ln -sf ${nam}-${ver}.jar $RPM_BUILD_ROOT%{_javadir}/mojo/${nam}.jar
install -m 644 ${nam}/pom.xml $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.mojo-${nam}.pom
%add_to_maven_depmap org.codehaus.mojo ${nam} ${ver} JPP/mojo ${nam}
%endif

%if %{jruby_include}
ver=$(echo %{jruby_namedversion} | sed -e 's/-SNAPSHOT//')
nam=jruby-maven-plugin
install -m 644 ${nam}/target/${nam}-%{jruby_namedversion}.jar \
               $RPM_BUILD_ROOT%{_javadir}/mojo/${nam}-${ver}.jar
ln -sf ${nam}-${ver}.jar $RPM_BUILD_ROOT%{_javadir}/mojo/${nam}.jar
install -m 644 ${nam}/pom.xml $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.mojo-${nam}.pom
%add_to_maven_depmap org.codehaus.mojo ${nam} ${ver} JPP/mojo ${nam}

ver=$(echo %{jruby_stdlib_namedversion} | sed -e 's/-SNAPSHOT//')
nam=jruby-stdlib
install -m 644 ${nam}/target/${nam}-%{jruby_stdlib_namedversion}.jar \
               $RPM_BUILD_ROOT%{_javadir}/mojo/${nam}-${ver}.jar
ln -sf ${nam}-${ver}.jar $RPM_BUILD_ROOT%{_javadir}/mojo/${nam}.jar
install -m 644 ${nam}/pom.xml $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.mojo-${nam}.pom
%add_to_maven_depmap org.codehaus.mojo ${nam} ${ver} JPP/mojo ${nam}
%endif

%if %{jspc_include}
ver=$(echo %{jspc_namedversion} | sed -e 's/-SNAPSHOT//')
install -m 644 jspc/pom.xml $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.mojo-jspc.pom
%add_to_maven_depmap org.codehaus.mojo.jspc jspc ${ver} JPP/mojo jspc
install -m 644 jspc/jspc-compilers/pom.xml $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.mojo-jspc-compilers.pom
%add_to_maven_depmap org.codehaus.mojo.jspc jspc-compilers ${ver} JPP/mojo jspc-compilers

nam=jspc-compiler-api
install -m 644 jspc/${nam}/target/${nam}-%{jspc_namedversion}.jar \
               $RPM_BUILD_ROOT%{_javadir}/mojo/${nam}-${ver}.jar
ln -sf ${nam}-${ver}.jar $RPM_BUILD_ROOT%{_javadir}/mojo/${nam}.jar
install -m 644 jspc/${nam}/pom.xml $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.mojo-${nam}.pom
%add_to_maven_depmap org.codehaus.mojo.jspc ${nam} ${ver} JPP/mojo ${nam}
nam=jspc-compiler-tomcat5
install -m 644 jspc/jspc-compilers/${nam}/target/${nam}-%{jspc_namedversion}.jar \
               $RPM_BUILD_ROOT%{_javadir}/mojo/${nam}-${ver}.jar
ln -sf ${nam}-${ver}.jar $RPM_BUILD_ROOT%{_javadir}/mojo/${nam}.jar
install -m 644 jspc/jspc-compilers/${nam}/pom.xml $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.mojo-${nam}.pom
%add_to_maven_depmap org.codehaus.mojo.jspc ${nam} ${ver} JPP/mojo ${nam}
nam=jspc-compiler-tomcat6
install -m 644 jspc/jspc-compilers/${nam}/target/${nam}-%{jspc_namedversion}.jar \
               $RPM_BUILD_ROOT%{_javadir}/mojo/${nam}-${ver}.jar
ln -sf ${nam}-${ver}.jar $RPM_BUILD_ROOT%{_javadir}/mojo/${nam}.jar
install -m 644 jspc/jspc-compilers/${nam}/pom.xml $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.mojo-${nam}.pom
%add_to_maven_depmap org.codehaus.mojo.jspc ${nam} ${ver} JPP/mojo ${nam}
nam=jspc-maven-plugin
install -m 644 jspc/${nam}/target/${nam}-%{jspc_namedversion}.jar \
               $RPM_BUILD_ROOT%{_javadir}/mojo/${nam}-${ver}.jar
ln -sf ${nam}-${ver}.jar $RPM_BUILD_ROOT%{_javadir}/mojo/${nam}.jar
install -m 644 jspc/${nam}/pom.xml $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.mojo-${nam}.pom
%add_to_maven_depmap org.codehaus.mojo.jspc ${nam} ${ver} JPP/mojo ${nam}
%endif

%if %{keytool_include}
ver=$(echo %{keytool_namedversion} | sed -e 's/-SNAPSHOT//')
nam=keytool-maven-plugin
install -m 644 ${nam}/target/${nam}-%{keytool_namedversion}.jar \
               $RPM_BUILD_ROOT%{_javadir}/mojo/${nam}-${ver}.jar
ln -sf ${nam}-${ver}.jar $RPM_BUILD_ROOT%{_javadir}/mojo/${nam}.jar
install -m 644 ${nam}/pom.xml $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.mojo-${nam}.pom
%add_to_maven_depmap org.codehaus.mojo ${nam} ${ver} JPP/mojo ${nam}
%endif

%if %{wagon_cifs_include}
ver=$(echo %{wagon_cifs_namedversion} | sed -e 's/-SNAPSHOT//')
install -m 644 maven-extensions/pom.xml $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.mojo-maven-extensions.pom
%add_to_maven_depmap org.codehaus.mojo.maven-extensions ${nam} 1 JPP/mojo maven-extensions
nam=wagon-cifs
install -m 644 maven-extensions/${nam}/target/${nam}-%{wagon_cifs_namedversion}.jar \
               $RPM_BUILD_ROOT%{_javadir}/mojo/${nam}-${ver}.jar
ln -sf ${nam}-${ver}.jar $RPM_BUILD_ROOT%{_javadir}/mojo/${nam}.jar
install -m 644 maven-extensions/${nam}/pom.xml $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.mojo-${nam}.pom
%add_to_maven_depmap org.codehaus.mojo.maven-extensions ${nam} ${ver} JPP/mojo ${nam}
%endif

%if %{mojo_archetypes_include}
ver=$(echo %{mojo_archetypes_namedversion} | sed -e 's/-SNAPSHOT//')
install -m 644 mojo-archetypes/pom.xml $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.mojo-mojo-archetypes.pom
%add_to_maven_depmap org.codehaus.mojo.archetypes mojo-archetypes ${ver} JPP/mojo mojo-archetypes
nam=maven-archetype-simple-jboss-jee
install -m 644 mojo-archetypes/${nam}/target/${nam}-%{mojo_archetypes_namedversion}.jar \
               $RPM_BUILD_ROOT%{_javadir}/mojo/${nam}-${ver}.jar
ln -sf ${nam}-${ver}.jar $RPM_BUILD_ROOT%{_javadir}/mojo/${nam}.jar
install -m 644 mojo-archetypes/${nam}/pom.xml $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.mojo-${nam}.pom
%add_to_maven_depmap org.codehaus.mojo.archetypes ${nam} ${ver} JPP/mojo ${nam}
%endif

%if %{mojo_archetypes_netbeans_include}
ver=$(echo %{mojo_archetypes_namedversion} | sed -e 's/-SNAPSHOT//')
ver=$(echo %{mojo_archetypes_netbeans_namedversion} | sed -e 's/-SNAPSHOT//')
nam=nbm-archetype
install -m 644 mojo-archetypes/${nam}/target/${nam}-%{mojo_archetypes_netbeans_namedversion}.jar \
               $RPM_BUILD_ROOT%{_javadir}/mojo/${nam}-${ver}.jar
ln -sf ${nam}-${ver}.jar $RPM_BUILD_ROOT%{_javadir}/mojo/${nam}.jar
install -m 644 mojo-archetypes/${nam}/pom.xml $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.mojo-${nam}.pom
%add_to_maven_depmap org.codehaus.mojo.archetypes ${nam} ${ver} JPP/mojo ${nam}
nam=netbeans-platform-app-archetype
install -m 644 mojo-archetypes/${nam}/target/${nam}-%{mojo_archetypes_netbeans_namedversion}.jar \
               $RPM_BUILD_ROOT%{_javadir}/mojo/${nam}-${ver}.jar
ln -sf ${nam}-${ver}.jar $RPM_BUILD_ROOT%{_javadir}/mojo/${nam}.jar
install -m 644 mojo-archetypes/${nam}/pom.xml $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.mojo-${nam}.pom
%add_to_maven_depmap org.codehaus.mojo.archetypes ${nam} ${ver} JPP/mojo ${nam}
%endif

%if %{native_include}
ver=$(echo %{native_namedversion} | sed -e 's/-SNAPSHOT//')
install -m 644 maven-native/pom.xml $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.mojo-maven-native.pom
%add_to_maven_depmap org.codehaus.mojo.natives maven-native ${ver} JPP/mojo maven-native
install -m 644 maven-native/maven-native-components/pom.xml $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.mojo-maven-native-components.pom
%add_to_maven_depmap org.codehaus.mojo.natives maven-native-components ${ver} JPP/mojo maven-native-components

nam=maven-native-api
install -m 644 maven-native/${nam}/target/${nam}-%{native_namedversion}.jar \
               $RPM_BUILD_ROOT%{_javadir}/mojo/${nam}-${ver}.jar
ln -sf ${nam}-${ver}.jar $RPM_BUILD_ROOT%{_javadir}/mojo/${nam}.jar
install -m 644 maven-native/${nam}/pom.xml $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.mojo-${nam}.pom
%add_to_maven_depmap org.codehaus.mojo.natives ${nam} ${ver} JPP/mojo ${nam}
nam=maven-native-bcc
install -m 644 maven-native/maven-native-components/${nam}/target/${nam}-%{native_namedversion}.jar \
               $RPM_BUILD_ROOT%{_javadir}/mojo/${nam}-${ver}.jar
ln -sf ${nam}-${ver}.jar $RPM_BUILD_ROOT%{_javadir}/mojo/${nam}.jar
install -m 644 maven-native/maven-native-components/${nam}/pom.xml $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.mojo-${nam}.pom
%add_to_maven_depmap org.codehaus.mojo.natives ${nam} ${ver} JPP/mojo ${nam}
nam=maven-native-generic-c
install -m 644 maven-native/maven-native-components/${nam}/target/${nam}-%{native_namedversion}.jar \
               $RPM_BUILD_ROOT%{_javadir}/mojo/${nam}-${ver}.jar
ln -sf ${nam}-${ver}.jar $RPM_BUILD_ROOT%{_javadir}/mojo/${nam}.jar
install -m 644 maven-native/maven-native-components/${nam}/pom.xml $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.mojo-${nam}.pom
%add_to_maven_depmap org.codehaus.mojo.natives ${nam} ${ver} JPP/mojo ${nam}
nam=maven-native-javah
install -m 644 maven-native/maven-native-components/${nam}/target/${nam}-%{native_namedversion}.jar \
               $RPM_BUILD_ROOT%{_javadir}/mojo/${nam}-${ver}.jar
ln -sf ${nam}-${ver}.jar $RPM_BUILD_ROOT%{_javadir}/mojo/${nam}.jar
install -m 644 maven-native/maven-native-components/${nam}/pom.xml $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.mojo-${nam}.pom
%add_to_maven_depmap org.codehaus.mojo.natives ${nam} ${ver} JPP/mojo ${nam}
nam=maven-native-manager
install -m 644 maven-native/maven-native-components/${nam}/target/${nam}-%{native_namedversion}.jar \
               $RPM_BUILD_ROOT%{_javadir}/mojo/${nam}-${ver}.jar
ln -sf ${nam}-${ver}.jar $RPM_BUILD_ROOT%{_javadir}/mojo/${nam}.jar
install -m 644 maven-native/maven-native-components/${nam}/pom.xml $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.mojo-${nam}.pom
%add_to_maven_depmap org.codehaus.mojo.natives ${nam} ${ver} JPP/mojo ${nam}
nam=maven-native-msvc
install -m 644 maven-native/maven-native-components/${nam}/target/${nam}-%{native_namedversion}.jar \
               $RPM_BUILD_ROOT%{_javadir}/mojo/${nam}-${ver}.jar
ln -sf ${nam}-${ver}.jar $RPM_BUILD_ROOT%{_javadir}/mojo/${nam}.jar
install -m 644 maven-native/maven-native-components/${nam}/pom.xml $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.mojo-${nam}.pom
%add_to_maven_depmap org.codehaus.mojo.natives ${nam} ${ver} JPP/mojo ${nam}
nam=native-maven-plugin
install -m 644 maven-native/${nam}/target/${nam}-%{native_namedversion}.jar \
               $RPM_BUILD_ROOT%{_javadir}/mojo/${nam}-${ver}.jar
ln -sf ${nam}-${ver}.jar $RPM_BUILD_ROOT%{_javadir}/mojo/${nam}.jar
install -m 644 maven-native/${nam}/pom.xml $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.mojo-${nam}.pom
%add_to_maven_depmap org.codehaus.mojo ${nam} ${ver} JPP/mojo ${nam}
%endif

%if %{minijar_include}
ver=$(echo %{minijar_namedversion} | sed -e 's/-SNAPSHOT//')
nam=minijar-maven-plugin
install -m 644 ${nam}/target/${nam}-%{minijar_namedversion}.jar \
               $RPM_BUILD_ROOT%{_javadir}/mojo/${nam}-${ver}.jar
ln -sf ${nam}-${ver}.jar $RPM_BUILD_ROOT%{_javadir}/mojo/${nam}.jar
install -m 644 ${nam}/pom.xml $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.mojo-${nam}.pom
%add_to_maven_depmap org.codehaus.mojo ${nam} ${ver} JPP/mojo ${nam}
%endif

%if %{appbundler_include}
ver=$(echo %{appbundler_namedversion} | sed -e 's/-SNAPSHOT//')
nam=appbundler-maven-plugin
install -m 644 mojo-sandbox/${nam}/target/${nam}-%{appbundler_namedversion}.jar \
               $RPM_BUILD_ROOT%{_javadir}/mojo/${nam}-${ver}.jar
ln -sf ${nam}-${ver}.jar $RPM_BUILD_ROOT%{_javadir}/mojo/${nam}.jar
install -m 644 mojo-sandbox/${nam}/pom.xml $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.mojo-${nam}.pom
%add_to_maven_depmap org.codehaus.mojo ${nam} ${ver} JPP/mojo ${nam}
%endif

%if %{appfuse_include}
ver=$(echo %{appfuse_namedversion} | sed -e 's/-SNAPSHOT//')
nam=appfuse-maven-plugin
install -m 644 mojo-sandbox/${nam}/target/${nam}-%{appfuse_namedversion}.jar \
               $RPM_BUILD_ROOT%{_javadir}/mojo/${nam}-${ver}.jar
ln -sf ${nam}-${ver}.jar $RPM_BUILD_ROOT%{_javadir}/mojo/${nam}.jar
install -m 644 mojo-sandbox/${nam}/pom.xml $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.mojo-${nam}.pom
%add_to_maven_depmap org.codehaus.mojo ${nam} ${ver} JPP/mojo ${nam}
%endif

%if %{apt_include}
ver=$(echo %{apt_namedversion} | sed -e 's/-SNAPSHOT//')
nam=apt-maven-plugin
install -m 644 ${nam}/target/${nam}-%{apt_namedversion}.jar \
               $RPM_BUILD_ROOT%{_javadir}/mojo/${nam}-${ver}.jar
ln -sf ${nam}-${ver}.jar $RPM_BUILD_ROOT%{_javadir}/mojo/${nam}.jar
install -m 644 ${nam}/pom.xml $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.mojo-${nam}.pom
%add_to_maven_depmap org.codehaus.mojo ${nam} ${ver} JPP/mojo ${nam}
%endif

%if %{batik_include}
ver=$(echo %{batik_namedversion} | sed -e 's/-SNAPSHOT//')
nam=batik-maven-plugin
install -m 644 mojo-sandbox/${nam}/target/${nam}-%{batik_namedversion}.jar \
               $RPM_BUILD_ROOT%{_javadir}/mojo/${nam}-${ver}.jar
ln -sf ${nam}-${ver}.jar $RPM_BUILD_ROOT%{_javadir}/mojo/${nam}.jar
install -m 644 mojo-sandbox/${nam}/pom.xml $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.mojo-${nam}.pom
%add_to_maven_depmap org.codehaus.mojo ${nam} ${ver} JPP/mojo ${nam}
%endif

%if %{cis_include}
ver=$(echo %{cis_namedversion} | sed -e 's/-SNAPSHOT//')
nam=cis-maven-plugin
install -m 644 mojo-sandbox/${nam}/target/${nam}-%{cis_namedversion}.jar \
               $RPM_BUILD_ROOT%{_javadir}/mojo/${nam}-${ver}.jar
ln -sf ${nam}-${ver}.jar $RPM_BUILD_ROOT%{_javadir}/mojo/${nam}.jar
install -m 644 mojo-sandbox/${nam}/pom.xml $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.mojo-${nam}.pom
%add_to_maven_depmap org.codehaus.mojo ${nam} ${ver} JPP/mojo ${nam}
%endif

%if %{cruisecontrol_include}
ver=$(echo %{cruisecontrol_namedversion} | sed -e 's/-SNAPSHOT//')
nam=cruisecontrol-maven-plugin
install -m 644 mojo-sandbox/${nam}/target/${nam}-%{cruisecontrol_namedversion}.jar \
               $RPM_BUILD_ROOT%{_javadir}/mojo/${nam}-${ver}.jar
ln -sf ${nam}-${ver}.jar $RPM_BUILD_ROOT%{_javadir}/mojo/${nam}.jar
install -m 644 mojo-sandbox/${nam}/pom.xml $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.mojo-${nam}.pom
%add_to_maven_depmap org.codehaus.mojo ${nam} ${ver} JPP/mojo ${nam}
%endif

%if %{dashboard_include}
ver=$(echo %{dashboard_namedversion} | sed -e 's/-SNAPSHOT//')
nam=dashboard-maven-plugin
install -m 644 mojo-sandbox/${nam}/target/${nam}-%{dashboard_namedversion}.jar \
               $RPM_BUILD_ROOT%{_javadir}/mojo/${nam}-${ver}.jar
ln -sf ${nam}-${ver}.jar $RPM_BUILD_ROOT%{_javadir}/mojo/${nam}.jar
install -m 644 mojo-sandbox/${nam}/pom.xml $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.mojo-${nam}.pom
%add_to_maven_depmap org.codehaus.mojo ${nam} ${ver} JPP/mojo ${nam}
%endif

%if %{deb_include}
ver=$(echo %{deb_namedversion} | sed -e 's/-SNAPSHOT//')
nam=deb-maven-plugin
install -m 644 mojo-sandbox/${nam}/target/${nam}-%{deb_namedversion}.jar \
               $RPM_BUILD_ROOT%{_javadir}/mojo/${nam}-${ver}.jar
ln -sf ${nam}-${ver}.jar $RPM_BUILD_ROOT%{_javadir}/mojo/${nam}.jar
install -m 644 mojo-sandbox/${nam}/pom.xml $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.mojo-${nam}.pom
%add_to_maven_depmap org.codehaus.mojo ${nam} ${ver} JPP/mojo ${nam}
%endif

%if %{delicious_include}
ver=$(echo %{delicious_namedversion} | sed -e 's/-SNAPSHOT//')
nam=delicious-maven-plugin
install -m 644 mojo-sandbox/${nam}/target/${nam}-%{delicious_namedversion}.jar \
               $RPM_BUILD_ROOT%{_javadir}/mojo/${nam}-${ver}.jar
ln -sf ${nam}-${ver}.jar $RPM_BUILD_ROOT%{_javadir}/mojo/${nam}.jar
install -m 644 mojo-sandbox/${nam}/pom.xml $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.mojo-${nam}.pom
%add_to_maven_depmap org.codehaus.mojo ${nam} ${ver} JPP/mojo ${nam}
%endif

%if %{ejbdoclet_include}
ver=$(echo %{ejbdoclet_namedversion} | sed -e 's/-SNAPSHOT//')
nam=ejbdoclet-maven-plugin
install -m 644 mojo-sandbox/${nam}/target/${nam}-%{ejbdoclet_namedversion}.jar \
               $RPM_BUILD_ROOT%{_javadir}/mojo/${nam}-${ver}.jar
ln -sf ${nam}-${ver}.jar $RPM_BUILD_ROOT%{_javadir}/mojo/${nam}.jar
install -m 644 mojo-sandbox/${nam}/pom.xml $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.mojo-${nam}.pom
%add_to_maven_depmap org.codehaus.mojo ${nam} ${ver} JPP/mojo ${nam}
%endif

%if %{emma_include}
ver=$(echo %{emma_namedversion} | sed -e 's/-SNAPSHOT//')
nam=emma-maven-plugin
install -m 644 mojo-sandbox/${nam}/target/${nam}-%{emma_namedversion}.jar \
               $RPM_BUILD_ROOT%{_javadir}/mojo/${nam}-${ver}.jar
ln -sf ${nam}-${ver}.jar $RPM_BUILD_ROOT%{_javadir}/mojo/${nam}.jar
install -m 644 mojo-sandbox/${nam}/pom.xml $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.mojo-${nam}.pom
%add_to_maven_depmap org.codehaus.mojo ${nam} ${ver} JPP/mojo ${nam}
%endif

%if %{fileutils_include}
ver=$(echo %{fileutils_namedversion} | sed -e 's/-SNAPSHOT//')
nam=fileutils-maven-plugin
install -m 644 mojo-sandbox/${nam}/target/${nam}-%{fileutils_namedversion}.jar \
               $RPM_BUILD_ROOT%{_javadir}/mojo/${nam}-${ver}.jar
ln -sf ${nam}-${ver}.jar $RPM_BUILD_ROOT%{_javadir}/mojo/${nam}.jar
install -m 644 mojo-sandbox/${nam}/pom.xml $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.mojo-${nam}.pom
%add_to_maven_depmap org.codehaus.mojo ${nam} ${ver} JPP/mojo ${nam}
%endif

%if %{fit_include}
ver=$(echo %{fit_namedversion} | sed -e 's/-SNAPSHOT//')
nam=fit-maven-plugin
install -m 644 mojo-sandbox/${nam}/target/${nam}-%{fit_namedversion}.jar \
               $RPM_BUILD_ROOT%{_javadir}/mojo/${nam}-${ver}.jar
ln -sf ${nam}-${ver}.jar $RPM_BUILD_ROOT%{_javadir}/mojo/${nam}.jar
install -m 644 mojo-sandbox/${nam}/pom.xml $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.mojo-${nam}.pom
%add_to_maven_depmap org.codehaus.mojo ${nam} ${ver} JPP/mojo ${nam}
%endif

%if %{freemarker_include}
ver=$(echo %{freemarker_namedversion} | sed -e 's/-SNAPSHOT//')
nam=freemarker-maven-plugin
install -m 644 mojo-sandbox/${nam}/target/${nam}-%{freemarker_namedversion}.jar \
               $RPM_BUILD_ROOT%{_javadir}/mojo/${nam}-${ver}.jar
ln -sf ${nam}-${ver}.jar $RPM_BUILD_ROOT%{_javadir}/mojo/${nam}.jar
install -m 644 mojo-sandbox/${nam}/pom.xml $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.mojo-${nam}.pom
%add_to_maven_depmap org.codehaus.mojo ${nam} ${ver} JPP/mojo ${nam}
%endif

%if %{ganalytics_include}
ver=$(echo %{ganalytics_namedversion} | sed -e 's/-SNAPSHOT//')
nam=ganalytics-maven-plugin
install -m 644 mojo-sandbox/ganalytics-maven-mojo/target/${nam}-%{ganalytics_namedversion}.jar \
               $RPM_BUILD_ROOT%{_javadir}/mojo/${nam}-${ver}.jar
ln -sf ${nam}-${ver}.jar $RPM_BUILD_ROOT%{_javadir}/mojo/${nam}.jar
install -m 644 mojo-sandbox/ganalytics-maven-mojo/pom.xml $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.mojo-${nam}.pom
%add_to_maven_depmap org.codehaus.mojo ${nam} ${ver} JPP/mojo ${nam}
%endif

%if %{graphing_include}
ver=$(echo %{graphing_namedversion} | sed -e 's/-SNAPSHOT//')
nam=graphing-maven-plugin
install -m 644 mojo-sandbox/${nam}/target/${nam}-%{graphing_namedversion}.jar \
               $RPM_BUILD_ROOT%{_javadir}/mojo/${nam}-${ver}.jar
ln -sf ${nam}-${ver}.jar $RPM_BUILD_ROOT%{_javadir}/mojo/${nam}.jar
install -m 644 mojo-sandbox/${nam}/pom.xml $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.mojo-${nam}.pom
%add_to_maven_depmap org.codehaus.mojo ${nam} ${ver} JPP/mojo ${nam}
%endif

%if %{hibernatedoclet_include}
ver=$(echo %{hibernatedoclet_namedversion} | sed -e 's/-SNAPSHOT//')
nam=hibernatedoclet-maven-plugin
install -m 644 mojo-sandbox/${nam}/target/${nam}-%{hibernatedoclet_namedversion}.jar \
               $RPM_BUILD_ROOT%{_javadir}/mojo/${nam}-${ver}.jar
ln -sf ${nam}-${ver}.jar $RPM_BUILD_ROOT%{_javadir}/mojo/${nam}.jar
install -m 644 mojo-sandbox/${nam}/pom.xml $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.mojo-${nam}.pom
%add_to_maven_depmap org.codehaus.mojo ${nam} ${ver} JPP/mojo ${nam}
%endif

%if %{ibatis_include}
ver=$(echo %{ibatis_namedversion} | sed -e 's/-SNAPSHOT//')
nam=ibatis-maven-plugin
install -m 644 mojo-sandbox/${nam}/target/${nam}-%{ibatis_namedversion}.jar \
               $RPM_BUILD_ROOT%{_javadir}/mojo/${nam}-${ver}.jar
ln -sf ${nam}-${ver}.jar $RPM_BUILD_ROOT%{_javadir}/mojo/${nam}.jar
install -m 644 mojo-sandbox/${nam}/pom.xml $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.mojo-${nam}.pom
%add_to_maven_depmap org.codehaus.mojo ${nam} ${ver} JPP/mojo ${nam}
%endif

%if %{j2me_include}
ver=$(echo %{j2me_namedversion} | sed -e 's/-SNAPSHOT//')
nam=j2me-maven-plugin
install -m 644 mojo-sandbox/${nam}/target/${nam}-%{j2me_namedversion}.jar \
               $RPM_BUILD_ROOT%{_javadir}/mojo/${nam}-${ver}.jar
ln -sf ${nam}-${ver}.jar $RPM_BUILD_ROOT%{_javadir}/mojo/${nam}.jar
install -m 644 mojo-sandbox/${nam}/pom.xml $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.mojo-${nam}.pom
%add_to_maven_depmap org.codehaus.mojo ${nam} ${ver} JPP/mojo ${nam}
%endif

%if %{jardiff_include}
ver=$(echo %{jardiff_namedversion} | sed -e 's/-SNAPSHOT//')
nam=jardiff-maven-plugin
install -m 644 mojo-sandbox/${nam}/target/${nam}-%{jardiff_namedversion}.jar \
               $RPM_BUILD_ROOT%{_javadir}/mojo/${nam}-${ver}.jar
ln -sf ${nam}-${ver}.jar $RPM_BUILD_ROOT%{_javadir}/mojo/${nam}.jar
install -m 644 mojo-sandbox/${nam}/pom.xml $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.mojo-${nam}.pom
%add_to_maven_depmap org.codehaus.mojo ${nam} ${ver} JPP/mojo ${nam}
%endif

%if %{jasperreports_include}
ver=$(echo %{jasperreports_namedversion} | sed -e 's/-SNAPSHOT//')
nam=jasperreports-maven-plugin
install -m 644 ${nam}/target/${nam}-%{jasperreports_namedversion}.jar \
               $RPM_BUILD_ROOT%{_javadir}/mojo/${nam}-${ver}.jar
ln -sf ${nam}-${ver}.jar $RPM_BUILD_ROOT%{_javadir}/mojo/${nam}.jar
install -m 644 ${nam}/pom.xml $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.mojo-${nam}.pom
%add_to_maven_depmap org.codehaus.mojo ${nam} ${ver} JPP/mojo ${nam}
%endif

%if %{jaxws_include}
ver=$(echo %{jaxws_namedversion} | sed -e 's/-SNAPSHOT//')
nam=jaxws-maven-plugin
install -m 644 mojo-sandbox/${nam}/target/${nam}-%{jaxws_namedversion}.jar \
               $RPM_BUILD_ROOT%{_javadir}/mojo/${nam}-${ver}.jar
ln -sf ${nam}-${ver}.jar $RPM_BUILD_ROOT%{_javadir}/mojo/${nam}.jar
install -m 644 mojo-sandbox/${nam}/pom.xml $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.mojo-${nam}.pom
%add_to_maven_depmap org.codehaus.mojo ${nam} ${ver} JPP/mojo ${nam}
%endif

%if %{jboss_packaging_include}
ver=$(echo %{jboss_packaging_namedversion} | sed -e 's/-SNAPSHOT//')
nam=jboss-packaging-maven-plugin
install -m 644 ${nam}/target/${nam}-%{jboss_packaging_namedversion}.jar \
               $RPM_BUILD_ROOT%{_javadir}/mojo/${nam}-${ver}.jar
ln -sf ${nam}-${ver}.jar $RPM_BUILD_ROOT%{_javadir}/mojo/${nam}.jar
install -m 644 ${nam}/pom.xml $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.mojo-${nam}.pom
%add_to_maven_depmap org.codehaus.mojo ${nam} ${ver} JPP/mojo ${nam}
%endif

%if %{jellyapi_include}
ver=$(echo %{jellyapi_namedversion} | sed -e 's/-SNAPSHOT//')
nam=jellyapi-maven-plugin
install -m 644 mojo-sandbox/jelly-maven-tools/${nam}/target/${nam}-%{jellyapi_namedversion}.jar \
               $RPM_BUILD_ROOT%{_javadir}/mojo/${nam}-${ver}.jar
ln -sf ${nam}-${ver}.jar $RPM_BUILD_ROOT%{_javadir}/mojo/${nam}.jar
install -m 644 mojo-sandbox/jelly-maven-tools/${nam}/pom.xml $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.mojo-${nam}.pom
%add_to_maven_depmap org.codehaus.mojo ${nam} ${ver} JPP/mojo ${nam}
%endif

%if %{jellymojo_include}
ver=$(echo %{jellymojo_namedversion} | sed -e 's/-SNAPSHOT//')
nam=jellymojo-maven-archetype
install -m 644 mojo-sandbox/jelly-maven-tools/${nam}/target/${nam}-%{jellymojo_namedversion}.jar \
               $RPM_BUILD_ROOT%{_javadir}/mojo/${nam}-${ver}.jar
ln -sf ${nam}-${ver}.jar $RPM_BUILD_ROOT%{_javadir}/mojo/${nam}.jar
install -m 644 mojo-sandbox/jelly-maven-tools/${nam}/pom.xml $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.mojo-${nam}.pom
%add_to_maven_depmap org.codehaus.mojo ${nam} ${ver} JPP/mojo ${nam}
%endif

%if %{jettybin_include}
ver=$(echo %{jettybin_namedversion} | sed -e 's/-SNAPSHOT//')
nam=jettybin-maven-plugin
install -m 644 mojo-sandbox/${nam}/target/${nam}-%{jettybin_namedversion}.jar \
               $RPM_BUILD_ROOT%{_javadir}/mojo/${nam}-${ver}.jar
ln -sf ${nam}-${ver}.jar $RPM_BUILD_ROOT%{_javadir}/mojo/${nam}.jar
install -m 644 mojo-sandbox/${nam}/pom.xml $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.mojo-${nam}.pom
%add_to_maven_depmap org.codehaus.mojo ${nam} ${ver} JPP/mojo ${nam}
%endif

%if %{jetty_include}
ver=$(echo %{jetty_namedversion} | sed -e 's/-SNAPSHOT//')
nam=jetty-maven-plugin
install -m 644 mojo-sandbox/${nam}/target/${nam}-%{jetty_namedversion}.jar \
               $RPM_BUILD_ROOT%{_javadir}/mojo/${nam}-${ver}.jar
ln -sf ${nam}-${ver}.jar $RPM_BUILD_ROOT%{_javadir}/mojo/${nam}.jar
install -m 644 mojo-sandbox/${nam}/pom.xml $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.mojo-${nam}.pom
%add_to_maven_depmap org.codehaus.mojo ${nam} ${ver} JPP/mojo ${nam}
%endif

%if %{l10n_include}
ver=$(echo %{l10n_namedversion} | sed -e 's/-SNAPSHOT//')
nam=l10n-maven-plugin
install -m 644 ${nam}/target/${nam}-%{l10n_namedversion}.jar \
               $RPM_BUILD_ROOT%{_javadir}/mojo/${nam}-${ver}.jar
ln -sf ${nam}-${ver}.jar $RPM_BUILD_ROOT%{_javadir}/mojo/${nam}.jar
install -m 644 ${nam}/pom.xml $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.mojo-${nam}.pom
%add_to_maven_depmap org.codehaus.mojo ${nam} ${ver} JPP/mojo ${nam}
%endif

%if %{mant_include}
ver=$(echo %{mant_namedversion} | sed -e 's/-SNAPSHOT//')
nam=mant-maven-plugin
install -m 644 mojo-sandbox/${nam}/target/${nam}-%{mant_namedversion}.jar \
               $RPM_BUILD_ROOT%{_javadir}/mojo/${nam}-${ver}.jar
ln -sf ${nam}-${ver}.jar $RPM_BUILD_ROOT%{_javadir}/mojo/${nam}.jar
install -m 644 mojo-sandbox/${nam}/pom.xml $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.mojo-${nam}.pom
%add_to_maven_depmap org.codehaus.mojo ${nam} ${ver} JPP/mojo ${nam}
%endif

%if %{mojo_was_plugin_anttasks_include}
ver=$(echo %{mojo_was_plugin_anttasks_namedversion} | sed -e 's/-SNAPSHOT//')
install -m 644 mojo-sandbox/mojo-was/pom.xml $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.mojo-mojo-was.pom
%add_to_maven_depmap org.codehaus.mojo mojo-was ${ver} JPP/mojo mojo-was

nam=was-plugin-anttasks
install -m 644 mojo-sandbox/mojo-was/${nam}/target/${nam}-%{mojo_was_plugin_anttasks_namedversion}.jar \
               $RPM_BUILD_ROOT%{_javadir}/mojo/${nam}-${ver}.jar
ln -sf ${nam}-${ver}.jar $RPM_BUILD_ROOT%{_javadir}/mojo/${nam}.jar
install -m 644 mojo-sandbox/mojo-was/${nam}/pom.xml $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.mojo-${nam}.pom
%add_to_maven_depmap org.codehaus.mojo ${nam} ${ver} JPP/mojo ${nam}
%endif

%if %{buildinfo_include}
ver=$(echo %{buildinfo_namedversion} | sed -e 's/-SNAPSHOT//')
nam=maven-buildinfo-plugin
install -m 644 mojo-sandbox/${nam}/target/${nam}-%{buildinfo_namedversion}.jar \
               $RPM_BUILD_ROOT%{_javadir}/mojo/${nam}-${ver}.jar
ln -sf ${nam}-${ver}.jar $RPM_BUILD_ROOT%{_javadir}/mojo/${nam}.jar
install -m 644 mojo-sandbox/${nam}/pom.xml $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.mojo-${nam}.pom
%add_to_maven_depmap org.codehaus.mojo ${nam} ${ver} JPP/mojo ${nam}
%endif

%if %{changes_include}
ver=$(echo %{changes_namedversion} | sed -e 's/-SNAPSHOT//')
nam=maven-changes
install -m 644 mojo-sandbox/${nam}/target/${nam}-%{changes_namedversion}.jar \
               $RPM_BUILD_ROOT%{_javadir}/mojo/${nam}-${ver}.jar
ln -sf ${nam}-${ver}.jar $RPM_BUILD_ROOT%{_javadir}/mojo/${nam}.jar
install -m 644 mojo-sandbox/${nam}/pom.xml $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.mojo-${nam}.pom
%add_to_maven_depmap org.apache.maven ${nam} ${ver} JPP/mojo ${nam}
%endif

%if %{diagram_maker_include}
ver=$(echo %{diagram_maker_namedversion} | sed -e 's/-SNAPSHOT//')
install -m 644 mojo-sandbox/maven-diagram-maker/pom.xml $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.mojo-maven-diagram-maker.pom
%add_to_maven_depmap org.apache.maven.diagrams diagrams ${ver} JPP/mojo maven-diagram-maker
install -m 644 mojo-sandbox/maven-diagram-maker/connectors/pom.xml $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.mojo-diagram-maker-connectors.pom
%add_to_maven_depmap org.apache.maven.diagrams connectors ${ver} JPP/mojo diagram-maker-connectors

nam=connector-api
install -m 644 mojo-sandbox/maven-diagram-maker/${nam}/target/${nam}-%{diagram_maker_namedversion}.jar \
               $RPM_BUILD_ROOT%{_javadir}/mojo/${nam}-${ver}.jar
ln -sf ${nam}-${ver}.jar $RPM_BUILD_ROOT%{_javadir}/mojo/${nam}.jar
install -m 644 mojo-sandbox/maven-diagram-maker/${nam}/pom.xml $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.mojo-${nam}.pom
%add_to_maven_depmap org.apache.maven.diagrams ${nam} ${ver} JPP/mojo ${nam}
nam=connector-classes
install -m 644 mojo-sandbox/maven-diagram-maker/connectors/${nam}/target/${nam}-%{diagram_maker_namedversion}.jar \
               $RPM_BUILD_ROOT%{_javadir}/mojo/${nam}-${ver}.jar
ln -sf ${nam}-${ver}.jar $RPM_BUILD_ROOT%{_javadir}/mojo/${nam}.jar
install -m 644 mojo-sandbox/maven-diagram-maker/connectors/${nam}/pom.xml $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.mojo-${nam}.pom
%add_to_maven_depmap org.apache.maven.diagrams.connectors ${nam} ${ver} JPP/mojo ${nam}
nam=connector-dependencies
install -m 644 mojo-sandbox/maven-diagram-maker/connectors/${nam}/target/${nam}-%{diagram_maker_namedversion}.jar \
               $RPM_BUILD_ROOT%{_javadir}/mojo/${nam}-${ver}.jar
ln -sf ${nam}-${ver}.jar $RPM_BUILD_ROOT%{_javadir}/mojo/${nam}.jar
install -m 644 mojo-sandbox/maven-diagram-maker/connectors/${nam}/pom.xml $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.mojo-${nam}.pom
%add_to_maven_depmap org.apache.maven.diagrams.connectors ${nam} ${ver} JPP/mojo ${nam}
nam=diagrams-gui
install -m 644 mojo-sandbox/maven-diagram-maker/${nam}/target/${nam}-%{diagram_maker_namedversion}.jar \
               $RPM_BUILD_ROOT%{_javadir}/mojo/${nam}-${ver}.jar
ln -sf ${nam}-${ver}.jar $RPM_BUILD_ROOT%{_javadir}/mojo/${nam}.jar
install -m 644 mojo-sandbox/maven-diagram-maker/${nam}/pom.xml $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.mojo-${nam}.pom
%add_to_maven_depmap org.apache.maven.diagrams ${nam} ${ver} JPP/mojo ${nam}
nam=graph-api
install -m 644 mojo-sandbox/maven-diagram-maker/${nam}/target/${nam}-%{diagram_maker_namedversion}.jar \
               $RPM_BUILD_ROOT%{_javadir}/mojo/${nam}-${ver}.jar
ln -sf ${nam}-${ver}.jar $RPM_BUILD_ROOT%{_javadir}/mojo/${nam}.jar
install -m 644 mojo-sandbox/maven-diagram-maker/${nam}/pom.xml $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.mojo-${nam}.pom
%add_to_maven_depmap org.apache.maven.diagrams ${nam} ${ver} JPP/mojo ${nam}
ver=$(echo %{diagrams_namedversion} | sed -e 's/-SNAPSHOT//')
nam=maven-diagrams-plugin
install -m 644 mojo-sandbox/maven-diagram-maker/${nam}/target/${nam}-%{diagrams_namedversion}.jar \
               $RPM_BUILD_ROOT%{_javadir}/mojo/${nam}-${ver}.jar
ln -sf ${nam}-${ver}.jar $RPM_BUILD_ROOT%{_javadir}/mojo/${nam}.jar
install -m 644 mojo-sandbox/maven-diagram-maker/${nam}/pom.xml $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.mojo-${nam}.pom
%add_to_maven_depmap org.apache.maven.plugins ${nam} ${ver} JPP/mojo ${nam}
%endif

%if %{hsqldb_include}
ver=$(echo %{hsqldb_namedversion} | sed -e 's/-SNAPSHOT//')
nam=maven-hsqldb-plugin
install -m 644 mojo-sandbox/${nam}/target/${nam}-%{hsqldb_namedversion}.jar \
               $RPM_BUILD_ROOT%{_javadir}/mojo/${nam}-${ver}.jar
ln -sf ${nam}-${ver}.jar $RPM_BUILD_ROOT%{_javadir}/mojo/${nam}.jar
install -m 644 mojo-sandbox/${nam}/pom.xml $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.mojo-${nam}.pom
%add_to_maven_depmap org.codehaus.mojo ${nam} ${ver} JPP/mojo ${nam}
%endif

%if %{springbeandoc_include}
ver=$(echo %{springbeandoc_namedversion} | sed -e 's/-SNAPSHOT//')
nam=maven-springbeandoc-plugin
install -m 644 mojo-sandbox/${nam}/target/${nam}-%{springbeandoc_namedversion}.jar \
               $RPM_BUILD_ROOT%{_javadir}/mojo/${nam}-${ver}.jar
ln -sf ${nam}-${ver}.jar $RPM_BUILD_ROOT%{_javadir}/mojo/${nam}.jar
install -m 644 mojo-sandbox/${nam}/pom.xml $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.mojo-${nam}.pom
%add_to_maven_depmap org.codehaus.mojo ${nam} ${ver} JPP/mojo ${nam}
%endif

%if %{testing_simple_include}
ver=$(echo %{testing_simple_namedversion} | sed -e 's/-SNAPSHOT//')
nam=maven-simple-plugin
install -m 644 mojo-sandbox/maven-plugin-testing/${nam}/target/${nam}-%{testing_simple_namedversion}.jar \
               $RPM_BUILD_ROOT%{_javadir}/mojo/${nam}-${ver}.jar
ln -sf ${nam}-${ver}.jar $RPM_BUILD_ROOT%{_javadir}/mojo/${nam}.jar
install -m 644 mojo-sandbox/maven-plugin-testing/${nam}/pom.xml $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.mojo-${nam}.pom
%add_to_maven_depmap org.apache.maven.plugin.simple ${nam} ${ver} JPP/mojo ${nam}
%endif

%if %{pomtools_include}
ver=$(echo %{pomtools_namedversion} | sed -e 's/-SNAPSHOT//')
nam=pomtools-maven-plugin
install -m 644 mojo-sandbox/${nam}/target/${nam}-%{pomtools_namedversion}.jar \
               $RPM_BUILD_ROOT%{_javadir}/mojo/${nam}-${ver}.jar
ln -sf ${nam}-${ver}.jar $RPM_BUILD_ROOT%{_javadir}/mojo/${nam}.jar
install -m 644 mojo-sandbox/${nam}/pom.xml $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.mojo-${nam}.pom
%add_to_maven_depmap org.codehaus.mojo ${nam} ${ver} JPP/mojo ${nam}
%endif

%if %{properties_include}
ver=$(echo %{properties_namedversion} | sed -e 's/-SNAPSHOT//')
nam=properties-maven-plugin
install -m 644 mojo-sandbox/${nam}/target/${nam}-%{properties_namedversion}.jar \
               $RPM_BUILD_ROOT%{_javadir}/mojo/${nam}-${ver}.jar
ln -sf ${nam}-${ver}.jar $RPM_BUILD_ROOT%{_javadir}/mojo/${nam}.jar
install -m 644 mojo-sandbox/${nam}/pom.xml $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.mojo-${nam}.pom
%add_to_maven_depmap org.codehaus.mojo ${nam} ${ver} JPP/mojo ${nam}
%endif

%if %{push_include}
ver=$(echo %{push_namedversion} | sed -e 's/-SNAPSHOT//')
nam=push-maven-plugin
install -m 644 mojo-sandbox/${nam}/target/${nam}-%{push_namedversion}.jar \
               $RPM_BUILD_ROOT%{_javadir}/mojo/${nam}-${ver}.jar
ln -sf ${nam}-${ver}.jar $RPM_BUILD_ROOT%{_javadir}/mojo/${nam}.jar
install -m 644 mojo-sandbox/${nam}/pom.xml $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.mojo-${nam}.pom
%add_to_maven_depmap org.codehaus.mojo ${nam} ${ver} JPP/mojo ${nam}
%endif

%if %{retroweaver_include}
ver=$(echo %{retroweaver_namedversion} | sed -e 's/-SNAPSHOT//')
nam=retroweaver-maven-plugin
install -m 644 mojo-sandbox/${nam}/target/${nam}-%{retroweaver_namedversion}.jar \
               $RPM_BUILD_ROOT%{_javadir}/mojo/${nam}-${ver}.jar
ln -sf ${nam}-${ver}.jar $RPM_BUILD_ROOT%{_javadir}/mojo/${nam}.jar
install -m 644 mojo-sandbox/${nam}/pom.xml $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.mojo-${nam}.pom
%add_to_maven_depmap org.codehaus.mojo ${nam} ${ver} JPP/mojo ${nam}
%endif

%if %{rat_include}
ver=$(echo %{rat_namedversion} | sed -e 's/-SNAPSHOT//')
nam=rat-maven-plugin
install -m 644 ${nam}/target/${nam}-%{rat_namedversion}.jar \
               $RPM_BUILD_ROOT%{_javadir}/mojo/${nam}-${ver}.jar
ln -sf ${nam}-${ver}.jar $RPM_BUILD_ROOT%{_javadir}/mojo/${nam}.jar
install -m 644 ${nam}/pom.xml $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.mojo-${nam}.pom
%add_to_maven_depmap org.codehaus.mojo ${nam} ${ver} JPP/mojo ${nam}
%endif

%if %{rmic_include}
ver=$(echo %{rmic_namedversion} | sed -e 's/-SNAPSHOT//')
nam=rmic-maven-plugin
install -m 644 ${nam}/target/${nam}-%{rmic_namedversion}.jar \
               $RPM_BUILD_ROOT%{_javadir}/mojo/${nam}-${ver}.jar
ln -sf ${nam}-${ver}.jar $RPM_BUILD_ROOT%{_javadir}/mojo/${nam}.jar
install -m 644 ${nam}/pom.xml $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.mojo-${nam}.pom
%add_to_maven_depmap org.codehaus.mojo ${nam} ${ver} JPP/mojo ${nam}
%endif

%if %{rpm_include}
ver=$(echo %{rpm_namedversion} | sed -e 's/-SNAPSHOT//')
nam=rpm-maven-plugin
install -m 644 ${nam}/target/${nam}-%{rpm_namedversion}.jar \
               $RPM_BUILD_ROOT%{_javadir}/mojo/${nam}-${ver}.jar
ln -sf ${nam}-${ver}.jar $RPM_BUILD_ROOT%{_javadir}/mojo/${nam}.jar
install -m 644 ${nam}/pom.xml $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.mojo-${nam}.pom
%add_to_maven_depmap org.codehaus.mojo ${nam} ${ver} JPP/mojo ${nam}
%endif

%if %{rubyscript_include}
install -m 644 mojo-sandbox/rubyscript-maven-tools/pom.xml $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.mojo-rubyscript-maven-tools.pom
%add_to_maven_depmap org.codehaus.mojo rubyscript-maven-tools 2 JPP/mojo rubyscript-maven-tools
install -m 644 mojo-sandbox/rubyscript-maven-tools/rubyscript-parent-maven-plugin/pom.xml $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.mojo-rubyscript-parent-maven-plugin.pom
%add_to_maven_depmap org.codehaus.mojo rubyscript-parent-maven-plugin 1 JPP/mojo rubyscript-parent-maven-plugin
ver=$(echo %{rubyscript_namedversion} | sed -e 's/-SNAPSHOT//')
nam=archetype-maven-rubyscript
install -m 644 mojo-sandbox/rubyscript-maven-tools/${nam}/target/${nam}-%{rubyscript_namedversion}.jar \
               $RPM_BUILD_ROOT%{_javadir}/mojo/${nam}-${ver}.jar
ln -sf ${nam}-${ver}.jar $RPM_BUILD_ROOT%{_javadir}/mojo/${nam}.jar
install -m 644 mojo-sandbox/rubyscript-maven-tools/${nam}/pom.xml $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.mojo-${nam}.pom
%add_to_maven_depmap org.codehaus.mojo ${nam} ${ver} JPP/mojo ${nam}
%endif

%if %{runtime_builder_include}
ver=$(echo %{runtime_builder_namedversion} | sed -e 's/-SNAPSHOT//')
nam=runtime-builder-maven-plugin
install -m 644 mojo-sandbox/runtime-maven-plugin/target/${nam}-%{runtime_builder_namedversion}.jar \
               $RPM_BUILD_ROOT%{_javadir}/mojo/${nam}-${ver}.jar
ln -sf ${nam}-${ver}.jar $RPM_BUILD_ROOT%{_javadir}/mojo/${nam}.jar
install -m 644 mojo-sandbox/runtime-maven-plugin/pom.xml $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.mojo-${nam}.pom
%add_to_maven_depmap org.codehaus.mojo ${nam} ${ver} JPP/mojo ${nam}
%endif

%if %{runtime_builder_include}
ver=$(echo %{script_namedversion} | sed -e 's/-SNAPSHOT//')
nam=script-maven-plugin
install -m 644 mojo-sandbox/${nam}/target/${nam}-%{script_namedversion}.jar \
               $RPM_BUILD_ROOT%{_javadir}/mojo/${nam}-${ver}.jar
ln -sf ${nam}-${ver}.jar $RPM_BUILD_ROOT%{_javadir}/mojo/${nam}.jar
install -m 644 mojo-sandbox/${nam}/pom.xml $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.mojo-${nam}.pom
%add_to_maven_depmap org.codehaus.mojo ${nam} ${ver} JPP/mojo ${nam}
%endif

%if %{shade_include}
ver=$(echo %{shade_namedversion} | sed -e 's/-SNAPSHOT//')
nam=shade-maven-plugin
install -m 644 mojo-sandbox/${nam}/target/${nam}-%{shade_namedversion}.jar \
               $RPM_BUILD_ROOT%{_javadir}/mojo/${nam}-${ver}.jar
ln -sf ${nam}-${ver}.jar $RPM_BUILD_ROOT%{_javadir}/mojo/${nam}.jar
install -m 644 mojo-sandbox/${nam}/pom.xml $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.mojo-${nam}.pom
%add_to_maven_depmap org.codehaus.mojo ${nam} ${ver} JPP/mojo ${nam}
%endif

%if %{shell_include}
ver=$(echo %{shell_namedversion} | sed -e 's/-SNAPSHOT//')
nam=shell-maven-plugin
install -m 644 mojo-sandbox/${nam}/target/${nam}-%{shell_namedversion}.jar \
               $RPM_BUILD_ROOT%{_javadir}/mojo/${nam}-${ver}.jar
ln -sf ${nam}-${ver}.jar $RPM_BUILD_ROOT%{_javadir}/mojo/${nam}.jar
install -m 644 mojo-sandbox/${nam}/pom.xml $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.mojo-${nam}.pom
%add_to_maven_depmap org.codehaus.mojo ${nam} ${ver} JPP/mojo ${nam}
%endif

%if %{springdoclet_include}
ver=$(echo %{springdoclet_namedversion} | sed -e 's/-SNAPSHOT//')
nam=springdoclet-maven-plugin
install -m 644 mojo-sandbox/${nam}/target/${nam}-%{springdoclet_namedversion}.jar \
               $RPM_BUILD_ROOT%{_javadir}/mojo/${nam}-${ver}.jar
ln -sf ${nam}-${ver}.jar $RPM_BUILD_ROOT%{_javadir}/mojo/${nam}.jar
install -m 644 mojo-sandbox/${nam}/pom.xml $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.mojo-${nam}.pom
%add_to_maven_depmap org.codehaus.mojo ${nam} ${ver} JPP/mojo ${nam}
%endif

%if %{sysdeo_tomcat_include}
ver=$(echo %{sysdeo_tomcat_namedversion} | sed -e 's/-SNAPSHOT//')
dnam=sysdeo-tomcat-maven-plugin
jnam=sysdeo-tomcat-plugin
install -m 644 ${dnam}/target/${dnam}-%{sysdeo_tomcat_namedversion}.jar \
               $RPM_BUILD_ROOT%{_javadir}/mojo/${jnam}-${ver}.jar
ln -sf ${jnam}-${ver}.jar $RPM_BUILD_ROOT%{_javadir}/mojo/${jnam}.jar
install -m 644 ${dnam}/pom.xml $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.mojo-${jnam}.pom
%add_to_maven_depmap org.codehaus.mojo ${jnam} ${ver} JPP/mojo ${jnam}
%endif

%if %{visibroker_include}
ver=$(echo %{visibroker_namedversion} | sed -e 's/-SNAPSHOT//')
nam=visibroker-maven-plugin
install -m 644 mojo-sandbox/${nam}/target/${nam}-%{visibroker_namedversion}.jar \
               $RPM_BUILD_ROOT%{_javadir}/mojo/${nam}-${ver}.jar
ln -sf ${nam}-${ver}.jar $RPM_BUILD_ROOT%{_javadir}/mojo/${nam}.jar
install -m 644 mojo-sandbox/${nam}/pom.xml $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.mojo-${nam}.pom
%add_to_maven_depmap org.codehaus.mojo ${nam} ${ver} JPP/mojo ${nam}
%endif

%if %{wagon_include}
ver=$(echo %{wagon_namedversion} | sed -e 's/-SNAPSHOT//')
nam=wagon-maven-plugin
install -m 644 mojo-sandbox/${nam}/target/${nam}-%{wagon_namedversion}.jar \
               $RPM_BUILD_ROOT%{_javadir}/mojo/${nam}-${ver}.jar
ln -sf ${nam}-${ver}.jar $RPM_BUILD_ROOT%{_javadir}/mojo/${nam}.jar
install -m 644 mojo-sandbox/${nam}/pom.xml $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.mojo-${nam}.pom
%add_to_maven_depmap org.codehaus.mojo ${nam} ${ver} JPP/mojo ${nam}
%endif

%if %{webdoclet_include}
ver=$(echo %{webdoclet_namedversion} | sed -e 's/-SNAPSHOT//')
nam=webdoclet-maven-plugin
install -m 644 mojo-sandbox/${nam}/target/${nam}-%{webdoclet_namedversion}.jar \
               $RPM_BUILD_ROOT%{_javadir}/mojo/${nam}-${ver}.jar
ln -sf ${nam}-${ver}.jar $RPM_BUILD_ROOT%{_javadir}/mojo/${nam}.jar
install -m 644 mojo-sandbox/${nam}/pom.xml $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.mojo-${nam}.pom
%add_to_maven_depmap org.codehaus.mojo ${nam} ${ver} JPP/mojo ${nam}
%endif

%if %{xfire_include}
ver=$(echo %{xfire_namedversion} | sed -e 's/-SNAPSHOT//')
nam=xfire-maven-plugin
install -m 644 mojo-sandbox/${nam}/target/${nam}-%{xfire_namedversion}.jar \
               $RPM_BUILD_ROOT%{_javadir}/mojo/${nam}-${ver}.jar
ln -sf ${nam}-${ver}.jar $RPM_BUILD_ROOT%{_javadir}/mojo/${nam}.jar
install -m 644 mojo-sandbox/${nam}/pom.xml $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.mojo-${nam}.pom
%add_to_maven_depmap org.codehaus.mojo ${nam} ${ver} JPP/mojo ${nam}
%endif

%if %{xjc_include}
ver=$(echo %{xjc_namedversion} | sed -e 's/-SNAPSHOT//')
nam=xjc-maven-plugin
install -m 644 mojo-sandbox/${nam}/target/${nam}-%{xjc_namedversion}.jar \
               $RPM_BUILD_ROOT%{_javadir}/mojo/${nam}-${ver}.jar
ln -sf ${nam}-${ver}.jar $RPM_BUILD_ROOT%{_javadir}/mojo/${nam}.jar
install -m 644 mojo-sandbox/${nam}/pom.xml $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.mojo-${nam}.pom
%add_to_maven_depmap org.codehaus.mojo ${nam} ${ver} JPP/mojo ${nam}
%endif

%if %{xsltc_include}
ver=$(echo %{xsltc_namedversion} | sed -e 's/-SNAPSHOT//')
nam=xsltc-maven-plugin
install -m 644 mojo-sandbox/${nam}/target/${nam}-%{xsltc_namedversion}.jar \
               $RPM_BUILD_ROOT%{_javadir}/mojo/${nam}-${ver}.jar
ln -sf ${nam}-${ver}.jar $RPM_BUILD_ROOT%{_javadir}/mojo/${nam}.jar
install -m 644 mojo-sandbox/${nam}/pom.xml $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.mojo-${nam}.pom
%add_to_maven_depmap org.codehaus.mojo ${nam} ${ver} JPP/mojo ${nam}
%endif

%if %{native2ascii_include}
ver=$(echo %{native2ascii_namedversion} | sed -e 's/-SNAPSHOT//')
nam=native2ascii-maven-plugin
install -m 644 ${nam}/target/${nam}-%{native2ascii_namedversion}.jar \
               $RPM_BUILD_ROOT%{_javadir}/mojo/${nam}-${ver}.jar
ln -sf ${nam}-${ver}.jar $RPM_BUILD_ROOT%{_javadir}/mojo/${nam}.jar
install -m 644 ${nam}/pom.xml $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.mojo-${nam}.pom
%add_to_maven_depmap org.codehaus.mojo ${nam} ${ver} JPP/mojo ${nam}
%endif

%if %{netbeans_freeform_include}
ver=$(echo %{netbeans_freeform_namedversion} | sed -e 's/-SNAPSHOT//')
nam=netbeans-freeform-maven-plugin
install -m 644 ${nam}/target/${nam}-%{netbeans_freeform_namedversion}.jar \
               $RPM_BUILD_ROOT%{_javadir}/mojo/${nam}-${ver}.jar
ln -sf ${nam}-${ver}.jar $RPM_BUILD_ROOT%{_javadir}/mojo/${nam}.jar
install -m 644 ${nam}/pom.xml $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.mojo-${nam}.pom
%add_to_maven_depmap org.codehaus.mojo ${nam} ${ver} JPP/mojo ${nam}
%endif

%if %{openjpa_include}
ver=$(echo %{openjpa_namedversion} | sed -e 's/-SNAPSHOT//')
nam=openjpa-maven-plugin
install -m 644 ${nam}/target/${nam}-%{openjpa_namedversion}.jar \
               $RPM_BUILD_ROOT%{_javadir}/mojo/${nam}-${ver}.jar
ln -sf ${nam}-${ver}.jar $RPM_BUILD_ROOT%{_javadir}/mojo/${nam}.jar
install -m 644 ${nam}/pom.xml $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.mojo-${nam}.pom
%add_to_maven_depmap org.codehaus.mojo ${nam} ${ver} JPP/mojo ${nam}
%endif

%if %{osxappbundle_include}
ver=$(echo %{osxappbundle_namedversion} | sed -e 's/-SNAPSHOT//')
nam=osxappbundle-maven-plugin
install -m 644 ${nam}/target/${nam}-%{osxappbundle_namedversion}.jar \
               $RPM_BUILD_ROOT%{_javadir}/mojo/${nam}-${ver}.jar
ln -sf ${nam}-${ver}.jar $RPM_BUILD_ROOT%{_javadir}/mojo/${nam}.jar
install -m 644 ${nam}/pom.xml $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.mojo-${nam}.pom
%add_to_maven_depmap org.codehaus.mojo ${nam} ${ver} JPP/mojo ${nam}
%endif

%if %{ounce_include}
ver=$(echo %{ounce_namedversion} | sed -e 's/-SNAPSHOT//')
nam=ounce-maven-plugin
install -m 644 ${nam}/target/${nam}-%{ounce_namedversion}.jar \
               $RPM_BUILD_ROOT%{_javadir}/mojo/${nam}-${ver}.jar
ln -sf ${nam}-${ver}.jar $RPM_BUILD_ROOT%{_javadir}/mojo/${nam}.jar
install -m 644 ${nam}/pom.xml $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.mojo-${nam}.pom
%add_to_maven_depmap org.codehaus.mojo ${nam} ${ver} JPP/mojo ${nam}
%endif

%if %{plugin_support_include}
ver=$(echo %{plugin_support_namedversion} | sed -e 's/-SNAPSHOT//')
nam=plugin-support
install -m 644 ${nam}/target/${nam}-%{plugin_support_namedversion}.jar \
               $RPM_BUILD_ROOT%{_javadir}/mojo/${nam}-${ver}.jar
ln -sf ${nam}-${ver}.jar $RPM_BUILD_ROOT%{_javadir}/mojo/${nam}.jar
install -m 644 ${nam}/pom.xml $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.mojo-${nam}.pom
%add_to_maven_depmap org.codehaus.mojo ${nam} ${ver} JPP/mojo ${nam}
%endif

%if %{retrotranslator_include}
ver=$(echo %{retrotranslator_namedversion} | sed -e 's/-SNAPSHOT//')
nam=retrotranslator-maven-plugin
install -m 644 ${nam}/target/${nam}-%{retrotranslator_namedversion}.jar \
               $RPM_BUILD_ROOT%{_javadir}/mojo/${nam}-${ver}.jar
ln -sf ${nam}-${ver}.jar $RPM_BUILD_ROOT%{_javadir}/mojo/${nam}.jar
install -m 644 ${nam}/pom.xml $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.mojo-${nam}.pom
%add_to_maven_depmap org.codehaus.mojo ${nam} ${ver} JPP/mojo ${nam}
%endif

%if %{sablecc_include}
ver=$(echo %{sablecc_namedversion} | sed -e 's/-SNAPSHOT//')
nam=sablecc-maven-plugin
install -m 644 ${nam}/target/${nam}-%{sablecc_namedversion}.jar \
               $RPM_BUILD_ROOT%{_javadir}/mojo/${nam}-${ver}.jar
ln -sf ${nam}-${ver}.jar $RPM_BUILD_ROOT%{_javadir}/mojo/${nam}.jar
install -m 644 ${nam}/pom.xml $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.mojo-${nam}.pom
%add_to_maven_depmap org.codehaus.mojo ${nam} ${ver} JPP/mojo ${nam}
%endif

%if %{selenium_include}
ver=$(echo %{selenium_namedversion} | sed -e 's/-SNAPSHOT//')
nam=selenium-maven-plugin
install -m 644 ${nam}/target/${nam}-%{selenium_namedversion}.jar \
               $RPM_BUILD_ROOT%{_javadir}/mojo/${nam}-${ver}.jar
ln -sf ${nam}-${ver}.jar $RPM_BUILD_ROOT%{_javadir}/mojo/${nam}.jar
install -m 644 ${nam}/pom.xml $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.mojo-${nam}.pom
%add_to_maven_depmap org.codehaus.mojo ${nam} ${ver} JPP/mojo ${nam}
%endif

%if %{shitty_include}
ver=$(echo %{shitty_namedversion} | sed -e 's/-SNAPSHOT//')
nam=shitty-maven-plugin
install -m 644 ${nam}/target/${nam}-%{shitty_namedversion}.jar \
               $RPM_BUILD_ROOT%{_javadir}/mojo/${nam}-${ver}.jar
ln -sf ${nam}-${ver}.jar $RPM_BUILD_ROOT%{_javadir}/mojo/${nam}.jar
install -m 644 ${nam}/pom.xml $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.mojo-${nam}.pom
%add_to_maven_depmap org.codehaus.mojo ${nam} ${ver} JPP/mojo ${nam}
%endif

%if %{smc_include}
ver=$(echo %{smc_namedversion} | sed -e 's/-SNAPSHOT//')
nam=smc-maven-plugin
install -m 644 ${nam}/target/${nam}-%{smc_namedversion}.jar \
               $RPM_BUILD_ROOT%{_javadir}/mojo/${nam}-${ver}.jar
ln -sf ${nam}-${ver}.jar $RPM_BUILD_ROOT%{_javadir}/mojo/${nam}.jar
install -m 644 ${nam}/pom.xml $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.mojo-${nam}.pom
%add_to_maven_depmap org.codehaus.mojo ${nam} ${ver} JPP/mojo ${nam}
%endif

%if %{solaris_include}
ver=$(echo %{solaris_namedversion} | sed -e 's/-SNAPSHOT//')
nam=solaris-maven-plugin
install -m 644 solaris/${nam}/target/${nam}-%{solaris_namedversion}.jar \
               $RPM_BUILD_ROOT%{_javadir}/mojo/${nam}-${ver}.jar
ln -sf ${nam}-${ver}.jar $RPM_BUILD_ROOT%{_javadir}/mojo/${nam}.jar
install -m 644 solaris/${nam}/pom.xml $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.mojo-${nam}.pom
%add_to_maven_depmap org.codehaus.mojo ${nam} ${ver} JPP/mojo ${nam}
install -m 644 solaris/pom.xml $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.mojo-solaris.pom
%add_to_maven_depmap org.codehaus.mojo solaris ${ver} JPP/mojo solaris
%endif

%if %{sql_include}
ver=$(echo %{sql_namedversion} | sed -e 's/-SNAPSHOT//')
nam=sql-maven-plugin
install -m 644 ${nam}/target/${nam}-%{sql_namedversion}.jar \
               $RPM_BUILD_ROOT%{_javadir}/mojo/${nam}-${ver}.jar
ln -sf ${nam}-${ver}.jar $RPM_BUILD_ROOT%{_javadir}/mojo/${nam}.jar
install -m 644 ${nam}/pom.xml $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.mojo-${nam}.pom
%add_to_maven_depmap org.codehaus.mojo ${nam} ${ver} JPP/mojo ${nam}
%endif

%if %{taglist_include}
ver=$(echo %{taglist_namedversion} | sed -e 's/-SNAPSHOT//')
nam=taglist-maven-plugin
install -m 644 ${nam}/target/${nam}-%{taglist_namedversion}.jar \
               $RPM_BUILD_ROOT%{_javadir}/mojo/${nam}-${ver}.jar
ln -sf ${nam}-${ver}.jar $RPM_BUILD_ROOT%{_javadir}/mojo/${nam}.jar
install -m 644 ${nam}/pom.xml $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.mojo-${nam}.pom
%add_to_maven_depmap org.codehaus.mojo ${nam} ${ver} JPP/mojo ${nam}
%endif

%if %{tomcat_include}
ver=$(echo %{tomcat_namedversion} | sed -e 's/-SNAPSHOT//')
nam=tomcat-maven-plugin
install -m 644 ${nam}/target/${nam}-%{tomcat_namedversion}.jar \
               $RPM_BUILD_ROOT%{_javadir}/mojo/${nam}-${ver}.jar
ln -sf ${nam}-${ver}.jar $RPM_BUILD_ROOT%{_javadir}/mojo/${nam}.jar
install -m 644 ${nam}/pom.xml $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.mojo-${nam}.pom
%add_to_maven_depmap org.codehaus.mojo ${nam} ${ver} JPP/mojo ${nam}
%endif

%if %{webstart_include}
ver=$(echo %{pack200_anttasks_namedversion} | sed -e 's/-SNAPSHOT//')
nam=webstart-pack200-anttasks
install -m 644 webstart/${nam}/target/${nam}-%{pack200_anttasks_namedversion}.jar \
               $RPM_BUILD_ROOT%{_javadir}/mojo/${nam}-${ver}.jar
ln -sf ${nam}-${ver}.jar $RPM_BUILD_ROOT%{_javadir}/mojo/${nam}.jar
install -m 644 webstart/${nam}/pom.xml $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.mojo-${nam}.pom
%add_to_maven_depmap org.codehaus.mojo ${nam} ${ver} JPP/mojo ${nam}

ver=$(echo %{webstart_namedversion} | sed -e 's/-SNAPSHOT//')
install -m 644 webstart/pom.xml $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.mojo-webstart.pom
%add_to_maven_depmap org.codehaus.mojo webstart-maven-plugin-parent ${ver} JPP/mojo webstart

nam=webstart-pack200-jdk14
install -m 644 webstart/${nam}/target/${nam}-%{webstart_namedversion}.jar \
               $RPM_BUILD_ROOT%{_javadir}/mojo/${nam}-${ver}.jar
ln -sf ${nam}-${ver}.jar $RPM_BUILD_ROOT%{_javadir}/mojo/${nam}.jar
install -m 644 webstart/${nam}/pom.xml $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.mojo-${nam}.pom
%add_to_maven_depmap org.codehaus.mojo ${nam} ${ver} JPP/mojo ${nam}
nam=webstart-pack200-jdk15
install -m 644 webstart/${nam}/target/${nam}-%{webstart_namedversion}.jar \
               $RPM_BUILD_ROOT%{_javadir}/mojo/${nam}-${ver}.jar
ln -sf ${nam}-${ver}.jar $RPM_BUILD_ROOT%{_javadir}/mojo/${nam}.jar
install -m 644 webstart/${nam}/pom.xml $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.mojo-${nam}.pom
%add_to_maven_depmap org.codehaus.mojo ${nam} ${ver} JPP/mojo ${nam}
nam=webstart-maven-plugin
install -m 644 webstart/${nam}/target/${nam}-%{webstart_namedversion}.jar \
               $RPM_BUILD_ROOT%{_javadir}/mojo/${nam}-${ver}.jar
ln -sf ${nam}-${ver}.jar $RPM_BUILD_ROOT%{_javadir}/mojo/${nam}.jar
install -m 644 webstart/${nam}/pom.xml $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.mojo-${nam}.pom
%add_to_maven_depmap org.codehaus.mojo ${nam} ${ver} JPP/mojo ${nam}
nam=webstart-jarsigner-api
install -m 644 webstart/${nam}/target/${nam}-%{webstart_namedversion}.jar \
               $RPM_BUILD_ROOT%{_javadir}/mojo/${nam}-${ver}.jar
ln -sf ${nam}-${ver}.jar $RPM_BUILD_ROOT%{_javadir}/mojo/${nam}.jar
install -m 644 webstart/${nam}/pom.xml $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.mojo-${nam}.pom
%add_to_maven_depmap org.codehaus.mojo ${nam} ${ver} JPP/mojo ${nam}
nam=webstart-jnlp-servlet
ver=1.0
install -m 644 webstart/${nam}/target/${nam}-%{webstart_servlet_namedversion}.jar \
               $RPM_BUILD_ROOT%{_javadir}/mojo/${nam}-${ver}.jar
ln -sf ${nam}-${ver}.jar $RPM_BUILD_ROOT%{_javadir}/mojo/${nam}.jar
install -m 644 webstart/${nam}/pom.xml $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.mojo-${nam}.pom
%add_to_maven_depmap org.codehaus.mojo ${nam} ${webstart_servlet_namedversion} JPP/mojo ${nam}
%endif

%if %{wsdl2java_include}
ver=$(echo %{wsdl2java_namedversion} | sed -e 's/-SNAPSHOT//')
nam=wsdl2java-maven-plugin
install -m 644 ${nam}/target/${nam}-%{wsdl2java_namedversion}.jar \
               $RPM_BUILD_ROOT%{_javadir}/mojo/${nam}-${ver}.jar
ln -sf ${nam}-${ver}.jar $RPM_BUILD_ROOT%{_javadir}/mojo/${nam}.jar
install -m 644 ${nam}/pom.xml $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.mojo-${nam}.pom
%add_to_maven_depmap org.codehaus.mojo ${nam} ${ver} JPP/mojo ${nam}
%endif

%if %{xdoclet_include}
ver=$(echo %{xdoclet_namedversion} | sed -e 's/-SNAPSHOT//')
nam=xdoclet-maven-plugin
install -m 644 ${nam}/target/${nam}-%{xdoclet_namedversion}.jar \
               $RPM_BUILD_ROOT%{_javadir}/mojo/${nam}-${ver}.jar
ln -sf ${nam}-${ver}.jar $RPM_BUILD_ROOT%{_javadir}/mojo/${nam}.jar
install -m 644 ${nam}/pom.xml $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.mojo-${nam}.pom
%add_to_maven_depmap org.codehaus.mojo ${nam} ${ver} JPP/mojo ${nam}
%endif

%if %{xmlbeans_include}
ver=$(echo %{xmlbeans_namedversion} | sed -e 's/-SNAPSHOT//')
nam=xmlbeans-maven-plugin
install -m 644 ${nam}/target/${nam}-%{xmlbeans_namedversion}.jar \
               $RPM_BUILD_ROOT%{_javadir}/mojo/${nam}-${ver}.jar
ln -sf ${nam}-${ver}.jar $RPM_BUILD_ROOT%{_javadir}/mojo/${nam}.jar
install -m 644 ${nam}/pom.xml $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.mojo-${nam}.pom
%add_to_maven_depmap org.codehaus.mojo ${nam} ${ver} JPP/mojo ${nam}
%endif

%if %{xml_include}
ver=$(echo %{xml_namedversion} | sed -e 's/-SNAPSHOT//')
nam=xml-maven-plugin
install -m 644 ${nam}/target/${nam}-%{xml_namedversion}.jar \
               $RPM_BUILD_ROOT%{_javadir}/mojo/${nam}-${ver}.jar
ln -sf ${nam}-${ver}.jar $RPM_BUILD_ROOT%{_javadir}/mojo/${nam}.jar
install -m 644 ${nam}/pom.xml $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.mojo-${nam}.pom
%add_to_maven_depmap org.codehaus.mojo ${nam} ${ver} JPP/mojo ${nam}
%endif

%if %{xslt_include}
ver=$(echo %{xslt_namedversion} | sed -e 's/-SNAPSHOT//')
nam=xslt-maven-plugin
install -m 644 ${nam}/target/${nam}-%{xslt_namedversion}.jar \
               $RPM_BUILD_ROOT%{_javadir}/mojo/${nam}-${ver}.jar
ln -sf ${nam}-${ver}.jar $RPM_BUILD_ROOT%{_javadir}/mojo/${nam}.jar
install -m 644 ${nam}/pom.xml $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.mojo-${nam}.pom
%add_to_maven_depmap org.codehaus.mojo ${nam} ${ver} JPP/mojo ${nam}
%endif


# javadoc
install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}

%if %{appassembler_include}
install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}/appassembler-booter
cp -pr appassembler/appassembler-booter/target/site/apidocs/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}/appassembler-booter
install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}/appassembler-maven-plugin
cp -pr appassembler/appassembler-maven-plugin/target/site/apidocs/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}/appassembler-maven-plugin
install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}/appassembler-model
cp -pr appassembler/appassembler-model/target/site/apidocs/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}/appassembler-model
%endif

%if %{aspectj_include}
install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}/aspectj-maven-plugin
cp -pr aspectj-maven-plugin/target/site/apidocs/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}/aspectj-maven-plugin
%endif

%if %{axistools_include}
install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}/axistools-maven-plugin
cp -pr axistools-maven-plugin/target/site/apidocs/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}/axistools-maven-plugin
%endif

%if %{build_helper_include}
install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}/build-helper-maven-plugin
cp -pr build-helper-maven-plugin/target/site/apidocs/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}/build-helper-maven-plugin
%endif

%if %{castor_include}
install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}/castor-maven-plugin
cp -pr castor-maven-plugin/target/site/apidocs/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}/castor-maven-plugin
%endif

%if %{clirr_include}
install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}/clirr-maven-plugin
cp -pr clirr-maven-plugin/target/site/apidocs/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}/clirr-maven-plugin
%endif

%if %{cobertura_include}
install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}/cobertura-maven-plugin
cp -pr cobertura-maven-plugin/target/site/apidocs/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}/cobertura-maven-plugin
%endif

%if %{commons_attributes_include}
install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}/commons-attributes-maven-plugin
cp -pr commons-attributes-maven-plugin/target/site/apidocs/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}/commons-attributes-maven-plugin
%endif

%if %{docbook_include}
install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}/docbook-maven-plugin
cp -pr docbook-maven-plugin/target/site/apidocs/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}/docbook-maven-plugin
%endif

%if %{exec_include}
install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}/exec-maven-plugin
cp -pr exec-maven-plugin/target/site/apidocs/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}/exec-maven-plugin
%endif

%if %{findbugs_include}
install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}/findbugs-maven-plugin
cp -pr findbugs-maven-plugin/target/site/apidocs/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}/findbugs-maven-plugin
%endif

%if %{hibernate2_include}
install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}/hibernate2-maven-plugin
cp -pr hibernate2-maven-plugin/target/site/apidocs/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}/hibernate2-maven-plugin
%endif

%if %{hibernate3_include}
install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}/hibernate3-maven-plugin
cp -pr hibernate3/hibernate3-maven-plugin/target/site/apidocs/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}/hibernate3-maven-plugin
install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}/maven-hibernate3-api
cp -pr hibernate3/maven-hibernate3-api/target/site/apidocs/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}/maven-hibernate3-api
install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}/maven-hibernate3-jdk14
cp -pr hibernate3/maven-hibernate3-components/maven-hibernate3-jdk14/target/site/apidocs/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}/maven-hibernate3-jdk14
install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}/maven-hibernate3-jdk15
cp -pr hibernate3/maven-hibernate3-components/maven-hibernate3-jdk15/target/site/apidocs/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}/maven-hibernate3-jdk15
%endif

%if %{jalopy_include}
install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}/jalopy-maven-plugin
cp -pr jalopy-maven-plugin/target/site/apidocs/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}/jalopy-maven-plugin
%endif

%if %{javacc_include}
install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}/javacc-maven-plugin
cp -pr javacc-maven-plugin/target/site/apidocs/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}/javacc-maven-plugin
%endif

%if %{javancss_include}
install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}/javancss-maven-plugin
cp -pr javancss-maven-plugin/target/site/apidocs/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}/javancss-maven-plugin
%endif

%if %{jaxb2_include}
install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}/jaxb2-maven-plugin
cp -pr jaxb2-maven-plugin/target/site/apidocs/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}/jaxb2-maven-plugin
%endif

%if %{jboss_include}
install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}/jboss-maven-plugin
cp -pr jboss-maven-plugin/target/site/apidocs/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}/jboss-maven-plugin
%endif

%if %{jdepend_include}
install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}/jdepend-maven-plugin
cp -pr jdepend-maven-plugin/target/site/apidocs/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}/jdepend-maven-plugin
%endif

%if %{jdiff_include}
install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}/jdiff-maven-plugin
cp -pr jdiff-maven-plugin/target/site/apidocs/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}/jdiff-maven-plugin
%endif

%if %{jpox_include}
install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}/jpox-maven-plugin
cp -pr jpox-maven-plugin/target/site/apidocs/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}/jpox-maven-plugin
%endif

%if %{jruby_include}
install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}/jruby-maven-plugin
cp -pr jruby-maven-plugin/target/site/apidocs/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}/jruby-maven-plugin
%endif

%if %{jspc_include}
install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}/jspc-compiler-api
cp -pr jspc/jspc-compiler-api/target/site/apidocs/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}/jspc-compiler-api
install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}/jspc-compiler-tomcat5
cp -pr jspc/jspc-compilers/jspc-compiler-tomcat5/target/site/apidocs/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}/jspc-compiler-tomcat5
install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}/jspc-compiler-tomcat6
cp -pr jspc/jspc-compilers/jspc-compiler-tomcat6/target/site/apidocs/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}/jspc-compiler-tomcat6
install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}/jspc-maven-plugin
cp -pr jspc/jspc-maven-plugin/target/site/apidocs/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}/jspc-maven-plugin
%endif

%if %{keytool_include}
install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}/keytool-maven-plugin
cp -pr keytool-maven-plugin/target/site/apidocs/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}/keytool-maven-plugin
%endif

%if %{native_include}
install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}/maven-native-api
cp -pr maven-native/maven-native-api/target/site/apidocs/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}/maven-native-api
install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}/maven-native-bcc
cp -pr maven-native/maven-native-components/maven-native-bcc/target/site/apidocs/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}/maven-native-bcc
install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}/maven-native-generic-c
cp -pr maven-native/maven-native-components/maven-native-generic-c/target/site/apidocs/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}/maven-native-generic-c
install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}/maven-native-javah
cp -pr maven-native/maven-native-components/maven-native-javah/target/site/apidocs/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}/maven-native-javah
install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}/maven-native-manager
cp -pr maven-native/maven-native-components/maven-native-manager/target/site/apidocs/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}/maven-native-manager
install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}/maven-native-msvc
cp -pr maven-native/maven-native-components/maven-native-msvc/target/site/apidocs/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}/maven-native-msvc
install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}/native-maven-plugin
cp -pr maven-native/native-maven-plugin/target/site/apidocs/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}/native-maven-plugin
%endif

%if %{minijar_include}
install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}/minijar-maven-plugin
cp -pr minijar-maven-plugin/target/site/apidocs/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}/minijar-maven-plugin
%endif

%if %{appbundler_include}
install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}/appbundler-maven-plugin
cp -pr mojo-sandbox/appbundler-maven-plugin/target/site/apidocs/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}/appbundler-maven-plugin
%endif

%if %{appfuse_include}
install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}/appfuse-maven-plugin
cp -pr mojo-sandbox/appfuse-maven-plugin/target/site/apidocs/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}/appfuse-maven-plugin
%endif

%if %{apt_include}
install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}/apt-maven-plugin
cp -pr apt-maven-plugin/target/site/apidocs/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}/apt-maven-plugin
%endif

%if %{batik_include}
install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}/batik-maven-plugin
cp -pr mojo-sandbox/batik-maven-plugin/target/site/apidocs/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}/batik-maven-plugin
%endif

%if %{cis_include}
install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}/cis-maven-plugin
cp -pr mojo-sandbox/cis-maven-plugin/target/site/apidocs/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}/cis-maven-plugin
%endif

%if %{cruisecontrol_include}
install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}/cruisecontrol-maven-plugin
cp -pr mojo-sandbox/cruisecontrol-maven-plugin/target/site/apidocs/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}/cruisecontrol-maven-plugin
%endif

%if %{dashboard_include}
install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}/dashboard-maven-plugin
cp -pr mojo-sandbox/dashboard-maven-plugin/target/site/apidocs/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}/dashboard-maven-plugin
%endif

%if %{deb_include}
install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}/deb-maven-plugin
cp -pr mojo-sandbox/deb-maven-plugin/target/site/apidocs/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}/deb-maven-plugin
%endif

%if %{delicious_include}
install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}/delicious-maven-plugin
cp -pr mojo-sandbox/delicious-maven-plugin/target/site/apidocs/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}/delicious-maven-plugin
%endif

%if %{ejbdoclet_include}
install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}/ejbdoclet-maven-plugin
cp -pr mojo-sandbox/ejbdoclet-maven-plugin/target/site/apidocs/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}/ejbdoclet-maven-plugin
%endif

%if %{emma_include}
install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}/emma-maven-plugin
cp -pr mojo-sandbox/emma-maven-plugin/target/site/apidocs/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}/emma-maven-plugin
%endif

%if %{fileutils_include}
install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}/fileutils-maven-plugin
cp -pr mojo-sandbox/fileutils-maven-plugin/target/site/apidocs/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}/fileutils-maven-plugin
%endif

%if %{fit_include}
install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}/fit-maven-plugin
cp -pr mojo-sandbox/fit-maven-plugin/target/site/apidocs/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}/fit-maven-plugin
%endif

%if %{ganalytics_include}
install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}/ganalytics-maven-plugin
cp -pr mojo-sandbox/ganalytics-maven-mojo/target/site/apidocs/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}/ganalytics-maven-plugin
%endif

%if %{graphing_include}
install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}/graphing-maven-plugin
cp -pr mojo-sandbox/graphing-maven-plugin/target/site/apidocs/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}/graphing-maven-plugin
%endif

%if %{hibernatedoclet_include}
install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}/hibernatedoclet-maven-plugin
cp -pr mojo-sandbox/hibernatedoclet-maven-plugin/target/site/apidocs/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}/hibernatedoclet-maven-plugin
%endif

%if %{ibatis_include}
install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}/ibatis-maven-plugin
cp -pr mojo-sandbox/ibatis-maven-plugin/target/site/apidocs/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}/ibatis-maven-plugin
%endif

%if %{j2me_include}
install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}/j2me-maven-plugin
cp -pr mojo-sandbox/j2me-maven-plugin/target/site/apidocs/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}/j2me-maven-plugin
%endif

%if %{jardiff_include}
install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}/jardiff-maven-plugin
cp -pr mojo-sandbox/jardiff-maven-plugin/target/site/apidocs/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}/jardiff-maven-plugin
%endif

%if %{jasperreports_include}
install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}/jasperreports-maven-plugin
cp -pr jasperreports-maven-plugin/target/site/apidocs/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}/jasperreports-maven-plugin
%endif

%if %{jaxws_include}
install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}/jaxws-maven-plugin
cp -pr mojo-sandbox/jaxws-maven-plugin/target/site/apidocs/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}/jaxws-maven-plugin
%endif

%if %{jboss_packaging_include}
install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}/jboss-packaging-maven-plugin
cp -pr jboss-packaging-maven-plugin/target/site/apidocs/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}/jboss-packaging-maven-plugin
%endif

%if %{jellyapi_include}
install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}/jellyapi-maven-plugin
cp -pr mojo-sandbox/jelly-maven-tools/jellyapi-maven-plugin/target/site/apidocs/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}/jellyapi-maven-plugin
%endif

%if %{jettybin_include}
install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}/jettybin-maven-plugin
cp -pr mojo-sandbox/jettybin-maven-plugin/target/site/apidocs/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}/jettybin-maven-plugin
%endif

%if %{jetty_include}
install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}/jetty-maven-plugin
cp -pr mojo-sandbox/jetty-maven-plugin/target/site/apidocs/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}/jetty-maven-plugin
%endif

%if %{l10n_include}
install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}/l10n-maven-plugin
cp -pr l10n-maven-plugin/target/site/apidocs/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}/l10n-maven-plugin
%endif

%if %{mant_include}
install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}/mant-maven-plugin
cp -pr mojo-sandbox/mant-maven-plugin/target/site/apidocs/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}/mant-maven-plugin
%endif

%if %{mojo_was_plugin_anttasks_include}
install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}/was-plugin-anttasks
cp -pr mojo-sandbox/mojo-was/was-plugin-anttasks/target/site/apidocs/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}/was-plugin-anttasks
%endif

%if %{buildinfo_include}
install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}/maven-buildinfo-plugin
cp -pr mojo-sandbox/maven-buildinfo-plugin/target/site/apidocs/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}/maven-buildinfo-plugin
%endif

%if %{changes_include}
install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}/maven-changes
cp -pr mojo-sandbox/maven-changes/target/site/apidocs/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}/maven-changes
%endif

%if %{diagram_maker_include}
install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}/maven-diagram-maker-connector-api
cp -pr mojo-sandbox/maven-diagram-maker/connector-api/target/site/apidocs/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}/maven-diagram-maker-connector-api
install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}/maven-diagram-maker-connector-classes
cp -pr mojo-sandbox/maven-diagram-maker/connectors/connector-classes/target/site/apidocs/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}/maven-diagram-maker-connector-classes
install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}/maven-diagram-maker-connector-dependencies
cp -pr mojo-sandbox/maven-diagram-maker/connectors/connector-dependencies/target/site/apidocs/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}/maven-diagram-maker-connector-dependencies
install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}/maven-diagram-maker-diagrams-gui
cp -pr mojo-sandbox/maven-diagram-maker/diagrams-gui/target/site/apidocs/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}/maven-diagram-maker-diagrams-gui
install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}/maven-diagram-maker-graph-api
cp -pr mojo-sandbox/maven-diagram-maker/graph-api/target/site/apidocs/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}/maven-diagram-maker-graph-api
%endif

%if %{hsqldb_include}
install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}/maven-hsqldb-plugin
cp -pr mojo-sandbox/maven-hsqldb-plugin/target/site/apidocs/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}/maven-hsqldb-plugin
%endif

%if %{springbeandoc_include}
install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}/maven-springbeandoc-plugin
cp -pr mojo-sandbox/maven-springbeandoc-plugin/target/site/apidocs/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}/maven-springbeandoc-plugin
%endif

%if %{testing_simple_include}
install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}/maven-simple-plugin
cp -pr mojo-sandbox/maven-plugin-testing/maven-simple-plugin/target/site/apidocs/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}/maven-simple-plugin
%endif

%if %{pomtools_include}
install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}/pomtools-maven-plugin
cp -pr mojo-sandbox/pomtools-maven-plugin/target/site/apidocs/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}/pomtools-maven-plugin
%endif

%if %{properties_include}
install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}/properties-maven-plugin
cp -pr mojo-sandbox/properties-maven-plugin/target/site/apidocs/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}/properties-maven-plugin
%endif

%if %{push_include}
install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}/push-maven-plugin
cp -pr mojo-sandbox/push-maven-plugin/target/site/apidocs/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}/push-maven-plugin
%endif

%if %{retroweaver_include}
install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}/retroweaver-maven-plugin
cp -pr mojo-sandbox/retroweaver-maven-plugin/target/site/apidocs/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}/retroweaver-maven-plugin
%endif

%if %{rat_include}
install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}/rat-maven-plugin
cp -pr rat-maven-plugin/target/site/apidocs/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}/rat-maven-plugin
%endif

%if %{rmic_include}
install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}/rmic-maven-plugin
cp -pr rmic-maven-plugin/target/site/apidocs/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}/rmic-maven-plugin
%endif

%if %{rpm_include}
install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}/rpm-maven-plugin
cp -pr rpm-maven-plugin/target/site/apidocs/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}/rpm-maven-plugin
%endif

%if %{runtime_builder_include}
install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}/runtime-maven-plugin
cp -pr mojo-sandbox/runtime-maven-plugin/target/site/apidocs/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}/runtime-maven-plugin
%endif

%if %{script_include}
install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}/script-maven-plugin
cp -pr mojo-sandbox/script-maven-plugin/target/site/apidocs/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}/script-maven-plugin
%endif

%if %{shade_include}
install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}/shade-maven-plugin
cp -pr mojo-sandbox/shade-maven-plugin/target/site/apidocs/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}/shade-maven-plugin
%endif

%if %{shell_include}
install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}/shell-maven-plugin
cp -pr mojo-sandbox/shell-maven-plugin/target/site/apidocs/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}/shell-maven-plugin
%endif

%if %{springdoclet_include}
install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}/springdoclet-maven-plugin
cp -pr mojo-sandbox/springdoclet-maven-plugin/target/site/apidocs/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}/springdoclet-maven-plugin
%endif

%if %{sysdeo_tomcat_include}
install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}/sysdeo-tomcat-maven-plugin
cp -pr sysdeo-tomcat-maven-plugin/target/site/apidocs/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}/sysdeo-tomcat-maven-plugin
%endif

%if %{visibroker_include}
install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}/visibroker-maven-plugin
cp -pr mojo-sandbox/visibroker-maven-plugin/target/site/apidocs/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}/visibroker-maven-plugin
%endif

%if %{wagon_include}
install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}/wagon-maven-plugin
cp -pr mojo-sandbox/wagon-maven-plugin/target/site/apidocs/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}/wagon-maven-plugin
%endif

%if %{webdoclet_include}
install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}/webdoclet-maven-plugin
cp -pr mojo-sandbox/webdoclet-maven-plugin/target/site/apidocs/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}/webdoclet-maven-plugin
%endif

%if %{xfire_include}
install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}/xfire-maven-plugin
cp -pr mojo-sandbox/xfire-maven-plugin/target/site/apidocs/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}/xfire-maven-plugin
%endif

%if %{xjc_include}
install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}/xjc-maven-plugin
cp -pr mojo-sandbox/xjc-maven-plugin/target/site/apidocs/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}/xjc-maven-plugin
%endif

%if %{xsltc_include}
install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}/xsltc-maven-plugin
cp -pr mojo-sandbox/xsltc-maven-plugin/target/site/apidocs/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}/xsltc-maven-plugin
%endif

%if %{native2ascii_include}
install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}/native2ascii-maven-plugin
cp -pr native2ascii-maven-plugin/target/site/apidocs/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}/native2ascii-maven-plugin
%endif

%if %{netbeans_freeform_include}
install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}/netbeans-freeform-maven-plugin
cp -pr netbeans-freeform-maven-plugin/target/site/apidocs/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}/netbeans-freeform-maven-plugin
%endif

%if %{openjpa_include}
install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}/openjpa-maven-plugin
cp -pr openjpa-maven-plugin/target/site/apidocs/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}/openjpa-maven-plugin
%endif

%if %{plugin_support_include}
install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}/plugin-support
cp -pr plugin-support/target/site/apidocs/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}/plugin-support
%endif

%if %{retrotranslator_include}
install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}/retrotranslator-maven-plugin
cp -pr retrotranslator-maven-plugin/target/site/apidocs/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}/retrotranslator-maven-plugin
%endif

%if %{sablecc_include}
install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}/sablecc-maven-plugin
cp -pr sablecc-maven-plugin/target/site/apidocs/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}/sablecc-maven-plugin
%endif

%if %{selenium_include}
install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}/selenium-maven-plugin
cp -pr selenium-maven-plugin/target/site/apidocs/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}/selenium-maven-plugin
%endif

%if %{shitty_include}
install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}/shitty-maven-plugin
cp -pr shitty-maven-plugin/target/site/apidocs/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}/shitty-maven-plugin
%endif

%if %{smc_include}
install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}/smc-maven-plugin
cp -pr smc-maven-plugin/target/site/apidocs/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}/smc-maven-plugin
%endif

%if %{solaris_include}
install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}/solaris-maven-plugin
cp -pr solaris/solaris-maven-plugin/target/site/apidocs/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}/solaris-maven-plugin
%endif

%if %{sql_include}
install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}/sql-maven-plugin
cp -pr sql-maven-plugin/target/site/apidocs/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}/sql-maven-plugin
%endif

%if %{taglist_include}
install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}/taglist-maven-plugin
cp -pr taglist-maven-plugin/target/site/apidocs/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}/taglist-maven-plugin
%endif

%if %{tomcat_include}
install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}/tomcat-maven-plugin
cp -pr tomcat-maven-plugin/target/site/apidocs/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}/tomcat-maven-plugin
%endif

%if %{webstart_include}
install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}/webstart-pack200-jdk14
cp -pr webstart/webstart-pack200-jdk14/target/site/apidocs/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}/webstart-pack200-jdk14
install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}/webstart-pack200-jdk15
cp -pr webstart/webstart-pack200-jdk15/target/site/apidocs/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}/webstart-pack200-jdk15
install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}/webstart-maven-plugin
cp -pr webstart/webstart-maven-plugin/target/site/apidocs/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}/webstart-maven-plugin
install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}/webstart-jarsigner-api
cp -pr webstart/webstart-jarsigner-api/target/site/apidocs/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}/webstart-jarsigner-api
install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}/webstart-jnlp-servlet
cp -pr webstart/webstart-jnlp-servlet/target/site/apidocs/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}/webstart-jnlp-servlet
%endif

%if %{wsdl2java_include}
install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}/wsdl2java-maven-plugin
cp -pr wsdl2java-maven-plugin/target/site/apidocs/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}/wsdl2java-maven-plugin
%endif

%if %{xdoclet_include}
install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}/xdoclet-maven-plugin
cp -pr xdoclet-maven-plugin/target/site/apidocs/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}/xdoclet-maven-plugin
%endif

%if %{xmlbeans_include}
install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}/xmlbeans-maven-plugin
cp -pr xmlbeans-maven-plugin/target/site/apidocs/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}/xmlbeans-maven-plugin
%endif

%if %{xml_include}
install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}/xml-maven-plugin
cp -pr xml-maven-plugin/target/site/apidocs/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}/xml-maven-plugin
%endif

%if %{xslt_include}
install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}/xslt-maven-plugin
cp -pr xslt-maven-plugin/target/site/apidocs/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}/xslt-maven-plugin
%endif

ln -s %{name}-%{version} $RPM_BUILD_ROOT%{_javadocdir}/%{name} # ghost symlink

%if %{gcj_support}
export CLASSPATH=$(build-classpath gnu-crypto)
%{_bindir}/aot-compile-rpm
%endif
patch %buildroot/usr/share/maven2/poms/JPP.mojo-findbugs-maven-plugin.pom <<'EOF'
--- JPP.mojo-findbugs-maven-plugin.pom	2012-02-10 13:27:49.000000000 +0200
+++ JPP.mojo-findbugs-maven-plugin.pom	2012-02-11 19:02:04.000000000 +0200
@@ -135,11 +135,13 @@
       <artifactId>findbugs-ant</artifactId>
       <version>1.3.9</version>
     </dependency>
+    <!--
     <dependency>
       <groupId>jgoodies</groupId>
       <artifactId>plastic</artifactId>
       <version>1.2.0</version>
     </dependency>
+    -->
     <dependency>
       <groupId>org.codehaus.gmaven</groupId>
       <artifactId>gmaven-mojo</artifactId>
EOF

%files
%dir %{_javadir}/mojo
%{_datadir}/maven2/poms/JPP.mojo-mojo.pom
%{_datadir}/maven2/poms/JPP.mojo-mojo-sandbox.pom
%{_mavendepmapfragdir}/*
%if %{gcj_support}
%dir %{_libdir}/gcj/%{name}
%endif

%if %{antlr_include}
%files -n mojo-maven2-plugin-antlr
%{_javadir}/mojo/antlr*.jar
%{_datadir}/maven2/poms/JPP.mojo-antlr-maven-plugin*.pom
%if %{gcj_support}
%{_libdir}/gcj/%{name}/antlr-*.jar.*
%endif
%endif

%if %{appassembler_include}
%files -n mojo-maven2-plugin-appassembler
%{_javadir}/mojo/appassembler*.jar
%{_datadir}/maven2/poms/JPP.mojo-appassembler-maven-plugin.pom
%{_datadir}/maven2/poms/JPP.mojo-appassembler-booter.pom
%{_datadir}/maven2/poms/JPP.mojo-appassembler-model.pom
%{_datadir}/maven2/poms/JPP.mojo-appassembler.pom
%if %{gcj_support}
%{_libdir}/gcj/%{name}/appassembler-*.jar.*
%endif
%endif

%if %{appbundler_include}
%files -n mojo-maven2-plugin-appbundler
%{_javadir}/mojo/appbundler*.jar
%{_datadir}/maven2/poms/JPP.mojo-appbundler-maven-plugin*.pom
%if %{gcj_support}
%{_libdir}/gcj/%{name}/appbundler-*.jar.*
%endif
%endif

%if %{appfuse_include}
%files -n mojo-maven2-plugin-appfuse
%{_javadir}/mojo/appfuse*.jar
%{_datadir}/maven2/poms/JPP.mojo-appfuse-maven-plugin*.pom
%if %{gcj_support}
%{_libdir}/gcj/%{name}/appfuse-*.jar.*
%endif
%endif

%if %{apt_include}
%files -n mojo-maven2-plugin-apt
%{_javadir}/mojo/apt*.jar
%{_datadir}/maven2/poms/JPP.mojo-apt-maven-plugin*.pom
%if %{gcj_support}
%{_libdir}/gcj/%{name}/apt-*.jar.*
%endif
%endif

%if %{aspectj_include}
%files -n mojo-maven2-plugin-aspectj
%{_javadir}/mojo/aspectj*.jar
%{_datadir}/maven2/poms/JPP.mojo-aspectj-maven-plugin*.pom
%if %{gcj_support}
%{_libdir}/gcj/%{name}/aspectj-*.jar.*
%endif
%endif

%if %{axistools_include}
%files -n mojo-maven2-plugin-axistools
%{_javadir}/mojo/axistools*.jar
%{_datadir}/maven2/poms/JPP.mojo-axistools-maven-plugin*.pom
%if %{gcj_support}
%{_libdir}/gcj/%{name}/axistools-*.jar.*
%endif
%endif

%if %{batik_include}
%files -n mojo-maven2-plugin-batik
%{_javadir}/mojo/batik*.jar
%{_datadir}/maven2/poms/JPP.mojo-batik-maven-plugin*.pom
%if %{gcj_support}
%{_libdir}/gcj/%{name}/batik-*.jar.*
%endif
%endif

%if %{build_helper_include}
%files -n mojo-maven2-plugin-build-helper
%{_javadir}/mojo/build-helper*.jar
%{_datadir}/maven2/poms/JPP.mojo-build-helper-maven-plugin*.pom
%if %{gcj_support}
%{_libdir}/gcj/%{name}/build-helper-*.jar.*
%endif
%endif

%if %{buildinfo_include}
%files -n mojo-maven2-plugin-buildinfo
%{_javadir}/mojo/maven-buildinfo*.jar
%{_datadir}/maven2/poms/JPP.mojo-maven-buildinfo-plugin.pom
%if %{gcj_support}
%{_libdir}/gcj/%{name}/maven-buildinfo-*.jar.*
%endif
%endif

%if %{buildnumber_include}
%files -n mojo-maven2-plugin-buildnumber
%{_javadir}/mojo/buildnumber*.jar
%{_datadir}/maven2/poms/JPP.mojo-buildnumber-*.pom
%if %{gcj_support}
%{_libdir}/gcj/%{name}/buildnumber-*.jar.*
%endif
%endif

%if %{castor_include}
%files -n mojo-maven2-plugin-castor
%{_javadir}/mojo/castor*.jar
%{_datadir}/maven2/poms/JPP.mojo-castor-maven-plugin*.pom
%if %{gcj_support}
%{_libdir}/gcj/%{name}/castor-*.jar.*
%endif
%endif

%if %{changes_include}
%files -n mojo-maven2-changes
%{_javadir}/mojo/maven-changes*.jar
%{_datadir}/maven2/poms/JPP.mojo-maven-changes*.pom
%if %{gcj_support}
%{_libdir}/gcj/%{name}/changes-*.jar.*
%endif
%endif

%if %{cis_include}
%files -n mojo-maven2-plugin-cis
%{_javadir}/mojo/cis*.jar
%{_datadir}/maven2/poms/JPP.mojo-cis-maven-plugin*.pom
%if %{gcj_support}
%{_libdir}/gcj/%{name}/cis-*.jar.*
%endif
%endif

%if %{clirr_include}
%files -n mojo-maven2-plugin-clirr
%{_javadir}/mojo/clirr*.jar
%{_datadir}/maven2/poms/JPP.mojo-clirr-maven-plugin*.pom
%if %{gcj_support}
%{_libdir}/gcj/%{name}/clirr-*.jar.*
%endif
%endif

%if %{cobertura_include}
%files -n mojo-maven2-plugin-cobertura
%{_javadir}/mojo/cobertura*.jar
%{_datadir}/maven2/poms/JPP.mojo-cobertura-maven-plugin*.pom
%if %{gcj_support}
%{_libdir}/gcj/%{name}/cobertura-*.jar.*
%endif
%endif

%if %{commons_attributes_include}
%files -n mojo-maven2-plugin-commons-attributes
%{_javadir}/mojo/commons-attributes*.jar
%{_datadir}/maven2/poms/JPP.mojo-commons-attributes-maven-plugin*.pom
%if %{gcj_support}
%{_libdir}/gcj/%{name}/commons-attributes-*.jar.*
%endif
%endif

%if %{cruisecontrol_include}
%files -n mojo-maven2-plugin-cruisecontrol
%{_javadir}/mojo/cruisecontrol*.jar
%{_datadir}/maven2/poms/JPP.mojo-cruisecontrol-maven-plugin*.pom
%if %{gcj_support}
%{_libdir}/gcj/%{name}/cruisecontrol-*.jar.*
%endif
%endif

%if %{dashboard_include}
%files -n mojo-maven2-plugin-dashboard
%{_javadir}/mojo/dashboard*.jar
%{_datadir}/maven2/poms/JPP.mojo-dashboard-maven-plugin*.pom
%if %{gcj_support}
%{_libdir}/gcj/%{name}/dashboard-*.jar.*
%endif
%endif

%if %{dbunit_include}
%files -n mojo-maven2-plugin-dbunit
%{_javadir}/mojo/dbunit*.jar
%{_datadir}/maven2/poms/JPP.mojo-dbunit-maven-plugin*.pom
%if %{gcj_support}
%{_libdir}/gcj/%{name}/dbunit-*.jar.*
%endif
%endif

%if %{deb_include}
%files -n mojo-maven2-plugin-deb
%{_javadir}/mojo/deb*.jar
%{_datadir}/maven2/poms/JPP.mojo-deb-maven-plugin*.pom
%if %{gcj_support}
%{_libdir}/gcj/%{name}/deb-*.jar.*
%endif
%endif

%if %{delicious_include}
%files -n mojo-maven2-plugin-delicious
%{_javadir}/mojo/delicious*.jar
%{_datadir}/maven2/poms/JPP.mojo-delicious-maven-plugin*.pom
%if %{gcj_support}
%{_libdir}/gcj/%{name}/delicious-*.jar.*
%endif
%endif

%if %{diagram_maker_include}
%files -n mojo-maven2-diagram-maker
%{_javadir}/mojo/connector*.jar
%{_javadir}/mojo/diagrams-gui*.jar
%{_javadir}/mojo/graph-api*.jar
%{_javadir}/mojo/maven-diagrams-plugin*.jar
%{_datadir}/maven2/poms/JPP.mojo-diagrams-gui.pom
%{_datadir}/maven2/poms/JPP.mojo-connector*.pom
%{_datadir}/maven2/poms/JPP.mojo-maven-diagram-maker.pom
%{_datadir}/maven2/poms/JPP.mojo-diagram-maker-connectors.pom
%{_datadir}/maven2/poms/JPP.mojo-graph-api.pom
%{_datadir}/maven2/poms/JPP.mojo-maven-diagrams-plugin.pom
%if %{gcj_support}
%{_libdir}/gcj/%{name}/diagram-*.jar.*
%endif
%endif

%if %{docbook_include}
%files -n mojo-maven2-plugin-docbook
%{_javadir}/mojo/docbook*.jar
%{_datadir}/maven2/poms/JPP.mojo-docbook-maven-plugin*.pom
%if %{gcj_support}
%{_libdir}/gcj/%{name}/docbook-*.jar.*
%endif
%endif

%if %{ejbdoclet_include}
%files -n mojo-maven2-plugin-ejbdoclet
%{_javadir}/mojo/ejbdoclet*.jar
%{_datadir}/maven2/poms/JPP.mojo-ejbdoclet-maven-plugin*.pom
%if %{gcj_support}
%{_libdir}/gcj/%{name}/ejbdoclet-*.jar.*
%endif
%endif

%if %{emma_include}
%files -n mojo-maven2-plugin-emma
%{_javadir}/mojo/emma*.jar
%{_datadir}/maven2/poms/JPP.mojo-emma-maven-plugin*.pom
%if %{gcj_support}
%{_libdir}/gcj/%{name}/emma-*.jar.*
%endif
%endif

%if %{exec_include}
%files -n mojo-maven2-plugin-exec
%{_javadir}/mojo/exec*.jar
%{_datadir}/maven2/poms/JPP.mojo-exec-maven-plugin*.pom
%if %{gcj_support}
%{_libdir}/gcj/%{name}/exec-*.jar.*
%endif
%endif

%if %{fileutils_include}
%files -n mojo-maven2-plugin-fileutils
%{_javadir}/mojo/fileutils*.jar
%{_datadir}/maven2/poms/JPP.mojo-fileutils-maven-plugin*.pom
%if %{gcj_support}
%{_libdir}/gcj/%{name}/fileutils-*.jar.*
%endif
%endif

%if %{findbugs_include}
%files -n mojo-maven2-plugin-findbugs
%{_javadir}/mojo/findbugs*.jar
%{_datadir}/maven2/poms/JPP.mojo-findbugs-maven-plugin*.pom
%if %{gcj_support}
%{_libdir}/gcj/%{name}/findbugs-*.jar.*
%endif
%endif

%if %{fit_include}
%files -n mojo-maven2-plugin-fit
%{_javadir}/mojo/fit*.jar
%{_datadir}/maven2/poms/JPP.mojo-fit-maven-plugin*.pom
%if %{gcj_support}
%{_libdir}/gcj/%{name}/fit-*.jar.*
%endif
%endif

%if %{freemarker_include}
%files -n mojo-maven2-plugin-freemarker
%{_javadir}/mojo/freemarker*.jar
%{_datadir}/maven2/poms/JPP.mojo-freemarker-maven-plugin*.pom
%if %{gcj_support}
%{_libdir}/gcj/%{name}/freemarker-*.jar.*
%endif
%endif

%if %{ganalytics_include}
%files -n mojo-maven2-plugin-ganalytics
%{_javadir}/mojo/ganalytics*.jar
%{_datadir}/maven2/poms/JPP.mojo-ganalytics-maven-plugin*.pom
%if %{gcj_support}
%{_libdir}/gcj/%{name}/ganalytics-*.jar.*
%endif
%endif

%if %{graphing_include}
%files -n mojo-maven2-plugin-graphing
%{_javadir}/mojo/graphing*.jar
%{_datadir}/maven2/poms/JPP.mojo-graphing-maven-plugin*.pom
%if %{gcj_support}
%{_libdir}/gcj/%{name}/graphing-*.jar.*
%endif
%endif

%if %{hibernate2_include}
%files -n mojo-maven2-plugin-hibernate2
%{_javadir}/mojo/hibernate2*.jar
%{_datadir}/maven2/poms/JPP.mojo-hibernate2-maven-plugin*.pom
%if %{gcj_support}
%{_libdir}/gcj/%{name}/hibernate2-*.jar.*
%endif
%endif

%if %{hibernate3_include}
%files -n mojo-maven2-hibernate3
%{_javadir}/mojo/hibernate3-maven-plugin*.jar
%{_javadir}/mojo/maven-hibernate3*.jar
%{_datadir}/maven2/poms/JPP.mojo-hibernate3-maven-plugin.pom
%{_datadir}/maven2/poms/JPP.mojo-maven-hibernate3*.pom
%{_datadir}/maven2/poms/JPP.mojo-hibernate3.pom
%if %{gcj_support}
%{_libdir}/gcj/%{name}/hibernate3-*.jar.*
%endif
%endif

%if %{hibernatedoclet_include}
%files -n mojo-maven2-plugin-hibernatedoclet
%{_javadir}/mojo/hibernatedoclet*.jar
%{_datadir}/maven2/poms/JPP.mojo-hibernatedoclet-maven-plugin*.pom
%if %{gcj_support}
%{_libdir}/gcj/%{name}/hibernatedoclet-*.jar.*
%endif
%endif

%if %{hsqldb_include}
%files -n mojo-maven2-plugin-hsqldb
%{_javadir}/mojo/maven-hsqldb-plugin*.jar
%{_datadir}/maven2/poms/JPP.mojo-maven-hsqldb-plugin.pom
%if %{gcj_support}
%{_libdir}/gcj/%{name}/maven-hsqldb-plugin*.jar.*
%endif
%endif

%if %{ibatis_include}
%files -n mojo-maven2-plugin-ibatis
%{_javadir}/mojo/ibatis*.jar
%{_datadir}/maven2/poms/JPP.mojo-ibatis-maven-plugin*.pom
%if %{gcj_support}
%{_libdir}/gcj/%{name}/ibatis-*.jar.*
%endif
%endif

%if %{idlj_include}
%files -n mojo-maven2-plugin-idlj
%{_javadir}/mojo/idlj*.jar
%{_datadir}/maven2/poms/JPP.mojo-idlj-maven-plugin*.pom
%if %{gcj_support}
%{_libdir}/gcj/%{name}/idlj-*.jar.*
%endif
%endif

%if %{j2me_include}
%files -n mojo-maven2-plugin-j2me
%{_javadir}/mojo/j2me*.jar
%{_datadir}/maven2/poms/JPP.mojo-j2me-maven-plugin*.pom
%if %{gcj_support}
%{_libdir}/gcj/%{name}/j2me-*.jar.*
%endif
%endif

%if %{jalopy_include}
%files -n mojo-maven2-plugin-jalopy
%{_javadir}/mojo/jalopy*.jar
%{_datadir}/maven2/poms/JPP.mojo-jalopy-maven-plugin*.pom
%if %{gcj_support}
%{_libdir}/gcj/%{name}/jalopy-*.jar.*
%endif
%endif

%if %{jardiff_include}
%files -n mojo-maven2-plugin-jardiff
%{_javadir}/mojo/jardiff*.jar
%{_datadir}/maven2/poms/JPP.mojo-jardiff-maven-plugin*.pom
%if %{gcj_support}
%{_libdir}/gcj/%{name}/jardiff-*.jar.*
%endif
%endif

%if %{jasperreports_include}
%files -n mojo-maven2-plugin-jasperreports
%{_javadir}/mojo/jasperreports*.jar
%{_datadir}/maven2/poms/JPP.mojo-jasperreports-maven-plugin*.pom
%if %{gcj_support}
%{_libdir}/gcj/%{name}/jasperreports-*.jar.*
%endif
%endif

%if %{javacc_include}
%files -n mojo-maven2-plugin-javacc
%{_javadir}/mojo/javacc*.jar
%{_datadir}/maven2/poms/JPP.mojo-javacc-maven-plugin*.pom
%if %{gcj_support}
%{_libdir}/gcj/%{name}/javacc-*.jar.*
%endif
%endif

%if %{javancss_include}
%files -n mojo-maven2-plugin-javancss
%{_javadir}/mojo/javancss*.jar
%{_datadir}/maven2/poms/JPP.mojo-javancss-maven-plugin*.pom
%if %{gcj_support}
%{_libdir}/gcj/%{name}/javancss-*.jar.*
%endif
%endif

%if %{jaxb2_include}
%files -n mojo-maven2-plugin-jaxb2
%{_javadir}/mojo/jaxb2*.jar
%{_datadir}/maven2/poms/JPP.mojo-jaxb2-maven-plugin*.pom
%if %{gcj_support}
%{_libdir}/gcj/%{name}/jaxb2-*.jar.*
%endif
%endif

%if %{jaxws_include}
%files -n mojo-maven2-plugin-jaxws
%{_javadir}/mojo/jaxws*.jar
%{_datadir}/maven2/poms/JPP.mojo-jaxws-maven-plugin*.pom
%if %{gcj_support}
%{_libdir}/gcj/%{name}/jaxws-*.jar.*
%endif
%endif

%if %{jboss_include}
%files -n mojo-maven2-plugin-jboss
%{_javadir}/mojo/jboss*.jar
%{_datadir}/maven2/poms/JPP.mojo-jboss-maven-plugin*.pom
%if %{gcj_support}
%{_libdir}/gcj/%{name}/jboss-*.jar.*
%endif
%endif

%if %{jboss_packaging_include}
%files -n mojo-maven2-plugin-jboss-packaging
%{_javadir}/mojo/jboss-packaging*.jar
%{_datadir}/maven2/poms/JPP.mojo-jboss-packaging-maven-plugin*.pom
%if %{gcj_support}
%{_libdir}/gcj/%{name}/jboss-packaging-*.jar.*
%endif
%endif

%if %{jdepend_include}
%files -n mojo-maven2-plugin-jdepend
%{_javadir}/mojo/jdepend*.jar
%{_datadir}/maven2/poms/JPP.mojo-jdepend-maven-plugin*.pom
%if %{gcj_support}
%{_libdir}/gcj/%{name}/jdepend-*.jar.*
%endif
%endif

%if %{jdiff_include}
%files -n mojo-maven2-plugin-jdiff
%{_javadir}/mojo/jdiff*.jar
%{_datadir}/maven2/poms/JPP.mojo-jdiff-maven-plugin*.pom
%if %{gcj_support}
%{_libdir}/gcj/%{name}/jdiff-*.jar.*
%endif
%endif

%if %{jellyapi_include}
%files -n mojo-maven2-plugin-jellyapi
%{_javadir}/mojo/jellyapi*.jar
%{_datadir}/maven2/poms/JPP.mojo-jellyapi-maven-plugin*.pom
%if %{gcj_support}
%{_libdir}/gcj/%{name}/jellyapi-*.jar.*
%endif
%endif

%if %{jellymojo_include}
%files -n mojo-maven2-archetype-jellymojo
%{_javadir}/mojo/jellymojo*.jar
%{_datadir}/maven2/poms/JPP.mojo-jellymojo*.pom
%if %{gcj_support}
%{_libdir}/gcj/%{name}/jellymojo-*.jar.*
%endif
%endif

%if %{jetty_include}
%files -n mojo-maven2-plugin-jetty
%{_javadir}/mojo/jetty*.jar
%{_datadir}/maven2/poms/JPP.mojo-jetty-maven-plugin*.pom
%if %{gcj_support}
%{_libdir}/gcj/%{name}/jetty-*.jar.*
%endif
%endif

%if %{jettybin_include}
%files -n mojo-maven2-plugin-jettybin
%{_javadir}/mojo/jettybin*.jar
%{_datadir}/maven2/poms/JPP.mojo-jettybin-maven-plugin*.pom
%if %{gcj_support}
%{_libdir}/gcj/%{name}/jettybin-*.jar.*
%endif
%endif

%if %{jpox_include}
%files -n mojo-maven2-plugin-jpox
%{_javadir}/mojo/jpox*.jar
%{_datadir}/maven2/poms/JPP.mojo-jpox-maven-plugin*.pom
%if %{gcj_support}
%{_libdir}/gcj/%{name}/jpox-*.jar.*
%endif
%endif

%if %{jruby_include}
%files -n mojo-maven2-jruby
%{_javadir}/mojo/jruby*.jar
%{_datadir}/maven2/poms/JPP.mojo-jruby*.pom
%if %{gcj_support}
%{_libdir}/gcj/%{name}/jruby-*.jar.*
%endif
%endif

%if %{jspc_include}
%files -n mojo-maven2-plugin-jspc
%{_javadir}/mojo/jspc-maven-plugin*.jar
%{_javadir}/mojo/jspc-compiler-api*.jar
%{_datadir}/maven2/poms/JPP.mojo-jspc-maven-plugin.pom
%{_datadir}/maven2/poms/JPP.mojo-jspc-compiler-api.pom
%{_datadir}/maven2/poms/JPP.mojo-jspc-compilers.pom
%{_datadir}/maven2/poms/JPP.mojo-jspc.pom
%if %{gcj_support}
%{_libdir}/gcj/%{name}/jspc-*.jar.*
%endif

%files -n mojo-maven2-jspc-compiler-tomcat5
%{_javadir}/mojo/jspc-compiler-tomcat5*.jar
%{_datadir}/maven2/poms/JPP.mojo-jspc-compiler-tomcat5.pom
%if %{gcj_support}
%{_libdir}/gcj/%{name}/jspc-*.jar.*
%endif

%files -n mojo-maven2-jspc-compiler-tomcat6
%{_javadir}/mojo/jspc-compiler-tomcat6*.jar
%{_datadir}/maven2/poms/JPP.mojo-jspc-compiler-tomcat6.pom
%if %{gcj_support}
%{_libdir}/gcj/%{name}/jspc-*.jar.*
%endif
%endif

%if %{wagon_cifs_include}
%files -n mojo-maven2-wagon-cifs
%{_javadir}/mojo/wagon-cifs*.jar
%{_datadir}/maven2/poms/JPP.mojo-wagon-cifs.pom
%{_datadir}/maven2/poms/JPP.mojo-maven-extensions.pom
%if %{gcj_support}
%{_libdir}/gcj/%{name}/wagon-cifs-*.jar.*
%endif
%endif

%if %{keytool_include}
%files -n mojo-maven2-plugin-keytool
%{_javadir}/mojo/keytool*.jar
%{_datadir}/maven2/poms/JPP.mojo-keytool-maven-plugin*.pom
%if %{gcj_support}
%{_libdir}/gcj/%{name}/keytool-*.jar.*
%endif
%endif

%if %{mojo_archetypes_include}
%files -n mojo-maven2-archetypes
%{_javadir}/mojo/maven-archetype-simple-jboss-jee*.jar
%{_javadir}/mojo/nbm-archetype*.jar
%{_javadir}/mojo/netbeans-platform-app-archetype*.jar
%{_datadir}/maven2/poms/JPP.mojo-maven-archetype-simple-jboss-jee.pom
%{_datadir}/maven2/poms/JPP.mojo-nbm-archetype.pom
%{_datadir}/maven2/poms/JPP.mojo-netbeans-platform-app-archetype.pom
%{_datadir}/maven2/poms/JPP.mojo-mojo-archetypes.pom
%if %{gcj_support}
%{_libdir}/gcj/%{name}/archetype-*.jar.*
%endif
%endif

%if %{l10n_include}
%files -n mojo-maven2-plugin-l10n
%{_javadir}/mojo/l10n*.jar
%{_datadir}/maven2/poms/JPP.mojo-l10n-maven-plugin*.pom
%if %{gcj_support}
%{_libdir}/gcj/%{name}/l10n-*.jar.*
%endif
%endif

%if %{mant_include}
%files -n mojo-maven2-plugin-mant
%{_javadir}/mojo/mant*.jar
%{_datadir}/maven2/poms/JPP.mojo-mant-maven-plugin*.pom
%if %{gcj_support}
%{_libdir}/gcj/%{name}/mant-*.jar.*
%endif
%endif

%if %{mojo_was_plugin_anttasks_include}
%files -n mojo-maven2-was
%{_javadir}/mojo/was*.jar
%{_datadir}/maven2/poms/JPP.mojo-was*.pom
%{_datadir}/maven2/poms/JPP.mojo-mojo-was.pom
%if %{gcj_support}
%{_libdir}/gcj/%{name}/was-*.jar.*
%endif
%endif

%if %{minijar_include}
%files -n mojo-maven2-plugin-minijar
%{_javadir}/mojo/minijar*.jar
%{_datadir}/maven2/poms/JPP.mojo-minijar-maven-plugin*.pom
%if %{gcj_support}
%{_libdir}/gcj/%{name}/minijar-*.jar.*
%endif
%endif

%if %{native_include}
%files -n mojo-maven2-natives
%{_javadir}/mojo/maven-native*.jar
%{_javadir}/mojo/native-maven-plugin*.jar
%{_datadir}/maven2/poms/JPP.mojo-native-maven-plugin.pom
%{_datadir}/maven2/poms/JPP.mojo-maven-native*.pom
%if %{gcj_support}
%{_libdir}/gcj/%{name}/native-*.jar.*
%{_libdir}/gcj/%{name}/maven-native-*.jar.*
%endif
%endif

%if %{native2ascii_include}
%files -n mojo-maven2-plugin-native2ascii
%{_javadir}/mojo/native2ascii*.jar
%{_datadir}/maven2/poms/JPP.mojo-native2ascii-maven-plugin*.pom
%if %{gcj_support}
%{_libdir}/gcj/%{name}/native2ascii-*.jar.*
%endif
%endif

%if %{netbeans_freeform_include}
%files -n mojo-maven2-plugin-netbeans-freeform
%{_javadir}/mojo/netbeans-freeform*.jar
%{_datadir}/maven2/poms/JPP.mojo-netbeans-freeform-maven-plugin*.pom
%if %{gcj_support}
%{_libdir}/gcj/%{name}/netbeans-freeform-*.jar.*
%endif
%endif

%if %{openjpa_include}
%files -n mojo-maven2-plugin-openjpa
%{_javadir}/mojo/openjpa*.jar
%{_datadir}/maven2/poms/JPP.mojo-openjpa-maven-plugin*.pom
%if %{gcj_support}
%{_libdir}/gcj/%{name}/openjpa-*.jar.*
%endif
%endif

%if %{osxappbundle_include}
%files -n mojo-maven2-plugin-osxappbundle
%{_javadir}/mojo/osxappbundle*.jar
%{_datadir}/maven2/poms/JPP.mojo-osxappbundle-maven-plugin*.pom
%if %{gcj_support}
%{_libdir}/gcj/%{name}/osxappbundle-*.jar.*
%endif
%endif

%if %{ounce_include}
%files -n mojo-maven2-plugin-ounce
%{_javadir}/mojo/ounce*.jar
%{_datadir}/maven2/poms/JPP.mojo-ounce-maven-plugin*.pom
%if %{gcj_support}
%{_libdir}/gcj/%{name}/ounce-*.jar.*
%endif
%endif

%if %{plugin_support_include}
%files -n mojo-maven2-support
%{_javadir}/mojo/plugin-support*.jar
%{_datadir}/maven2/poms/JPP.mojo-plugin-support*.pom
%if %{gcj_support}
%{_libdir}/gcj/%{name}/plugin-support-*.jar.*
%endif
%endif

%if %{pomtools_include}
%files -n mojo-maven2-plugin-pomtools
%{_javadir}/mojo/pomtools*.jar
%{_datadir}/maven2/poms/JPP.mojo-pomtools-maven-plugin*.pom
%if %{gcj_support}
%{_libdir}/gcj/%{name}/pomtools-*.jar.*
%endif
%endif

%if %{properties_include}
%files -n mojo-maven2-plugin-properties
%{_javadir}/mojo/properties*.jar
%{_datadir}/maven2/poms/JPP.mojo-properties-maven-plugin*.pom
%if %{gcj_support}
%{_libdir}/gcj/%{name}/properties-*.jar.*
%endif
%endif

%if %{push_include}
%files -n mojo-maven2-plugin-push
%{_javadir}/mojo/push*.jar
%{_datadir}/maven2/poms/JPP.mojo-push-maven-plugin*.pom
%if %{gcj_support}
%{_libdir}/gcj/%{name}/push-*.jar.*
%endif
%endif

%if %{retroweaver_include}
%files -n mojo-maven2-plugin-retroweaver
%{_javadir}/mojo/retroweaver*.jar
%{_datadir}/maven2/poms/JPP.mojo-retroweaver-maven-plugin*.pom
%if %{gcj_support}
%{_libdir}/gcj/%{name}/retroweaver-*.jar.*
%endif
%endif

%if %{retrotranslator_include}
%files -n mojo-maven2-plugin-retrotranslator
%{_javadir}/mojo/retrotranslator*.jar
%{_datadir}/maven2/poms/JPP.mojo-retrotranslator-maven-plugin*.pom
%if %{gcj_support}
%{_libdir}/gcj/%{name}/retrotranslator-*.jar.*
%endif
%endif

%if %{rat_include}
%files -n mojo-maven2-plugin-rat
%{_javadir}/mojo/rat*.jar
%{_datadir}/maven2/poms/JPP.mojo-rat-maven-plugin*.pom
%if %{gcj_support}
%{_libdir}/gcj/%{name}/rat-*.jar.*
%endif
%endif

%if %{rmic_include}
%files -n mojo-maven2-plugin-rmic
%{_javadir}/mojo/rmic*.jar
%{_datadir}/maven2/poms/JPP.mojo-rmic-maven-plugin*.pom
%if %{gcj_support}
%{_libdir}/gcj/%{name}/rmic-*.jar.*
%endif
%endif

%if %{rpm_include}
%files -n mojo-maven2-plugin-rpm
%{_javadir}/mojo/rpm*.jar
%{_datadir}/maven2/poms/JPP.mojo-rpm-maven-plugin*.pom
%if %{gcj_support}
%{_libdir}/gcj/%{name}/rpm-*.jar.*
%endif
%endif

%if %{rubyscript_include}
%files -n mojo-maven2-archetype-rubyscript
%{_javadir}/mojo/archetype-maven-rubyscript*.jar
%{_datadir}/maven2/poms/JPP.mojo-archetype-maven-rubyscript.pom
%{_datadir}/maven2/poms/JPP.mojo-rubyscript-maven-tools.pom
%{_datadir}/maven2/poms/JPP.mojo-rubyscript-parent-maven-plugin.pom
%if %{gcj_support}
%{_libdir}/gcj/%{name}/archetype-maven-rubyscript-*.jar.*
%endif
%endif

%if %{runtime_builder_include}
%files -n mojo-maven2-plugin-runtime-builder
%{_javadir}/mojo/runtime-builder*.jar
%{_datadir}/maven2/poms/JPP.mojo-runtime-builder-maven-plugin*.pom
%if %{gcj_support}
%{_libdir}/gcj/%{name}/runtime-builder-*.jar.*
%endif
%endif

%if %{sablecc_include}
%files -n mojo-maven2-plugin-sablecc
%{_javadir}/mojo/sablecc*.jar
%{_datadir}/maven2/poms/JPP.mojo-sablecc-maven-plugin*.pom
%if %{gcj_support}
%{_libdir}/gcj/%{name}/sablecc-*.jar.*
%endif
%endif

%if %{script_include}
%files -n mojo-maven2-plugin-script
%{_javadir}/mojo/script*.jar
%{_datadir}/maven2/poms/JPP.mojo-script-maven-plugin*.pom
%if %{gcj_support}
%{_libdir}/gcj/%{name}/script-*.jar.*
%endif
%endif

%if %{selenium_include}
%files -n mojo-maven2-plugin-selenium
%{_javadir}/mojo/selenium*.jar
%{_datadir}/maven2/poms/JPP.mojo-selenium-maven-plugin*.pom
%if %{gcj_support}
%{_libdir}/gcj/%{name}/selenium-*.jar.*
%endif
%endif

%if %{shade_include}
%files -n mojo-maven2-plugin-shade
%{_javadir}/mojo/shade*.jar
%{_datadir}/maven2/poms/JPP.mojo-shade-maven-plugin*.pom
%if %{gcj_support}
%{_libdir}/gcj/%{name}/shade-*.jar.*
%endif
%endif

%if %{shell_include}
%files -n mojo-maven2-plugin-shell
%{_javadir}/mojo/shell*.jar
%{_datadir}/maven2/poms/JPP.mojo-shell-maven-plugin*.pom
%if %{gcj_support}
%{_libdir}/gcj/%{name}/shell-*.jar.*
%endif
%endif

%if %{shitty_include}
%files -n mojo-maven2-plugin-shitty
%{_javadir}/mojo/shitty*.jar
%{_datadir}/maven2/poms/JPP.mojo-shitty-maven-plugin*.pom
%if %{gcj_support}
%{_libdir}/gcj/%{name}/shitty-*.jar.*
%endif
%endif

%if %{testing_simple_include}
%files -n mojo-maven2-plugin-simple
%{_javadir}/mojo/maven-simple-plugin*.jar
%{_datadir}/maven2/poms/JPP.mojo-maven-simple-plugin.pom
%if %{gcj_support}
%{_libdir}/gcj/%{name}/maven-simple-plugin*.jar.*
%endif
%endif

%if %{smc_include}
%files -n mojo-maven2-plugin-smc
%{_javadir}/mojo/smc*.jar
%{_datadir}/maven2/poms/JPP.mojo-smc-maven-plugin*.pom
%if %{gcj_support}
%{_libdir}/gcj/%{name}/smc-*.jar.*
%endif
%endif

%if %{springbeandoc_include}
%files -n mojo-maven2-plugin-springbeandoc
%{_javadir}/mojo/maven-springbeandoc-plugin*.jar
%{_datadir}/maven2/poms/JPP.mojo-maven-springbeandoc-plugin.pom
%if %{gcj_support}
%{_libdir}/gcj/%{name}/maven-springbeandoc-plugin*.jar.*
%endif
%endif

%if %{springdoclet_include}
%files -n mojo-maven2-plugin-springdoclet
%{_javadir}/mojo/springdoclet*.jar
%{_datadir}/maven2/poms/JPP.mojo-springdoclet-maven-plugin*.pom
%if %{gcj_support}
%{_libdir}/gcj/%{name}/springdoclet-*.jar.*
%endif
%endif

%if %{sql_include}
%files -n mojo-maven2-plugin-sql
%{_javadir}/mojo/sql*.jar
%{_datadir}/maven2/poms/JPP.mojo-sql-maven-plugin*.pom
%if %{gcj_support}
%{_libdir}/gcj/%{name}/sql-*.jar.*
%endif
%endif

%if %{sysdeo_tomcat_include}
%files -n mojo-maven2-plugin-sysdeo-tomcat
%{_javadir}/mojo/sysdeo-tomcat*.jar
%{_datadir}/maven2/poms/JPP.mojo-sysdeo-tomcat-plugin.pom
%if %{gcj_support}
%{_libdir}/gcj/%{name}/sysdeo-tomcat-*.jar.*
%endif
%endif

%if %{taglist_include}
%files -n mojo-maven2-plugin-taglist
%{_javadir}/mojo/taglist*.jar
%{_datadir}/maven2/poms/JPP.mojo-taglist-maven-plugin*.pom
%if %{gcj_support}
%{_libdir}/gcj/%{name}/taglist-*.jar.*
%endif
%endif

%if %{tomcat_include}
%files -n mojo-maven2-plugin-tomcat
%{_javadir}/mojo/tomcat*.jar
%{_datadir}/maven2/poms/JPP.mojo-tomcat-maven-plugin*.pom
%if %{gcj_support}
%{_libdir}/gcj/%{name}/tomcat-*.jar.*
%endif
%endif

%if %{visibroker_include}
%files -n mojo-maven2-plugin-visibroker
%{_javadir}/mojo/visibroker*.jar
%{_datadir}/maven2/poms/JPP.mojo-visibroker-maven-plugin*.pom
%if %{gcj_support}
%{_libdir}/gcj/%{name}/visibroker-*.jar.*
%endif
%endif

%if %{wagon_include}
%files -n mojo-maven2-plugin-wagon
%{_javadir}/mojo/wagon*.jar
%{_datadir}/maven2/poms/JPP.mojo-wagon-maven-plugin*.pom
%if %{gcj_support}
%{_libdir}/gcj/%{name}/wagon-*.jar.*
%endif
%endif

%if %{webdoclet_include}
%files -n mojo-maven2-plugin-webdoclet
%{_javadir}/mojo/webdoclet*.jar
%{_datadir}/maven2/poms/JPP.mojo-webdoclet-maven-plugin*.pom
%if %{gcj_support}
%{_libdir}/gcj/%{name}/webdoclet-*.jar.*
%endif
%endif

%if %{webstart_include}
%files -n mojo-maven2-plugin-webstart
%{_javadir}/mojo/webstart*.jar
%{_datadir}/maven2/poms/JPP.mojo-webstart*.pom
%if %{gcj_support}
%{_libdir}/gcj/%{name}/webstart-*.jar.*
%endif
%endif

%if %{wsdl2java_include}
%files -n mojo-maven2-plugin-wsdl2java
%{_javadir}/mojo/wsdl2java*.jar
%{_datadir}/maven2/poms/JPP.mojo-wsdl2java-maven-plugin*.pom
%if %{gcj_support}
%{_libdir}/gcj/%{name}/wsdl2java-*.jar.*
%endif
%endif

%if %{xdoclet_include}
%files -n mojo-maven2-plugin-xdoclet
%{_javadir}/mojo/xdoclet*.jar
%{_datadir}/maven2/poms/JPP.mojo-xdoclet-maven-plugin*.pom
%if %{gcj_support}
%{_libdir}/gcj/%{name}/xdoclet-*.jar.*
%endif
%endif

%if %{xfire_include}
%files -n mojo-maven2-plugin-xfire
%{_javadir}/mojo/xfire*.jar
%{_datadir}/maven2/poms/JPP.mojo-xfire-maven-plugin*.pom
%if %{gcj_support}
%{_libdir}/gcj/%{name}/xfire-*.jar.*
%endif
%endif

%if %{xjc_include}
%files -n mojo-maven2-plugin-xjc
%{_javadir}/mojo/xjc*.jar
%{_datadir}/maven2/poms/JPP.mojo-xjc-maven-plugin*.pom
%if %{gcj_support}
%{_libdir}/gcj/%{name}/xjc-*.jar.*
%endif
%endif

%if %{xmlbeans_include}
%files -n mojo-maven2-plugin-xmlbeans
%{_javadir}/mojo/xmlbeans*.jar
%{_datadir}/maven2/poms/JPP.mojo-xmlbeans-maven-plugin*.pom
%if %{gcj_support}
%{_libdir}/gcj/%{name}/xmlbeans-*.jar.*
%endif
%endif

%if %{xml_include}
%files -n mojo-maven2-plugin-xml
%{_javadir}/mojo/xml*.jar
%{_datadir}/maven2/poms/JPP.mojo-xml-maven-plugin*.pom
%if %{gcj_support}
%{_libdir}/gcj/%{name}/xml-*.jar.*
%endif
%endif

%if %{xslt_include}
%files -n mojo-maven2-plugin-xslt
%{_javadir}/mojo/xslt*.jar
%{_datadir}/maven2/poms/JPP.mojo-xslt-maven-plugin*.pom
%if %{gcj_support}
%{_libdir}/gcj/%{name}/xslt-*.jar.*
%endif
%endif

%if %{xsltc_include}
%files -n mojo-maven2-plugin-xsltc
%{_javadir}/mojo/xsltc*.jar
%{_datadir}/maven2/poms/JPP.mojo-xsltc-maven-plugin*.pom
%if %{gcj_support}
%{_libdir}/gcj/%{name}/xsltc-*.jar.*
%endif
%endif

%if %{solaris_include}
%files -n mojo-maven2-solaris
%{_javadir}/mojo/solaris*.jar
%{_datadir}/maven2/poms/JPP.mojo-solaris*.pom
%if %{gcj_support}
%{_libdir}/gcj/%{name}/solaris-*.jar.*
%endif
%endif

%files javadoc
%{_javadocdir}/*

%changelog
* Sat Feb 11 2012 Igor Vlasenko <viy@altlinux.ru> 0:17-alt20_8jpp6
- fixed findbugs dependencies

* Fri Feb 10 2012 Igor Vlasenko <viy@altlinux.ru> 0:17-alt19_8jpp6
- disabled xfire

* Fri Feb 10 2012 Igor Vlasenko <viy@altlinux.ru> 0:17-alt18_8jpp6
- new version

* Sun Jan 22 2012 Igor Vlasenko <viy@altlinux.ru> 0:17-alt18_7jpp6
- fixed build (poi25 mapping)

* Sat Jan 21 2012 Igor Vlasenko <viy@altlinux.ru> 0:17-alt17_7jpp6
- use new jasperreports2

* Sun Jan 15 2012 Igor Vlasenko <viy@altlinux.ru> 0:17-alt16_7jpp6
- new version

* Thu Jun 02 2011 Igor Vlasenko <viy@altlinux.ru> 0:17-alt16_1jpp5
- fixed build

* Sat Feb 26 2011 Igor Vlasenko <viy@altlinux.ru> 0:17-alt15_1jpp5
- build with velocity14; added jpp-depmapping for velocity 

* Mon Feb 07 2011 Igor Vlasenko <viy@altlinux.ru> 0:17-alt14_1jpp5
- build without hibernate3

* Mon Feb 07 2011 Igor Vlasenko <viy@altlinux.ru> 0:17-alt13_1jpp5
- fixed build

* Tue Feb 01 2011 Igor Vlasenko <viy@altlinux.ru> 0:17-alt12_1jpp5
- restored build of archetypes

* Thu Jan 27 2011 Igor Vlasenko <viy@altlinux.ru> 0:17-alt11_1jpp5
- fixed modello plugin dep

* Sun Jan 23 2011 Igor Vlasenko <viy@altlinux.ru> 0:17-alt10_1jpp5
- fixed build with plexus-archiver a7;
  hacks wrapped as if_with plexus_a7

* Thu Dec 30 2010 Igor Vlasenko <viy@altlinux.ru> 0:17-alt9_1jpp5
- fixed build with new groovy

* Sat Dec 04 2010 Igor Vlasenko <viy@altlinux.ru> 0:17-alt8_1jpp5
- fixed build with new fop, batik

* Thu Sep 30 2010 Igor Vlasenko <viy@altlinux.ru> 0:17-alt7_1jpp5
- fixed build with new maven 2.0.8

* Wed May 19 2010 Igor Vlasenko <viy@altlinux.ru> 0:17-alt6_1jpp5
- explicit selection of java5 compiler

* Tue Mar 23 2010 Igor Vlasenko <viy@altlinux.ru> 0:17-alt5_1jpp5
- fixed build with new javancss

* Tue Jun 09 2009 Igor Vlasenko <viy@altlinux.ru> 0:17-alt4_1jpp5
- fixed build

* Fri Mar 13 2009 Igor Vlasenko <viy@altlinux.ru> 0:17-alt3_1jpp5
- more plugins

* Tue Mar 03 2009 Igor Vlasenko <viy@altlinux.ru> 0:17-alt2_1jpp5
- added plugins

* Fri Feb 13 2009 Igor Vlasenko <viy@altlinux.ru> 0:17-alt1_1jpp5
- new version

* Wed Dec 10 2008 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt1_10jpp5
- fixed build w/jpp5

* Mon Dec 03 2007 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt1_10jpp1.7
- converted from JPackage by jppimport script

* Sat Nov 24 2007 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt1_0jpp1.7
- converted from JPackage by jppimport script
- disabled jpox, fit, xmlbeans
