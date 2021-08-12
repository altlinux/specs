Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-alternatives rpm-macros-java
# END SourceDeps(oneline)
BuildRequires: /proc rpm-build-java
BuildRequires: jpackage-default
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:		voms-clients-java
Version:	3.3.2
Release:	alt1_4jpp11
Summary:	Virtual Organization Membership Service Java clients

License:	ASL 2.0
URL:		https://wiki.italiangrid.it/VOMS
Source0:	https://github.com/italiangrid/voms-clients/archive/v%{version}/%{name}-%{version}.tar.gz
BuildArch:	noarch

BuildRequires:	maven-local
BuildRequires:	mvn(commons-cli:commons-cli)
BuildRequires:	mvn(commons-io:commons-io)
BuildRequires:	mvn(junit:junit)
BuildRequires:	mvn(org.italiangrid:voms-api-java)
BuildRequires:	voms-api-java >= 3.3.2
Requires:	voms-api-java >= 3.3.2


# Older versions of voms-clients did not have alternatives
Conflicts:	voms-clients < 2.0.12

Provides:	voms-clients = %{version}-%{release}
Source44: import.info

%description
The Virtual Organization Membership Service (VOMS) is an attribute authority
which serves as central repository for VO user authorization information,
providing support for sorting users into group hierarchies, keeping track of
their roles and other attributes in order to issue trusted attribute
certificates and SAML assertions used in the Grid environment for
authorization purposes.

This package provides the Java version of the command line clients for VOMS:
voms-proxy-init, voms-proxy-destroy and voms-proxy-info.

%prep
%setup -q -n voms-clients-%{version}

# Remove maven-javadoc-plugin configuration
# We are not building the javadoc for this package
# And its presence causes the EPEL 8 build to fail
%pom_remove_plugin org.apache.maven.plugins:maven-javadoc-plugin

# Do not create source jars
%pom_remove_plugin org.apache.maven.plugins:maven-source-plugin

# Don't do assembly
%pom_remove_plugin :maven-assembly-plugin

# Remove license plugin
%pom_remove_plugin com.mycila.maven-license-plugin:maven-license-plugin

%build
%mvn_build -j -- -Dmaven.compiler.source=1.8 -Dmaven.compiler.target=1.8 -Dmaven.javadoc.source=1.8 -Dmaven.compiler.release=8

%install
%mvn_install

mkdir -p %{buildroot}%{_bindir}

cat > %{buildroot}%{_bindir}/voms-proxy-init3 << EOF
#!/bin/sh
VOMS_CLIENTS_JAVA_OPTIONS=\${VOMS_CLIENTS_JAVA_OPTIONS:-"-XX:+UseSerialGC -Xmx16m"}
java \$VOMS_CLIENTS_JAVA_OPTIONS -cp \$(build-classpath voms-clients-java voms-api-java canl-java bcpkix bcprov commons-cli commons-io) org.italiangrid.voms.clients.VomsProxyInit "\$@"
EOF
chmod 755 %{buildroot}%{_bindir}/voms-proxy-init3

cat > %{buildroot}%{_bindir}/voms-proxy-info3 << EOF
#!/bin/sh
VOMS_CLIENTS_JAVA_OPTIONS=\${VOMS_CLIENTS_JAVA_OPTIONS:-"-XX:+UseSerialGC -Xmx16m"}
java \$VOMS_CLIENTS_JAVA_OPTIONS -cp \$(build-classpath voms-clients-java voms-api-java canl-java bcpkix bcprov commons-cli commons-io) org.italiangrid.voms.clients.VomsProxyInfo "\$@"
EOF
chmod 755 %{buildroot}%{_bindir}/voms-proxy-info3

cat > %{buildroot}%{_bindir}/voms-proxy-destroy3 << EOF
#!/bin/sh
VOMS_CLIENTS_JAVA_OPTIONS=\${VOMS_CLIENTS_JAVA_OPTIONS:-"-XX:+UseSerialGC -Xmx16m"}
java \$VOMS_CLIENTS_JAVA_OPTIONS -cp \$(build-classpath voms-clients-java voms-api-java canl-java bcpkix bcprov commons-cli commons-io) org.italiangrid.voms.clients.VomsProxyDestroy "\$@"
EOF
chmod 755 %{buildroot}%{_bindir}/voms-proxy-destroy3

touch %{buildroot}%{_bindir}/voms-proxy-init
chmod 755 %{buildroot}%{_bindir}/voms-proxy-init
touch %{buildroot}%{_bindir}/voms-proxy-info
chmod 755 %{buildroot}%{_bindir}/voms-proxy-info
touch %{buildroot}%{_bindir}/voms-proxy-destroy
chmod 755 %{buildroot}%{_bindir}/voms-proxy-destroy

mkdir -p %{buildroot}%{_mandir}/man1
install -p -m 644 man/voms-proxy-init.1 \
    %{buildroot}%{_mandir}/man1/voms-proxy-init3.1
install -p -m 644 man/voms-proxy-info.1 \
    %{buildroot}%{_mandir}/man1/voms-proxy-info3.1
install -p -m 644 man/voms-proxy-destroy.1 \
    %{buildroot}%{_mandir}/man1/voms-proxy-destroy3.1

touch %{buildroot}%{_mandir}/man1/voms-proxy-init.1
touch %{buildroot}%{_mandir}/man1/voms-proxy-info.1
touch %{buildroot}%{_mandir}/man1/voms-proxy-destroy.1

mkdir -p %{buildroot}%{_mandir}/man5
install -p -m 644 man/vomsdir.5 %{buildroot}%{_mandir}/man5/vomsdir.5
install -p -m 644 man/vomses.5 %{buildroot}%{_mandir}/man5/vomses.5
for rpm404_ghost in %{_bindir}/voms-proxy-destroy %{_bindir}/voms-proxy-info %{_bindir}/voms-proxy-init %{_mandir}/man1/voms-proxy-destroy.1* %{_mandir}/man1/voms-proxy-info.1* %{_mandir}/man1/voms-proxy-init.1*
do
    mkdir -p %buildroot`dirname "$rpm404_ghost"`
    touch %buildroot"$rpm404_ghost"
done
install -d $RPM_BUILD_ROOT/%_altdir; cat >$RPM_BUILD_ROOT/%_altdir/voms-proxy-init_voms-clients-java<<EOF
%{_bindir}/voms-proxy-init	%{_bindir}/voms-proxy-init3	90
%{_mandir}/man1/voms-proxy-init.1.gz	%{_mandir}/man1/voms-proxy-init3.1.gz	%{_bindir}/voms-proxy-init3
EOF
install -d $RPM_BUILD_ROOT/%_altdir; cat >$RPM_BUILD_ROOT/%_altdir/voms-proxy-info_voms-clients-java<<EOF
%{_bindir}/voms-proxy-info	%{_bindir}/voms-proxy-info3	90
%{_mandir}/man1/voms-proxy-info.1.gz	%{_mandir}/man1/voms-proxy-info3.1.gz	%{_bindir}/voms-proxy-info3
EOF
install -d $RPM_BUILD_ROOT/%_altdir; cat >$RPM_BUILD_ROOT/%_altdir/voms-proxy-destroy_voms-clients-java<<EOF
%{_bindir}/voms-proxy-destroy	%{_bindir}/voms-proxy-destroy3	90
%{_mandir}/man1/voms-proxy-destroy.1.gz	%{_mandir}/man1/voms-proxy-destroy3.1.gz	%{_bindir}/voms-proxy-destroy3
EOF


%files -f .mfiles
%_altdir/voms-proxy-destroy_voms-clients-java
%_altdir/voms-proxy-info_voms-clients-java
%_altdir/voms-proxy-init_voms-clients-java
%dir %{_javadir}/%{name}
%{_bindir}/voms-proxy-destroy3
%{_bindir}/voms-proxy-info3
%{_bindir}/voms-proxy-init3
%{_mandir}/man1/voms-proxy-destroy3.1*
%{_mandir}/man1/voms-proxy-info3.1*
%{_mandir}/man1/voms-proxy-init3.1*
%{_mandir}/man5/vomsdir.5*
%{_mandir}/man5/vomses.5*
%doc AUTHORS README.md
%doc --no-dereference LICENSE

%changelog
* Wed Aug 04 2021 Igor Vlasenko <viy@altlinux.org> 3.3.2-alt1_4jpp11
- update

* Thu Jun 10 2021 Igor Vlasenko <viy@altlinux.org> 3.3.2-alt1_2jpp11
- new version

* Tue Oct 08 2019 Igor Vlasenko <viy@altlinux.ru> 3.3.0-alt1_6jpp8
- new version

