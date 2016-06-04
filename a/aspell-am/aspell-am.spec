%define _enable_debug_packages %{nil}
%define debug_package          %{nil}

%define src_ver 0.03-1
%define fname aspell6-%{languagecode}
%define aspell_ver 0.60
%define languageenglazy Amharic
%define languagecode am
%define lc_ctype am_ET

Summary:       %{languageenglazy} files for aspell
Name:          aspell-%{languagecode}
Version:       0.03.1
Release:       alt1_15
Group:         System/Internationalization
Source:        http://ftp.gnu.org/gnu/aspell/dict/%{languagecode}/%{fname}-%{src_ver}.tar.bz2
URL:		   http://aspell.net/
License:	   GPL
Provides: spell-%{languagecode}

BuildRequires: aspell >= %{aspell_ver}
Requires:      aspell >= %{aspell_ver}

# Mageia Stuff
Requires:      locales-%{languagecode}
# aspell = 1, myspell = 2, lang-specific = 3
Provides:      aspell-dictionary
Provides:      aspell-%{lc_ctype}

Autoreqprov:   no
Source44: import.info

%description
An %{languageenglazy} dictionary for use with aspell, a spelling checker.

%prep
%setup -q -n %{fname}-%{src_ver}

%build
# don't use configure macro
./configure

%make

%install
%makeinstall_std

chmod 644 Copyright README* 

%files
%doc Copyright README* doc/*
%{_libdir}/aspell/*
%{_datadir}/aspell/*


%changelog
* Sat Jun 04 2016 Igor Vlasenko <viy@altlinux.ru> 0.03.1-alt1_15
- update by mgaimport

