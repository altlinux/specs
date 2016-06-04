%define _enable_debug_packages %{nil}
%define debug_package          %{nil}

#
# NOTE: rpm is unable to package filenames in an enocidng other than the
# the one it is currently using; so this package has to be build with
# an iso-8859-* locale; eg: LC_ALL=fr rpm -be specfile
#

%define src_ver 3.3-2

%define languageenglazy Romanian
%define languagecode ro
%define lc_ctype ro_RO

Summary:       %{languageenglazy} files for aspell
Name:          aspell-%{languagecode}
Version:       3.3.2
Release:       alt1_6
Group:         System/Internationalization
Source:        ftp://ftp.gnu.org/gnu/aspell/dict/ro/aspell5-ro-%{src_ver}.tar.bz2
URL:           http://aspell.net/
License:	   Free

BuildRequires: aspell >= 0.50
Requires:      aspell >= 0.50

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
%setup -q -n aspell5-ro-%{src_ver}

%build
# don't use configure macro
./configure

%make

%install
%makeinstall_std

#cp doc/README README.%{languagecode}
chmod 644 README Copyright 

%files
%doc README Copyright
%{_libdir}/aspell*/*
%{_datadir}/aspell/*


%changelog
* Sat Jun 04 2016 Igor Vlasenko <viy@altlinux.ru> 3.3.2-alt1_6
- update by mgaimport

