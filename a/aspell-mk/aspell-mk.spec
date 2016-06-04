%define _enable_debug_packages %{nil}
%define debug_package          %{nil}

%define src_ver 0.50-0
%define languageenglazy Macedonian
%define languagecode mk
%define lc_ctype mk_MK

Summary:       %{languageenglazy} files for aspell
Name:          aspell-%{languagecode}
Version:       0.50.0
Release:       alt1_16
Group:         System/Internationalization
Source:	       http://ftp.gnu.org/gnu/aspell/dict/%{languagecode}/aspell-%{languagecode}-%{src_ver}.tar.bz2
URL:		   http://aspell.net/
License:	   GPL

BuildRequires: aspell >= 0.50
Requires:      aspell >= 0.50

# Mageia Stuff
Requires:      locales-%{languagecode}
Provides:      aspell-dictionary
Provides:	   aspell-%{lc_ctype}

Autoreqprov:   no
Source44: import.info

%description
A %{languageenglazy} dictionary for use with aspell, a spelling checker.

%prep
%setup -q -n %{name}-%{src_ver}

%build
# don't use configure macro
./configure

%make

%install
%makeinstall_std

mkdir -p $RPM_BUILD_ROOT/%{_datadir}/aspell
mkdir -p $RPM_BUILD_ROOT/%{_libdir}/aspell

chmod 644 Copyright README* 

%files
%doc README* Copyright 
%{_libdir}/aspell*/*
%{_datadir}/aspell/*


%changelog
* Sat Jun 04 2016 Igor Vlasenko <viy@altlinux.ru> 0.50.0-alt1_16
- update by mgaimport

