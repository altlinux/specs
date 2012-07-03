Name:           maven1-plugins
Version:        1.1
Release:        alt5
Summary:        convenience package for all maven1 plugins

Group:          Development/Java
License:        Apache Software License 2.0
URL:            http://maven.apache.org/

Requires: maven1
Requires: maven1-plugin-announcement maven1-plugin-antlr maven1-plugin-appserver maven1-plugin-aspectwerkz maven1-plugin-cactus-jcoverage-integration maven1-plugin-caller maven1-plugin-castor maven1-plugin-changelog maven1-plugin-changes maven1-plugin-checkstyle maven1-plugin-cruisecontrol maven1-plugin-developer-activity maven1-plugin-dist maven1-plugin-docbook maven1-plugin-ear maven1-plugin-ejb maven1-plugin-faq maven1-plugin-file-activity maven1-plugin-gump maven1-plugin-html2xdoc maven1-plugin-idea maven1-plugin-itest maven1-plugin-j2ee maven1-plugin-jboss maven1-plugin-jbuilder maven1-plugin-jcoverage maven1-plugin-jdee maven1-plugin-jdepend maven1-plugin-jdeveloper maven1-plugin-jdiff maven1-plugin-jellydoc maven1-plugin-jetty maven1-plugin-jira maven1-plugin-jnlp maven1-plugin-junitdoclet maven1-plugin-jxr maven1-plugin-latex maven1-plugin-latka maven1-plugin-license maven1-plugin-linkcheck maven1-plugin-multichanges maven1-plugin-multiproject maven1-plugin-native maven1-plugin-nsis maven1-plugin-pdf maven1-plugin-pmd maven1-plugin-rar maven1-plugin-repository maven1-plugins-base maven1-plugin-scm maven1-plugin-shell maven1-plugin-site maven1-plugin-source maven1-plugin-struts maven1-plugin-tasklist maven1-plugin-test maven1-plugin-touchstone maven1-plugin-touchstone-partner maven1-plugin-uberjar maven1-plugin-vdoclet maven1-plugin-war maven1-plugin-webserver maven1-plugin-webstart maven1-plugin-xdoc
Requires: saxon-scripts
Requires: maven-scm
#Provides: maven-plugins = %version-%release
Obsoletes:  maven-plugins < 1.1-alt4

BuildArch:      noarch

%description
convenience package for all maven plugins

%prep

%build

%install

install -dm 755 $RPM_BUILD_ROOT%{_bindir}

%files

%changelog
* Thu Jan 12 2012 Igor Vlasenko <viy@altlinux.ru> 1.1-alt5
- provides maven-plugins no more

* Sun Aug 28 2011 Igor Vlasenko <viy@altlinux.ru> 1.1-alt4
- renamed to maven1-plugins

* Wed Nov 28 2007 Igor Vlasenko <viy@altlinux.ru> 1.1-alt3
- added maven-scm

* Thu Aug 02 2007 Igor Vlasenko <viy@altlinux.ru> 1.1-alt2
- added Requires: saxon-scripts

* Fri Jul 20 2007 Igor Vlasenko <viy@altlinux.ru> 1.1-alt1
- first build
