%define _enable_debug_packages %{nil}
%define debug_package          %{nil}

%define src_ver 1.2.1-0
%define fname aspell6-%{languagecode}
%define aspell_ver 0.60
%define languageenglazy Lithuanian
%define languagecode lt
%define lc_ctype lt_LT

Summary:       %{languageenglazy} files for aspell
Name:          aspell-%{languagecode}
Version:       1.2.1
Release:       alt1_16
Group:         System/Internationalization
Source:        http://ftp.gnu.org/gnu/aspell/dict/%{languagecode}/%{fname}-%{src_ver}.tar.bz2
URL:		   http://aspell.net/
License:	   Free Software (see Copyright file)
Provides: spell-%{languagecode}

BuildRequires: aspell >= %{aspell_ver}
Requires:      aspell >= %{aspell_ver}

# Mageia Stuff
Requires:      locales-%{languagecode}
Provides:      aspell-dictionary
Provides:      aspell-%{lc_ctype}

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

chmod 644 Copyright README* doc/*

%files
%doc README* Copyright doc/*
%{_libdir}/aspell/*
%{_datadir}/aspell/*


%changelog
* Sat Jun 04 2016 Igor Vlasenko <viy@altlinux.ru> 1.2.1-alt1_16
- update by mgaimport

