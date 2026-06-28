Group: File tools

Name:           lynis
Version:        3.1.6
Release:        alt2
Summary:        Security and system auditing tool
License:        GPLv3
Group:          File tools
URL:            https://cisofy.com/lynis/
Source0:        https://cisofy.com/files/%name-%version.tar.gz

BuildArch:      noarch

# See https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %_var

%global bashcompdir %(pkg-config --variable=completionsdir bash-completion)

BuildRequires:  bash-completion-util-linux
BuildRequires:  git-core
BuildRequires:  procps

Requires:       audit
Requires:       e2fsprogs
Requires:       module-init-tools

# Optional dependencies detected by the automatic shell dependency scanner.

# dropbearkey is used only when an existing Dropbear installation
# and /etc/dropbear configuration are detected.
%filter_from_requires /^dropbear$/d
%filter_from_requires /^\/usr\/bin\/dropbearkey$/d

# defaults is used only by a macOS-specific package test.
%filter_from_requires /^gnustep-base$/d

# Commands specific to other operating systems or optional code paths.
%filter_from_requires /.usr.xpg4.bin.sh/d
%filter_from_requires /sbin.kldstat/d
%filter_from_requires /usr.bin.isainfo/d
%filter_from_requires /usr.bin.sw_vers/d
%filter_from_requires /usr.libexec.ApplicationFirewall.socketfilterfw/d
%filter_from_requires /usr.sbin.bootinfo/d
%filter_from_requires /usr.sbin.modinfo/d
%filter_from_requires /usr.sbin.prtconf/d
%filter_from_requires /usr.xpg4.bin.id/d

%description
Lynis is an auditing and hardening tool for Unix/Linux and you might even call
it a compliance tool. It scans the system and installed software. Then it
performs many individual security control checks. It determines the hardening
state of the machine, detects security issues and provides suggestions to
improve the security defense of the system.

%prep
%setup -q -n %name

# Make sisyphus_check happy.
sed -i -E 's/(\(python)/\13/' include/functions

%build
# Empty build.

%install
mkdir -p %buildroot%_sysconfdir/%name
install -p default.prf %buildroot%_sysconfdir/%name/

mkdir -p %buildroot%_bindir
install -p lynis %buildroot%_bindir/

mkdir -p %buildroot%_mandir/man8
install -p lynis.8 %buildroot%_mandir/man8/

mkdir -p %buildroot%_datadir/%name/include/
# Forced by upstream. Otherwise these scripts cannot be executed.
install -p include/* %buildroot%_datadir/%name/include/
chmod 0644 %buildroot%_datadir/%name/include/*

mkdir -p %buildroot%_datadir/%name/plugins/
install -p plugins/* %buildroot%_datadir/%name/plugins/
chmod 0640 %buildroot%_datadir/%name/plugins/*

cp -pR db/ %buildroot%_datadir/%name/

mkdir -p %buildroot%bashcompdir
install -p extras/bash_completion.d/lynis %buildroot%bashcompdir/

for rpm404_ghost in \
    %_localstatedir/log/lynis.log \
    %_localstatedir/log/lynis-report.dat
do
    mkdir -p %buildroot"$(dirname "$rpm404_ghost")"
    touch %buildroot"$rpm404_ghost"
done

%check
# Sanity check.
./lynis audit system --quick

%files
%doc CHANGELOG* CONTRIBUTORS* FAQ* README*
%doc extras/systemd/
%doc --no-dereference LICENSE
%_bindir/lynis
%bashcompdir/*
%_datadir/lynis/
%_mandir/man8/lynis.8*
%dir %_sysconfdir/%name
%config(noreplace) %_sysconfdir/%name/default.prf
%ghost %_localstatedir/log/lynis.log
%ghost %_localstatedir/log/lynis-report.dat

%changelog
* Thu Jun 25 2026 Pavel Vasenkov <pav@altlinux.org> 3.1.6-alt2
- Removed redundant dependencies (Closes: #59615)

* Mon Jun 15 2026 Pavel Vasenkov <pav@altlinux.org> 3.1.6-alt1
- update new release 3.1.6 (Closes: #52018)

* Fri Mar 01 2024 Pavel Vasenkov <pav@altlinux.org> 3.0.9-alt1
- update new release 3.0.9 (Closed: #49562)

* Mon Dec 04 2023 Grigory Ustinov <grenka@altlinux.org> 3.0.0-alt3
- Fixed FTBFS (Closes: #48583).

* Tue Jul 14 2020 Pavel Vasenkov <pav@altlinux.org> 3.0.0-alt2
- initial build for sisyphus

* Mon Jul 06 2020 Igor Vlasenko <viy@altlinux.ru> 3.0.0-alt1_1
- update to new release by fcimport

* Thu Mar 05 2020 Igor Vlasenko <viy@altlinux.ru> 2.7.5-alt1_5
- update to new release by fcimport

* Sat Sep 28 2019 Igor Vlasenko <viy@altlinux.ru> 2.7.5-alt1_4
- update to new release by fcimport

* Tue Aug 06 2019 Igor Vlasenko <viy@altlinux.ru> 2.7.5-alt1_2
- update to new release by fcimport

* Mon Jul 01 2019 Igor Vlasenko <viy@altlinux.ru> 2.7.5-alt1_1
- update to new release by fcimport

* Tue Mar 05 2019 Igor Vlasenko <viy@altlinux.ru> 2.7.1-alt1_1
- update to new release by fcimport

* Tue Sep 16 2014 Igor Vlasenko <viy@altlinux.ru> 1.6.1-alt1_1
- update to new release by fcimport

* Wed Sep 10 2014 Igor Vlasenko <viy@altlinux.ru> 1.5.9-alt1_1
- update to new release by fcimport

* Thu Jun 26 2014 Igor Vlasenko <viy@altlinux.ru> 1.5.6-alt1_1
- update to new release by fcimport

* Wed May 14 2014 Igor Vlasenko <viy@altlinux.ru> 1.5.0-alt1_1
- update to new release by fcimport

* Tue Apr 01 2014 Igor Vlasenko <viy@altlinux.ru> 1.4.4-alt1_1
- update to new release by fcimport

* Tue Mar 04 2014 Igor Vlasenko <viy@altlinux.ru> 1.4.3-alt1_1
- update to new release by fcimport

* Fri Feb 21 2014 Igor Vlasenko <viy@altlinux.ru> 1.4.1-alt1_1
- update to new release by fcimport

* Thu Jan 23 2014 Igor Vlasenko <viy@altlinux.ru> 1.3.9-alt1_1
- update to new release by fcimport

* Sat Jan 04 2014 Igor Vlasenko <viy@altlinux.ru> 1.3.8-alt1_1
- update to new release by fcimport

* Tue Dec 24 2013 Igor Vlasenko <viy@altlinux.ru> 1.3.7-alt1_1
- update to new release by fcimport

* Sat Dec 07 2013 Igor Vlasenko <viy@altlinux.ru> 1.3.6-alt1_1
- update to new release by fcimport

* Tue Aug 27 2013 Igor Vlasenko <viy@altlinux.ru> 1.2.9-alt1_6
- update to new release by fcimport

* Fri Apr 26 2013 Igor Vlasenko <viy@altlinux.ru> 1.2.9-alt1_5
- initial fc import

