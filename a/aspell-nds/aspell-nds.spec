%define _enable_debug_packages %{nil}
%define debug_package          %{nil}

%define src_ver 0.01-0
%define fname aspell6-%{languagecode}
%define aspell_ver 0.60
%define languageenglazy Low-Saxon
%define languagecode nds
%define lc_ctype nds_DE

Summary:       %{languageenglazy} files for aspell
Name:          aspell-%{languagecode}
Version:       0.01.0
Release:       alt1_16
Group:         System/Internationalization
Source:        http://ftp.gnu.org/gnu/aspell/dict/%{languagecode}/%{fname}-%{src_ver}.tar.bz2
URL:		   http://aspell.net/
License:	   GPL
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

chmod 644 Copyright README* 

# if there is isn't a qwertz.kbd provided by aspell, create it
if [ ! -r ${RPM_BUILD_ROOT}/%{_libdir}/aspell/qwertz.kbd \
	-a ! -r /%{_libdir}/aspell/qwertz.kbd ]
then
	cat /%{_libdir}/aspell/standard.kbd | \
	perl -p -e 's/ty/tz/; s/yu/zu/; s/zx/yx/' \
	> ${RPM_BUILD_ROOT}/%{_libdir}/aspell/qwertz.kbd
fi

%files
%doc Copyright README*
%{_libdir}/aspell/*
%{_datadir}/aspell/*


%changelog
* Sat Jun 04 2016 Igor Vlasenko <viy@altlinux.ru> 0.01.0-alt1_16
- update by mgaimport

