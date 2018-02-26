%define _unpackaged_files_terminate_build 1

Name: homebank
Version: 4.4
Release: alt1

# Note: _unstable suffix sometimes appears in some versions of the tarball.
%define _version %{version}
#_unstable

Summary: Free easy personal accounting for all!
License: %gpl2plus
Group: Graphical desktop/GNOME
Url: http://%name.free.fr/index.php

Packager: Alexey Rusakov <ktirf@altlinux.ru>

Source: http://%name.free.fr/public/%name-%_version.tar.gz

BuildRequires(pre): rpm-build-licenses

# From configure.ac
BuildPreReq: intltool
BuildPreReq: glib2-devel >= 2.14
BuildPreReq: libgtk+2-devel >= 2.12
BuildPreReq: libofx-devel

BuildPreReq: perl-XML-Parser shared-mime-info desktop-file-utils

%description
HomeBank is the free software you have always wanted to manage your
personal accounts at home. The main concept is to be light, simple and
very easy to use.

It brings you many features that allow you to analyze your finances in
a detailed way instantly and dynamically with powerful report tools
based on filtering and graphical charts.

Furthermore HomeBank benefits now for more than 10 years of users
experience and feedback as its development started in 1995 on Amiga
computers. It is now available on Amiga, GNU/Linux, and will probably be
soon available for Microsoft Windows and MacOS X systems, as GTK+ exists
on it.

%package help
Summary: Help files for HomeBank
Group: Graphical desktop/GNOME
Requires: homebank = %version-%release
BuildArch: noarch

%description help
HomeBank is the free software you have always wanted to manage your
personal accounts at home. The main concept is to be light, simple and
very easy to use.

It brings you many features that allow you to analyze your finances in
a detailed way instantly and dynamically with powerful report tools
based on filtering and graphical charts.

This package contains help files for HomeBank. The manual is easy to
read and rather useful for a first time user.

%prep
%setup -q -n %name-%_version

%build
%configure \
    --with-ofx

%make_build

%install
%make_install DESTDIR=%buildroot install

%find_lang --with-gnome %name

%files -f %name.lang
%_bindir/%name
%_desktopdir/%name.desktop
%dir %_datadir/%name
%dir %_datadir/%name/images
%_datadir/%name/images/*
%_datadir/%name/icons/
%_datadir/%name/datas/
%_datadir/mime-info/%name.keys
%_datadir/mime-info/%name.mime
%_datadir/mime/packages/%name.xml
%_iconsdir/hicolor/*/apps/%name.*

%files help
%dir %_datadir/%name/help
%_datadir/%name/help/*

%exclude %_datadir/application-registry/%name.applications

%changelog
* Sun Mar 13 2011 Yuri N. Sedunov <aris@altlinux.org> 4.4-alt1
- 4.4
- spec cleanup

* Sat Aug 22 2009 Alexey Rusakov <ktirf@altlinux.org> 4.0.4-alt1
- New version.
- Moved help files to a separate noarch subpackage (addressing a notice
  from repocop).

* Sat Apr 04 2009 Alexey Rusakov <ktirf@altlinux.org> 4.0.2-alt1
- Repocop-reported fixes:
  + removed deprecated post/postun macros;
  + added Packager tag.
- Specfile cleaned up, buildreqs updated.

* Thu Apr 10 2008 Igor Vlasenko <viy@altlinux.ru> 3.5-alt1.qa1
- NMU (by repocop): the following fixes applied:
 * update_menus for homebank

* Sat Oct 13 2007 Alexey Rusakov <ktirf@altlinux.org> 3.5-alt1
- new version (3.5)
- updated files list

* Sun Jul 01 2007 Alexey Rusakov <ktirf@altlinux.org> 3.4-alt1
- new version (3.4)

* Wed Jun 13 2007 Alexey Rusakov <ktirf@altlinux.org> 3.3-alt1
- Initial Sisyphus version

