# BEGIN SourceDeps(oneline):
BuildRequires: /usr/bin/gconftool-2 pkgconfig(glib-2.0)
# END SourceDeps(oneline)
Name:             buoh
License:          GPLv2+
Group:            Networking/Other
Version:          0.8.2
Release:          alt2_9
Summary:          Online comics reader
URL:              http://buoh.steve-o.org/
Source:           http://buoh.steve-o.org/downloads/buoh-%{version}.tar.bz2
BuildRequires:    desktop-file-utils perl perl-XML-Parser gettext libgtk+2-devel libsoup22-devel libgnomeui-devel libGConf-devel
Requires(post):   GConf2
Requires(postun): GConf2
Source44: import.info

%description
Buoh is a reader for online strips comics. It has a number of features,
including: Selecting your favorites comic through a list of more than 130
comics, easy & simple an eye-candy view of an online comic, browsing over
the comic strip archives.

%prep
%setup -q

perl -i -npe 's,#include\s*<(?:glib/gmessages|glib/gversionmacros|glib/gmacros|glib/gtypes|glib/gthread|glibconfig)\.h>,#include <glib.h>,' `pcregrep -rl '#include\s*<\(glib/gmessages\|glib/gversionmacros\|glib/gmacros\|glib/gtypes\|glib/gthread\|glibconfig\)\.h>' .`


%build
%configure
make %{?_smp_mflags}

%install
export GCONF_DISABLE_MAKEFILE_SCHEMA_INSTALL=1
make install DESTDIR=$RPM_BUILD_ROOT

perl -pi -e "s,Terminal=0,Terminal=false,g" $RPM_BUILD_ROOT%{_datadir}/applications/buoh.desktop
desktop-file-install --delete-original			\
  --vendor=fedora								\
  --dir $RPM_BUILD_ROOT%{_datadir}/applications \
  --add-category X-Fedora						\
  $RPM_BUILD_ROOT%{_datadir}/applications/buoh.desktop

%post
export GCONF_CONFIG_SOURCE=`gconftool-2 --get-default-source`
gconftool-2 --makefile-install-rule %{_sysconfdir}/gconf/schemas/buoh.schemas > /dev/null  || :
killall -HUP gconfd-2 &>/dev/null || :

%postun
if [ "$1" -gt 1 ]; then
  export GCONF_CONFIG_SOURCE=`gconftool-2 --get-default-source`
  gconftool-2 --makefile-uninstall-rule %{_sysconfdir}/gconf/schemas/buoh.schemas >/dev/null || :
  killall -HUP gconfd-2 &>/dev/null || :
fi

%preun
if [ "$1" -eq 0 ]; then
  export GCONF_CONFIG_SOURCE=`gconftool-2 --get-default-source`
  gconftool-2 --makefile-uninstall-rule %{_sysconfdir}/gconf/schemas/buoh.schemas > /dev/null || :
  killall -HUP gconfd-2 &>/dev/null || :
fi
		  
%files
%doc AUTHORS COPYING INSTALL README NEWS TODO
%dir %{_datadir}/buoh
%dir %{_datadir}/buoh/comics
%dir %{_datadir}/buoh/ui
%{_bindir}/buoh
%{_sysconfdir}/gconf/schemas/buoh.schemas
%{_datadir}/applications/fedora-buoh.desktop
%{_datadir}/buoh/comics/comics.xml
%{_datadir}/buoh/ui/buoh-ui.xml
%{_datadir}/icons/hicolor/64x64/apps/buoh.png
%{_datadir}/icons/hicolor/16x16/apps/buoh.png

%changelog
* Sat Apr 14 2012 Igor Vlasenko <viy@altlinux.ru> 0.8.2-alt2_9
- fixed build with new glib

* Sat Dec 17 2011 Igor Vlasenko <viy@altlinux.ru> 0.8.2-alt1_9
- initial import by fcimport

