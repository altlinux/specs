Name: steghide
Version: 0.5.1
Release: alt5

Summary: A steganography program

License: GPLv2
Group: File tools

Url: http://steghide.sourceforge.net
Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: http://prdownloads.sourceforge.net/steghide/steghide-%version.tar
Patch: steghide-0.5.1-gcc41.patch
Patch2: steghide-0.5.1-mhash.patch
Patch3: steghide-0.5.1-gcc43.patch

# BEGIN SourceDeps(oneline):
BuildRequires: %_bindir/doxygen %_bindir/perl gcc-c++ perl(FileHandle.pm)
# END SourceDeps(oneline)

BuildRequires: automake autoconf
BuildRequires: gettext-devel libtool automake autoconf
BuildRequires: libmcrypt-devel libmhash-devel libjpeg-devel zlib-devel

Requires: libmcrypt >= 2.5.8-2
Source44: import.info

%description
Steghide is a steganography program that is able to hide data in various kinds
of image- and audio-files. The color- respectivly sample-frequencies are not
changed thus making the embedding resistant against first-order statistical
tests. Features of steghide include compression and encryption of embedded
data,

embedding of a checksum to verify the integrity of the extracted data and
support for jpeg, bmp, wav and au files.

%prep
%setup
%patch0 -p1
%patch2 -p1
%patch3 -p1 -b .gcc43

%build
%autoreconf
%configure
%make_build CXXFLAGS="$RPM_OPT_FLAGS"

%install
%makeinstall_std
rm -rf %buildroot%_docdir/%name/*

%find_lang %name

%check
# make check

%files -f %name.lang
%_bindir/steghide
%_man1dir/steghide.1*

%doc ABOUT-NLS BUGS CREDITS HISTORY README TODO

%changelog
* Wed Oct 23 2013 Vitaly Lipatov <lav@altlinux.ru> 0.5.1-alt5
- build to ALT Linux Sisyphus

* Mon Sep 09 2013 Igor Vlasenko <viy@altlinux.ru> 0.5.1-alt4_22
- update to new release by fcimport

* Mon Apr 29 2013 Igor Vlasenko <viy@altlinux.ru> 0.5.1-alt4_21
- initial fc import

* Thu Nov 27 2008 Victor Forsyuk <force@altlinux.org> 0.5.1-alt4
- Fix FTBFS with gcc43.

* Sat Dec 29 2007 Victor Forsyuk <force@altlinux.org> 0.5.1-alt3
- Fix FTBFS in current build environment.

* Tue May 16 2006 Victor Forsyuk <force@altlinux.ru> 0.5.1-alt2
- Fix FTBFS with gcc4.

* Mon Jul 18 2005 Victor Forsyuk <force@altlinux.ru> 0.5.1-alt1
- Initial build.
