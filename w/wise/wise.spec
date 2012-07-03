%define name	wise
%define version	2.4.1
%define release	alt1

Name: wise
Version: 2.4.1
Release: %release
Summary: Comparisons of DNA and protein sequences
Group: Sciences/Biology
License: GPL
Url: http://www.ebi.ac.uk/Wise2/doc_wise2.html
Packager: Boris Savelev <boris@altlinux.org>

Source: http://www.ebi.ac.uk/~birney/wise2/%name%version.tar.gz
Source1: manpages.tar
Patch1: 01_welcome-csh.dpatch
Patch2: 02_isnumber.dpatch

# Automatically added by buildreq on Mon Jul 06 2009
BuildRequires: OpenSP docbook-dtds docbook-to-man glib-devel w3c-markup-validator-libs

%description
Wise2 is a package focused on comparisons of biopolymers, commonly DNA and
protein sequence. Wise2's particular forte is the comparison of DNA sequence
at the level of its protein translation. This comparison allows the simulta-
neous prediction of say gene structure with homology based alignment.

The Wise2 package was principally written by Ewan Birney, who wrote the main
genewise and estwise programs. The protein comparison database search program
was written by Richard Copley using the underlying Wise2 libraries.
Wise2 also uses code from Sean Eddy for reading HMMs and
for Extreme value distribution fitting.

%prep
%setup -n %name%version
%patch1 -p1
%patch2 -p1
tar xf %SOURCE1

%build
%make_build CFLAGS="-c %optflags `glib-config --cflags`"  EXTRALIBS="-lm -lglib" -C src all
%make -C manpages

%install
install -d -m 755 %buildroot%_bindir
install -m 755 src/models/{pswdb,psw,genewisedb,estwisedb,estwise,genewise,dba,dnal,genomewise} %buildroot%_bindir
install -d -m 755 %buildroot%_datadir/%name
install -m 644 wisecfg/* %buildroot%_datadir/%name
install -d -m 755 %buildroot%_man1dir
cp manpages/*.1 %buildroot%_man1dir

# configuration
install -d -m 755 %buildroot%_sysconfdir/profile.d
echo "export WISECONFIGDIR=%_datadir/%name" > %buildroot%_sysconfdir/profile.d/%name.sh
echo "setenv WISECONFIGDIR %_datadir/%name" > %buildroot%_sysconfdir/profile.d/%name.csh

%files
%doc README LICENSE docs
%_bindir/*
%_datadir/%name
%_man1dir/*
%config(noreplace) %_sysconfdir/profile.d/*

%changelog
* Mon Jul 06 2009 Boris Savelev <boris@altlinux.org> 2.4.1-alt1
- initial build from Mandriva

* Thu Jan 03 2008 Olivier Blin <oblin@mandriva.com> 2.2.0-5mdv2008.1
+ Revision: 140932
- restore BuildRoot

  + Thierry Vignaud <tvignaud@mandriva.com>
    - kill re-definition of %%buildroot on Pixel's request

* Wed Aug 08 2007 Eric Fernandez <zeb@mandriva.org> 2.2.0-5mdv2008.0
+ Revision: 60257
- version number fix

* Tue Dec 19 2006 Eric Fernandez <zeb@mandriva.org> 2.2.0-4mdv2007.0
+ Revision: 100256
- Import wise

* Mon Jun 26 2006 Eric Fernandez <zeb@zebulon.org.uk> 2.2.0-4mdv2007.0
- rebuild
- use mkrel

* Fri Jul 29 2005 Guillaume Rousse <guillomovitch@mandriva.org> 2.2.0-3mdk
- spec cleanup

* Fri Jul 23 2004 Guillaume Rousse <guillomovitch@mandrake.org> 2.2.0-2mdk
- rpmbuildupdate aware

* Sat Jan 24 2004 Guillaume Rousse <guillomovitch@mandrake.org> 2.2.0-1mdk
- first mdk release, after a spec file stolen from Luc Ducazu <luc@biolinux.org>

