Name: sc
Version: 7.16
Release: alt3.qa1

Summary: Spreadsheet Calculator
License: PD
Group: Sciences/Mathematics
Packager: Alexey Voinov <voins@altlinux.ru>

URL: ftp://ibiblio.org/pub/Linux/apps/financial/spreadsheet
Source0: %name-%version.tar

# Automatically added by buildreq on Tue Apr 06 2004
BuildRequires: libncurses-devel libtinfo-devel

%description
This is a much modified version of the public domain spread sheet sc, which was
posted to Usenet several years ago by Mark Weiser as vc, originally by James
Gosling. It is based on rectangular table much like a financial spreadsheet.

%prep
%setup -q

%build
make CFLAGS="-DSYSV3 $RPM_OPT_FLAGS" LIBDIR=%_docdir/%name-%version

%install
mkdir -p $RPM_BUILD_ROOT{%_bindir,%_libdir,%_man1dir,%_docdir/%name-%version}
make install prefix=$RPM_BUILD_ROOT%_prefix MANDIR=$RPM_BUILD_ROOT%_man1dir \
	LIBDIR=$RPM_BUILD_ROOT%_docdir/%name-%version

mkdir -p %buildroot%_desktopdir
cat > %buildroot%_desktopdir/%{name}.desktop <<EOF
[Desktop Entry]
Version=1.0
Type=Application
Name=Spreadsheet Calculator
Comment=Spreadsheet Calculator
Icon=utilities-terminal
Exec=%{name}
Terminal=true
Categories=Utility;Calculator;
EOF

%files
%doc CHANGES README sc.doc psc.doc tutorial.sc VMS_NOTES torev build.com
%_bindir/*
%_man1dir/*
%_desktopdir/%{name}.desktop

%changelog
* Sat Apr 16 2011 Igor Vlasenko <viy@altlinux.ru> 7.16-alt3.qa1
- NMU: converted menu to desktop file

* Tue Sep 22 2009 Alexey Voinov <voins@altlinux.ru> 7.16-alt3
- debian patch applied
- update-menus removed

* Mon Jan 17 2005 Alexey Voinov <voins@altlinux.ru> 7.16-alt2
- gcc34 patch added

* Tue Apr 06 2004 Alexey Voinov <voins@altlinux.ru> 7.16-alt1
- updated version (7.16)
- removed all obsolete patches
- spec clean up

* Sun Oct 27 2002 Alexey Voinov <voins@voins.program.ru> 6.21-alt2
- rebuilt with gcc3.2
- spec cleanup
- buildreq updated

* Sat May 19 2001 Alexey Voinov <voins@voins.program.ru>
- initial build (source and patch from debian)

