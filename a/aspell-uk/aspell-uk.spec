%define aspell_ver 0.60
%define sourcename spell-uk-%{version}

Name:		aspell-uk
Summary:	Aspell spelling dictionary for Ukrainian
Version:	1.6.5
Release:	alt2
Group:		System/Internationalization
URL:		http://ispell-uk.sourceforge.net/
Source:		%{sourcename}.tgz
License:	GPL and LGPL
Packager:	Roman Savochenko <rom_as@altlinux.ru>
Patch:		spell-uk-1.6.5-alt-Makefile.patch

#arch-dependent(byte-order)?
#BuildArch:	noarch
#ExcludeArch:	ia64

# Automatically added by buildreq on Thu Jan 18 2007
BuildRequires: aspell perl-Encode perl-PerlIO

Requires:	aspell >= %aspell_ver
BuildRequires:	aspell >= %aspell_ver
#iconv

Provides: aspell-dictionary

%description
This is ukrainian dictionary for spellchecking with aspell program

%prep
%setup -q -n %{sourcename}
%patch -p1

%build
%make aspell

%install
#rm -fr $RPM_BUILD_ROOT
%make install-aspell-dict PREFIX=$RPM_BUILD_ROOT

mv $RPM_BUILD_ROOT%{_libdir}/aspell/*.dat $RPM_BUILD_ROOT%{_datadir}/aspell/

%files
%doc README README.uk TODO Copyright COPYING.GPL COPYING.LGPL
%{_datadir}/aspell/*
%{_libdir}/aspell*/uk*
%{_libdir}/aspell*/koi8-u-nl*

%changelog
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
