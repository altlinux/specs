# BEGIN SourceDeps(oneline):
BuildRequires: /usr/bin/perl pkgconfig(gtk+-2.0) pkgconfig(gtk+-3.0) pkgconfig(x11)
# END SourceDeps(oneline)
%define _libexecdir %_prefix/libexec
Name:		mate-dialogs
Version:	1.4.0
Release:	alt1_1.1
Summary:	Display dialog boxes from shell scripts
Group:		File tools
License:	LGPLv2+
URL:		http://mate-desktop.or
Source:		http://pub.mate-desktop.org/releases/1.4/%{name}-%{version}.tar.xz

BuildRequires: mate-doc-utils >= 1.0.0
BuildRequires: glib2-devel >= 2.7.3
BuildRequires: gtk2-devel
BuildRequires: libmatenotify-devel >= 1.1.0
BuildRequires: scrollkeeper
BuildRequires: which
BuildRequires: gettext
BuildRequires: intltool
BuildRequires: mate-common

%description
mate-dialogs lets you display Gtk+ dialog boxes from the command line and through
shell scripts. It is similar to gdialog, but is intended to be saner. It comes
from the same family as dialog, Xdialog, and cdialog.

%prep
%setup -q
NOCONFIGURE=1 ./autogen.sh

%build

%configure \
	--disable-static \
	--enable-libmatenotify

make %{?_smp_mflags}


%install
make install DESTDIR=$RPM_BUILD_ROOT

# we don't want a perl dependency just for this
rm $RPM_BUILD_ROOT%{_bindir}/gdialog

# save space by linking identical images in translated docs
helpdir=$RPM_BUILD_ROOT%{_datadir}/mate/help/%{name}
for f in $helpdir/C/figures/*.png; do
  b="$(basename $f)"
  for d in $helpdir/*; do
    if [ -d "$d" -a "$d" != "$helpdir/C" ]; then
      g="$d/figures/$b"
      if [ -f "$g" ]; then
        if cmp -s $f $g; then
          rm "$g"; ln -s "../../C/figures/$b" "$g"
        fi
      fi
    fi
  done
done

%find_lang mate-dialogs


%files
%doc COPYING AUTHORS NEWS THANKS README
%{_bindir}/matedialog
%{_datadir}/matedialog
%{_mandir}/man1/matedialog.1.*
%{_datadir}/locale/*/LC_MESSAGES/*.mo
%{_datadir}/mate/help/matedialog/*/figures/*.png
%{_datadir}/mate/help/matedialog/*/*.xml
%{_datadir}/omf/matedialog/*.omf


%changelog
* Wed Oct 24 2012 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1.4.0-alt1_1.1
- Build for Sisyphus

* Thu Aug 02 2012 Igor Vlasenko <viy@altlinux.ru> 1.4.0-alt1_1
- 20120801 mate snapshot

* Wed Jun 27 2012 Igor Vlasenko <viy@altlinux.ru> 1.2.0-alt2_1
- 20120622 mate snapshot

* Mon Apr 30 2012 Igor Vlasenko <viy@altlinux.ru> 1.2.0-alt1_1
- converted by srpmconvert script

