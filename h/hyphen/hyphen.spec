Name: hyphen
Summary: A text hyphenation library
Version: 2.7.1
Release: alt2
License: LGPLv2+ or MPLv1.1
Group: System/Libraries
URL: http://hunspell.sourceforge.net/
Packager: Valery Inozemtsev <shrek@altlinux.ru>

Source: http://downloads.sourceforge.net/hunspell/%name-%version.tar.gz

BuildRequires: gcc-c++

%description
Hyphen is a library for high quality hyphenation and justification

%package -n lib%name
Summary: A text hyphenation library
Group: System/Libraries

%description -n lib%name
Hyphen is a library for high quality hyphenation and justification

%package -n lib%name-devel
Summary: Files for developing with hyphen
Group: Development/C++
Requires: lib%name = %version-%release

%description -n lib%name-devel
Includes and definitions for developing with hyphen

%package en
Summary: English hyphenation rules
Group: Text tools
Requires: lib%name

%description en
English hyphenation rules

%prep
%setup -q

%build
%configure \
	--disable-static
%make_build

%install
%make DESTDIR=%buildroot install

cd %buildroot%_datadir/hyphen/
en_US_aliases="en en_AU en_BS en_BZ en_CA en_GH en_GB en_IE en_IN en_JM en_NA en_NZ en_PH en_TT en_ZA en_ZW"
for lang in $en_US_aliases; do
        ln -s hyph_en_US.dic hyph_$lang.dic
done

%files -n lib%name
%doc AUTHORS README README.* THANKS TODO
%_libdir/*.so.*
%dir %_datadir/hyphen

%files -n lib%name-devel
%_includedir/hyphen.h
%_bindir/substrings.pl
%_libdir/*.so

%files en
%doc README_hyph_en_US.txt
%_datadir/hyphen/hyph_en*.dic

%changelog
* Fri Apr 01 2011 Valery Inozemtsev <shrek@altlinux.ru> 2.7.1-alt2
- rebuild for debuginfo (closes: #25310)

* Sun Jan 30 2011 Valery Inozemtsev <shrek@altlinux.ru> 2.7.1-alt1
- 2.7.1

* Sat Oct 16 2010 Valery Inozemtsev <shrek@altlinux.ru> 2.6-alt1
- 2.6
- added some doc (closes: #17435)

* Mon May 03 2010 Valery Inozemtsev <shrek@altlinux.ru> 2.5-alt1
- 2.5

* Sat Nov 22 2008 Valery Inozemtsev <shrek@altlinux.ru> 2.4-alt2
- removed obsolete %%post_ldconfig/%%postun_ldconfig calls

* Thu Sep 04 2008 Valery Inozemtsev <shrek@altlinux.ru> 2.4-alt1
- 2.4

* Sun Dec 30 2007 Valery Inozemtsev <shrek@altlinux.ru> 2.3-alt2
- new varient alias

* Sat Dec 29 2007 Valery Inozemtsev <shrek@altlinux.ru> 2.3-alt1
- initial release
