%define _enable_debug_packages %{nil}
%define debug_package          %{nil}

%define src_ver 0.99.4.2-0
%define fname aspell6-%{languagecode}
%define aspell_ver 0.60
%define languageenglazy Hungarian
%define languagecode hu
%define lc_ctype hu_HU

Summary:       %{languageenglazy} files for aspell
Name:          aspell-%{languagecode}
Version:       0.99.4.2.0
Release:       alt1_14
Group:         System/Internationalization
Source:        http://ftp.gnu.org/gnu/aspell/dict/%{languagecode}/%{fname}-%{src_ver}.tar.bz2
URL:		   http://aspell.sourceforge.net/
#Source:	       http://prdownloads.sourceforge.net/wordlist-hu/wordlist-hu-%{src_ver}.tar.bz2
#URL:		   http://wordlist-hu.sourceforge.net
License:	   GPL

BuildRequires: aspell >= %{aspell_ver}
Requires:      aspell >= %{aspell_ver}

# Mageia Stuff
Requires:      locales-%{languagecode}
Provides:      aspell-dictionary
Provides:	   aspell-%{lc_ctype}
Provides:      spell-%{languagecode}

Autoreqprov:   no
Source44: import.info

%description
A %{languageenglazy} dictionary for use with aspell, a spelling checker.

%prep
%setup -q -n %{fname}-%{src_ver}

%build
# don't use configure macro
./configure

%make

%install
%makeinstall_std

#cp doc/README README.%{languagecode}
#chmod 644 README Copyright README.%{languagecode}

%files
%doc README* Copyright doc/*
%{_libdir}/aspell/*
%{_datadir}/aspell/*


%changelog
* Sat Jun 04 2016 Igor Vlasenko <viy@altlinux.ru> 0.99.4.2.0-alt1_14
- update by mgaimport

