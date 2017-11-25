# BEGIN SourceDeps(oneline):
BuildRequires: gcc-c++ libmagic-devel libnetdude-devel
# END SourceDeps(oneline)
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:           libnetdude
Version:        0.11
Release:        alt2_16
Summary:        Management framework for pcap packet traces

Group:          System/Libraries
License:        MIT with advertising
URL:            http://netdude.sourceforge.net/
Source0:        http://downloads.sourceforge.net/netdude/libnetdude-%{version}.tar.gz
Source1:        libnetdude-lndtool-wrapper.sh
# -Werror=format-security
Patch0:         libnetdude-0.11-format-security.patch

BuildRequires:  glib-devel, libpcapnav-devel gtk-doc gtk-doc-mkpdf, tcpdump, /bin/sed
BuildRequires:  libpcap-devel
Source44: import.info

%description
libnetdude allows to implement trace file manipulations at a much higher level
of abstraction than code written directly on top of the pcap library. It also
provides a command-line interface that directly lets you script all packet-
mangling capabilities provided by the set of plugins you have installed.

%package        devel
Summary:        Development files for %{name}
Group:          Development/Other
Requires:       %{name} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
%setup -q
%patch0 -p1

# Rewrite our wrapperscript to have a versioned directory
sed -e 's,###loc###,%{name}/%{version},' %{SOURCE1} > libnetdude-lndtool-wrapper.sh


%build
%configure \
        --disable-static \
        --datadir=%{_libdir} \
        --with-html-dir=%{_datadir}/gtk-doc/html/%{name}/
%make_build
#pushd docs
#%make_build docs
#popd

%install
make install DESTDIR=%{buildroot} INSTALL="install -p"

# Wrapper workaround for conflicting binary
mkdir -p %{buildroot}%{_libdir}/%{name}/%{version}
mv %{buildroot}%{_bindir}/lndtool %{buildroot}%{_libdir}/%{name}/%{version}/lndtool
install -D -m 755 -p libnetdude-lndtool-wrapper.sh %{buildroot}%{_bindir}/lndtool
find %{buildroot} -name '*.la' -exec rm -f {} ';'

#mv %{buildroot}%{_datadir}/gtk-doc/html/%{name}/%{name}/* %{buildroot}%{_datadir}/gtk-doc/html/%{name}/
#rm -rf %{buildroot}%{_datadir}/gtk-doc/html/%{name}/%{name}/


%files
%doc README COPYING
%{_libdir}/*.so.*
%{_libdir}/%{name}/

%files devel
%doc README COPYING ChangeLog TODO
%{_bindir}/lndtool
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/%{name}/%{version}/lndtool
#%{_datadir}/gtk-doc/html/%{name}/

%changelog
* Sat Nov 25 2017 Igor Vlasenko <viy@altlinux.ru> 0.11-alt2_16
- fixed build

* Wed Sep 27 2017 Igor Vlasenko <viy@altlinux.ru> 0.11-alt1_16
- update to new release by fcimport

* Thu Mar 16 2017 Igor Vlasenko <viy@altlinux.ru> 0.11-alt1_14
- update to new release by fcimport

* Mon Feb 15 2016 Igor Vlasenko <viy@altlinux.ru> 0.11-alt1_13
- update to new release by fcimport

* Sun Sep 20 2015 Igor Vlasenko <viy@altlinux.ru> 0.11-alt1_12
- update to new release by fcimport

* Wed Aug 27 2014 Igor Vlasenko <viy@altlinux.ru> 0.11-alt1_11
- update to new release by fcimport

* Mon Aug 12 2013 Igor Vlasenko <viy@altlinux.ru> 0.11-alt1_8
- update to new release by fcimport

* Wed May 01 2013 Igor Vlasenko <viy@altlinux.ru> 0.11-alt1_7
- initial fc import

