Summary:	Cgoban is an X board for playing Go (Weiqi)
Name:		cgoban
Version:	1.9.14
Release:	alt2.qa1
Group:		Games/Boards
License:	GPL
URL:		http://cgoban1.sourceforge.net/
Packager:   Paul Wolneykien <manowar@altlinux.ru>

Source:		http://prdownloads.sourceforge.net/cgoban1/%{name}-%{version}.tar.gz

# Automatically added by buildreq on Tue Mar 29 2011 (-ba)
BuildRequires: libXt-devel

%description
   Cgoban (Complete Goban) is for Unix systems with X11. It has the ability
to be a computerized Go board, view and edit smart-go files, and connect to
Go servers on the Internet.

%prep
%setup -q

%configure

%build
%make

%install
%makeinstall
# mkdir $RPM_BUILD_ROOT/usr/share
install -D -m 0644 cgoban_icon.png %buildroot%{_datadir}/pixmaps/%{name}.png
mkdir -p -m 0755 %buildroot%{_datadir}/applications
cat >%buildroot%{_datadir}/applications/%{name}.desktop <<EOF
[Desktop Entry]
Name=CGoban
Categories=Game;BoardGame;
Comment=CGoban board with Gnugo interface
Exec=%{_bindir}/%{name}
Icon=%{name}
Version=1.0
Type=Application
EOF

%files
%defattr(-,root,root,755)
%doc COPYING README TODO
%{_bindir}/*
%{_mandir}/man6/*
%{_datadir}/pixmaps/cgoban.png
%{_datadir}/applications/%{name}.desktop

%changelog
* Sun Apr 10 2011 Igor Vlasenko <viy@altlinux.ru> 1.9.14-alt2.qa1
- NMU: dropped obsolete menu entry

* Tue Mar 29 2011 Paul Wolneykien <manowar@altlinux.ru> 1.9.14-alt2
- Update of the build requires.

* Thu Aug 13 2009 Paul Wolneykien <manowar@altlinux.ru> 1.9.14-alt1
- Initial release for ALTLinux.

* Thu Oct 25 2002 Kevin Sonney <ksonney@redhat.com> 1.9.14-0.2
- latest dev build
- tested rpm spec on RHL 7.x

* Thu Oct 25 2002 Kevin Sonney <ksonney@redhat.com> 1.9.14-0.1
- version jump
- remove patches
- modify .spec to be included in mainline cgoban1 distribution

* Mon Oct 22 2002 Kevin Sonney <ksonney@redhat.com> 1.9.12-0.4
- change desktop/menu entry description

* Mon Oct 21 2002 Kevin Sonney <ksonney@redhat.com> 1.9.12-0.3
- rename binary to cgoban1
- added desktop entry for gnome

* Thu Aug 22 2002 Kevin Sonney <ksonney@redhat.com> 1.9.12-0.2
- Better patch to Makefile.in
- still needs porting to the new autoconf
- can now use %configure macro
- clean out fluxbox comments form my template .spec file
- bad hacks for man pages & doc lcoations

* Thu Aug 22 2002 Kevin Sonney <ksonney@redhat.com> 1.9.12-0.1
- Initial Spec File
- lots of fixes to the spec to get it to build right as an RPM
- patched the Makefile.in to correct autoconf error
- needs porting to the new autoconf

# end of file
