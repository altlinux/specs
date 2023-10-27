# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
# no clients for now; needs perl
%def_enable syslog_helper
Name:       rpm-helper
Version:    0.24.22
Release:    alt1_1
Summary:    Mageia helper scripts for rpm scriptlets
License:    GPLv2+
Group:      System/Base
URL:        https://gitweb.mageia.org/software/rpm/rpm-helper/
VCS:        git://git.mageia.org/software/rpm/rpm-helper
Source0:    %{name}-%{version}.tar
Requires(pre): shadow-utils

BuildArch:  noarch

Patch33: %{name}-altlinux-adaptation.patch
Patch34: rpm-helper.macros.in.alt-remove-unsupported.patch

Requires:   rpm-macros-%name = %EVR

# for clients in  autoimports
Provides: /usr/share/rpm-helper/create-file
Provides: /usr/share/rpm-helper/add-user
Provides: /usr/share/rpm-helper/del-user
Provides: /usr/share/rpm-helper/add-service
Provides: /usr/share/rpm-helper/del-service
%if_enabled syslog_helper
Provides: /usr/share/rpm-helper/add-syslog
Provides: /usr/share/rpm-helper/del-syslog
# for test
BuildRequires: perl(ExtUtils/Command/MM.pm)
%endif

%description
Helper scripts for rpm installation.
For compatibility with Mandriva, Mageia, ROSA.

%package -n rpm-macros-%name
Summary: Mageia compatibility set of macro from %name
Group: System/Base
BuildArch: noarch

%description -n rpm-macros-%name
Mageia compatibility set of macro from %{name}.
For compatibility with Mandriva, Mageia, ROSA.

%prep
%setup -q
%patch33 -p1
%if_disabled syslog_helper
%patch34 -p0
%endif

%install
%makeinstall_std rpmmacrosdir=%{_rpmmacrosdir}

mv %buildroot%{_rpmmacrosdir}/{macros.,}%{name}

# not ported to ALTLinux
rm -rf %buildroot%{_localstatedir}/lib/%{name}/systemd-migration
%if_disabled syslog_helper
rm -f %buildroot%{_datadir}/%{name}/{add-syslog,del-syslog}
%endif

%check
%if_enabled syslog_helper
%__make test
%endif

%files
%doc README NEWS AUTHORS
%{_datadir}/%{name}
%{_localstatedir}/lib/%{name}
%config(noreplace) %{_sysconfdir}/sysconfig/ssl

%files -n rpm-macros-%name
%{_rpmmacrosdir}/%{name}

%changelog
* Fri Oct 27 2023 Igor Vlasenko <viy@altlinux.org> 0.24.22-alt1_1
- new version

* Sat Oct 27 2018 Igor Vlasenko <viy@altlinux.ru> 0.24.17-alt2_5
- added provides for autoimports

* Thu Apr 12 2018 Igor Vlasenko <viy@altlinux.ru> 0.24.17-alt2_4
- updated internal Requires.

* Wed Apr 11 2018 Igor Vlasenko <viy@altlinux.ru> 0.24.17-alt1_4
- port for Sisyphus

