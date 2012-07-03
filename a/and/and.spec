# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-fedora-compat
# END SourceDeps(oneline)
Name:      and
Version:   1.2.2
Release:   alt2_15
Summary:   Auto nice daemon

License:   GPLv2
Group:     System/Servers

URL:       http://and.sourceforge.net
Source0:   http://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
Source1:   and.sysconf
Source2:   and.service
Patch1:    and-1.2.2-makefile.patch


Obsoletes: and-sysvinit < %{version}-%{release}
Provides:  and-sysvinit = %{version}-%{release}

Obsoletes:  and-units < %{version}-%{release}
Provides:   and-units = %{version}-%{release}



provides:	and-sysvinit = %{version}-%{release}
Obsoletes:	and-sysvinit < 1.2.2-11

provides:	and-units = %{version}-%{release}
Obsoletes:	and-units < 1.2.2-11
Source44: import.info



%description
The auto nice daemon renices and even kills jobs according to their CPU time,
owner, and command name. This is especially useful on production machines with
lots of concurrent CPU-intensive jobs and users that tend to forget to
nice their jobs.

%prep            
%setup1 -q
%patch1 -p1 -b .org

%build
make %{?_smp_mflags} \
     CFLAGS='%{optflags}' \
     PREFIX=%{_prefix} \
     INSTALL_ETC=%{_sysconfdir} \
     INSTALL_SBIN=%{_sbindir} \
     INSTALL_MAN=%{_mandir}

%install
mkdir -p %{buildroot}%{_sysconfdir}
mkdir -p %{buildroot}%{_sbindir}
mkdir -p %{buildroot}%{_mandir}/man8
mkdir -p %{buildroot}%{_mandir}/man5
make PREFIX=%{buildroot}%{_prefix} \
     INSTALL_ETC=%{buildroot}%{_sysconfdir} \
     INSTALL_SBIN=%{buildroot}%{_sbindir} \
     INSTALL_MAN=%{buildroot}%{_mandir} install 

mkdir -p %{buildroot}%{_sysconfdir}/sysconfig
install -p -m 0644 %{SOURCE1} %{buildroot}%{_sysconfdir}/sysconfig/and

mkdir -p %{buildroot}%{_unitdir}
install -p -m 0644 %{SOURCE2} %{buildroot}%{_unitdir}

%post
if [ $1 -eq 1 ]; then
   /bin/systemctl daemon-reload >/dev/null 2>&1 || :
fi

%preun
if [ $1 -eq 1 ]; then
   /bin/systemctl --no-reload disable and.service >/dev/null 2>&1 || :
   /bin/systemctl stop and.service >/dev/null 2>&1 || :
fi

%postun
if [ $0 -en 0 ]; then
   /bin/systemctl try-restart and.service >/dev/null 2>&1 || :
fi

%files
%doc README LICENSE CHANGELOG
%config(noreplace) %{_sysconfdir}/and/
%config(noreplace) %{_sysconfdir}/sysconfig/and
%{_sbindir}/*
%{_mandir}/man5/*.*
%{_mandir}/man8/*.*
%{_unitdir}/and.service

%changelog
* Wed Mar 21 2012 Igor Vlasenko <viy@altlinux.ru> 1.2.2-alt2_15
- rebuild to get rid of #27020

* Sat Jan 21 2012 Igor Vlasenko <viy@altlinux.ru> 1.2.2-alt1_15
- update to new release by fcimport

* Mon Nov 07 2011 Igor Vlasenko <viy@altlinux.ru> 1.2.2-alt1_14
- update to new release by fcimport

* Thu Jul 14 2011 Igor Vlasenko <viy@altlinux.ru> 1.2.2-alt1_13
- initial release by fcimport

