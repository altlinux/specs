%define src_ver 0.50.1-0
%define languageenglazy Norwegian Bokmaal
%define languagecode nb
%define _enable_debug_packages %{nil}
%define debug_package %{nil}

Summary:	%{languageenglazy} files for aspell
Name:		aspell-%{languagecode}
Version:	0.50.1
Release:	alt1_10
Group:		System/Internationalization
Source0:	ftp://ftp.gnu.org/aspell/aspell-%{languagecode}-%{src_ver}.tar.bz2
URL:		http://aspell.sourceforge.net/
License:	GPL
Provides:	spell-no
Provides:	spell-nb

BuildRequires:	aspell >= 0.50
Requires:	aspell >= 0.50

# Mageia Stuff
Requires:	locales-%{languagecode}
Provides:	aspell-dictionary
Provides:	aspell-no = 0.50.2-13
Obsoletes:	aspell-no
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

%files
%doc README Copyright
%{_libdir}/aspell*/*
%{_datadir}/aspell/*


%changelog
* Sat Jun 04 2016 Igor Vlasenko <viy@altlinux.ru> 0.50.1-alt1_10
- update by mgaimport

