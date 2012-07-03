
Name: monodevelop-python
Version: 2.8.6.4
Release: alt1

Summary: Python Language Binding
License: MIT/X11
Group: Development/Other
Packager: Mono Maintainers Team <mono@packages.altlinux.org>
Url: http://www.monodevelop.org/

Source: %name-%version.tar

# FIXME deps
%add_findreq_skiplist %_prefix/lib/monodevelop/AddIns/PyBinding/PyBinding.dll
Requires: monodevelop >= %version

BuildRequires: mono-mcs monodevelop mono-addins-devel libgtk-sharp2-devel
BuildRequires: /proc

%description
MonoDevelop is a full-featured integrated development environment (IDE) for
mono and Gtk#. It was originally a port of SharpDevelop 0.98.

Python Language Binding

%prep
%setup -q

%__subst "s|^linuxpkgconfigdir = @libdir@/pkgconfig|linuxpkgconfigdir = %_pkgconfigdir|" \
	Makefile.include

%build
./configure --prefix=/usr
%make

%install
%make_install DESTDIR=%buildroot install

%files
%_prefix/lib/monodevelop/AddIns/PyBinding/*

%changelog
* Mon Feb 20 2012 Alexey Shabalin <shaba@altlinux.ru> 2.8.6.4-alt1
- 2.8.6.4

* Thu Mar 10 2011 Alexey Shabalin <shaba@altlinux.ru> 2.4-alt1
- 2.4

* Tue Dec 15 2009 Alexey Shabalin <shaba@altlinux.ru> 2.2-alt1
- 2.2

* Tue Dec 08 2009 Alexey Shabalin <shaba@altlinux.ru> 0.2-alt1
- Initial build for ALTLinux
