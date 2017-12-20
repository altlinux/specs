# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%global debug_package %{nil}
%global languagecode uk
%global debug_package %{nil}

Summary:	Ukrainian dictionaries for aspell
Name:		aspell-%{languagecode}
Version:	1.8.0
Release:	alt2_1

URL:		http://ispell-uk.sourceforge.net/
Source:		http://freefr.dl.sourceforge.net/project/ispell-uk/spell-uk/%{version}/spell-uk-%{version}.tgz
License:	LGPLv3
Group:		Text tools

Requires:	aspell >= 0.60
BuildRequires:	aspell >= 0.60
BuildRequires:	perl-Encode
Source44: import.info
Patch: spell-uk-1.8.0-perl526.patch

%description
This is Ukrainian dictionary for spellchecking with aspell program

%prep
%setup -q -n spell-uk-%{version}
%patch -p1

%build
make ASPELL_ENC=utf-8 ASPELL_ENC_NAME=utf-8 myspell aspell uk.cwl.gz ukrainian

%install
make install PREFIX="$RPM_BUILD_ROOT"
rm -rf %{buildroot}%{_datadir}/doc/%{name}-%{version}

%files
%doc README README.uk TODO Copyright COPYING.GPL COPYING.LGPL
%{_libdir}/aspell*/uk*
%{_libdir}/aspell*/koi8-u-nl*
%{_datadir}/aspell/*

%changelog
* Wed Dec 20 2017 Igor Vlasenko <viy@altlinux.ru> 1.8.0-alt2_1
- fixed build with new perl 5.26

* Sat Nov 18 2017 Igor Vlasenko <viy@altlinux.ru> 1.8.0-alt1_1
- new version

* Sat Jan 26 2013 Igor Vlasenko <viy@altlinux.ru> 1.6.5-alt3
- applied repocop patches

* Fri May 11 2012 Roman Savochenko <rom_as@altlinux.ru> 1.6.5-alt2
- Restore "mv /usr/lib/aspell/*.dat /usr/share/aspell"

* Thu Sep 22 2011 Igor Vlasenko <viy@altlinux.ru> 1.6.5-alt1
- new version

* Thu Jul 12 2007 Igor Vlasenko <viy@altlinux.ru> 1.4.0-alt1
- new version
- mv /usr/lib/aspell/uk_affix.dat %%{_datadir}/aspell/

* Sun Jan 21 2007 Igor Vlasenko <viy@altlinux.ru> 1.2-alt2
- packaged .dat file

* Thu Jan 18 2007 Igor Vlasenko <viy@altlinux.ru> 1.2-alt1
- Release 1.2

* Tue Jul 20 2004 Vital Khilko <vk@altlinux.ru> 0.60-alt1
- special nonofficial version for aspell 0.6

* Fri Apr 23 2004 Vital Khilko <vk@altlinux.ru> 0.50-alt3
- fixed #3957

* Mon Oct 20 2003 Vital Khilko <vk@altlinux.ru> 0.50-alt2
- fix dependencies

* Tue Sep 16 2003 Vital Khilko <vk@altlinux.ru> 0.50-alt1
- New official package from aspell.net
