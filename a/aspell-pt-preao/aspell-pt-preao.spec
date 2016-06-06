%define _enable_debug_packages %{nil}
%define debug_package          %{nil}

%define intname aspell6
%define intver 20120714

%define languageglazy Portuguese
%define languagecode pt-preao
%define lc_ctype pt_PT-preao


Summary:	%{languageglazy} files previous to 1990 orthography agreement for aspell
Name:		aspell-%{languagecode}
Version:	0.60.0
Release:	alt1_9
Group:		System/Internationalization
License:	GPL
URL:		http://aspell.sourceforge.net/
# http://ftp.gnu.org/gnu/aspell/dict/%{languagecode}/aspell-%{languagecode}-%{src_ver}.tar.bz2
Source0:	http://natura.di.uminho.pt/download/sources/Dictionaries/aspell6/%{intname}.%{languagecode}-%{intver}.tar.bz2
BuildRequires:	aspell >= 0.60
Requires:	aspell >= 0.60
# Mandriva Stuff
Requires:	locales-pt
Provides:	aspell-dictionary
Provides:	aspell-%{lc_ctype}
Provides:	%{intname}-%{lc_ctype}
Provides:	%{intname}-%{languagecode}
Source44: import.info

%description
A %{languageglazy} dictionary previous to the orthography agreement made in 1990
to use with aspell, a spelling checker.
Version %{intver}.

%prep
%setup -qn %{intname}-%{lc_ctype}-%{intver}-0

%build
# don't use configure macro
./configure
%make

%install
%makeinstall_std

%files
%doc README Copyright COPYING doc/LEIAME-preao.txt
%{_libdir}/aspell
%{_datadir}/aspell/*


%changelog
* Mon Jun 06 2016 Igor Vlasenko <viy@altlinux.ru> 0.60.0-alt1_9
- converted for ALT Linux by srpmconvert tools

