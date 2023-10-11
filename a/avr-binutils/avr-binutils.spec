Group: Development/Tools
# BEGIN SourceDeps(oneline):
BuildRequires: /usr/bin/bison /usr/bin/expect /usr/bin/flex /usr/bin/m4 /usr/bin/runtest gcc-c++ texinfo zlib-devel
# END SourceDeps(oneline)
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%define target avr

Name:           %{target}-binutils
Version:        2.35
Release:        alt1_2
Epoch:          2
Summary:        Cross Compiling GNU binutils targeted at %{target}
License:        GPLv2+
URL:            http://www.gnu.org/software/binutils/
Source0:        ftp://ftp.gnu.org/pub/gnu/binutils/binutils-%{version}.tar.xz
Source1:        README.fedora
#add widespread options to avr-size: --format=avr -mcu=XX
Patch1: http://distribute.atmel.no/tools/opensource/avr-gcc/binutils-2.20.1/30-binutils-2.20.1-avr-size.patch
Patch2: avr-binutils-config.patch

BuildRequires:  gawk makeinfo gcc
#for autoreconf:
BuildRequires:  gettext-tools libasprintf-devel automake
BuildRequires:  autoconf_2.60
%set_autoconf_version 2.60
Provides: bundled(libiberty)
Source44: import.info

%description
This is a Cross Compiling version of GNU binutils, which can be used to
assemble and link binaries for the %{target} platform, instead of for the
native %{_arch} platform.


%prep
%setup -q -c
pushd binutils-%{version}
%patch1 -p2 -b .avr-size
%patch2 -p1 -b .config

# We call configure directly rather than via macros, thus if
# we are using LTO, we have to manually fix the broken configure
# scripts
pushd libiberty
autoconf -f
popd
pushd intl
autoconf -f
popd

popd 
cp %{SOURCE1} .

# known to fail on (arm?)
rm binutils-*/ld/testsuite/ld-elf/pr22450.*

# first build with old cc?
[ %version = 2.35 ] && rm binutils-*/ld/testsuite/ld-elf/notes.exp

%build

mkdir -p build
pushd build
CFLAGS="$RPM_OPT_FLAGS" ../binutils-%{version}/configure --prefix=%{_prefix} \
  --libdir=%{_libdir} --mandir=%{_mandir} --infodir=%{_infodir} \
  --target=%{target} --disable-werror --disable-nls
%make_build
popd

%check
cd build
%ifnarch %ix86 %arm
# on x86 can't find proper config, export does not ot help for gas
# export DEJAGNU=`pwd`/binutils/site.exp
make check
%endif

%install
pushd build
make install DESTDIR=$RPM_BUILD_ROOT
popd
# these are for win targets only
rm -f $RPM_BUILD_ROOT%{_mandir}/man1/%{target}-{dlltool,windres}.1
# we don't want these as we are a cross version
rm -r $RPM_BUILD_ROOT%{_infodir}
rm    $RPM_BUILD_ROOT%{_libdir}/libiberty.a ||:

%pre
# upgrade from binutils 2.26
if [ -L /usr/avr ]; then
  echo link /usr/avr detected. removing...
  rm /usr/avr
fi




%files
%doc --no-dereference binutils-%{version}/COPYING binutils-%{version}/COPYING.LIB
%doc binutils-%{version}/README README.fedora
%{_prefix}/%{target}
%{_bindir}/%{target}-*
%{_mandir}/man1/%{target}-*.1*


%changelog
* Wed Oct 11 2023 Alexey Sheplyakov <asheplyakov@altlinux.org> 2:2.35-alt1_2
- NMU: fixed FTBFS (use autoconf 2.69)

* Wed Nov 18 2020 Igor Vlasenko <viy@altlinux.ru> 2:2.35-alt1_1
- update to new release by fcimport

* Sat Oct 10 2020 Igor Vlasenko <viy@altlinux.ru> 2:2.32-alt1_5
- rebuild on armh

* Sat Feb 09 2019 Igor Vlasenko <viy@altlinux.ru> 2:2.32-alt1_1
- new version

* Tue Feb 05 2019 Igor Vlasenko <viy@altlinux.ru> 2:2.30-alt1_3
- new version (closes: #36040)

* Sun Feb 03 2019 Igor Vlasenko <viy@altlinux.ru> 2:2.26-alt2
- NMU: rebuild on aarch64

* Fri Feb 03 2017 Grigory Milev <week@altlinux.ru> 2:2.26-alt1
- New version released

* Mon Jun 20 2016 Grigory Milev <week@altlinux.ru> 2:2.25-alt3
- Cleanup build requires

* Mon May 16 2016 Grigory Milev <week@altlinux.ru> 2:2.25-alt2
- Remove avr-binutils from build requires - fix for fist ARM build

* Sat Jan 09 2016 Grigory Milev <week@altlinux.ru> 2:2.25-alt1
- New version from Atmel (Toolchain 3.5.0)

* Thu Mar 13 2014 Grigory Milev <week@altlinux.ru> 2:2.23.2-alt1
- New version released

* Mon Oct 14 2013 Grigory Milev <week@altlinux.ru> 2:2.23.1-alt1
- Build last version from Atmel with most of 8 bits AVR controllers supported

* Fri Feb 01 2013 Grigory Milev <week@altlinux.ru> 1:2.23.51.0.8-alt1
- new version released
- 30-binutils-2.20.1-avr-size.patch from fedore added

* Thu Jan 13 2011 Grigory Milev <week@altlinux.ru> 1:2.21-alt1
- new version released
- updated from fc src.rpm
- removed coff patch
- fixed link paths

* Mon Nov 29 2010 Grigory Milev <week@altlinux.ru> 1:2.20.51.0.9-alt2
- fix build requires

* Wed Nov 03 2010 Grigory Milev <week@altlinux.ru> 1:2.20.51.0.9-alt1
- New version released

* Wed Dec 02 2009 Grigory Milev <week@altlinux.ru> 1:2.18.50.0.3-alt3
- fix build requires
- build using gcc 3.4

* Sat Jan 12 2008 Grigory Milev <week@altlinux.ru> 1:2.18.50.0.3-alt2
- added avr coff patch

* Wed Jan 09 2008 Grigory Milev <week@altlinux.ru> 1:2.18.50.0.3-alt1
- New version released

* Wed Sep 21 2005 Grigory Milev <week@altlinux.ru> 1:2.16-alt1
- New version released

* Fri Sep  5 2003 Grigory Milev <week@altlinux.ru> 1:2.14-alt1
- 2.14 released

* Thu Jun 19 2003 Grigory Milev <week@altlinux.ru> 20030512-alt1
- new version released

* Tue Apr 22 2003 Grigory Milev <week@altlinux.ru> 20030414-alt1
- new version (cvs snapshot 20030414)

* Mon Feb 10 2003 Grigory Milev <week@altlinux.ru> 2.13.75-alt2
- new version (snapshot 030118)

* Tue Nov  5 2002 Grigory Milev <week@altlinux.ru> 2.13.75-021028
- new version (snapshot)

* Wed Oct 30 2002 Grigory Milev <week@altlinux.ru> 2.11.2-alt1
- Initial build for ALT Linux 

* Tue Mar 27 2002 Theodore Roth <troth@verinet.com>
- dir directive for %{_prefix}/avr/{bin,lib}

* Mon Mar 17 2002 Theodore Roth <troth@verinet.com>
- Initial spec file.

