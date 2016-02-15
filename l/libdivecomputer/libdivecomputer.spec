# BEGIN SourceDeps(oneline):
BuildRequires: pkgconfig(libusb-1.0)
# END SourceDeps(oneline)
Group: Other
%add_optflags %optflags_shared
#global        snapdate   20120717
#global        snaphash   4bc477b
#global        snapver    {snapdate}.git{snaphash}

Name:           libdivecomputer
Version:        0.4.2
#Release:        2.{snapver}{?dist}
Release:        alt1_5
Summary:        Library for communication with dive computers

License:        LGPLv2+
URL:            http://libdivecomputer.org
Source0:        http://libdivecomputer.org/releases/%{name}-%{version}.tar.gz
# Sources generated using:
# git clone git://libdivecomputer.git.sourceforge.net/gitroot/libdivecomputer/libdivecomputer && cd libdivecomputer
# git archive --format=tar --prefix=libdivecomputer-4bc477b/ 4bc477b | xz -z > libdivecomputer-0.1.0-20120717git4bc477b.tar.xz
#Source0:        libdivecomputer-0.1.0-20120717git4bc477b.tar.xz

BuildRequires:  libusb-devel
Source44: import.info
#BuildRequires:  autoconf

%description
Libdivecomputer is a cross-platform and open source library for
communication with dive computers from various manufacturers.

Supported devices:

    Suunto
        Solution
        Eon, Solution Alpha and Solution Nitrox/Vario
        Vyper, Cobra, Vytec, Vytec DS, D3, Spyder, Gekko, Mosquito,
        Stinger and Zoop
        Vyper2, Cobra2, Cobra3, Vyper Air and HelO2
        D9, D6, D4, D9tx, D6i and D4i
    Uwatec
        Aladin
        Memomouse
        Smart and Galileo (infrared)
    Reefnet
        Sensus
        Sensus Pro
        Sensus Ultra
    Oceanic, Aeris, Sherwood, Hollis, Genesis and Tusa (Pelagic)
        VT Pro, Versa Pro, Pro Plus 2, Wisdom, Atmos 2, Atmos AI,
        Atmos Elite, ...
        Veo 250, Veo 180Nx, XR2, React Pro, DG02, Insight, ...
        Atom 2.0, VT3, Datamask, Geo, Geo 2.0, Veo 2.0, Veo 3.0, Pro
        Plus 2.1, Compumask, Elite T3, Epic, Manta, IQ-900 (Zen),
        IQ-950 (Zen Air), IQ-750 (Element II), ...
    Mares
        Nemo, Nemo Excel, Nemo Apneist, ...
        Puck, Puck Air, Nemo Air, Nemo Wide, ...
        Darwin, Darwin Air, M1, M2, Airlab
        Icon HD, Icon HD Net Ready
    Heinrichs Weikamp
        OSTC, OSTC Mk.2 and OSTC 2N
        Frog
    Cressi, Zeagle and Mares (Seiko)
        Edy, Nemo Sport
        N2iTiON3
    Atomic Aquatics
        Cobalt

Note: Backends marked with an asterisk (*) are not yet included in the
source code.

%package        devel
Group: Other
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

# Linus seems to prefer that this library is compiled with static:
# http://lists.hohndel.org/pipermail/subsurface/2012-July/000283.html
# And since subsurface is pretty much the only desktop application that
# uses that library and I plan to maintain both (being in contact with
# upstream), I am fine with this for the moment.

%package        static
Group: Other
Summary:        Static files for %{name}
Requires:       %{name}%{?_isa} = %{version}

%description    static
The %{name}-static package contains static files for
developing applications that use %{name}.


%prep
#setup -q -n {name}-{snaphash}
%setup -q

%build
#autoreconf --install
%configure 
sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool
make %{?_smp_mflags}


%install
make install DESTDIR=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -name '*.la' -exec rm -f {} ';'

rm $RPM_BUILD_ROOT/%{_bindir}/{aladin,atom2,d9,darwin,edy,eon,frog,iconhd}
rm $RPM_BUILD_ROOT/%{_bindir}/{leonardo,memomouse,n2ition3,nemo,ostc,predator}
rm $RPM_BUILD_ROOT/%{_bindir}/{puck,sensus,sensuspro,sensusultra,smart,solution}
rm $RPM_BUILD_ROOT/%{_bindir}/{veo250,vtpro,vyper,vyper2}

%files
%doc NEWS README
%{_libdir}/*.so.*
%{_bindir}/universal

%files devel
%doc
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/%{name}.pc

%files static
%doc
%{_libdir}/*.a


%changelog
* Mon Feb 15 2016 Igor Vlasenko <viy@altlinux.ru> 0.4.2-alt1_5
- update to new release by fcimport

* Sun Sep 20 2015 Igor Vlasenko <viy@altlinux.ru> 0.4.2-alt1_4
- update to new release by fcimport

* Wed Aug 27 2014 Igor Vlasenko <viy@altlinux.ru> 0.4.2-alt1_3
- update to new release by fcimport

* Tue Jul 01 2014 Igor Vlasenko <viy@altlinux.ru> 0.4.2-alt1_2
- update to new release by fcimport

* Tue Feb 25 2014 Igor Vlasenko <viy@altlinux.ru> 0.4.2-alt1_1
- update to new release by fcimport

* Mon Aug 12 2013 Igor Vlasenko <viy@altlinux.ru> 0.4.1-alt1_2
- update to new release by fcimport

* Mon Jul 08 2013 Igor Vlasenko <viy@altlinux.ru> 0.4.1-alt1_1
- update to new release by fcimport

* Tue May 21 2013 Igor Vlasenko <viy@altlinux.ru> 0.4.0-alt1_1
- update to new release by fcimport

* Thu Apr 25 2013 Igor Vlasenko <viy@altlinux.ru> 0.3.0-alt1_2
- initial fc import

