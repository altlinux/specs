# BEGIN SourceDeps(oneline):
BuildRequires: unzip
# END SourceDeps(oneline)
%define _enable_debug_packages %{nil}
%define debug_package          %{nil}

# NOTE: as of version 0.50-2, the wordlist isn't using accents;
# so we fix that with a small script in %setup section; that should
# be removed once an accented wordlist is included

%define src_ver 2.1.20000225a-2
%define fname aspell6-%{languagecode}
%define aspell_ver 0.60
%define languagelocal esperanto
%define languageeng esperanto
%define languageenglazy Esperanto
%define languagecode eo
%define lc_ctype eo_XX

Summary:       %{languageenglazy} files for aspell
Name:          aspell-%{languagecode}
Version:       2.1.20000225a.2
Release:       alt1_9
Group:         System/Internationalization
Source:        http://ftp.gnu.org/gnu/aspell/dict/%{languagecode}/%{fname}-%{src_ver}.tar.bz2
URL:	       http://aspell.sourceforge.net/
License:       GPL
Provides: spell-eo


BuildRequires: aspell
Requires:      aspell

# Mageia Stuff
# aspell = 1, myspell = 2, lang-specific = 3
Provides:      aspell-dictionary

Autoreqprov:   no
Source44: import.info

%description
A %{languageenglazy} dictionary for use with aspell, a spelling checker.

%prep
%setup -q -n %{fname}-%{src_ver}

%build
./configure
#%make

# the word list doesn't use accents; fixing that
cat << EOF > fixaccents.sh
#!/bin/bash
cat - | \
  sed 's/C[Xx]/ĉ/g' | sed 's/cx/ĉ/g' | \
  sed 's/G[Xx]/Ĝ/g' | sed 's/gx/ĝ/g' | \
  sed 's/H[Xx]/Ĥ/g' | sed 's/hx/ĥ/g' | \
  sed 's/J[Xx]/Ĵ/g' | sed 's/jx/ĵ/g' | \
  sed 's/S[Xx]/Ŝ/g' | sed 's/sx/ŝ/g' | \
  sed 's/U[Xx]/Ŭ/g' | sed 's/ux/ŭ/g' | \
  iconv -f utf-8 -t iso-8859-3
EOF
preunzip -c eo.cwl | sh ./fixaccents.sh | (LC_ALL=C sort) > eo.wl
aspell  --lang=eo create master ./eo.rws < eo.wl

%install
make DESTDIR=$RPM_BUILD_ROOT install

# fix doc perms
chmod 644 README

%files
%doc README
%{_libdir}/aspell/*
%{_datadir}/aspell/*


%changelog
* Sat Jun 04 2016 Igor Vlasenko <viy@altlinux.ru> 2.1.20000225a.2-alt1_9
- converted for ALT Linux by srpmconvert tools

