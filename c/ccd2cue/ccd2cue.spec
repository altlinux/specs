Name: ccd2cue
Version: 0.5
Release: alt1

Summary: CCD sheet to CUE sheet converter
License: GPL
Group: Archiving/Cd burning
Url: https://www.gnu.org/software/ccd2cue/
Source: %name-0.5.tar.gz 

# Automatically added by buildreq on Thu Jul 18 2019
# optimized out: glibc-kernheaders-generic glibc-kernheaders-x86 gnu-config perl perl-Encode perl-Text-Unidecode perl-Unicode-EastAsianWidth perl-Unicode-Normalize perl-libintl perl-parent python-base sh4
BuildRequires: help2man makeinfo

%description
GNU ccd2cue is a CCD sheet to CUE sheet converter. It supports the full
extent of CUE sheet format expressiveness, including mixed-mode discs
and CD-Text meta-data.

%prep
%setup -q 

%build
%configure
%make
touch doc/release/latest-news.texi
%make info html

%install
%makeinstall
%find_lang --with-man %name

%files -f %name.lang
%doc README THANKS TODO
%doc doc/%name.html
%_bindir/*
%_infodir/*.*
%_man1dir/*.*

%changelog
* Thu Jul 18 2019 Fr. Br. George <george@altlinux.ru> 0.5-alt1
- Initial build for ALT

