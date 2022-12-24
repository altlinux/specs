Group: Games/Other
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:           pmars
Version:        0.9.2
Release:        alt2_27
Summary:        Portable corewar system with ICWS'94 extensions

License:        GPLv2+
URL:            http://www.koth.org/pmars/
Source0:        http://downloads.sourceforge.net/corewar/%{name}-%{version}.tar.gz
# Patch to disable stripping of binary in spec file
Patch0:         pmars-0.9.2-nostrip.patch
#Show compiler commands
Patch1:         pmars-0.9.2-CCat.patch
Patch2:         pmars-sfprintf-format.patch
BuildRequires:  gcc
BuildRequires:  libX11-devel
Requires:       fonts-bitmap-75dpi
Source44: import.info

%description
pMARS is a Memory Array Redcode Simulator (MARS) for corewar.

    * portable, run it on your Mac at home or VAX at work
    * free and comes with source
    * core displays for DOS, Mac and UNIX
    * implements a new redcode dialect, ICWS'94, while remaining compatible
      with ICWS'88
    * powerful redcode extensions: multi-line EQUates, FOR/ROF text repetition
    * one of the fastest simulators written in a high level language
    * full-featured, programmable debugger
    * runs the automated tournament "KotH" at http://www.koth.org and
      http://www.ecst.csuchico.edu/~pizza/koth/ and the annual ICWS tournaments

%prep
%setup -q
%patch0 -p0 -b .nostrip
%patch1 -p0 -b .CCat
%patch2 -p0 -b .printf

# Make temporary doc dir
mkdir doc_install
cp -a doc doc_install
rm doc_install/doc/pmars.6


%build
make -C src CFLAGS="%{optflags} -DEXT94 -DXWINGRAPHX -DPERMUTATE -std=gnu89"


%install
install -D -p -m 755 src/pmars %{buildroot}%{_bindir}/pmars
install -D -p -m 644 doc/pmars.6 %{buildroot}%{_mandir}/man6/pmars.6



%files
%doc AUTHORS ChangeLog CONTRIB COPYING README config/ doc_install/doc/ warriors/
%{_bindir}/pmars
%{_mandir}/man6/pmars.6*

%changelog
* Sat Dec 24 2022 Igor Vlasenko <viy@altlinux.org> 0.9.2-alt2_27
- update to new release by fcimport

* Wed Sep 27 2017 Igor Vlasenko <viy@altlinux.ru> 0.9.2-alt2_17
- update to new release by fcimport

* Thu Mar 16 2017 Igor Vlasenko <viy@altlinux.ru> 0.9.2-alt2_15
- update to new release by fcimport

* Wed Feb 17 2016 Igor Vlasenko <viy@altlinux.ru> 0.9.2-alt2_14
- update to new release by fcimport

* Sun Sep 20 2015 Igor Vlasenko <viy@altlinux.ru> 0.9.2-alt2_13
- update to new release by fcimport

* Wed Aug 27 2014 Igor Vlasenko <viy@altlinux.ru> 0.9.2-alt2_12
- update to new release by fcimport

* Tue Jul 01 2014 Igor Vlasenko <viy@altlinux.ru> 0.9.2-alt2_11
- update to new release by fcimport

* Tue Feb 25 2014 Igor Vlasenko <viy@altlinux.ru> 0.9.2-alt2_10
- update to new release by fcimport

* Mon Aug 12 2013 Igor Vlasenko <viy@altlinux.ru> 0.9.2-alt2_9
- update to new release by fcimport

* Fri Feb 22 2013 Igor Vlasenko <viy@altlinux.ru> 0.9.2-alt2_8
- update to new release by fcimport

* Fri Jul 27 2012 Igor Vlasenko <viy@altlinux.ru> 0.9.2-alt2_7
- update to new release by fcimport

* Fri Mar 02 2012 Igor Vlasenko <viy@altlinux.ru> 0.9.2-alt2_6
- rebuild with fixed sourcedep analyser (#27020)

* Sat Jan 21 2012 Igor Vlasenko <viy@altlinux.ru> 0.9.2-alt1_6
- update to new release by fcimport

* Mon May 23 2011 Igor Vlasenko <viy@altlinux.ru> 0.9.2-alt1_5
- converted from Fedora by srpmconvert script

