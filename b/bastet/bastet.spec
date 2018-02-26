# BEGIN SourceDeps(oneline):
BuildRequires: gcc-c++
# END SourceDeps(oneline)
BuildRequires: boost-program_options-devel
Name:		bastet
Version:	0.43
Release:	alt3_15
Summary:	An evil falling bricks game

Group:		Games/Other
License:	GPLv3+
URL:		http://fph.altervista.org/prog/bastet.html
Source0:	http://fph.altervista.org/prog/files/%{name}-%{version}.tgz
Source1:	%{name}.desktop
# self-made icon
Source2:	%{name}.png

BuildRequires:	boost-devel boost-filesystem-devel boost-wave-devel boost-graph-parallel-devel boost-math-devel boost-mpi-devel boost-program_options-devel boost-signals-devel boost-intrusive-devel boost-asio-devel ncurses-devel desktop-file-utils
Source44: import.info


%description
Bastet is a simple ncurses-based falling bricks like game. Unlike 
normal, however, Bastet does not choose your next brick at random. 
Instead, it uses a special algorithm designed to choose the worst 
brick possible. As you can imagine, playing Bastet can be a very 
frustrating experience!


%prep
%setup -q
# remove reference to Tetris to match our guidelines
sed -e 's/Tetris(R)/any falling bricks game/g' -e 's/Tetris/falling bricks game/g' \
-e 's/tetris/falling bricks game/g' README > README.new
mv -f README.new README
# remove also any reference to Tetris in the bastet manpage
sed -e 's/Tetris(r)/any falling bricks game/g' -e 's/tetris/falling bricks game/g' \
bastet.6 > bastet.6.new
mv -f bastet.6.new bastet.6


%build

make %{?_smp_mflags} CXXFLAGS="%{optflags}"


%install

mkdir -p %{buildroot}%{_bindir}

install -p -m 755 bastet %{buildroot}%{_bindir}/bastet

# below the desktop file and icon stuff
desktop-file-install \
	--dir=%{buildroot}%{_datadir}/applications	\
	%{SOURCE1}

mkdir -p %{buildroot}%{_datadir}/icons/hicolor/32x32/apps

install -p -m 0644 %{SOURCE2}				\
	%{buildroot}%{_datadir}/icons/hicolor/32x32/apps/%{name}.png

# manpage
mkdir -p %{buildroot}%{_mandir}/man6/
      install -p -m 0644 %{name}.6 \
      %{buildroot}%{_mandir}/man6/%{name}.6


%files
%doc AUTHORS LICENSE NEWS README
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}.png
%{_mandir}/man6/*


%changelog
* Tue Jun 26 2012 Igor Vlasenko <viy@altlinux.ru> 0.43-alt3_15
- fixed build

* Wed May 09 2012 Igor Vlasenko <viy@altlinux.ru> 0.43-alt2_15
- update to new release by fcimport

* Thu Apr 05 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.43-alt2_14.1
- Rebuilt with Boost 1.49.0

* Fri Mar 02 2012 Igor Vlasenko <viy@altlinux.ru> 0.43-alt2_14
- rebuild with fixed sourcedep analyser (#27020)

* Fri Jan 20 2012 Igor Vlasenko <viy@altlinux.ru> 0.43-alt1_14
- update to new release by fcimport

* Sun Dec 04 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.43-alt1_13.1
- Rebuilt with Boost 1.48.0

* Fri Nov 25 2011 Igor Vlasenko <viy@altlinux.ru> 0.43-alt1_13
- update to new release by fcimport

* Fri Jul 29 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.43-alt1_12.1
- Rebuilt with Boost 1.47.0

* Thu Jul 28 2011 Igor Vlasenko <viy@altlinux.ru> 0.43-alt1_12
- update to new release by fcimport

* Fri Jul 01 2011 Igor Vlasenko <viy@altlinux.ru> 0.43-alt1_11
- initial release by fcimport

