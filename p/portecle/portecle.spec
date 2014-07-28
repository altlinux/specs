Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-java
BuildRequires: unzip
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-compat
%define fedora 21
# %%name or %%version is ahead of its definition. Predefining for rpm 4.0 compatibility.
%define name portecle
%define version 1.7
%global docdir  %{_docdir}/%{name}-%{version}/doc

Name:           portecle
Version:        1.7
Release:        alt2_8jpp7
Summary:        Multipurpose keystore and certificate tool

License:        GPLv2+
URL:            http://portecle.sourceforge.net/
Source0:        http://downloads.sourceforge.net/portecle/%{name}-%{version}-src.zip
Source1:        portecle.sh.in
# http://portecle.git.sourceforge.net/git/gitweb.cgi?p=portecle/portecle;a=commitdiff;h=02e4545
Patch0:         %{name}-1.7-no-jre-check.patch

BuildArch:      noarch
BuildRequires:  ant
BuildRequires:  bouncycastle >= 1.44
BuildRequires:  desktop-file-utils
BuildRequires:  jpackage-utils
Requires:       bouncycastle >= 1.44
# >= 1.7.5-3.9 for _prefer_jre in launcher script (#461683, #498831)
Requires:       jpackage-utils >= 1.7.5-3.9
Requires:       icon-theme-hicolor
Requires:       jre >= 1.6.0
Source44: import.info

%description
Portecle is a user friendly GUI application for creating, managing and
examining keystores, keys, certificates, certificate requests,
certificate revocation lists and more.


%prep
%setup -q -n %{name}-%{version}-src
%patch0 -p1
rm -r src/main/net/sf/portecle/version # see Patch0
rm lib/*.jar
cp -p src/main/net/sf/portecle/images/splash.png doc/images/


%build
%ant -Djar.classpath= -Dhelpbaseurl=file://%{docdir}/ \
    -Dbcprov.jar=$(build-classpath bcprov) jar


%install

install -Dpm 644 build/portecle.jar $RPM_BUILD_ROOT%{_javadir}/portecle.jar

install -Dpm 644 src/icons/portecle.png \
    $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/32x32/apps/portecle.png
desktop-file-install \
%if 0%{?fedora} && 0%{?fedora} < 19
    --vendor=fedora \
%endif
    --mode=644 \
    --add-mime-type=application/x-pkcs7-certificates \
    --dir=$RPM_BUILD_ROOT%{_datadir}/applications src/etc/portecle.desktop

# Enable experimental features in non-EL builds by default
install -dm 755 $RPM_BUILD_ROOT%{_bindir}
exp="%{?rhel:false}%{!?rhel:true}"
sed -e "s|@DOCDIR@|%{docdir}|" -e "s|@EXPERIMENTAL@|$exp|" %{SOURCE1} \
    > $RPM_BUILD_ROOT%{_bindir}/portecle
chmod 755 $RPM_BUILD_ROOT%{_bindir}/portecle

mkdir -p $RPM_BUILD_ROOT`dirname /etc/java/%name.conf`
touch $RPM_BUILD_ROOT/etc/java/%name.conf


%files
%doc README.txt LICENSE.txt NEWS.txt doc/
%{_bindir}/portecle
%{_javadir}/portecle.jar
%{_datadir}/applications/*portecle.desktop
%{_datadir}/icons/hicolor/32x32/apps/portecle.png
%config(noreplace,missingok) /etc/java/%name.conf


%changelog
* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 1.7-alt2_8jpp7
- new release

* Tue Oct 09 2012 Igor Vlasenko <viy@altlinux.ru> 1.7-alt2_6jpp7
- new version

* Tue Oct 09 2012 Igor Vlasenko <viy@altlinux.ru> 1.7-alt1_6jpp7
- new version

