# BEGIN SourceDeps(oneline):
BuildRequires: bzlib-devel libsocket
# END SourceDeps(oneline)
%set_verify_elf_method unresolved=relaxed
BuildRequires: gcc-c++
Summary: Hercules S/370, ESA/390, and z/Architecture emulator
Name: hercules
Version: 3.12
Release: alt2
License: QPL
Group: Emulators
URL: http://www.hercules-390.eu/
Source0: http://downloads.hercules-390.eu/%{name}-%{version}.tar.gz
#Source0: https://github.com/rbowler/spinhawk/archive/%{version}.tar.gz
Source1: hercules.cnf
Source2: hercules-run
Source3: README-rpm
Source4: generic.prm
Patch0: %{name}-3.10-fedora.patch
BuildRequires: zlib-devel
BuildRequires: bzip2-devel
BuildRequires: libcap-devel
BuildRequires: libtool
BuildRequires: libltdl7-devel
Source44: import.info
Patch33: hercules-3.08-alt-link.patch


%description
Hercules is an emulator for the IBM System/370, ESA/390, and z/Architecture
series of mainframe computers. It is capable of running any IBM operating
system and applications that a real system will run, as long as the hardware
needed is emulated. Hercules can emulate FBA and CKD DASD, tape, printer,
card reader, card punch, channel-to-channel adapter, LCS Ethernet, and
printer-keyboard, 3270 terminal, and 3287 printer devices.


%prep
#%setup -q -n spinhawk-%{version}
%setup -q

%patch0 -p1 -b .fedora

rm autoconf/libtool.m4
autoreconf -f -i

# remove unbundled stuff
rm ltdl.[ch]

# Scripts to be looked at, not executed from the docs
chmod -x util/*
# remove Makefile
rm util/Makefile*
%patch33 -p1


%build
%configure \
    --enable-external-gui \
    --enable-optimization="%{optflags}"

make %{?_smp_mflags} V=1


%install
make install DESTDIR=%{buildroot}

mkdir -p %{buildroot}%{_sysconfdir}/hercules
# Install config files
install -p -m 0644 %{SOURCE1} %{buildroot}%{_sysconfdir}/hercules/
install -p -m 0644 %{SOURCE4} %{buildroot}%{_sysconfdir}/hercules/

# Install our wrapper script (takes care of tunnel networking)
install -D -p -m 0755 %{SOURCE2} %{buildroot}%{_sbindir}/hercules-run

# Copy our README to be included as doc
install -p -m 0644 %{SOURCE3} README-rpm

# Create empty directory where to store system images
mkdir -p %{buildroot}%{_sharedstatedir}/hercules

# Remove Makefile from html docs
rm html/Makefile*

# Remove libtool archives
rm %{buildroot}%{_libdir}/hercules/*.la
rm %{buildroot}%{_libdir}/*.la


%files
%doc COPYRIGHT README-rpm
%doc README.{COMMADPT,ECPSVM,HDL,HERCLOGO,NETWORKING,TAPE}
%doc RELEASE.NOTES hercules.cnf html/ util/
%dir %{_sysconfdir}/hercules/
%attr(0644, root, root) %config(noreplace) %{_sysconfdir}/hercules/hercules.cnf
%attr(0644, root, root) %config(noreplace) %{_sysconfdir}/hercules/generic.prm
%{_bindir}/*
%{_sbindir}/*
%{_datadir}/hercules/
%dir %{_libdir}/hercules/
%{_libdir}/hercules/*.so
%{_libdir}/*.so
%{_mandir}/man?/*
%dir %{_sharedstatedir}/hercules/


%changelog
* Tue Nov 08 2016 Denis Medvedev <nbr@altlinux.org> 3.12-alt2
- Compile to sisyphus

* Wed Mar 02 2016 Igor Vlasenko <viy@altlinux.ru> 3.12-alt1_2
- update to new release by fcimport

* Mon Sep 21 2015 Igor Vlasenko <viy@altlinux.ru> 3.11-alt1_2
- update to new release by fcimport

* Mon Oct 20 2014 Igor Vlasenko <viy@altlinux.ru> 3.11-alt1_1
- update to new release by fcimport

* Fri Feb 21 2014 Igor Vlasenko <viy@altlinux.ru> 3.10-alt1_1
- update to new release by fcimport

* Sat Dec 07 2013 Igor Vlasenko <viy@altlinux.ru> 3.09-alt1_2
- update to new release by fcimport

* Mon Aug 05 2013 Igor Vlasenko <viy@altlinux.ru> 3.09-alt1_1
- update to new release by fcimport

* Mon Jun 10 2013 Igor Vlasenko <viy@altlinux.ru> 3.08.2-alt1_1
- update to new release by fcimport

* Thu Mar 21 2013 Igor Vlasenko <viy@altlinux.ru> 3.08.1-alt1_1
- update to new release by fcimport

* Wed Mar 13 2013 Igor Vlasenko <viy@altlinux.ru> 3.08-alt1_2
- update to new release by fcimport

* Mon Jan 21 2013 Igor Vlasenko <viy@altlinux.ru> 3.08-alt1_1
- initial fc import

