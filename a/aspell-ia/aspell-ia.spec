%define _enable_debug_packages %{nil}
%define debug_package          %{nil}

%define src_ver 0.50-1

%define languageenglazy Interlingua
%define languagecode ia
%define lc_ctype ia_XX

Summary:       %{languageenglazy} files for aspell
Name:          aspell-%{languagecode}
Version:       0.50.1
Release:       alt1_16
Group:         System/Internationalization
Source:        ftp://ftp.gnu.org/gnu/aspell/dict/%{languagecode}/aspell-%{languagecode}-%{src_ver}.tar.bz2
URL:           http://aspell.net/
License:	   LGPL
Provides: spell-%{languagecode}

BuildRequires: aspell >= 0.50
Requires:      aspell >= 0.50

# Mageia Stuff
#there is currently no interlingua locale
#Requires:      locales-%{languagecode}
Provides:      aspell-dictionary
Provides:	   aspell-%{lc_ctype}

Autoreqprov:   no
Source44: import.info

%description
An %{languageenglazy} dictionary for use with aspell, a spelling checker.

%prep
%setup -q -n %{name}-%{src_ver}

%build

# don't use configure macro
./configure

%make

%install
%makeinstall_std

chmod 644 Copyright README* doc/*

%files
%doc README* Copyright 
%doc doc/*
%{_libdir}/aspell*/*
%{_datadir}/aspell/*


%changelog
* Sat Jun 04 2016 Igor Vlasenko <viy@altlinux.ru> 0.50.1-alt1_16
- update by mgaimport

