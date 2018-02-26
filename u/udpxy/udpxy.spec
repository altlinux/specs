# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-fedora-compat
# END SourceDeps(oneline)
%global buildversion 21
%global realversion 1.0-Chipmunk-build%{buildversion}

Name:           udpxy
Version:        1.0.21
Release:        alt3_2
Summary:        UDP-to-HTTP multicast traffic relay daemon

Group:          Networking/Other
License:        GPLv3+
URL:            http://sourceforge.net/projects/udpxy/
Source0:        http://downloads.sourceforge.net/%{name}/%{name}.%{realversion}.tgz
Source1:        udpxy.service
Source44: import.info
Source45: udpxy.init
Source46: udpxy.sysconfig



%description
udpxy is a UDP-to-HTTP multicast traffic relay daemon:
it forwards UDP traffic from a given multicast subscription
to the requesting HTTP client.

%prep
%setup -q -n %{name}-1.0-Chipmunk-%{buildversion}

sed -i "s|CFLAGS += -W -Wall -Werror --pedantic|CFLAGS += %{optflags}|g" Makefile

%build
make %{?_smp_mflags}


%install

sed -i "s|INSTALLROOT := /usr/local|INSTALLROOT := %{buildroot}/usr|g" Makefile
sed -i 's|ln -s $(INSTALLROOT)/bin/$(EXEC)|ln -s $(EXEC)|g' Makefile

make install

install -D -p -m 0644 %{SOURCE1} %{buildroot}%{_unitdir}/%{name}.service

install -D -m 755 %{SOURCE45} %buildroot%_initdir/%name
install -D -m 644 %{SOURCE46} %buildroot%_sysconfdir/sysconfig/%name


%post
%post_service %name
%preun
%preun_service %name
%files
%doc README CHANGES gpl.txt udpxy-manual-RU.rtf
%{_bindir}/%{name}
%{_bindir}/udpxrec
%{_unitdir}/%{name}.service

%_initdir/%name
%config(noreplace) %_sysconfdir/sysconfig/%name



%changelog
* Sat Feb 18 2012 Igor Vlasenko <viy@altlinux.ru> 1.0.21-alt3_2
- cleaned up depandencies

* Sat Feb 18 2012 Igor Vlasenko <viy@altlinux.ru> 1.0.21-alt2_2
- added sys V init script

* Fri Feb 17 2012 Igor Vlasenko <viy@altlinux.ru> 1.0.21-alt1_2
- converted for Sisyphus

