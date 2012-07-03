Name:           notecase
Version:        1.9.8
Release:        alt2.qa2
Summary:        A hierarchical text notes manager.
Packager:	Mykola S. Grechukh <gns@altlinux.ru>
Group:          Office
License:        BSD
URL:            http://notecase.sourceforge.net/
Source:         notecase-1.9.8_src.tar.gz
Patch0:         notecase-alt-include-cstdio.patch
Patch1:         notecase-gtksourceview.patch
Patch2:         notecase-1.9.8-alt-DSO.patch
BuildRequires:  libgtk+2-devel libgtksourceview-devel desktop-file-utils gettext gnome-vfs-devel
BuildRequires:	gcc-c++
Requires(post): desktop-file-utils shared-mime-info
Requires(postun): desktop-file-utils shared-mime-info

%description
NoteCase is a hierarchical text notes manager (outliner).
It helps you organize your everyday text notes into a single document
with individual notes placed into a tree-like structure. To ensure your
privacy an encrypted document format is supported along with a standard
unencrypted one.

%prep
%setup -q -n %name-%version
%patch0 -p1
%patch1 -p1
%patch2 -p0

%build
%make_build

%install
%makeinstall
%find_lang %{name}
desktop-file-install --dir %buildroot%_desktopdir \
	--remove-category=Application \
	--add-category=TextTools \
	%buildroot%_desktopdir/notecase.desktop

%files -f %{name}.lang
%defattr(-, root, root)
%{_bindir}/notecase
%dir %{_docdir}/notecase
%{_docdir}/notecase/help.ncd
%{_datadir}/pixmaps/notecase.xpm
%{_datadir}/applications/notecase.desktop
%{_datadir}/mime/packages/notecase.xml

%changelog
* Wed Jun 13 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.9.8-alt2.qa2
- Fixed build

* Tue May 24 2011 Repocop Q. A. Robot <repocop@altlinux.org> 1.9.8-alt2.qa1
- NMU (by repocop). See http://www.altlinux.org/Tools/Repocop
- applied repocop fixes:
  * freedesktop-desktop-file-proposed-patch for notecase

* Fri Apr 16 2010 Mykola Grechukh <gns@altlinux.ru> 1.9.8-alt2
- build fixed

* Mon Oct 05 2009 Mykola S. Grechukh <gns@altlinux.ru> 1.9.8-alt1
- initial build for ALT Linux

* Fri Jan 12 2007 Miroslav Rajcic <miroslav.rajcic@inet.hr>
- icon is now installed in /usr/share/pixmaps instead of /usr/share/icons
* Sat Oct 22 2005 Miroslav Rajcic <miroslav.rajcic@inet.hr>
- using .tar.gz instead of .zip for source archive
* Tue Aug 02 2005 Miroslav Rajcic <miroslav.rajcic@inet.hr>
- using %{?dist} macro instead of hardcoded distro code
* Mon Jun 06 2005 Miroslav Rajcic <miroslav.rajcic@inet.hr>
- using %find_lang macro instead of hardcoded list of .po files
* Thu Apr 14 2005 Miroslav Rajcic <miroslav.rajcic@inet.hr>
- updated build requirements information, added update-desktop-database call
* Thu Jan 20 2005 Miroslav Rajcic <miroslav.rajcic@inet.hr>
- updated packager and vendor fields, added new locale files to file list
* Wed Oct 20 2004 Neil Zanella <nzanella@users.sourceforge.net>
- Added desktop entry support
* Wed Oct 07 2004 Neil Zanella <nzanella@users.sourceforge.net>
- Moved some functionality out of SPEC file and into Makefile.
* Wed Oct 06 2004 Neil Zanella <nzanella@users.sourceforge.net>
- XPM icon is now more application-friendly and security fixes
* Tue Oct 04 2004 Neil Zanella <nzanella@users.sourceforge.net>
- minor modifications
* Sun Oct 03 2004 Neil Zanella <nzanella@users.sourceforge.net>
- initial release
