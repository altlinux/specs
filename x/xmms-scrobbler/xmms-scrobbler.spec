%undefine __libtoolize

# hack needed for minus sign in macro
%define tr_() %(printf %%s %1 | tr -- _ -)
%def_disable bmp_plugin
%define subst_enable_bmp_plugin %{subst_enable bmp_plugin}

Name: xmms-scrobbler
Version: 0.4.0
Release: alt1

Summary: XMMS Audioscrobbler plugin
License: LGPL
Group: Sound

Url: http://www.last.fm/
Source: %name-%version.tar.gz

BuildPreReq: gcc-c++ pkgconfig
BuildPreReq: libcurl-devel >= 7.9.7 libmusicbrainz-devel >= 2.0.0
BuildPreReq: libxmms-devel >= 1.2.4

%if_enabled bmp_plugin
BuildPreReq: libbeep-devel >= 0.9.7  glib2-devel >= 2.4.0 libgtk+2-devel >= 2.4.0
%endif

# Automatically added by buildreq on Sun Jun 27 2010
BuildRequires: gcc-c++ libcurl-devel libmusicbrainz-devel libtag-devel libxmms-devel

%description
XMMS plugin to send your listening data to audioscrobbler.

%if_enabled bmp_plugin
%package -n beep-scrobbler
Summary: BMP Audioscrobbler plugin
Group: Sound

%description -n beep-scrobbler
BMP plugin to send your listening data to audioscrobbler.
%endif #bmp

%prep
%setup

%build
%configure %tr_ %subst_enable_bmp_plugin
%make_build

%install
%make_install install DESTDIR=%buildroot

%files
%_libdir/xmms/General/*.so
%doc AUTHORS ChangeLog KnownIssues NEWS README* TODO

%if_enabled bmp_plugin
%files -n beep-scrobbler
%_libdir/bmp/General/*.so
%doc AUTHORS ChangeLog KnownIssues NEWS README* TODO
%endif

%changelog
* Sun Jun 27 2010 Michael Shigorin <mike@altlinux.org> 0.4.0-alt1
- 0.4.0 (maybe closes: #15857)
- disabled BMP plugin build by default (fixes welcome)
- buildreq

* Fri Mar 30 2007 ALT QA Team Robot <qa-robot@altlinux.org> 0.3.8.1-alt1.1.0
- Rebuilt due to libcurl.so.3 -> libcurl.so.4 soname change.

* Fri Dec 29 2006 ALT QA Team Robot <qa-robot@altlinux.org> 0.3.8.1-alt1.1
- Rebuilt due to libcrypto.so.4 -> libcrypto.so.6 soname change.

* Wed Oct 26 2005 Andrey Rahmatullin <wrar@altlinux.ru> 0.3.8.1-alt1
- initial build
