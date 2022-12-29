Group: System/Base
BuildRequires: gcc-c++
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name: beesu
Version: 2.7
# Don't ever decrease this version (unless beesu update) or the subpackages will go backwards.
# It is easier to do this than to track a separate release field.
Release: alt2_42
Summary: Graphical wrapper for su
URL: http://www.honeybeenet.altervista.org
License: GPLv2+
Source0: http://honeybeenet.altervista.org/beesu/files/beesu-sources/%{name}-%{version}.tar.bz2

BuildRequires: gcc-c++

Requires: pam pam0_timestamp
Requires: consolehelper
#Requires: userpasswd

Obsoletes: nautilus-beesu-manager
Obsoletes: caja-beesu-manager
Obsoletes: nemo-beesu-manager
Obsoletes: gedit-beesu-plugin
Obsoletes: pluma-beesu-plugin
Source44: import.info

%description
Beesu is a wrapper around su and works with consolehelper under
Fedora to let you have a graphic interface like gksu.

%prep
%setup -q

%build
%make_build CFLAGS="%{optflags} -fno-delete-null-pointer-checks"

%install
mkdir -p %{buildroot}%{_datadir}/%{name}
%makeinstall_std

mkdir -p %{buildroot}%{_sysconfdir}/bash_completion.d/
mv %{buildroot}%{_sysconfdir}/profile.d/beesu-bash-completion.sh \
 %{buildroot}%{_sysconfdir}/bash_completion.d/
mkdir -p %buildroot/etc/pam.d
cat > %buildroot/etc/pam.d/config-util <<'EOF'
#%%PAM-1.0
auth		sufficient	pam_rootok.so
auth		sufficient	pam_timestamp.so
auth		include		system-auth
account		required	pam_permit.so
session		required	pam_permit.so
session		optional	pam_xauth.so
session		optional	pam_timestamp.so
EOF


%files
%doc README
%doc --no-dereference COPYING
%config(noreplace) %{_sysconfdir}/%{name}.conf
%config(noreplace) %{_sysconfdir}/pam.d/%{name}
%config(noreplace) %{_sysconfdir}/security/console.apps/%{name}
%{_sysconfdir}/bash_completion.d/%{name}-bash-completion.sh
%{_sbindir}/%{name}
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*
/etc/pam.d/config-util


%changelog
* Thu Dec 29 2022 Igor Vlasenko <viy@altlinux.org> 2.7-alt2_42
- dropped requires on userpasswd (closes: #44764)

* Wed Oct 10 2018 Igor Vlasenko <viy@altlinux.ru> 2.7-alt2_34
- update to new release by fcimport

* Wed Sep 27 2017 Igor Vlasenko <viy@altlinux.ru> 2.7-alt2_31
- update to new release by fcimport

* Thu Mar 16 2017 Igor Vlasenko <viy@altlinux.ru> 2.7-alt2_29
- update to new release by fcimport

* Mon Dec 19 2016 Igor Vlasenko <viy@altlinux.ru> 2.7-alt2_28
- update to new release by fcimport

* Mon Aug 12 2013 Igor Vlasenko <viy@altlinux.ru> 2.7-alt2_12
- update to new release by fcimport

* Mon Jul 08 2013 Igor Vlasenko <viy@altlinux.ru> 2.7-alt2_11
- update to new release by fcimport

* Fri Feb 22 2013 Igor Vlasenko <viy@altlinux.ru> 2.7-alt2_9
- update to new release by fcimport

* Fri Jul 27 2012 Igor Vlasenko <viy@altlinux.ru> 2.7-alt2_8
- update to new release by fcimport

* Wed May 09 2012 Igor Vlasenko <viy@altlinux.ru> 2.7-alt2_7
- update to new release by fcimport

* Wed Mar 21 2012 Igor Vlasenko <viy@altlinux.ru> 2.7-alt2_6
- rebuild to get rid of #27020

* Tue Feb 21 2012 Igor Vlasenko <viy@altlinux.ru> 2.7-alt1_6
- update to new release by fcimport

* Wed Feb 01 2012 Igor Vlasenko <viy@altlinux.ru> 2.7-alt1_5
- update to new release by fcimport

* Tue Oct 25 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 2.7-alt1_4.1
- Rebuild with Python-2.7

* Tue Aug 23 2011 Igor Vlasenko <viy@altlinux.ru> 2.7-alt1_4
- initial release by fcimport

