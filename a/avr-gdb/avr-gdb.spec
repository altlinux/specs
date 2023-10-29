Group: Development/Tools
# BEGIN SourceDeps(oneline):
BuildRequires: /usr/bin/bison /usr/bin/expect /usr/bin/flex /usr/bin/m4 /usr/bin/runtest perl(Exporter.pm) swig texinfo
# END SourceDeps(oneline)
BuildRequires: /usr/bin/pod2man
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%define target avr

Name:           %{target}-gdb
Version:        8.1
Release:        alt1_5
Summary:        GDB for (remote) debugging %{target} binaries
License:        GPLv2+
URL:            http://www.sourceware.org/gdb/
Source0:        http://ftp.gnu.org/gnu/gdb/gdb-%{version}.tar.xz
Source1:        README.fedora

BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  libncurses++-devel libncurses-devel libncursesw-devel libtic-devel libtinfo-devel
BuildRequires:  zlib-devel
BuildRequires:  makeinfo
BuildRequires:  gnu-config

Provides: bundled(libiberty)
Source44: import.info

%description
This is a special version of GDB, the GNU Project debugger, for (remote)
debugging %{target} binaries. GDB allows you to see what is going on
inside another program while it executes or what another program was doing at
the moment it crashed. 


%prep
%setup -q -c
cp %{SOURCE1} .


%build
cp -a /usr/share/gnu-config/config.{guess,sub} gdb-%{version}/
mkdir -p build
pushd build
CFLAGS="$RPM_OPT_FLAGS -D_GNU_SOURCE" \
  ../gdb-%{version}/configure --prefix=%{_prefix} \
  --libdir=%{_libdir} --mandir=%{_mandir} --infodir=%{_infodir} \
  --target=%{target} --disable-nls --disable-werror \
  --with-system-zlib
%make_build
popd


%install
pushd build
make install DESTDIR=$RPM_BUILD_ROOT
popd

# we don't want these as we are a cross version
rm -r $RPM_BUILD_ROOT%{_infodir}
rm -r $RPM_BUILD_ROOT%{_datadir}/gdb
# Should not be installed
rm    $RPM_BUILD_ROOT%{_libdir}/libavr-sim.a

# no need for devel files
rm -rf $RPM_BUILD_ROOT%{_includedir}

%files
%doc gdb-%{version}/COPYING* gdb-%{version}/README*
%{_bindir}/%{name}*
%{_bindir}/avr-run
%{_mandir}/man1/avr-*
%{_mandir}/man5/avr-*


%changelog
* Sun Oct 29 2023 Alexey Sheplyakov <asheplyakov@altlinux.org> 8.1-alt1_5
- NMU: fixed FTBFS on LoongArch (use fresh config.guess,sub)

* Sat Oct 10 2020 Igor Vlasenko <viy@altlinux.ru> 8.1-alt1_4
- rebuild on armh

* Wed Feb 06 2019 Igor Vlasenko <viy@altlinux.ru> 8.1-alt1_2
- new version

* Sun May 29 2016 Igor Vlasenko <viy@altlinux.ru> 7.1-alt1_13
- update to new release by fcimport

* Mon Sep 21 2015 Igor Vlasenko <viy@altlinux.ru> 7.1-alt1_12
- update to new release by fcimport

* Wed Sep 10 2014 Igor Vlasenko <viy@altlinux.ru> 7.1-alt1_11
- update to new release by fcimport

* Tue Jul 01 2014 Igor Vlasenko <viy@altlinux.ru> 7.1-alt1_10
- update to new release by fcimport

* Thu Aug 22 2013 Igor Vlasenko <viy@altlinux.ru> 7.1-alt1_9
- update to new release by fcimport

* Fri Jul 12 2013 Igor Vlasenko <viy@altlinux.ru> 7.1-alt1_8
- update to new release by fcimport

* Thu Apr 25 2013 Igor Vlasenko <viy@altlinux.ru> 7.1-alt1_7
- initial fc import

