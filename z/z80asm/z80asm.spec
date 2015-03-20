Name:		z80asm
Version:	1.8
Release:	alt2
Summary:	Z80 Assembler
Group:		Development/Other
License:	GPLv3+
URL:		http://savannah.nongnu.org/projects/%{name}/
Source0:	http://download.savannah.gnu.org/releases/%{name}/%{name}-%{version}.tar.gz
Packager: Ilya Mashkin <oddity@altlinux.ru>
# Don't use bundled libraries!
# Also patch Makefile to separate test target to support RPM check
Patch0:		z80asm-1.8-no-bundled-libs.patch

BuildRequires:	dos2unix
Source44: import.info

%description
z80asm is an assembler for the Z80 microprocessor. The assembler aims
to be portable and complete. Of course it assembles all official
mnemonics, but it also aims to assemble the unofficial mnemonics.
The assembler was written with the MSX computer in mind as the target
platform, but it can be used for any system with a Z80 in it. Some
header files with labels of MSX specific addresses (BIOS, BDOS, system
variables) are included.

%prep
%setup -q

# Fix line endings
dos2unix examples/hello.asm

# Don't use bundled libraries!
# Also patch Makefile to separate test target to support RPM check
%patch -P 0 -p1 -b .no-bundled-libs
rm -rf gnulib

%build
make %{?_smp_mflags} CFLAGS="%{optflags}"

%check
make %{?_smp_mflags} CFLAGS="%{optflags}" test

%install
install -d -m0755 %{buildroot}%{_bindir}
install -p -m0755 %{name} %{buildroot}%{_bindir}
install -d -m0755 %{buildroot}%{_mandir}/man1
install -p -m0644 %{name}.1 %{buildroot}%{_mandir}/man1
install -d -m0755 %{buildroot}%{_datadir}/%{name}
install -p -m0644 headers/*.asm %{buildroot}%{_datadir}/%{name}

%files
%doc COPYING GPL3 ChangeLog examples
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*
%{_datadir}/%{name}

%changelog
* Fri Mar 20 2015 Ilya Mashkin <oddity@altlinux.ru> 1.8-alt2
- build for Sisyphus

* Tue Sep 16 2014 Igor Vlasenko <viy@altlinux.ru> 1.8-alt1_7
- update to new release by fcimport

* Mon Jul 07 2014 Igor Vlasenko <viy@altlinux.ru> 1.8-alt1_6
- update to new release by fcimport

* Wed Jul 31 2013 Igor Vlasenko <viy@altlinux.ru> 1.8-alt1_5
- update to new release by fcimport

* Wed Feb 27 2013 Igor Vlasenko <viy@altlinux.ru> 1.8-alt1_4
- update to new release by fcimport

* Thu Aug 02 2012 Igor Vlasenko <viy@altlinux.ru> 1.8-alt1_3
- update to new release by fcimport

* Fri May 18 2012 Igor Vlasenko <viy@altlinux.ru> 1.8-alt1_2
- converted for Sisyphus

