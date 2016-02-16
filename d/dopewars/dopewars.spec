# BEGIN SourceDeps(oneline):
BuildRequires: /usr/bin/desktop-file-install glib2-devel libSDL-devel libesd-devel libgtk+2-devel libncurses-devel libsocket
# END SourceDeps(oneline)
# State dir for savegames
%global _localstatedir /var/lib/games
# SVN release
%global rel 1033

Summary:	A drug dealing game
Name:		dopewars
Version:	1.5.12
Release:	alt1_19.%{rel}svn
URL:		http://dopewars.sourceforge.net/
License:	GPLv2+
Group:		Games/Other
#Source0:	http://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
## The source tarball has been generated followingly:
# svn co https://svn.sourceforge.net/svnroot/dopewars/dopewars/trunk dopewars
# tar jcf dopewars-%{version}-%{rel}svn.tar.bz2
Source0:	%{name}-%{version}-%{rel}svn.tar.bz2

BuildRequires:	desktop-file-utils
BuildRequires:	gtk2-devel
BuildRequires:	ncurses-devel
BuildRequires:	libSDL_mixer-devel

# SVN stuff
BuildRequires:	automake
BuildRequires:	autoconf
BuildRequires:	libtool
BuildRequires:	gettext
Source44: import.info

%description
Based on John E. Dell's old Drug Wars game, dopewars is a simulation of an
imaginary drug market. dopewars is an All-American game which features
buying, selling, and trying to get past the cops!

The first thing you need to do is pay off your debt to the Loan Shark. After
that, your goal is to make as much money as possible (and stay alive)! You
have one month of game time to make your fortune.

dopewars supports multiple players via. TCP/IP. Chatting to and fighting
with other players (computer or human) is supported; check the command line
switches (via dopewars -h) for further information.

%package sdl
Summary:	SDL sound support for dopewars
Group:		Games/Other
Requires:	%{name} = %{version}
%description sdl
This package adds a plugin to dopewars to allow sound to be output via.
the Simple DirectMedia Layer mixer (SDL_mixer).

%prep
#%setup -q
%setup -q -n %{name}

# Clean out svn stuff
find . -name .svn | xargs rm -rf;
# Fix documentation
iconv -f ISO-8859-1 -t UTF-8 ChangeLog > ChangeLog.new && \
mv ChangeLog.new ChangeLog
chmod 644 doc/*.html

%build
NOCONFIGURE=1 autoreconf -vif
%configure \
	--enable-shared --disable-static \
	--enable-gui-server --enable-curses-client \
	--enable-gui-client --with-sdl --without-esd
make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot}
%find_lang %{name}

# Fix desktop file install
mv %{buildroot}/%{_datadir}/gnome/apps/Games/dopewars.desktop .
iconv -f ISO-8859-1 -t UTF-8 dopewars.desktop > dopewars.desktop.new && \
mv dopewars.desktop{.new,}
desktop-file-install --vendor="" \
--dir=${RPM_BUILD_ROOT}%{_datadir}/applications dopewars.desktop

# Remove documentation installed by make install
rm -rf %{buildroot}%{_docdir}


%post
%{_bindir}/dopewars -C %{_var}/dopewars.sco

%files -f %{name}.lang
%doc ChangeLog LICENCE NEWS README doc/*.html doc/example-cfg
# Score file needs to be writable by games group
%attr(0664,root,games) %{_var}/lib/games/dopewars.sco
# Bin file needs to be able to write into score file
%attr(2711,root,games) %{_bindir}/dopewars
%{_mandir}/man6/*
%{_libdir}/dopewars
%exclude %{_libdir}/dopewars/libsound_sdl.so
%{_datadir}/applications/*
%{_datadir}/pixmaps/*
%{_datadir}/dopewars

%files sdl
%{_libdir}/dopewars/libsound_sdl.so

%changelog
* Tue Feb 16 2016 Igor Vlasenko <viy@altlinux.ru> 1.5.12-alt1_19.1033svn
- update to new release by fcimport

* Sun Sep 20 2015 Igor Vlasenko <viy@altlinux.ru> 1.5.12-alt1_18.1033svn
- update to new release by fcimport

* Tue Jul 01 2014 Igor Vlasenko <viy@altlinux.ru> 1.5.12-alt1_15.1033svn
- update to new release by fcimport

* Mon Aug 12 2013 Igor Vlasenko <viy@altlinux.ru> 1.5.12-alt1_14.1033svn
- update to new release by fcimport

* Mon Jun 10 2013 Igor Vlasenko <viy@altlinux.ru> 1.5.12-alt1_13.1033svn
- update to new release by fcimport

* Fri Feb 22 2013 Igor Vlasenko <viy@altlinux.ru> 1.5.12-alt1_12.1033svn
- update to new release by fcimport

* Sun Jul 29 2012 Igor Vlasenko <viy@altlinux.ru> 1.5.12-alt1_11.1033svn
- new release

* Mon May 23 2011 Igor Vlasenko <viy@altlinux.ru> 1.5.12-alt1_10.1033svn
- converted from Fedora by srpmconvert script

