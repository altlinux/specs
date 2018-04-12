# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:       rpm-helper
Version:    0.24.17
Release:    alt2_4
Summary:    Mageia helper scripts for rpm scriptlets
License:    GPL
Group:      System/Base
URL:        http://www.mageia.org/
Source0:    %{name}-%{version}.tar
BuildArch:  noarch

Patch0:     %{name}-altlinux-adaptation.patch
Patch1:     rpm-helper.macros.in.alt-remove-unsupported.patch

Requires:   rpm-macros-%name = %EVR

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

%patch0 -p1
%patch1 -p0

%install
%makeinstall_std rpmmacrosdir=%{_rpmmacrosdir}

mv %buildroot%{_rpmmacrosdir}/%{name}{.macros,}

# not ported to ALTLinux
rm -f %buildroot%{_datadir}/%{name}/{add-syslog,del-syslog}
rm -rf %buildroot%{_localstatedir}/lib/%{name}/systemd-migration

%check
# add-syslog; not ported to ALT
#make test

%files
%doc README NEWS AUTHORS
%{_datadir}/%{name}
%{_localstatedir}/lib/%{name}
%config(noreplace) %{_sysconfdir}/sysconfig/ssl

%files -n rpm-macros-%name
%{_rpmmacrosdir}/%{name}

%changelog
* Thu Apr 12 2018 Igor Vlasenko <viy@altlinux.ru> 0.24.17-alt2_4
- updated internal Requires.

* Wed Apr 11 2018 Igor Vlasenko <viy@altlinux.ru> 0.24.17-alt1_4
- port for Sisyphus

