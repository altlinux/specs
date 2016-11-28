Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
BuildRequires: /usr/bin/desktop-file-install unzip
# END SourceDeps(oneline)
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
%global bcver   1.51

Name:           portecle
Version:        1.10
Release:        alt1_1jpp8
Summary:        Multipurpose keystore and certificate tool

License:        GPLv2+
URL:            http://portecle.sourceforge.net/
Source0:        http://downloads.sourceforge.net/portecle/%{name}-%{version}-src.zip
Source1:        portecle.sh.in

BuildArch:      noarch
BuildRequires:  ant
BuildRequires:  bouncycastle >= %{bcver}
BuildRequires:  bouncycastle-pkix >= %{bcver}
BuildRequires:  desktop-file-utils
BuildRequires:  jpackage-utils
Requires:       bouncycastle >= %{bcver}
Requires:       bouncycastle-pkix >= %{bcver}
# >= 1.7.5-3.9 for _prefer_jre in launcher script (#461683, #498831)
Requires:       jpackage-utils >= 1.7.5
Requires:       icon-theme-hicolor
BuildRequires:  java-devel >= 1.7.0
Requires:       jre >= 1.7.0
Source44: import.info

%description
Portecle is a user friendly GUI application for creating, managing and
examining keystores, keys, certificates, certificate requests,
certificate revocation lists and more.


%prep
%setup -q -n %{name}-%{version}-src
rm lib/bc*.jar
cp -p src/main/net/sf/portecle/images/splash.png doc/images/


%build
%ant -Djar.classpath= -Dhelpbaseurl=file://%{_docdir}/%{name}/doc/ \
    -Dbcprov.jar=$(build-classpath bcprov) \
    -Dbcpkix.jar=$(build-classpath bcpkix) jar


%install

install -Dpm 644 build/portecle.jar $RPM_BUILD_ROOT%{_javadir}/portecle.jar

install -Dpm 644 src/icons/portecle.png \
    $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/32x32/apps/portecle.png
desktop-file-install \
    --mode=644 \
    --add-mime-type=application/x-pkcs7-certificates \
    --dir=$RPM_BUILD_ROOT%{_datadir}/applications src/etc/portecle.desktop
install -Dpm 644 src/etc/portecle.appdata.xml \
    $RPM_BUILD_ROOT%{_datadir}/appdata/portecle.appdata.xml

# Enable experimental features in non-EL builds by default
install -dm 755 $RPM_BUILD_ROOT%{_bindir}
exp="%{?rhel:false}%{!?rhel:true}"
sed -e "s|@DOCDIR@|%{_docdir}/%{name}/doc|" -e "s|@EXPERIMENTAL@|$exp|" %{SOURCE1} \
    > $RPM_BUILD_ROOT%{_bindir}/portecle
chmod 755 $RPM_BUILD_ROOT%{_bindir}/portecle

mkdir -p $RPM_BUILD_ROOT`dirname /etc/java/%name.conf`
touch $RPM_BUILD_ROOT/etc/java/%name.conf


%files
%doc LICENSE.txt
%doc README.txt NEWS.txt doc/
%{_bindir}/portecle
%{_javadir}/portecle.jar
%{_datadir}/appdata/portecle.appdata.xml
%{_datadir}/applications/*portecle.desktop
%{_datadir}/icons/hicolor/32x32/apps/portecle.png
%config(noreplace,missingok) /etc/java/%name.conf


%changelog
* Fri Nov 25 2016 Igor Vlasenko <viy@altlinux.ru> 1.10-alt1_1jpp8
- new version

* Fri Feb 05 2016 Igor Vlasenko <viy@altlinux.ru> 1.9-alt1_1jpp8
- java 8 mass update

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 1.7-alt2_9jpp7
- new release

* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 1.7-alt2_8jpp7
- new release

* Tue Oct 09 2012 Igor Vlasenko <viy@altlinux.ru> 1.7-alt2_6jpp7
- new version

* Tue Oct 09 2012 Igor Vlasenko <viy@altlinux.ru> 1.7-alt1_6jpp7
- new version

