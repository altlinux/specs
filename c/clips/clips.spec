Summary:	Clips language for expert systems
Name:		clips
Version:	6.23
Release:	alt1.2
License:	BSD style
Group:		Development/Other
Url:		http://www.ghg.net/clips/download/source/
Source0:	http://www.ghg.net/clips/download/source/clipssrc.tar.bz2
Source1:	http://www.ghg.net/clips/download/source/x-prjct.tar.bz2
Source2:	http://www.ghg.net/clips/download/source/makefile.bz2
Source3:	http://www.ghg.net/clips/download/source/clips.hlp
Source4:	http://www.ghg.net/clips/download/documentation/abstract.pdf
Source5:	http://www.ghg.net/clips/download/documentation/apg.pdf
Source6:	http://www.ghg.net/clips/download/documentation/arch5-1.pdf
Source7:	http://www.ghg.net/clips/download/documentation/bpg.pdf
Source8:	http://www.ghg.net/clips/download/documentation/ig.pdf
Source9:	http://www.ghg.net/clips/download/documentation/usrguide.pdf
#Patch0:	clips-setup.patch.bz2
#Patch1:	clips-6.21-lib64.patch.bz2
Patch2:        clips-6.21-gcc4.patch.bz2

BuildRequires: libX11-devel libXaw-devel libXext-devel libXmu-devel libXt-devel libtinfo-devel linux-libc-headers xorg-x11-bitmaps

%package	X11
Summary:	X interface to Clips
Group:		Development/Other
Requires:	clips

%description
This is the Clips expert systems language.

%description -l ru_RU.KOI8-R
óÒÅÄÁ ÄÌÑ ÒÁÚÒÁÂÏÔËÉ ÜËÓÐÅÒÔÎÙÈ ÓÉÓÔÅÍ

%description -l ru_RU.UTF-8
Ð¡Ñ€ÐµÐ´Ð° Ð´Ð»Ñ Ñ€Ð°Ð·Ñ€Ð°Ð±Ð¾Ñ‚ÐºÐ¸ ÑÐºÑÐ¿ÐµÑ€Ñ‚Ð½Ñ‹Ñ… ÑÐ¸ÑÑ‚ÐµÐ¼

%description	X11
X interface to Clips.

%description	X11 -l ru_RU.KOI8-R
çÒÁÆÉÞÅÓËÉÊ ÉÎÔÅÒÆÅÊÓ ÄÌÑ Clips.

%prep
%setup -q -a 1 -c
mv x-prjct/makefile/makefile.x clipssrc/clipssrc
mv x-prjct/xinterface/* clipssrc/clipssrc
#%patch0 -p0 -b .setup
#%patch1 -p1 -b .lib64
%patch2 -p1 -b .gcc4
#%patch3 -p0 -b .Xaw3d
bzcat %SOURCE2 > clipssrc/clipssrc/makefile

%build
cd clipssrc/clipssrc
%make
%make -f makefile.x LIB=%{_lib}

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p -m 0755 $RPM_BUILD_ROOT%{_prefix}/{bin,doc,share/clips}
install -m 0755 -s clipssrc/clipssrc/clips $RPM_BUILD_ROOT%{_bindir}/
install -m 0755 -s clipssrc/clipssrc/xclips $RPM_BUILD_ROOT%{_bindir}/
install -m 0644 %SOURCE3 $RPM_BUILD_ROOT%{_datadir}/clips/
cp %SOURCE3 .
mkdir -p $RPM_BUILD_ROOT%{_docdir}/clips-%PACKAGE_VERSION
for i in %SOURCE4 %SOURCE5 %SOURCE6 %SOURCE7 %SOURCE8 %SOURCE9; do
install -m 0644 $i $RPM_BUILD_ROOT%{_docdir}/clips-%PACKAGE_VERSION
done

%files
%{_bindir}/clips
%{_docdir}/clips-%PACKAGE_VERSION
%{_datadir}/clips

%files X11
%{_bindir}/xclips
%doc clips.hlp
 
%changelog 
* Wed Mar 16 2011 Igor Vlasenko <viy@altlinux.ru> 6.23-alt1.2
- NMU: spec cleanup; removed robot-unfriendly recurrent release

* Wed Dec 08 2010 Igor Vlasenko <viy@altlinux.ru> 6.23-alt1.1
- rebuild with new openssl and/or boost by request of git.alt administrator

* Tue May 30 2006 Dmitri Kuzishchin <dim@altlinux.ru> 6.23-alt1
- Version 6.23

* Wed May 10 2006 Dmitri Kuzishchin <dim@altlinux.ru> 6.21-alt1
- fisrt ALT package
