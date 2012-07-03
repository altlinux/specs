Summary: xppaut -- Phase Plane Plus Auto: Solves many kinds of equations

Name: xppaut
Version: 6.10
Release: alt1

License: GPL
Group: Sciences/Mathematics
Url: http://www.math.pitt.edu/~bard/xpp/xpp.html
Packager: Vlasenko Igor <viy@altlinux.ru>
Source: http://ftp.debian.org/debian/pool/main/x/xppaut/%{name}%{version}.tar
Source1: %{name}_16.xpm
Source2: %{name}_32.xpm
Source3: %{name}_48.xpm
Patch0: http://ftp.debian.org/debian/pool/main/x/xppaut/xppaut-5.98-fix-build-alt-1.diff

# Automatically added by buildreq on Wed May 14 2008 (-bi)
BuildRequires: libX11-devel

%description
XPPAUT is a tool for solving

   * differential equations,
   * difference equations,
   * delay equations,
   * functional equations,
   * boundary value problems, and
   * stochastic equations.

The code brings together a number of useful algorithms and is extremely portable. All the graphics and interface are written completely in Xlib which explains the somewhat idiosyncratic and primitive widgets interface.
 Homepage: http://www.math.pitt.edu/~bard/xpp/xpp.html


%prep
%setup -c -n %{name}-%{version}
#patch0 -p1
find . -name '*~' -delete

%build

%make_build CFLAGS=' -g -pedantic -O -DNOERRNO -DNON_UNIX_STDIO -DAUTO -DCVODE_YES -DHAVEDLL -DMYSTR1=$(MAJORVER) -DMYSTR2=$(MINORVER) -I/usr/include/X11' LDFLAGS=

%install
make install DESTDIR=$RPM_BUILD_ROOT BINDIR=%_bindir MANDIR=%_man1dir DOCDIR=/usr/share/doc/xppaut
mv $RPM_BUILD_ROOT/usr/share/doc/%{name} ./%{name}-doc
install -m644 -D %SOURCE1 $RPM_BUILD_ROOT%_miconsdir/%{name}.xpm
install -m644 -D %SOURCE2 $RPM_BUILD_ROOT%_niconsdir/%{name}.xpm
install -m644 -D %SOURCE3 $RPM_BUILD_ROOT%_liconsdir/%{name}.xpm
mkdir -p %buildroot%_desktopdir
cat > %buildroot%_desktopdir/%{name}.desktop <<EOF
[Desktop Entry]
Version=1.0
Type=Application
Name=XPPAut
Comment=%{summary}
Icon=%{name}
Exec=%{name}
Terminal=false
Categories=Science;Math;
EOF

# for help to work --- path to help
pushd $RPM_BUILD_ROOT%_docdir; %__ln_s %{name}-%{version} %{name}; popd

%files
%doc %{name}-doc/* HISTORY
%_bindir/*
%_man1dir/*
#%_libdir/%name
%_docdir/%{name}
%_miconsdir/%{name}.xpm
%_niconsdir/%{name}.xpm
%_liconsdir/%{name}.xpm
%_desktopdir/%{name}.desktop

%changelog
* Sun Oct 02 2011 Igor Vlasenko <viy@altlinux.ru> 6.10-alt1
- new version

* Sat Mar 26 2011 Igor Vlasenko <viy@altlinux.ru> 5.98-alt2
- converted debian menu to freedesktop

* Wed Nov 19 2008 Igor Vlasenko <viy@altlinux.ru> 5.98-alt1.1
- NMU (by repocop): the following fixes applied:
 * update_menus for xppaut

* Wed May 14 2008 Igor Vlasenko <viy@altlinux.ru> 5.98-alt1
- new version

* Tue Mar 04 2008 Igor Vlasenko <viy@altlinux.ru> 5.91-alt3
- rebuild with new values of _?iconsdir

* Tue Sep 27 2005 Igor Vlasenko <viy@altlinux.ru> 5.91-alt2
- minor cleanup in %_docdir

* Thu Jul 21 2005 Igor Vlasenko <viy@altlinux.org> 5.91-alt1
- first build for AltLinux
