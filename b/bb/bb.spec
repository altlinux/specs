Name: bb
Version: 1.3
Release: alt0.5

Summary: BB - the portable AAlib demo
License: GPL
Group: Toys

%define realver %{version}rc1

Url: http://aa-project.sourceforge.net/bb
Source: http://unc.dl.sourceforge.net/sourceforge/aa-project/%name-%realver.tar.gz
Patch: bb-1.3.0-alt-gcc34.patch
Packager: Michael Shigorin <mike@altlinux.org>

Summary(ru_RU.KOI8-R): BB - ÄÅÍÏ AAlib
Summary(uk_UA.KOI8-U): BB - ÄÅÍÏ AAlib
Summary(pl): BB - przeno¶ne demo

# see .desktop
Requires: sound_handler

# Automatically added by buildreq on Thu May 15 2008
BuildRequires: aalib-devel libX11-devel libgpm-devel libmikmod-devel libslang-devel
BuildRequires: chrpath

%description
BB is an high quality audio-visual demonstration for your text
terminal. It is portable demo, so you can run it on plenty of
operating systems.

%description -l ru_RU.KOI8-R
BB - ×ÙÓÏËÏËÁÞÅÓÔ×ÅÎÎÁÑ ÁÕÄÉÏ×ÉÚÕÁÌØÎÁÑ ÄÅÍÏÎÓÔÒÁÃÉÑ ×ÏÚÍÏÖÎÏÓÔÅÊ
aalib ÄÌÑ ÔÅËÓÔÏ×ÙÈ ÔÅÒÍÉÎÁÌÏ×.

%description -l uk_UA.KOI8-U
BB - ×ÉÓÏËÏÑË¦ÓÎÁ ÁÕÄ¦Ï×¦ÚÕÁÌØÎÁ ÄÅÍÏÎÓÔÒÁÃ¦Ñ ÍÏÖÌÉ×ÏÓÔÅÊ
aalib ÄÌÑ ÔÅËÓÔÏ×ÉÈ ÔÅÒÍ¦ÎÁÌ¦×.

%description -l pl
BB jest wysokiej jako¶ci demem z grafik± i d¼wiêkiem, dzia³aj±cym na
terminalu tekstowym. Jest przeno¶ne - dzia³a na wielu systemach
operacyjnych.

%prep
%setup -n %name-1.3.0
%patch -p1

%build
%autoreconf
%configure
%make_build
# and just in case
chrpath -d %name

%install
%makeinstall

mkdir -p %buildroot%_desktopdir
cat > %buildroot%_desktopdir/%name.desktop <<EOF
[Desktop Entry]
Version=1.0
Type=Application
Name=BB
Comment=BB -- AA demo
Icon=%{name}
Exec=sound_wrapper %_bindir/%name -dim -bold -boldfont
Terminal=false
Categories=Game;Amusement;
EOF

%files
%doc AUTHORS ChangeLog NEWS README
%_datadir/%name/
%_bindir/*
%_desktopdir/%name.desktop
%_man1dir/*

%changelog
* Thu Dec 15 2011 Michael Shigorin <mike@altlinux.org> 1.3-alt0.5
- dropped RPATH on the floor
- minor spec cleanup

* Sat Apr 16 2011 Igor Vlasenko <viy@altlinux.ru> 1.3-alt0.4.qa1
- NMU: converted menu to desktop file

* Wed Dec 03 2008 Michael Shigorin <mike@altlinux.org> 1.3-alt0.4
- applied repocop patch

* Thu May 15 2008 Michael Shigorin <mike@altlinux.org> 1.3-alt0.3
- buildreq
- spec macro abuse cleanup

* Thu Feb 24 2005 Michael Shigorin <mike@altlinux.ru> 1.3-alt0.2
- rebuilt with gcc3.4 (thanks Stanislav Ievlev for fix suggestion)

* Mon Apr 12 2004 Michael Shigorin <mike@altlinux.ru> 1.3-alt0.1
- built for ALT Linux (1.3rc1)
- heh, it was Mon Apr 28 2003 when this package was basically done :-D
  still minor spec fixes/cleanups...
- spec adapted from PLD <feedback@pld.org.pl>
  All persons listed below can be reached at <cvs_login>@pld.org.pl
  arturs, filon, kloczek, qboosh
