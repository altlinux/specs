# vim: set ft=spec: -*- rpm-spec -*-

Name: ruby-gnome2-all
Version: 0.90.5
Release: alt3

Summary: Ruby bindings for GNOME-2.x
Group: Development/Ruby
License: LGPL
Url: http://ruby-gnome2.sourceforge.jp/

Packager: Ruby Maintainers Team <ruby@packages.altlinux.org>

Obsoletes: ruby-gnome2-full
Requires: libruby >= 1.8-alt3

%global reqpkg() %{expand:Requires: ruby-%%{1} = %%version-%%release}

%reqpkg glib2
%reqpkg gdkpixbuf2
%reqpkg pango
%reqpkg atk
%reqpkg gtk2
%reqpkg bonobo2
%reqpkg bonoboui2
%reqpkg gconf2
%reqpkg goocanvas
%reqpkg gnome2
%reqpkg gnomecanvas2
%reqpkg gnomeprint2
%reqpkg gnomeprintui2
%reqpkg gnomevfs
%reqpkg gst
%reqpkg gtkglext
%reqpkg gtkhtml2
#%%reqpkg gtkmozembed
%reqpkg gtksourceview
%reqpkg gtksourceview2
%reqpkg libart2
%reqpkg libglade2
#%reqpkg panelapplet2
%reqpkg rsvg2
%reqpkg vte

Source: %name-%version.tar
Patch: %name-%version-%release.patch

# Automatically added by buildreq on Sun Jan 11 2009 (-bi)
BuildRequires: gst-plugins-devel libglade-devel libgnomeprintui-devel libgnomeui-devel libgoocanvas-devel libgtkglext-devel libgtkhtml2-devel libgtksourceview-devel libgtksourceview1-devel libjpeg-devel librsvg-devel libvte-devel ruby-rcairo-devel ruby-pkg-config libcairo-gobject-devel libpixman-devel xorg-dri2proto-devel xorg-glproto-devel libXau-devel libXdmcp-devel libXext-devel libXdamage-devel libpng-devel libudev-devel libXxf86vm-devel
#libgnome-panel-devel 

%description
This project is a set of Ruby language bindings for the various
application development libraries included with the GNOME/GTK+
environment. This project is for GTK+2.0 or later.

This is a virtual package which requires all ruby-gnome2 modules.

%package -n ruby-gnome2-samples
Summary: Sample scripts for ruby-gnome2 project
Group: Development/Ruby
BuildArch: noarch
Requires: ruby ruby-stdlibs

%description -n ruby-gnome2-samples
This package contains sample scripts for ruby-gnome2 project.

You should install appropriate modules in order to run this scripts.

%package -n ruby-glib2
Summary: Ruby bindings for Glib-2.x
Group: Development/Ruby
#Requires: ruby-gettext

%description -n ruby-glib2
Ruby/GLib2 is a Ruby binding of GLib-2.x.

It is recommended to install ruby-gettext.

%package -n ruby-glib2-devel
Summary: Development files for Ruby/GLib2
Group: Development/Ruby
BuildArch: noarch
PreReq: libruby-devel
Requires: libruby-devel
%reqpkg glib2

%description -n ruby-glib2-devel
Development files for Ruby/GLib2.

%package -n ruby-gio2
Summary: Ruby binding for gio-2.0.x
Group: Development/Ruby
%reqpkg glib2

%description -n ruby-gio2
Ruby/GIO is a Ruby binding of gio-2.0.x.

%package -n ruby-gdkpixbuf2
Summary: Ruby bindings for GdkPixbuf-2.x
Group: Development/Ruby

%description -n ruby-gdkpixbuf2
Ruby/GdkPixbuf2 is a Ruby binding of GdkPixbuf-2.x.

%package -n ruby-pango
Summary: Ruby bindings for pango-1.x
Group: Development/Ruby

%description -n ruby-pango
Ruby/Pango is a Ruby binding of pango-1.x.

%package -n ruby-pango-devel
Summary: Development files for Ruby/Pango
Group: Development/Ruby
BuildArch: noarch
PreReq: libruby-devel
Requires: ruby-rcairo-devel
%reqpkg pango
%reqpkg glib2-devel

%description -n ruby-pango-devel
Development files for Ruby/Pango.

%package -n ruby-atk
Summary: Ruby bindings for ATK-1.0.x
Group: Development/Ruby

%description -n ruby-atk
Ruby/ATK is a Ruby binding of ATK-1.0.x or later.

%package -n ruby-atk-devel
Summary: Development files for Ruby/ATK
Group: Development/Ruby
BuildArch: noarch
PreReq: libruby-devel
%reqpkg atk
%reqpkg glib2-devel

%description -n ruby-atk-devel
Development files for Ruby/ATK.

%package -n ruby-gtk2
Summary: Ruby bindings for GTK+-2.0.x
Group: Development/Ruby

%description -n ruby-gtk2
Ruby/GTK2 is a Ruby binding of GTK+-2.0.x.

%package -n ruby-bonobo2
Summary: Ruby bindings for libbonobo-2.x
Group: Development/Ruby

%description -n ruby-bonobo2
Ruby/Bonobo2 is a Ruby binding of libbonobo-2.x.

%package -n ruby-bonoboui2
Summary: Ruby bindings for libbonoboui-2.x
Group: Development/Ruby

%description -n ruby-bonoboui2
Ruby/BonoboUI2 is a Ruby binding of libbonoboui-2.x.

%package -n ruby-gconf2
Summary: Ruby bindings for GConf-1.2.x
Group: Development/Ruby

%description -n ruby-gconf2
Ruby/GConf2 is a Ruby binding of GConf-1.2.x.

%package -n ruby-gnome2
Summary: Ruby bindings for libgnome/libgnomeui-2.x
Group: Development/Ruby

%description -n ruby-gnome2
Ruby/GNOME2 is a Ruby binding of libgnome/libgnomeui-2.x.

%package -n ruby-gnomecanvas2
Summary: Ruby bindings for GnomeCanvas-2.x
Group: Development/Ruby

%description -n ruby-gnomecanvas2
Ruby/GnomeCanvas2 is a Ruby binding of GnomeCanvas-2.x.

%package -n ruby-gnomeprint2
Summary: Ruby bindings for libgnomeprint
Group: Development/Ruby
Obsoletes: ruby-gnomeprint

%description -n ruby-gnomeprint2
Ruby/GnomePrint is a Ruby binding of libgnomeprint.

%package -n ruby-gnomeprint2-devel
Summary: Development files for Ruby/GnomePrint
Group: Development/Ruby
BuildArch: noarch
PreReq: libruby-devel
%reqpkg gnomeprint2

%description -n ruby-gnomeprint2-devel
Development files for Ruby/GnomePrint.

%package -n ruby-gnomeprintui2
Summary: Ruby bindings for libgnomeprintui
Group: Development/Ruby
Obsoletes: ruby-gnomeprintui

%description -n ruby-gnomeprintui2
Ruby/GnomePrintUI is a Ruby binding of libgnomeprintui.

%package -n ruby-gnomevfs
Summary: Ruby bindings for GnomeVFS-2.0.x
Group: Development/Ruby
Obsoletes: ruby-gnomevfs2

%description -n ruby-gnomevfs
Ruby/GnomeVFS is a Ruby binding of GnomeVFS-2.0.x.

%package -n ruby-goocanvas
Summary: Ruby bindings for GooCanvas
Group: Development/Ruby

%description -n ruby-goocanvas
Ruby/GStreamer is a Ruby binding for GooCanvas.

%package -n ruby-gst
Summary: Ruby bindings for GStreamer
Group: Development/Ruby

%description -n ruby-gst
Ruby/GStreamer is a Ruby binding for GStreamer.

%package -n ruby-gtkglext
Summary: Ruby bindings for GtkGLExt
Group: Development/Ruby

%description -n ruby-gtkglext
Ruby/GtkGLExt is a Ruby binding of GtkGLExt.

%package -n ruby-gtkhtml2
Summary: Ruby bindings for GtkHtml2
Group: Development/Ruby

%description -n ruby-gtkhtml2
Ruby/GtkHtml2 is a Ruby binding of GtkHtml2.

%package -n ruby-gtkmozembed
Summary: Ruby bindings for GtkMozEmbed
Group: Development/Ruby

%description -n ruby-gtkmozembed
Ruby/GtkMozEmbed is a Ruby binding of GtkMozEmbed a widget embedding a
Mozilla Gecko renderer.

%package -n ruby-gtksourceview
Summary: Ruby bindings for gtksourceview-1.0.x
Group: Development/Ruby

%description -n ruby-gtksourceview
Ruby/GtkSourceView is a Ruby binding of gtksourceview-1.0.x.

%package -n ruby-gtksourceview2
Summary: Ruby bindings for gtksourceview-2.x
Group: Development/Ruby

%description -n ruby-gtksourceview2
Ruby/GtkSourceView is a Ruby binding of gtksourceview-2.x.

%package -n ruby-libart2
Summary: Ruby bindings for Libart_lgpl
Group: Development/Ruby
Obsoletes: ruby-libart

%description -n ruby-libart2
Ruby/Libart2 is a Ruby binding of Libart_lgpl.

%package -n ruby-libart2-devel
Summary: Development files for Ruby/Libart2
Group: Development/Ruby
BuildArch: noarch
PreReq: libruby-devel
%reqpkg libart2

%description -n ruby-libart2-devel
Development files for Ruby/Libart2.

%package -n ruby-libglade2
Summary: Ruby bindings for Libglade2
Group: Development/Ruby

%description -n ruby-libglade2
Ruby/Libglade2 is a Ruby bindings of Libglade2.
This provides a very simple interface to the libglade library,
to load interfaces dynamically from a glade file.

%package -n ruby-libglade2-devel
Summary: Development files for Ruby/Libglade2
Group: Development/Ruby
BuildArch: noarch
%reqpkg libglade2

%description -n ruby-libglade2-devel
Development files for Ruby/Libglade2.

This packagee contains ruby-glade-create-template utility.

#%package -n ruby-panelapplet2
#Summary: Ruby bindings for libpanel-applet-2.6.x
#Group: Development/Ruby
#Obsoletes: ruby-gnomepanel-applet

#%description -n ruby-panelapplet2
#Ruby/PanelApplet2 is a Ruby binding of libpanel-applet-2.6.x.

%package -n ruby-rsvg2
Summary: Ruby bindings for librsvg
Group: Development/Ruby
Obsoletes: ruby-rsvg

%description -n ruby-rsvg2
Ruby/RSVG is a Ruby binding of librsvg.

%package -n ruby-vte
Summary: Ruby bindings for VTE
Group: Development/Ruby

%description -n ruby-vte
Ruby/VTE is a Ruby binding of VTE.

%prep
%setup -q
%patch -p1

# Unsupported.  Last commit 2005-12-05 19:41:20
rm -rf libgda
# Permanently b0rken
rm -rf poppler
# Not ported to new xulrunner
rm -rf gtkmozembed

%build
export RUBYOPT=-rvendor-specific
%ruby_configure --strict
%make_build rubyhdrdir=%ruby_includedir

%install
%make_install DESTDIR=%buildroot rubyhdrdir=%buildroot%ruby_includedir install
# We don't need win32 hacks
rm -f %buildroot%ruby_sitelibdir/libart2.rb

mkdir samples
cp -rp gconf/sample samples/gconf2
cp -rp gdk_pixbuf2/sample samples/gdkpixbuf2
cp -rp glib2/sample samples/glib2
cp -rp gnomecanvas/sample samples/gnomecanvas2
cp -rp gnomeprint/sample samples/gnomeprint2
cp -rp gnomeprintui/sample samples/gnomeprintui2
cp -rp gnome/sample samples/gnome2
cp -rp goocanvas/sample samples/goocanvas
cp -rp gstreamer/sample samples/gst
cp -rp gtk2/sample samples/gtk2
cp -rp gtkglext/sample samples/gtkglext
cp -rp gtkhtml2/sample samples/gtkhtml2
#cp -rp gtkmozembed/sample samples/gtkmozembed
cp -rp gtksourceview/sample samples/gtksourceview
cp -rp gtksourceview2/sample samples/gtksourceview2
cp -rp libart/sample samples/libart2
cp -rp libglade/sample samples/libglade2
#cp -rp panel-applet/sample samples/panelapplet2
cp -rp pango/sample samples/pango
#cp -rp poppler/sample samples/poppler
cp -rp rsvg2/sample samples/rsvg2
cp -rp vte/sample samples/vte

%files

%files -n ruby-gnome2-samples
%doc AUTHORS ChangeLog NEWS README
%doc samples/*

%files -n ruby-glib2
%doc glib2/README
%ruby_sitearchdir/glib2.so
%ruby_sitelibdir/glib2.rb

%files -n ruby-glib2-devel
#_includedir/ruby/*/rbgcompat.h
#_includedir/ruby/*/rbglib.h
#_includedir/ruby/*/rbgutil.h
#_includedir/ruby/*/rbgobject.h
#_includedir/ruby/*/glib-enum-types.h
%ruby_sitelibdir/glib-mkenums.rb
%ruby_sitelibdir/mkmf-gnome2.rb

%files -n ruby-gio2
%doc gio2/README
%ruby_sitearchdir/gio2.so
%ruby_sitelibdir/gio2.rb

%files -n ruby-gdkpixbuf2
%doc gdk_pixbuf2/README
%ruby_sitearchdir/gdk_pixbuf2.so
%ruby_sitelibdir/gdk_pixbuf2.rb

%files -n ruby-pango
%doc pango/README
%ruby_sitearchdir/pango.so
%ruby_sitelibdir/pango.rb

%files -n ruby-pango-devel
%_includedir/ruby/*/rbpango.h
%_includedir/ruby/*/rbpangoversion.h

%files -n ruby-atk
%doc atk/README
%ruby_sitearchdir/atk.so
%ruby_sitelibdir/atk.rb

%files -n ruby-atk-devel
%_includedir/ruby/*/rbatk.h
%_includedir/ruby/*/rbatkversion.h

%files -n ruby-gtk2
%doc gtk2/README
%ruby_sitearchdir/gtk2.so
%ruby_sitelibdir/gtk2.rb
%dir %ruby_sitelibdir/gtk2
%ruby_sitelibdir/gtk2/base.rb

%files -n ruby-bonobo2
%ruby_sitearchdir/bonobo2.so
%ruby_sitelibdir/bonobo2.rb

%files -n ruby-bonoboui2
%ruby_sitearchdir/bonoboui2.so
%ruby_sitelibdir/bonoboui2.rb

%files -n ruby-gconf2
%doc gconf/README
%ruby_sitearchdir/gconf2.so
%ruby_sitelibdir/gconf2.rb

%files -n ruby-goocanvas
%doc goocanvas/README
%ruby_sitearchdir/goocanvas.so
%ruby_sitelibdir/goocanvas.rb

%files -n ruby-gnome2
%doc gnome/README
%ruby_sitearchdir/gnome2.so
%ruby_sitelibdir/gnome2.rb

%files -n ruby-gnomecanvas2
%doc gnomecanvas/README
%ruby_sitearchdir/gnomecanvas2.so
%ruby_sitelibdir/gnomecanvas2.rb

%files -n ruby-gnomeprint2
%doc gnomeprint/README
%ruby_sitearchdir/gnomeprint2.so
%ruby_sitelibdir/gnomeprint2.rb

%files -n ruby-gnomeprint2-devel
%_includedir/ruby/*/rblibgnomeprintversion.h

%files -n ruby-gnomeprintui2
%doc gnomeprintui/README
%ruby_sitearchdir/gnomeprintui2.so
%ruby_sitelibdir/gnomeprintui2.rb

%files -n ruby-gnomevfs
%doc gnomevfs/README
%ruby_sitearchdir/gnomevfs.so
%ruby_sitelibdir/gnomevfs.rb

%files -n ruby-gst
%ruby_sitearchdir/gst.so
%ruby_sitelibdir/gst.rb

%files -n ruby-gtkglext
%doc gtkglext/README
%ruby_sitearchdir/gtkglext.so
%ruby_sitelibdir/gtkglext.rb

%files -n ruby-gtkhtml2
%doc gtkhtml2/README
%ruby_sitearchdir/gtkhtml2.so
%ruby_sitelibdir/gtkhtml2.rb

#%%files -n ruby-gtkmozembed
#%%doc gtkmozembed/README
#%%ruby_sitearchdir/gtkmozembed.so
#%%ruby_sitelibdir/gtkmozembed.rb

%files -n ruby-gtksourceview
%doc gtksourceview/README
%ruby_sitearchdir/gtksourceview.so
%ruby_sitelibdir/gtksourceview.rb

%files -n ruby-gtksourceview2
%doc gtksourceview2/README
%ruby_sitearchdir/gtksourceview2.so
%ruby_sitelibdir/gtksourceview2.rb

%files -n ruby-libart2
%doc libart/README
%ruby_sitearchdir/libart2.so

%files -n ruby-libart2-devel
%_includedir/ruby/*/rbart.h

%files -n ruby-libglade2
%doc libglade/README
%ruby_sitearchdir/libglade2.so
%ruby_sitelibdir/libglade2.rb

%files -n ruby-libglade2-devel
%_bindir/ruby-glade-create-template

#%files -n ruby-panelapplet2
#%doc panel-applet/README
#%ruby_sitearchdir/panelapplet2*.so
#%ruby_sitelibdir/panelapplet2.rb

%files -n ruby-rsvg2
%doc rsvg2/README
%ruby_sitearchdir/rsvg2.so
%ruby_sitelibdir/rsvg2.rb

%files -n ruby-vte
%doc vte/README
%ruby_sitearchdir/vte.so
%ruby_sitelibdir/vte.rb

%changelog
* Sun May 29 2011 Alexey Shabalin <shaba@altlinux.ru> 0.90.5-alt3
- removed panelapplet module

* Tue May 03 2011 Timur Aitov <timonbl4@altlinux.org> 0.90.5-alt2
- Repair build

* Sun Jan 09 2011 Alexey I. Froloff <raorn@altlinux.org> 0.90.5-alt1
- [0.90.5]
  + Re-added gio2 module
  + Removed gtk2-devel package

* Thu Jul 15 2010 Alexey I. Froloff <raorn@altlinux.org> 0.19.4-alt1
- [0.19.4]
  + Removed gio2 module

* Mon Apr 12 2010 Alexey I. Froloff <raorn@altlinux.org> 0.19.3-alt1
- [0.19.3]

* Fri Jun 26 2009 Alexey I. Froloff <raorn@altlinux.org> 0.19.0-alt0.3
- Rebuilt with Ruby 1.9

* Tue Jun 23 2009 Alexey I. Froloff <raorn@altlinux.org> 0.19.0-alt0.2
- Rebuilt with new libpng12

* Sat May 09 2009 Alexey I. Froloff <raorn@altlinux.org> 0.19.0-alt0.1
- SVN snapshot 20090404 (trunk)

* Sun Jan 11 2009 Sir Raorn <raorn@altlinux.ru> 0.18.1-alt2
- Updated build deps

* Thu Dec 25 2008 Sir Raorn <raorn@altlinux.ru> 0.18.1-alt1
- [0.18.1]

* Sat Oct 04 2008 Sir Raorn <raorn@altlinux.ru> 0.18.0-alt1
- [0.18.0]
- New packages:
 + goocanvas
 + gtksourceview2
- Unmasked deps on ruby(cairo) in several packages (closes: #17425)

* Tue Sep 02 2008 Sir Raorn <raorn@altlinux.ru> 0.16.0-alt8
- Disabled gtkmozembed (not ported to new xulrunner)

* Sun May 25 2008 Sir Raorn <raorn@altlinux.ru> 0.16.0-alt7
- Updated to trunk r3231
- Disabled poppler (permanently b0rken)

* Sun Mar 30 2008 Sir Raorn <raorn@altlinux.ru> 0.16.0-alt6
- Updated to trunk r2901
- New packages:
 + bonobo2
 + bonoboui2
 + gst

* Mon Jan 21 2008 Sir Raorn <raorn@altlinux.ru> 0.16.0-alt5
- Package libgtksourceview 1.8.x renamed to libgtksourceview1

* Mon Oct 08 2007 Sir Raorn <raorn@altlinux.ru> 0.16.0-alt4
- CVS snapshot 20071004
 + Fixed build with new glib2
 + Fixed build with poppler 0.6
 + ruby 1.9 compatibility fixes

* Fri Feb 02 2007 Sir Raorn <raorn@altlinux.ru> 0.16.0-alt3
- Obsolete old package names.  No provides added since depentant
  packages needs to be rebuilt

* Sat Jan 27 2007 Sir Raorn <raorn@altlinux.ru> 0.16.0-alt2
- gtk2-devel should depend on gtk2
- ruby-gettext is recommended for glib2, mention it in description

* Fri Jan 26 2007 Sir Raorn <raorn@altlinux.ru> 0.16.0-alt1
- Built for Sisyphus

