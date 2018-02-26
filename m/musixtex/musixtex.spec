Name: musixtex
Version: T101
Release: alt3.1
Source: ftp://ctan.tug.org/tex-archive/macros/musixtex/taupin/%{name}-%{version}.tar.gz
Source1: musixtex-install.sh
Source2: musixtex-readme
URL: http://www.gmd.de/Misc/Music/musixtex/
Copyright: free copying
Group: Publishing
Summary: MusiXTeX - source files, documentation, musixtex format
BuildRequires: tetex-core >= 2.0-alt0.8
Packager: Yuri N. Sedunov <aris@altlinux.ru>

%description
TeX extensions for music typesetting.
The package allows you to use TeX to write polyphonic, orchestral or
instrumental music. MusixTeX is growing up from MusicTeX and has
advantages both in set of macros and quality of output.
The package contains source files (macros, styles), fonts (mf, tfm),
documentation and the MusiXTeX+plain format.

%package doc
Summary: Documentation for MusixTeX
Group: Publishing
Requires:	%{name} = %{version}

%description doc
This package contents documentation for MisicTeX - Tex extensions for
music typesetting.

%package -n musixflx
Summary: Line breaking program for MusiXTeX.
Group: Publishing
Requires:	%{name} = %{version}

%description -n musixflx
Line breaking program for MusiXTeX.
This program meets the second stage in MusiXTeX's three-pass system.

%prep
%setup -q -c musixtex

%build
cd systems/c-source
%{__cc} -o musixflx musixflx.c

%install
export PREFIX=$RPM_BUILD_ROOT
%_buildshell %SOURCE1
mkdir -p  $RPM_BUILD_ROOT%{_bindir}
mkdir -p  $RPM_BUILD_ROOT%{_docdir}/%{name}
cp doc/license.txt %SOURCE2 $RPM_BUILD_ROOT%{_docdir}/%{name}/
ln -s tex $RPM_BUILD_ROOT%{_bindir}/%{name}
install -m755 systems/c-source/musixflx $RPM_BUILD_ROOT%{_bindir}

%clean

%files
%defattr(-,root,root)
%doc 

%{_datadir}/texmf/fonts/source/public/%{name}
%{_datadir}/texmf/fonts/tfm/public/%{name}
%{_datadir}/texmf/tex/generic/%{name}
%{_datadir}/texmf/web2c/%{name}.*
%{_bindir}/%{name}

%files doc
%{_datadir}/texmf/doc/%{name}
%{_docdir}/%{name}

%files -n musixflx
%defattr(-,root,root)
%{_bindir}/musixflx


%changelog
* Fri Nov 06 2009 Repocop Q. A. Robot <repocop@altlinux.org> T101-alt3.1
- NMU (by repocop): the following fixes applied:
  * altlinux-policy-tex-obsolete-util-calls-in-post for musixtex

* Fri Jan 17 2003 Alexander Bokovoy <ab@altlinux.ru> T101-alt3
- Rebuild against tetex-2.0-alt0.8

* Tue Nov 6 2001 Yuri N. Sedunov <aris@altlinux.ru> alt1
- First build for Sisyphus


