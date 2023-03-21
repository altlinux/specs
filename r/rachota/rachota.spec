Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires: /usr/bin/desktop-file-install swig
# END SourceDeps(oneline)
BuildRequires: /proc rpm-build-java
BuildRequires: jpackage-default
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%global checkout 602hg
Name:           rachota
Version:        2.4
Release:        alt1_1.602hgjpp11
Summary:        Straightforward timetracking

License:        CDDL-1.0
URL:            http://rachota.sourceforge.net/en/index.html
## Upstream does not provide any source tarball.
## We have to check them out via mercurial.
# hg clone http://hg.code.sf.net/p/rachota/code rachota
# cd rachota
# hg update -c 602
# cd ..
# tar caf rachota.tar.gz rachota
Source0:        %{name}.tar.gz
Source1:        %{name}.desktop
Source2:        %{name}.png

BuildArch:      noarch

BuildRequires:  jpackage-utils

BuildRequires:  junit

BuildRequires:  maven-local

BuildRequires:  desktop-file-utils

Requires:       jpackage-utils

Requires:       java
Source44: import.info

%description
Rachota is a portable application for timetracking different projects. It runs
everywhere. It displays time data in diagram form, creates customized reports
and invoices or analyses measured data and suggests hints to improve user's
time usage. The totally portable yet personal timetracker. 

%package javadoc
Group: Development/Java
Summary:        Javadocs for %{name}
Requires:       jpackage-utils
BuildArch: noarch

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q -n %{name}

%build
%mvn_build -- -Dmaven.compiler.source=1.8 -Dmaven.compiler.target=1.8 -Dmaven.javadoc.source=1.8 -Dmaven.compiler.release=8

%install
%mvn_install

%jpackage_script org.cesilko.rachota.gui.MainWindow "" "" %{name} %{name} true

install -D -m 644 %{SOURCE2} $RPM_BUILD_ROOT%{_datadir}/pixmaps/%{name}.png

desktop-file-install --dir=$RPM_BUILD_ROOT%{_datadir}/applications %{SOURCE1}

mkdir -p $RPM_BUILD_ROOT`dirname /etc/java/%{name}.conf`
touch $RPM_BUILD_ROOT/etc/java/%{name}.conf



%files -f .mfiles
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.png
%config(noreplace,missingok) /etc/java/%{name}.conf

%files javadoc -f .mfiles-javadoc


%changelog
* Mon Mar 20 2023 Igor Vlasenko <viy@altlinux.org> 2.4-alt1_1.602hgjpp11
- new version

* Mon Jun 07 2021 Igor Vlasenko <viy@altlinux.org> 2.3-alt1_21.20130104cvsjpp11
- rebuild with java11 and use jvm_run

* Sat Feb 15 2020 Igor Vlasenko <viy@altlinux.ru> 2.3-alt1_18.20130104cvsjpp8
- fc update

* Sun May 26 2019 Igor Vlasenko <viy@altlinux.ru> 2.3-alt1_16.20130104cvsjpp8
- new version

* Mon Apr 16 2018 Igor Vlasenko <viy@altlinux.ru> 2.3-alt1_14.20130104cvsjpp8
- java update

* Thu Nov 09 2017 Igor Vlasenko <viy@altlinux.ru> 2.3-alt1_13.20130104cvsjpp8
- fc27 update

* Tue Oct 17 2017 Igor Vlasenko <viy@altlinux.ru> 2.3-alt1_12.20130104cvsjpp8
- new jpp release

* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 2.3-alt1_11.20130104cvsjpp8
- new fc release

* Wed Feb 10 2016 Igor Vlasenko <viy@altlinux.ru> 2.3-alt1_10.20130104cvsjpp8
- java8 mass update

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 2.3-alt1_7.20130104cvsjpp7
- new release

* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 2.3-alt1_6.20130104cvsjpp7
- new release

* Thu Feb 07 2013 Igor Vlasenko <viy@altlinux.ru> 2.3-alt1_5.20130104cvsjpp7
- fc update

* Tue Sep 18 2012 Igor Vlasenko <viy@altlinux.ru> 2.3-alt1_4.20120110cvsjpp7
- new version

