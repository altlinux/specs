# BEGIN SourceDeps(oneline):
BuildRequires: libICE-devel libSM-devel libX11-devel libXext-devel libXt-devel
# END SourceDeps(oneline)
Summary(ru_RU.KOI8-R): Tgif - пакет 2-мерной графики
Name:		tgif
Version:	4.2.5
Release:	alt2_2
Summary:	2-D drawing tool
Group:		Graphics

License:	QPL
URL:		http://bourbon.usc.edu/tgif/
Source0:	http://downloads.sourceforge.net/%{name}/%{name}-QPL-%{version}.tar.gz
# http://tyche.pu-toyama.ac.jp/~a-urasim/tgif/
Patch10:	tgif-textcursor-a-urasim.patch
# Check below later
Patch101:	tgif-QPL-4.1.45-size-debug.patch

BuildRequires:	xorg-cf-files gccmakedep imake
BuildRequires:	desktop-file-utils
BuildRequires:	gettext
BuildRequires:	libXmu-devel
BuildRequires:	libidn-devel
BuildRequires:	zlib-devel
Requires:	ghostscript-utils ghostscript
Requires:	netpbm
Requires:	fonts-bitmap-75dpi
Requires:	fonts-bitmap-75dpi
Source44: import.info

%description
Tgif  -  Xlib based interactive 2-D drawing facility under
X11.  Supports hierarchical construction of  drawings  and
easy  navigation  between  sets  of drawings.  It's also a
hyper-graphics (or hyper-structured-graphics)  browser  on
the World-Wide-Web.


%description -l ru_RU.KOI8-R
Tgif является пакетом для двумерной графики. Он поддерживает создание иерархических
изображений и легкую навигацию между наборами изображений. Он также является
броузером гиперграфики для WWW.

%prep
%setup -q -n %{name}-QPL-%{version}
# Upstream says the below is wrong, for now dropping
#%%patch10 -p0 -b textcursor
# Check later
#%%patch101 -p1 -b .size

%{__perl} -pi \
	-e 's,JISX-0208-1983-0,EUC-JP,g' \
	po/ja/ja.po

# use scalable bitmap font
%{__sed} \
	-e s,alias\-mincho,misc\-mincho,g \
	-e s,alias\-gothic,jis\-fixed,g \
	-i po/ja/Tgif.ad

# Fix desktop file
%{__sed} -i.icon -e 's|Icon=tgif|Icon=tgificon|' \
	po/ja/tgif.desktop

# Fix installation path for icon files
%{__sed} -i.path \
	-e '/InstallNonExec.*hicolor/s|\$(TGIFDIR)|\$(DATADIR)/icons/|' \
	-e '/MakeDirectories.*hicolor/s|\$(TGIFDIR)|\$(DATADIR)/icons/|' \
	Imakefile

%build
%{__cp} -pf Tgif.tmpl-linux Tgif.tmpl
%{__sed} -i.mode -e 's|0664|0644|' Tgif.tmpl

xmkmf
%{__sed} -i.mode -e 's|0444|0644|' Makefile
DEFOPTS='-DOVERTHESPOT -DUSE_XT_INITIALIZE -D_ENABLE_NLS -DPRINT_CMD=\"lpr\" -DA4PAPER'
%{__make} %{?_smp_mflags} \
	CC="%{__cc} %{optflags}" \
	MOREDEFINES="$DEFOPTS" \
	TGIFDIR=%{_datadir}/tgif/ \
	LOCAL_LIBRARIES="-lXmu -lXt -lX11" \
	tgif

pushd po
xmkmf 
%{__sed} -i.mode -e 's|0444|0644|' Makefile
%{__make} \
	Makefile \
	Makefiles \
	depend \
	all
popd

%install
%{__rm} -rf $RPM_BUILD_ROOT/

%{__make} \
	DESTDIR=$RPM_BUILD_ROOT/ \
	BINDIR=/usr/libexec/ \
	TGIFDIR=%{_datadir}/tgif/ \
	INSTALLFLAGS="-cp" \
	DATADIR=%{_datadir} \
	install \
	install.man

# wrap tgif
%{__mkdir_p} $RPM_BUILD_ROOT%{_bindir}/
%{__install} -cpm 0755 po/ja/tgif-wrapper.sh \
	$RPM_BUILD_ROOT%{_bindir}/%{name}

%{__rm} -f $RPM_BUILD_ROOT%{_datadir}/tgif/*.obj
%{__install} -cpm 0644 *.obj \
	$RPM_BUILD_ROOT%{_datadir}/tgif/


# Japanese specific
%{__mkdir_p} $RPM_BUILD_ROOT%{_datadir}/X11/ja/app-defaults/
%{__install} -cpm 0644 \
	po/ja/Tgif.ad \
	$RPM_BUILD_ROOT%{_datadir}/X11/ja/app-defaults/Tgif

pushd po
%{__make} \
	DESTDIR=$RPM_BUILD_ROOT/ \
	INSTALLFLAGS="-cp" \
	install
popd

# desktop file & icon
%{__mkdir_p} $RPM_BUILD_ROOT%{_datadir}/applications/
desktop-file-install \
	--remove-category 'Application' \
	--remove-category 'X-Fedora' \
	--vendor 'fedora' \
	--dir $RPM_BUILD_ROOT%{_datadir}/applications/ \
	po/ja/tgif.desktop


%{find_lang} tgif

%files -f %{name}.lang
%doc AUTHORS
%doc ChangeLog
%doc Copyright
%doc HISTORY
%doc LICENSE.QPL
%doc README*
%doc VMS_MAKE_TGIF.COM 
%doc example.tex 
%doc po/ja/README.jp

%{_bindir}/%{name}
/usr/libexec/%{name}
%{_mandir}/man1/%{name}.1*

%{_datadir}/%{name}/
# Currently no package owns the following directories
%dir %{_datadir}/X11/ja/
%dir %{_datadir}/X11/ja/app-defaults/
%{_datadir}/X11/ja/app-defaults/Tgif

%{_datadir}/icons/hicolor/*/apps/%{name}icon.png
%{_datadir}/applications/*-%{name}.desktop

%changelog
* Wed Mar 21 2012 Igor Vlasenko <viy@altlinux.ru> 4.2.5-alt2_2
- rebuild to get rid of #27020

* Tue Jan 10 2012 Igor Vlasenko <viy@altlinux.ru> 4.2.5-alt1_2
- update to new release by fcimport

* Sat Sep 17 2011 Igor Vlasenko <viy@altlinux.ru> 4.2.5-alt1_1
- new release by fedoraimport

* Fri Apr 04 2008 Igor Vlasenko <viy@altlinux.ru> 4.1.45-alt1
- new version

* Tue Dec 20 2005 Igor Vlasenko <viy@altlinux.ru> 4.1.44-alt1
- new version;
- new url;
- picked up maintainership.

* Mon Sep 15 2003 Ott Alex <ott@altlinux.ru> 4.1.43-alt2
- Fixing spec

* Tue Sep 02 2003 Ott Alex <ott@altlinux.ru> 4.1.43-alt1
- New main release

* Sun Sep 01 2002 Ott Alex <ott@altlinux.ru> 4.1.42-alt1
- Initial build

