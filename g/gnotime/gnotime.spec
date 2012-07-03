Name: gnotime
Version: 2.3.0
Release: alt7.20111130
Summary: Tracks and reports time spent

Group: Office
License: GPLv3+
Url: http://gttr.sourceforge.net/
Source0: %name-%version.tar
Source1: gnome-cromagnon.png
Patch2: %name-2.3.0-alt-freedesktop.patch

Packager: Sergey Kurakin <kurakin@altlinux.org>

BuildPreReq: rpm-build-xdg

BuildRequires: ImageMagick-tools gcc-c++ guile18-devel intltool libXScrnSaver-devel libdbus-glib-devel libglade-devel libgnomeui-devel libgtkhtml3-devel libqof-devel librarian libxml2-devel

%description
The Gnome Time Tracker is a to-do list/diary/journal tool that can track
the amount of time spent on projects, and, among other things, generate
reports and invoices based on that time. It's being used it to keep
shopping lists, organize ideas, track bug reports, keep a diary
of activities, do some blogging, provide weekly status reports
to management, and even as a consultant billing system.

%prep
%setup -q
%patch2 -p1

cat > %name.menu << EOF
<!DOCTYPE Menu PUBLIC "-//freedesktop//DTD Menu 1.0//EN"
	"http://www.freedesktop.org/standards/menu-spec/1.0/menu.dtd">
<Menu>
	<Menu>
	<Name>Development</Name>
	<Exclude>
		<Filename>%name.desktop</Filename>
	</Exclude>
	</Menu>
</Menu>
EOF

%build
%autoreconf
%configure
%make_build
convert -resize 16x16 %SOURCE1 %name-16.png
convert -resize 32x32 %SOURCE1 %name-32.png

%install
%make_install install DESTDIR=%buildroot
install -D -m 644 %name-16.png %buildroot%_miconsdir/%name.png
install -D -m 644 %name-32.png %buildroot%_niconsdir/%name.png
install -D -m 644 %SOURCE1 %buildroot%_liconsdir/%name.png
install -D -m 644 %name.menu %buildroot%_xdgmenusdir/applications-merged/%name.menu

# Gnotime puts it's locale translations into gnotime-2.0.mo but it's gnome
# help files into html/gnotime....
%find_lang %name --with-gnome
%find_lang %name-2.0 --with-gnome
cat %name-2.0.lang >> %name.lang

%post
%gconf2_install %name

%preun
if [ $1 = 0 ]; then
%gconf2_uninstall %name
fi

%files -f %name.lang
%doc AUTHORS ChangeLog INSTALL NEWS README TODO
%config %_sysconfdir/gconf/schemas/*
%_bindir/*
%_datadir/%name
%_datadir/applications/%name.desktop
%_man1dir/*
%_miconsdir/%name.png
%_niconsdir/%name.png
%_liconsdir/%name.png
%_xdgmenusdir/applications-merged/%name.menu

%changelog
* Thu May 31 2012 Sergey Kurakin <kurakin@altlinux.org> 2.3.0-alt7.20111130
- git snapshot 20111130: build fixed

* Mon Apr 25 2011 Sergey Kurakin <kurakin@altlinux.org> 2.3.0-alt6.20100926
- build fixed (buildreq)

* Sat Dec 11 2010 Sergey Kurakin <kurakin@altlinux.org> 2.3.0-alt5.20100926
- fixed repocop warning (freedesktop-desktop)

* Sun Nov 21 2010 Sergey Kurakin <kurakin@altlinux.org> 2.3.0-alt4.20100926
- git snapshot 20100926

* Tue Nov 24 2009 Sergey Kurakin <kurakin@altlinux.org> 2.3.0-alt3
- fixed build (BuildRequires, configure.in)

* Sun Jul 26 2009 Sergey Kurakin <kurakin@altlinux.org> 2.3.0-alt2
- fixed build with qof-8.0
- obsolete post scripts removed
- icon added
- desktop file corrected for conformance with freedesktop standard

* Fri Mar 28 2008 Sergey Kurakin <kurakin@altlinux.ru> 2.3.0-alt1
- 2.3.0

* Tue May 16 2006 Ildar Mulyukov <ildar@altlinux.ru> 2.2.2-alt1
- First release for ALTLinux

* Tue Feb 08 2005 Mike Traum <mtraum@yahoo.com> - 0:2.2.1-0.fdr.1
- Added guile-devel to BuildRequires
- Changed location of the .desktop file
- Added qof libs, qof header files, and gconf schema which weren't being
  packaged

* Sun Jul 11 2004 Toshio Kuratomi <toshio[AT]tiki-lounge.com> - 0:2.2.1-0.fdr.1
- Upgrade to 2.2.1.
- Remove extraneous BuildRequires.
- Remove doc patches as they've gone in upstream.
- Removed smp flags as this version isn't smp-able.

* Mon Feb 02 2004 Toshio Kuratomi <toshio[AT]tiki-lounge.com> - 0:2.1.7-0.fdr.4
- Fix preun script which was calling gconftool on straw rather than
  gnotime.
- Add desktop-file-utils Requires and use them to (re)install
  the .desktop file so we can add --vendor and --add-category X-Fedora
- Add StartupNotify to the desktop file

* Wed Dec 31 2003 Toshio Kuratomi <toshio[AT]tiki-lounge.com> - 0:2.1.7-0.fdr.3
- Change the build process back to patching as there is no consensus
  and I agree with the patching argument rather than autogen-in-spec
  argument.
- Make sure the gconf schema gets installed into the sysconfigdir
- Use gconftool-2 in the post/postun scripts to install the schema
  into gconf.
- Make scrollkeeper non-optional.  Since most other fedora packages using
  scrollkeeper require it and not having scrollkeeper tends to make help
  unusable.

* Sun Dec 28 2003 Toshio Kuratomi <toshio[AT]tiki-lounge.com> - 0:2.1.7-0.fdr.2
- Fix up the BuildRequires -- if one package will pull in another
  automatically, then do not explicitly list it.
- Change the build process.  Instead of generating a post-autogen patch
  and patching the distributed source, run autogen.sh to regenerate the
  build infrastructure.  (This is necessary in the first place because
  the doc build structure needed to be modified.)

* Mon Dec 15 2003 Toshio Kuratomi <toshio[AT]tiki-lounge.com> - 0:2.1.7-0.fdr.1
- Initial Fedora RPM release.
- Partially adapted from the gnotime.spec.in by Eric Anderson
  <eric.anderson[AT]cordata.net> from the Red Hat directory in the
  gnotime distribution.
