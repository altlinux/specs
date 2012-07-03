%def_disable debug
%def_disable tcc

%define Name Frink
Name: frink
URL: http://catless.ncl.ac.uk/Programs/%Name
Version: 2.2.2
%define subver p4
Release: alt1
Summary: Static Testing and Formatting for Tcl Programs
Group: Development/Tcl
License: BSD
Source: ftp://catless.ncl.ac.uk/pub/%name-%version%subver.tar.bz2

%{?_enable_tcc:BuildRequires: tcc}

%description
%Name is a Tcl formatting and static check program. It can prettify
your program, and minimize, obfuscate, or sanity check it. It can also
do some rewriting.


%prep
%setup -q
subst '/^CFLAGS=/ s/\(-ansi\)i/\1/' configure.ac
%{?_enable_tcc:subst '/^CFLAGS=/ s/-ansi[[:blank:]]*//' configure.ac}
%{!?_enable_debug:subst '/^CFLAGS=/ s/-g[[:blank:]]*//g' configure.ac}


%build
%add_optflags -fno-strict-aliasing
autoreconf -fisv
%configure %{?_enable_tcc:CC=tcc}
%make_build
bzip2 --best --keep --force ChangeLog


%install
%make_install DESTDIR=%buildroot install


%files
%doc AUTHORS ChangeLog.* README
%_bindir/*


%changelog -n frink
* Fri Oct 27 2006 Led <led@altlinux.ru> 2.2.2-alt1
- initial build for Sisyphus

* Mon Jul 05 2004 - max@suse.de
- New version: 2.2.2p4
* Fri Feb 06 2004 - max@suse.de
- Added -fno-strict-aliasing to CFLAGS.
* Wed Nov 26 2003 - max@suse.de
- New version: 2.2.2p3
* Fri Jun 07 2002 - max@suse.de
- New package: frink-2.1.5
- A tool for static testing and formatting of Tcl programs.
