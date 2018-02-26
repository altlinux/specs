Summary: Simple GTK2 frontend for lsof
Name: glsof
Version: 0.9.17
Release: alt3.1.qa2
Packager: Eugene V. Horohorin <genix@altlinux.ru>
URL: http://glsof.sourceforge.net
Source0: %{name}-%{version}.tar.gz
License: GPL
Group: Monitoring

# Automatically added by buildreq on Tue Sep 16 2008
BuildRequires: libgnomeui-devel perl-XML-Parser libglade-devel

Requires: lsof libxml2 
BuildRequires: desktop-file-utils

%description
GTK-Lsof is a simple FrontEnd for LSOF.
You can Save output, Refresh (or Automatic Refresh) output,
select fields of out put and apply LSOF commands.

%prep
%setup -q

%build
%configure
%make

%install
export GCONF_DISABLE_MAKEFILE_SCHEMA_INSTALL=1
export GCONF_SCHEMA_FILE_DIR="%{buildroot}%{_sysconfdir}/gconf/schemas"
%makeinstall
%find_lang %{name}
desktop-file-install --dir %buildroot%_desktopdir \
	--remove-category=Application \
	--add-category=Monitor \
	%buildroot%_desktopdir/glsof.desktop

%post
export GCONF_CONFIG_SOURCE="$(gconftool-2 --get-default-source)"
gconftool-2 --makefile-install-rule %{_sysconfdir}/gconf/schemas/%{name}.schemas &>/dev/null || :

%preun
export GCONF_CONFIG_SOURCE="$(gconftool-2 --get-default-source)"
gconftool-2 --makefile-uninstall-rule %{_sysconfdir}/gconf/schemas/%{name}.schemas &>/dev/null || :

%files -f %{name}.lang
%_bindir/*
%_datadir/%{name}
#%%_datadir/%{name}/*
%_datadir/pixmaps/*
%_desktopdir/*
%{_sysconfdir}/gconf/schemas/%{name}.schemas
%doc README ChangeLog AUTHORS NEWS

%changelog
* Mon May 23 2011 Repocop Q. A. Robot <repocop@altlinux.org> 0.9.17-alt3.1.qa2
- NMU (by repocop). See http://www.altlinux.org/Tools/Repocop
- applied repocop fixes:
  * freedesktop-desktop-file-proposed-patch for glsof

* Thu Nov 19 2009 Repocop Q. A. Robot <repocop@altlinux.org> 0.9.17-alt3.1.qa1
- NMU (by repocop): the following fixes applied:
  * update_menus for glsof
  * postclean-05-filetriggers for spec file

* Sat Feb 14 2009 Alexey Rusakov <ktirf@altlinux.org> 0.9.17-alt3.1
- NMU: added libglade-devel to buildreqs

* Tue Sep 16 2008 Eugene V. Horohorin <genix@altlinux.ru> 0.9.17-alt3
- buildreq updated
- tag Packager added
- old-style menu removed

* Thu Dec 22 2005 Eugene V. Horohorin <genix@altlinux.ru> 0.9.17-alt2
- bug #8669 fixed (directory /usr/share/%name)

* Mon Jan 03 2005 Eugene V. Horohorin <genix@altlinux.ru> 0.9.17-alt1
- new version
- spec clean-up: using %find_lang (bug #5681), using glsof.schemas, %update_menus added

* Fri Jul 09 2004 Eugene V. Horohorin <genix@altlinux.ru> 0.9.16-alt1
- new version (0.9.16)

* Wed Apr 07 2004 Eugene V. Horohorin <genix@altlinux.ru> 0.9.15-alt1
- Implementation build

