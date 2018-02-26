
Name: accerciser
Version: 1.12.1
Release: alt5.1

Summary: An interactive Python tool for querying accessibility information
Url: http://live.gnome.org/Accerciser
License: %bsd

Group: Accessibility
Packager: Michael Pozhidaev <msp@altlinux.ru>

# Automatically added by buildreq on Sun Sep 28 2008
BuildRequires: GConf docbook-dtds gnome-doc-utils-xslt perl-XML-Parser python-devel libgio-devel libgtk+3-devel python-module-pyatspi

BuildRequires: rpm-build-licenses rpm-build-gnome gnome-doc-utils libGConf-devel
BuildPreReq: intltool
BuildRequires: desktop-file-utils

BuildArch: noarch
Source: %name-%version.tar

# debian watch file (for automation)
Source100: %name.watch

Requires: python-module-%name = %version-%release

%description
An interactive Python accessibility explorer.

%add_python_req_skip gtksourceview

%package -n python-module-%name
Summary: Python module for accerciser
Group: Development/Python
BuildArch: noarch
# The macro below is resolved into an empty string but confuses build process
#%_python_set_noarch

%description -n python-module-%name
An interactive Python accessibility explorer.

This package contains Python module for accerciser.

%prep
%setup -q

%build
%configure  --disable-scrollkeeper --without-pyreqs
%make_build

%install
%makeinstall_std
desktop-file-install --dir %buildroot%_desktopdir \
	--add-category=X-Development-Accessibility \
        %buildroot%_desktopdir/%name.desktop

%find_lang --with-gnome %name

%post
%gconf2_install accerciser

%preun
if [ $1 = 0 ]; then
%gconf2_uninstall accerciser
fi

%files -f %name.lang
%doc AUTHORS README COPYING NEWS ChangeLog
%_bindir/*
%_datadir/%name
%_datadir/applications/*
%_man1dir/*
%gconf_schemasdir/*
%_datadir/icons/hicolor/16x16/apps/%name.png
%_datadir/icons/hicolor/22x22/apps/%name.png
%_datadir/icons/hicolor/32x32/apps/%name.png
%_datadir/icons/hicolor/48x48/apps/accerciser.png
%_datadir/icons/hicolor/scalable/apps/accerciser.svg

%files -n python-module-%name
%python_sitelibdir/%name/

%changelog
* Sat Oct 22 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.12.1-alt5.1
- Rebuild with Python-2.7

* Wed Oct 19 2011 Igor Vlasenko <viy@altlinux.ru> 1.12.1-alt5
- updated watch file, updated future BuildRequires: for 3.2.x version

* Wed Oct 19 2011 Igor Vlasenko <viy@altlinux.ru> 1.12.1-alt4
- added future BuildRequires: for 3.2.x version

* Tue Oct 11 2011 Igor Vlasenko <viy@altlinux.ru> 1.12.1-alt3
- find_lang finds gnome_helpdir, no need to package it explicitly

* Mon Oct 10 2011 Igor Vlasenko <viy@altlinux.ru> 1.12.1-alt2
- use find_lang, updated desktop file categories

* Sun Oct 09 2011 Igor Vlasenko <viy@altlinux.ru> 1.12.1-alt1
- intermediate update to 1.12.1. added watch file.

* Sun Oct 10 2010 Michael Pozhidaev <msp@altlinux.ru> 1.11.1-alt1
- New version 1.11.1 (closes: #23423)

* Thu Jul 29 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.9.3-alt1
- Version 1.9.3

* Thu Mar 18 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.4.0-alt3
- Extracted python module into separate package

* Mon Nov 16 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.4.0-alt2.1
- Rebuilt with python 2.6

* Wed Oct 15 2008 Michael Pozhidaev <msp@altlinux.ru> 1.4.0-alt2
- Fixed gconf schema installation

* Sun Sep 28 2008 Michael Pozhidaev <msp@altlinux.ru> 1.4.0-alt1
- ALT Linux package

* Thu Apr 12 2007 Peter Parente <parente@cs.unc.edu>
- Added gconf schema install, uninstall, and files

* Mon Apr 02 2007 Peter Parente <parente@cs.unc.edu>
- Added without-pyreqs flag to avoid checking for modules at rpmbuild time
- Added locales to files section

* Wed Feb 22 2007 Peter Parente <parente@cs.unc.edu>
- First release
