
Name: monodevelop-database
Version: 2.8.6.4
Release: alt1

Summary: Monodevelop Database Addin
License: MIT/X11
Group: Development/Other
Packager: Mono Maintainers Team <mono@packages.altlinux.org>
Url: http://www.monodevelop.org/

Source: %name-%version.tar
Patch0: %name-%version-%release.patch

# FIXME deps
%add_findreq_skiplist %_prefix/lib/monodevelop/AddIns/MonoDevelop.Database/*.dll
Requires: monodevelop >= %version
Requires: mysql-connector-net mono-data-postgresql mono-data-sqlite mono-data

BuildRequires: mono-mcs monodevelop mono-addins-devel libgtk-sharp2-devel
BuildRequires: mysql-connector-net-devel mono-data-postgresql mono-data-sqlite mono-data
BuildRequires: /proc

%description
MonoDevelop is a full-featured integrated development environment (IDE) for
mono and Gtk#. It was originally a port of SharpDevelop 0.98.

Monodevelop Database Addin

%prep
%setup -q
%patch0 -p1

%__subst "s|^pkgconfigdir *= \$(prefix)/lib/pkgconfig|pkgconfigdir = %_pkgconfigdir|" \
	Makefile.am

%build
%autoreconf
%configure
%make

%install
%make_install DESTDIR=%buildroot install

for langdir in %buildroot%_prefix/lib/monodevelop/AddIns/MonoDevelop.Database/locale/*; do
echo "%lang($(basename $langdir)) $(echo $langdir |sed s!%buildroot!!)" >> %name.lang
done

%files -f %name.lang
%_prefix/lib/monodevelop/AddIns/MonoDevelop.Database/*.dll
%_prefix/lib/monodevelop/AddIns/MonoDevelop.Database/*.mdb
%dir %_prefix/lib/monodevelop/AddIns/MonoDevelop.Database/locale
%_prefix/lib/monodevelop/AddIns/MonoDevelop.Database/icons

%changelog
* Thu Feb 16 2012 Alexey Shabalin <shaba@altlinux.ru> 2.8.6.4-alt1
- 2.8.6.4

* Thu Mar 10 2011 Alexey Shabalin <shaba@altlinux.ru> 2.4-alt1
- 2.4

* Thu Mar 18 2010 Alexey Shabalin <shaba@altlinux.ru> 2.2-alt2
- rebuild with monodevelop-2.2.2

* Tue Dec 15 2009 Alexey Shabalin <shaba@altlinux.ru> 2.2-alt1
- 2.2

* Tue Dec 08 2009 Alexey Shabalin <shaba@altlinux.ru> 2.1.1-alt1
- 2.1.1

* Sat Jun 20 2009 Alexey Shabalin <shaba@altlinux.ru> 2.0-alt1
- Initial build for ALTLinux
