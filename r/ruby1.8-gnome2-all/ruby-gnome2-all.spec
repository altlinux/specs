# vim: set ft=spec: -*- rpm-spec -*-

%define ruby_major 1.8

Name: ruby%{ruby_major}-gnome2-all
Version: 0.90.5
Release: alt4

Summary: Ruby bindings for GNOME-2.x
Group: Development/Ruby
License: LGPL
Url: http://ruby-gnome2.sourceforge.jp/

Packager: Ruby Maintainers Team <ruby@packages.altlinux.org>

Requires: libruby%{ruby_major} >= 1.8-alt3

%global reqpkg() %{expand:Requires: ruby%{ruby_major}-%%{1} = %%version-%%release}

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

# function 'force_encoding' miss in Ruby 1.8.7
Patch1: ruby-gnome2-all-0.90.5-alt-glib2.patch

# Automatically added by buildreq on Sun Jan 11 2009 (-bi)
BuildRequires: gst-plugins-devel libglade-devel libgnomeprintui-devel libgnomeui-devel libgoocanvas-devel libgtkglext-devel libgtkhtml2-devel libgtksourceview-devel libgtksourceview1-devel libjpeg-devel librsvg-devel libvte-devel ruby%{ruby_major}-rcairo-devel ruby%{ruby_major}-pkg-config libcairo-gobject-devel libpixman-devel xorg-dri2proto-devel xorg-glproto-devel libXau-devel libXdmcp-devel libXext-devel libXdamage-devel libpng-devel libudev-devel libXxf86vm-devel
# libgnome-panel-devel 
%description
This project is a set of Ruby language bindings for the various
application development libraries included with the GNOME/GTK+
environment. This project is for GTK+2.0 or later.

This is a virtual package which requires all ruby-gnome2 modules.

%package -n ruby%{ruby_major}-gnome2-samples
Summary: Sample scripts for ruby-gnome2 project
Group: Development/Ruby
BuildArch: noarch
Requires: ruby%{ruby_major} ruby%{ruby_major}-stdlibs

%description -n ruby%{ruby_major}-gnome2-samples
This package contains sample scripts for ruby-gnome2 project.

You should install appropriate modules in order to run this scripts.

%package -n ruby%{ruby_major}-glib2
Summary: Ruby bindings for Glib-2.x
Group: Development/Ruby
#Requires: ruby-gettext

%description -n ruby%{ruby_major}-glib2
Ruby/GLib2 is a Ruby binding of GLib-2.x.

It is recommended to install ruby-gettext.

%package -n ruby%{ruby_major}-glib2-devel
Summary: Development files for Ruby/GLib2
Group: Development/Ruby
BuildArch: noarch
PreReq: libruby%{ruby_major}-devel
Requires: libruby%{ruby_major}-devel
%reqpkg glib2

%description -n ruby%{ruby_major}-glib2-devel
Development files for Ruby/GLib2.

%package -n ruby%{ruby_major}-gio2
Summary: Ruby binding for gio-2.0.x
Group: Development/Ruby
%reqpkg glib2

%description -n ruby%{ruby_major}-gio2
Ruby/GIO is a Ruby binding of gio-2.0.x.

%package -n ruby%{ruby_major}-gdkpixbuf2
Summary: Ruby bindings for GdkPixbuf-2.x
Group: Development/Ruby

%description -n ruby%{ruby_major}-gdkpixbuf2
Ruby/GdkPixbuf2 is a Ruby binding of GdkPixbuf-2.x.

%package -n ruby%{ruby_major}-pango
Summary: Ruby bindings for pango-1.x
Group: Development/Ruby

%description -n ruby%{ruby_major}-pango
Ruby/Pango is a Ruby binding of pango-1.x.

%package -n ruby%{ruby_major}-pango-devel
Summary: Development files for Ruby/Pango
Group: Development/Ruby
BuildArch: noarch
PreReq: libruby%{ruby_major}-devel
Requires: ruby%{ruby_major}-rcairo-devel
%reqpkg pango
%reqpkg glib2-devel

%description -n ruby%{ruby_major}-pango-devel
Development files for Ruby/Pango.

%package -n ruby%{ruby_major}-atk
Summary: Ruby bindings for ATK-1.0.x
Group: Development/Ruby

%description -n ruby%{ruby_major}-atk
Ruby/ATK is a Ruby binding of ATK-1.0.x or later.

%package -n ruby%{ruby_major}-atk-devel
Summary: Development files for Ruby/ATK
Group: Development/Ruby
BuildArch: noarch
PreReq: libruby%{ruby_major}-devel
%reqpkg atk
%reqpkg glib2-devel

%description -n ruby%{ruby_major}-atk-devel
Development files for Ruby/ATK.

%package -n ruby%{ruby_major}-gtk2
Summary: Ruby bindings for GTK+-2.0.x
Group: Development/Ruby

%description -n ruby%{ruby_major}-gtk2
Ruby/GTK2 is a Ruby binding of GTK+-2.0.x.

%package -n ruby%{ruby_major}-bonobo2
Summary: Ruby bindings for libbonobo-2.x
Group: Development/Ruby

%description -n ruby%{ruby_major}-bonobo2
Ruby/Bonobo2 is a Ruby binding of libbonobo-2.x.

%package -n ruby%{ruby_major}-bonoboui2
Summary: Ruby bindings for libbonoboui-2.x
Group: Development/Ruby

%description -n ruby%{ruby_major}-bonoboui2
Ruby/BonoboUI2 is a Ruby binding of libbonoboui-2.x.

%package -n ruby%{ruby_major}-gconf2
Summary: Ruby bindings for GConf-1.2.x
Group: Development/Ruby

%description -n ruby%{ruby_major}-gconf2
Ruby/GConf2 is a Ruby binding of GConf-1.2.x.

%package -n ruby%{ruby_major}-gnome2
Summary: Ruby bindings for libgnome/libgnomeui-2.x
Group: Development/Ruby

%description -n ruby%{ruby_major}-gnome2
Ruby/GNOME2 is a Ruby binding of libgnome/libgnomeui-2.x.

%package -n ruby%{ruby_major}-gnomecanvas2
Summary: Ruby bindings for GnomeCanvas-2.x
Group: Development/Ruby

%description -n ruby%{ruby_major}-gnomecanvas2
Ruby/GnomeCanvas2 is a Ruby binding of GnomeCanvas-2.x.

%package -n ruby%{ruby_major}-gnomeprint2
Summary: Ruby bindings for libgnomeprint
Group: Development/Ruby

%description -n ruby%{ruby_major}-gnomeprint2
Ruby/GnomePrint is a Ruby binding of libgnomeprint.

%package -n ruby%{ruby_major}-gnomeprint2-devel
Summary: Development files for Ruby/GnomePrint
Group: Development/Ruby
BuildArch: noarch
PreReq: libruby%{ruby_major}-devel
%reqpkg gnomeprint2

%description -n ruby%{ruby_major}-gnomeprint2-devel
Development files for Ruby/GnomePrint.

%package -n ruby%{ruby_major}-gnomeprintui2
Summary: Ruby bindings for libgnomeprintui
Group: Development/Ruby

%description -n ruby%{ruby_major}-gnomeprintui2
Ruby/GnomePrintUI is a Ruby binding of libgnomeprintui.

%package -n ruby%{ruby_major}-gnomevfs
Summary: Ruby bindings for GnomeVFS-2.0.x
Group: Development/Ruby

%description -n ruby%{ruby_major}-gnomevfs
Ruby/GnomeVFS is a Ruby binding of GnomeVFS-2.0.x.

%package -n ruby%{ruby_major}-goocanvas
Summary: Ruby bindings for GooCanvas
Group: Development/Ruby

%description -n ruby%{ruby_major}-goocanvas
Ruby/GStreamer is a Ruby binding for GooCanvas.

%package -n ruby%{ruby_major}-gst
Summary: Ruby bindings for GStreamer
Group: Development/Ruby

%description -n ruby%{ruby_major}-gst
Ruby/GStreamer is a Ruby binding for GStreamer.

%package -n ruby%{ruby_major}-gtkglext
Summary: Ruby bindings for GtkGLExt
Group: Development/Ruby

%description -n ruby%{ruby_major}-gtkglext
Ruby/GtkGLExt is a Ruby binding of GtkGLExt.

%package -n ruby%{ruby_major}-gtkhtml2
Summary: Ruby bindings for GtkHtml2
Group: Development/Ruby

%description -n ruby%{ruby_major}-gtkhtml2
Ruby/GtkHtml2 is a Ruby binding of GtkHtml2.

%package -n ruby%{ruby_major}-gtkmozembed
Summary: Ruby bindings for GtkMozEmbed
Group: Development/Ruby

%description -n ruby%{ruby_major}-gtkmozembed
Ruby/GtkMozEmbed is a Ruby binding of GtkMozEmbed a widget embedding a
Mozilla Gecko renderer.

%package -n ruby%{ruby_major}-gtksourceview
Summary: Ruby bindings for gtksourceview-1.0.x
Group: Development/Ruby

%description -n ruby%{ruby_major}-gtksourceview
Ruby/GtkSourceView is a Ruby binding of gtksourceview-1.0.x.

%package -n ruby%{ruby_major}-gtksourceview2
Summary: Ruby bindings for gtksourceview-2.x
Group: Development/Ruby

%description -n ruby%{ruby_major}-gtksourceview2
Ruby/GtkSourceView is a Ruby binding of gtksourceview-2.x.

%package -n ruby%{ruby_major}-libart2
Summary: Ruby bindings for Libart_lgpl
Group: Development/Ruby

%description -n ruby%{ruby_major}-libart2
Ruby/Libart2 is a Ruby binding of Libart_lgpl.

%package -n ruby%{ruby_major}-libart2-devel
Summary: Development files for Ruby/Libart2
Group: Development/Ruby
BuildArch: noarch
PreReq: libruby%{ruby_major}-devel
%reqpkg libart2

%description -n ruby%{ruby_major}-libart2-devel
Development files for Ruby/Libart2.

%package -n ruby%{ruby_major}-libglade2
Summary: Ruby bindings for Libglade2
Group: Development/Ruby

%description -n ruby%{ruby_major}-libglade2
Ruby/Libglade2 is a Ruby bindings of Libglade2.
This provides a very simple interface to the libglade library,
to load interfaces dynamically from a glade file.

%package -n ruby%{ruby_major}-libglade2-devel
Summary: Development files for Ruby/Libglade2
Group: Development/Ruby
BuildArch: noarch
%reqpkg libglade2

%description -n ruby%{ruby_major}-libglade2-devel
Development files for Ruby/Libglade2.

This packagee contains ruby-glade-create-template utility.

#%package -n ruby%{ruby_major}-panelapplet2
#Summary: Ruby bindings for libpanel-applet-2.6.x
#Group: Development/Ruby

#%description -n ruby%{ruby_major}-panelapplet2
#Ruby/PanelApplet2 is a Ruby binding of libpanel-applet-2.6.x.

%package -n ruby%{ruby_major}-rsvg2
Summary: Ruby bindings for librsvg
Group: Development/Ruby

%description -n ruby%{ruby_major}-rsvg2
Ruby/RSVG is a Ruby binding of librsvg.

%package -n ruby%{ruby_major}-vte
Summary: Ruby bindings for VTE
Group: Development/Ruby

%description -n ruby%{ruby_major}-vte
Ruby/VTE is a Ruby binding of VTE.

%prep
%setup -q
%patch -p1

%patch1 -p1

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

%files -n ruby%{ruby_major}-gnome2-samples
%doc AUTHORS ChangeLog NEWS README
%doc samples/*

%files -n ruby%{ruby_major}-glib2
%doc glib2/README
%ruby_sitearchdir/glib2.so
%ruby_sitelibdir/glib2.rb

%files -n ruby%{ruby_major}-glib2-devel
#_includedir/ruby/*/rbgcompat.h
#_includedir/ruby/*/rbglib.h
#_includedir/ruby/*/rbgutil.h
#_includedir/ruby/*/rbgobject.h
#_includedir/ruby/*/glib-enum-types.h
%ruby_sitelibdir/glib-mkenums.rb
%ruby_sitelibdir/mkmf-gnome2.rb

%files -n ruby%{ruby_major}-gio2
%doc gio2/README
%ruby_sitearchdir/gio2.so
%ruby_sitelibdir/gio2.rb

%files -n ruby%{ruby_major}-gdkpixbuf2
%doc gdk_pixbuf2/README
%ruby_sitearchdir/gdk_pixbuf2.so
%ruby_sitelibdir/gdk_pixbuf2.rb

%files -n ruby%{ruby_major}-pango
%doc pango/README
%ruby_sitearchdir/pango.so
%ruby_sitelibdir/pango.rb

%files -n ruby%{ruby_major}-pango-devel
%_includedir/ruby/*/rbpango.h
%_includedir/ruby/*/rbpangoversion.h

%files -n ruby%{ruby_major}-atk
%doc atk/README
%ruby_sitearchdir/atk.so
%ruby_sitelibdir/atk.rb

%files -n ruby%{ruby_major}-atk-devel
%_includedir/ruby/*/rbatk.h
%_includedir/ruby/*/rbatkversion.h

%files -n ruby%{ruby_major}-gtk2
%doc gtk2/README
%ruby_sitearchdir/gtk2.so
%ruby_sitelibdir/gtk2.rb
%dir %ruby_sitelibdir/gtk2
%ruby_sitelibdir/gtk2/base.rb

%files -n ruby%{ruby_major}-bonobo2
%ruby_sitearchdir/bonobo2.so
%ruby_sitelibdir/bonobo2.rb

%files -n ruby%{ruby_major}-bonoboui2
%ruby_sitearchdir/bonoboui2.so
%ruby_sitelibdir/bonoboui2.rb

%files -n ruby%{ruby_major}-gconf2
%doc gconf/README
%ruby_sitearchdir/gconf2.so
%ruby_sitelibdir/gconf2.rb

%files -n ruby%{ruby_major}-goocanvas
%doc goocanvas/README
%ruby_sitearchdir/goocanvas.so
%ruby_sitelibdir/goocanvas.rb

%files -n ruby%{ruby_major}-gnome2
%doc gnome/README
%ruby_sitearchdir/gnome2.so
%ruby_sitelibdir/gnome2.rb

%files -n ruby%{ruby_major}-gnomecanvas2
%doc gnomecanvas/README
%ruby_sitearchdir/gnomecanvas2.so
%ruby_sitelibdir/gnomecanvas2.rb

%files -n ruby%{ruby_major}-gnomeprint2
%doc gnomeprint/README
%ruby_sitearchdir/gnomeprint2.so
%ruby_sitelibdir/gnomeprint2.rb

%files -n ruby%{ruby_major}-gnomeprint2-devel
%_includedir/ruby/*/rblibgnomeprintversion.h

%files -n ruby%{ruby_major}-gnomeprintui2
%doc gnomeprintui/README
%ruby_sitearchdir/gnomeprintui2.so
%ruby_sitelibdir/gnomeprintui2.rb

%files -n ruby%{ruby_major}-gnomevfs
%doc gnomevfs/README
%ruby_sitearchdir/gnomevfs.so
%ruby_sitelibdir/gnomevfs.rb

%files -n ruby%{ruby_major}-gst
%ruby_sitearchdir/gst.so
%ruby_sitelibdir/gst.rb

%files -n ruby%{ruby_major}-gtkglext
%doc gtkglext/README
%ruby_sitearchdir/gtkglext.so
%ruby_sitelibdir/gtkglext.rb

%files -n ruby%{ruby_major}-gtkhtml2
%doc gtkhtml2/README
%ruby_sitearchdir/gtkhtml2.so
%ruby_sitelibdir/gtkhtml2.rb

#%%files -n ruby-gtkmozembed
#%%doc gtkmozembed/README
#%%ruby_sitearchdir/gtkmozembed.so
#%%ruby_sitelibdir/gtkmozembed.rb

%files -n ruby%{ruby_major}-gtksourceview
%doc gtksourceview/README
%ruby_sitearchdir/gtksourceview.so
%ruby_sitelibdir/gtksourceview.rb

%files -n ruby%{ruby_major}-gtksourceview2
%doc gtksourceview2/README
%ruby_sitearchdir/gtksourceview2.so
%ruby_sitelibdir/gtksourceview2.rb

%files -n ruby%{ruby_major}-libart2
%doc libart/README
%ruby_sitearchdir/libart2.so

%files -n ruby%{ruby_major}-libart2-devel
%_includedir/ruby/*/rbart.h

%files -n ruby%{ruby_major}-libglade2
%doc libglade/README
%ruby_sitearchdir/libglade2.so
%ruby_sitelibdir/libglade2.rb

%files -n ruby%{ruby_major}-libglade2-devel
%_bindir/ruby-glade-create-template

#%files -n ruby%{ruby_major}-panelapplet2
#%doc panel-applet/README
#%ruby_sitearchdir/panelapplet2*.so
#%ruby_sitelibdir/panelapplet2.rb

%files -n ruby%{ruby_major}-rsvg2
%doc rsvg2/README
%ruby_sitearchdir/rsvg2.so
%ruby_sitelibdir/rsvg2.rb

%files -n ruby%{ruby_major}-vte
%doc vte/README
%ruby_sitearchdir/vte.so
%ruby_sitelibdir/vte.rb

%changelog
* Sun May 29 2011 Alexey Shabalin <shaba@altlinux.ru> 0.90.5-alt4
- removed panelapplet module

* Tue May 03 2011 Timur Aitov <timonbl4@altlinux.org> 0.90.5-alt3
- Rebuild for ruby1.8

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

