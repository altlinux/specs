Epoch: 1
Group: Development/Tools
# BEGIN SourceDeps(oneline):
BuildRequires: gcc-c++ unzip
# END SourceDeps(oneline)
%brp_strip_none /usr/avr/lib/*
%define fedora 38
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
 # FORCE NOARCH
# This package is noarch intentionally, although it supplies binaries,
# as they're not intended for the build platform, but for AVR.
# The related discussion can be found here:
# https://www.redhat.com/archives/fedora-devel-list/2009-February/msg02261.html
%global _binaries_in_noarch_packages_terminate_build 0

Name:           avr-libc
Version:        2.0.0
Release:        alt6_20
Summary:        C library for use with GCC on Atmel AVR microcontrollers
License:        BSD-3-Clause
URL:            http://www.nongnu.org/avr-libc/
#Source0:        http://download.savannah.gnu.org/releases/avr-libc/avr-libc-%{version}.tar.bz2
#Source4:        http://distribute.atmel.no/tools/opensource/Atmel-AVR-GNU-Toolchain/3.4.2/avr/avr-patches.tar.gz
# since 3.4.3 atmel no longer distributes patch set, only patched sources in tarball
Source0:        http://distribute.atmel.no/tools/opensource/Atmel-AVR-GNU-Toolchain/3.5.4/avr-libc.tar.bz2#/avr-libc-%{version}+atmel.tar.bz2
Source1:        http://download.savannah.gnu.org/releases/avr-libc/avr-libc-manpages-%{version}.tar.bz2
Source2:        http://download.savannah.gnu.org/releases/avr-libc/avr-libc-user-manual-%{version}.tar.bz2
Source3:        http://download.savannah.gnu.org/releases/avr-libc/avr-libc-user-manual-%{version}.pdf.bz2
Patch0:         avr-libc-1.6.4-documentation.patch
Source5:        http://distribute.atmel.no/tools/opensource/Atmel-AVR-GNU-Toolchain/3.5.4/avr/avr8-headers.zip

BuildRequires:  avr-gcc, autoconf, automake, libtool
#BuildArch:      noarch
Source44: import.info
Conflicts: avr-binutils < 2:2.30

%description
AVR Libc is a Free Software project whose goal is to provide a high quality C
library for use with GCC on Atmel AVR microcontrollers.

AVR Libc is licensed under a single unified license. This so-called modified
Berkeley license is intented to be compatible with most Free Software licenses
like the GPL, yet impose as little restrictions for the use of the library in
closed-source commercial applications as possible.


%package doc
Group: Development/Tools
Summary:        AVR C library docs in html and pdf format
Requires:       %{name} = %{?epoch:%epoch:}%{version}-%{release}
Obsoletes:      %{name}-docs < %{version}-%{release}
BuildArch: noarch

%description doc
This package contains the AVR C library docs in html and pdf format, the main
package already contains the docs in man-page format (use "avr-man xxxx" to
access these).


%prep
%setup -q -c
# atmel's tarball needs some shuffling to have expected directory layout
# must be done in two steps because of conflicting libc directory
mv libc delete-libc
mv delete-libc/avr-libc/* .
rmdir delete-libc/avr-libc
tar -joxf %SOURCE1
%patch0  -p1 -b .nolatexbatch

I=0
unzip %{SOURCE5} -d avr8-headers
for i in ./avr8-headers/avr/io[0-9a-zA-Z]*.h
do
  cp $i include/avr/ -v
done

# Add html docs
mkdir html
cd html/
tar -jxvf %SOURCE2
cd -

# Add pdf manual
mkdir pdf
cd pdf/
bzip2 -dc %SOURCE3 > avr-libc-user-manual-%{version}.pdf
cd -

for i in doc/api/faq.dox doc/api/overview.dox include/stdio.h include/stdlib.h;
  do
    iconv -f CP1252 -t UTF8 $i > tmp
    mv tmp $i
done
sed -i 's|@DOC_INST_DIR@/man|%{_prefix}/avr/share/man|' scripts/avr-man.in


%build
./bootstrap

# really don't try to force distrowide flags on crosscompiled noarch
unset CC CXX CFLAGS CXXFLAGS FFLAGS FCFLAGS LDFLAGS LT_SYS_LIBRARY_PATH

# The ps doc ways in at 7Mb versus 2.5 for the pdf and has little added value
./configure --prefix=%{_prefix} --host=avr --build=`./config.guess` #--enable-doc
# don't use %{?_smp_mflags}, it breaks the build
make


%install
make install DESTDIR=$RPM_BUILD_ROOT

# put the man-pages in the FHS mandir and gzip them
mkdir -p $RPM_BUILD_ROOT%{_prefix}/avr/share
find man/ -type f -exec gzip {} \;
mv man  $RPM_BUILD_ROOT%{_prefix}/avr/share

# we only want to use %doc with an absolute path to avoid rpmbuild from erasing
# %{_docdir}/%{name}
mv $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version} $RPM_BUILD_ROOT%{_docdir}/%{name}
install -p -m 644 doc/TODO doc/CHANGES.old AUTHORS ChangeLog* LICENSE NEWS \
  pdf/* README $RPM_BUILD_ROOT%{_docdir}/%{name}
mkdir $RPM_BUILD_ROOT%{_docdir}/%{name}/html
cp -ap html/%{name}-user-manual*/* $RPM_BUILD_ROOT%{_docdir}/%{name}/html
chmod -R u=rwX,g=rX,o=rX $RPM_BUILD_ROOT%{_docdir}/%{name}/html


%files
%dir %{_prefix}/avr
%dir %{_prefix}/avr/share
%doc %{_prefix}/avr/share/man
%dir %{_docdir}/%{name}
%doc %{_docdir}/%{name}/AUTHORS
%doc %{_docdir}/%{name}/C*
%doc %{_docdir}/%{name}/LICENSE
%doc %{_docdir}/%{name}/NEWS
%doc %{_docdir}/%{name}/README
%doc %{_docdir}/%{name}/TODO
%doc %{_docdir}/%{name}/examples
%{_prefix}/avr/include
%{_prefix}/avr/lib
%{_bindir}/avr-man

%files doc
%doc %{_docdir}/%{name}/html
%doc %{_docdir}/%{name}/%{name}*.pdf

%changelog
* Tue Oct 10 2023 Igor Vlasenko <viy@altlinux.org> 1:2.0.0-alt6_20
- rebuild with new avr-gcc

* Sat May 07 2022 Igor Vlasenko <viy@altlinux.org> 1:2.0.0-alt6_15
- update to new release by fcimport

* Fri Aug 27 2021 Igor Vlasenko <viy@altlinux.org> 1:2.0.0-alt6_12
- fixed build with added process-lto

* Wed Nov 18 2020 Igor Vlasenko <viy@altlinux.ru> 1:2.0.0-alt6_10
- update to new release by fcimport

* Sat Oct 10 2020 Igor Vlasenko <viy@altlinux.ru> 1:2.0.0-alt6_9
- rebuild on armh

* Wed Feb 06 2019 Igor Vlasenko <viy@altlinux.ru> 1:2.0.0-alt6_6
- added conflict for altbug#36040

* Sun Feb 03 2019 Igor Vlasenko <viy@altlinux.ru> 1:2.0.0-alt5_6
- fixed build

* Fri Feb 03 2017 Grigory Milev <week@altlinux.ru> 1:2.0.0-alt5
- Updated from Atmel

* Mon Jun 20 2016 Grigory Milev <week@altlinux.ru> 1:2.0.0-alt4
- Buildreq cleanup

* Mon May 30 2016 Grigory Milev <week@altlinux.ru> 1:2.0.0-alt3
- Build requires cleanup

* Mon May 30 2016 Grigory Milev <week@altlinux.ru> 1:2.0.0-alt2
- Remove fonts from BuildRequires

* Tue Feb 16 2016 Grigory Milev <week@altlinux.ru> 1:2.0.0-alt1
- new version released
- fix bug #31800

* Thu Feb 12 2015 Grigory Milev <week@altlinux.ru> 1:1.8.1-alt1
- new version released
- update Atmel headers

* Fri Mar 14 2014 Grigory Milev <week@altlinux.ru> 1:1.8.0-alt5
- update Atmel headers to last version

* Wed Oct 16 2013 Grigory Milev <week@altlinux.ru> 1:1.8.0-alt4
- must be rebuilded with new avr-gcc

* Mon Oct 14 2013 Grigory Milev <week@altlinux.ru> 1:1.8.0-alt3
- last version from Atmel
- build with new avr-binutils and avr-gcc

* Fri Feb 01 2013 Grigory Milev <week@altlinux.ru> 1:1.8.0-alt2
- rebuild with new avr-binutils and avr-gcc

* Fri Feb 01 2013 Grigory Milev <week@altlinux.ru> 1:1.8.0-alt1
- new version released

* Thu Mar 17 2011 Grigory Milev <week@altlinux.ru> 1:1.7.1-alt2
- rebuilded with avr-gcc-4.5.1-alt3

* Thu Mar 10 2011 Grigory Milev <week@altlinux.ru> 1:1.7.1-alt1
- new version released

* Thu Jan 13 2011 Grigory Milev <week@altlinux.ru> 1:1.7.0-alt2
- rebuild by new binutils and gcc

* Wed Nov 03 2010 Grigory Milev <week@altlinux.ru> 1:1.7.0-alt1
- new version released

* Sun Nov 29 2009 Grigory Milev <week@altlinux.ru> 1:1.6.7-alt1
- new version released
- remove .pdf from manual package

* Tue Jun 23 2009 Grigory Milev <week@altlinux.ru> 1:1.6.6-alt1
- new version released (see ChangeLog inside package)

* Mon Dec 29 2008 Grigory Milev <week@altlinux.ru> 1:1.6.4-alt1
- new version released

* Mon May 19 2008 Grigory Milev <week@altlinux.ru> 1:1.6.2-alt1
- new version released
- fixed build requires (LaTex utf8.def)

* Wed Jan 09 2008 Grigory Milev <week@altlinux.ru> 1:1.6.1-alt1
- new version released

* Wed Oct  4 2006 Grigory Milev <week@altlinux.ru> 1:1.4.4-alt1
- new version released
- fixating spec
- move avr-man to doc package
- clean up spec

* Mon Sep 19 2005 Grigory Milev <week@altlinux.ru> 1:1.2.5-alt1
- new version released

* Fri Jun 03 2005 Grigory Milev <week@altlinux.ru> 1:1.2.3-alt1
- new version released
- do not compile documents, get it from precompiled (due some bugs)

* Fri Jan 21 2005 Grigory Milev <week@altlinux.ru> 1:1.2.0-alt1
- new version released

* Fri May 28 2004 Grigory Milev <week@altlinux.ru> 1:1.0.4-alt1
- new version released

* Tue Apr 13 2004 Grigory Milev <week@altlinux.ru> 1:1.0.3-alt1
- new version released

* Wed Oct  8 2003 Grigory Milev <week@altlinux.ru> 1:1.0-alt1
- first release
- build user-manual

* Fri Sep  5 2003 Grigory Milev <week@altlinux.ru> 20030805-alt1
- new cvs snapshot released

* Thu Jun 19 2003 Grigory Milev <week@altlinux.ru> 20030512-alt1
- new cvs snapshot released

* Tue Apr 22 2003 Grigory Milev <week@altlinux.ru> 20030414-alt1
- new snapshot version

* Mon Feb 10 2003 Grigory Milev <week@altlinux.ru> 20030203-alt2
- new cvs version (snapshot)

* Tue Nov  5 2002 Grigory Milev <week@altlinux.ru> 20021028-alt1.cvs
- new version (snapshot)

* Fri Oct 25 2002 Grigory Milev <week@altlinux.ru> 20020203-alt1
- Initial build for ALT Linux

* Fri May 03 2002 Theodore Roth <troth@verinet.com>
- Added patch to fix timer.h for mega128.

* Mon Apr 29 2002 Theodore Roth <troth@verinet.com>
- Added patch to fix headers.
- Fix strncasecmp_P macro in pgmspace.h.

* Wed Mar 27 2002 Theodore Roth <troth@verinet.com>
- Updated avr-gcc dependency to 3.0.4-2.
- Fixed up %files section to work with rh-7.1.

* Mon Mar 17 2002 Theodore Roth <troth@verinet.com>
- Initial spec file.


