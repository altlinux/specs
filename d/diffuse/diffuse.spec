Name:		diffuse
Version:	0.4.5
Release:	alt1.1
Summary:	Graphical tool for comparing and merging text files
License: 	GPLv2+
Group: 		Development/Tools
Packager:	Alex Negulescu <alecs@altlinux.org>
Url:		http://diffuse.sourceforge.net/
Source0:	%name-%version.tar.bz2
BuildArch:	noarch
BuildRequires:	libnss-role

%description
Diffuse is a graphical tool for merging and comparing text files.  Diffuse is
able to compare an arbitrary number of files side-by-side and gives users the
ability to manually adjust line matching and directly edit files.  Diffuse can
also retrieve revisions of files from Bazaar, CVS, Darcs, Git, Mercurial,
Monotone, Subversion, and SVK repositories for comparison and merging.


%prep
%setup -q

%build

%install
%__mkdir_p %buildroot
%__cp -a src/* %buildroot/

%clean
%__rm -rf %buildroot

%files
%defattr(-,root,root)
%_bindir/%name
%_datadir/%name/syntax/*
%_datadir/applications/%name.desktop
%_datadir/gnome/help/diffuse/*
%_datadir/omf/diffuse/*
%_datadir/pixmaps/diffuse.png
%config(noreplace) %_sysconfdir/diffuserc
%_mandir/man*/*
%doc AUTHORS ChangeLog COPYING README

%changelog
* Tue Oct 25 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.4.5-alt1.1
- Rebuild with Python-2.7

* Sun Sep 18 2011 Alex Negulescu <alecs@altlinux.org> 0.4.5-alt1
- initial build for ALT Linux
