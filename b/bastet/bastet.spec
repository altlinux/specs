# BEGIN SourceDeps(oneline):
BuildRequires: /usr/bin/desktop-file-install gcc-c++ unzip
# END SourceDeps(oneline)
BuildRequires: boost-program_options-devel
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:		bastet
Version:	0.43.1
Release:	alt1_22
Summary:	An evil falling bricks game

Group:		Games/Other
License:	GPLv3+
URL:		http://fph.altervista.org/prog/bastet.html
Source0:	https://github.com/fph/bastet/archive/%{version}.zip
Source1:	%{name}.desktop
# self-made icon
Source2:	%{name}.png
Patch0:		bastet-tr1.patch
Patch1:		bastet-fix-appdata.patch

BuildRequires:	boost-asio-devel boost-context-devel boost-coroutine-devel boost-devel boost-devel-headers boost-filesystem-devel boost-flyweight-devel boost-geometry-devel boost-graph-parallel-devel boost-interprocess-devel boost-locale-devel boost-lockfree-devel boost-log-devel boost-math-devel boost-mpi-devel boost-msm-devel boost-multiprecision-devel boost-polygon-devel boost-program_options-devel boost-python-devel boost-python-headers boost-signals-devel boost-wave-devel libncurses++-devel libncurses-devel libncursesw-devel libtic-devel libtinfo-devel desktop-file-utils
Source44: import.info


%description
Bastet is a simple ncurses-based falling bricks like game. Unlike 
normal, however, Bastet does not choose your next brick at random. 
Instead, it uses a special algorithm designed to choose the worst 
brick possible. As you can imagine, playing Bastet can be a very 
frustrating experience!


%prep
%setup -q

%patch0 -p1
%patch1 -p1

# remove reference to Tetris to match our guidelines
sed -e 's/Tetris(R)/any falling bricks game/g' -e 's/Tetris/falling bricks game/g' \
-e 's/tetris/falling bricks game/g' README > README.new
mv -f README.new README
# remove also any reference to Tetris in the bastet manpage
sed -e 's/Tetris(r)/any falling bricks game/g' -e 's/tetris/falling bricks game/g' \
bastet.6 > bastet.6.new
mv -f bastet.6.new bastet.6


%build

%make_build CXXFLAGS="%{optflags}"


%install

# install the AppData file
mkdir -p %{buildroot}%{_datadir}/appdata
cp bastet.appdata.xml %{buildroot}%{_datadir}/appdata/

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
%{_datadir}/appdata/%{name}.appdata.xml
%{_datadir}/icons/hicolor/*/apps/%{name}.png
%{_mandir}/man6/*


%changelog
* Sat Feb 03 2018 Igor Vlasenko <viy@altlinux.ru> 0.43.1-alt1_22
- update to new release by fcimport

* Wed Sep 27 2017 Igor Vlasenko <viy@altlinux.ru> 0.43.1-alt1_20
- update to new release by fcimport

* Thu Aug 03 2017 Igor Vlasenko <viy@altlinux.ru> 0.43.1-alt1_18
- update to new release by fcimport

* Thu Mar 16 2017 Igor Vlasenko <viy@altlinux.ru> 0.43.1-alt1_15
- update to new release by fcimport

* Thu Apr 07 2016 Dmitry V. Levin (QA) <qa_ldv@altlinux.org> 0.43-alt4_21.1.qa1
- NMU: rebuilt with boost 1.57.0 -> 1.58.0.

* Sat Jan 03 2015 Ivan A. Melnikov <iv@altlinux.org> 0.43-alt4_21.1
- rebuild with boost 1.57.0

* Mon Aug 12 2013 Igor Vlasenko <viy@altlinux.ru> 0.43-alt4_21
- update to new release by fcimport

* Mon Aug 05 2013 Igor Vlasenko <viy@altlinux.ru> 0.43-alt4_20
- update to new release by fcimport

* Mon Feb 11 2013 Igor Vlasenko <viy@altlinux.ru> 0.43-alt4_19
- update to new release by fcimport

* Fri Nov 30 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.43-alt4_17.1
- Rebuilt with Boost 1.52.0

* Wed Sep 05 2012 Igor Vlasenko <viy@altlinux.ru> 0.43-alt4_17
- rebuild with new boost

* Mon Aug 27 2012 Igor Vlasenko <viy@altlinux.ru> 0.43-alt3_17
- update to new release by fcimport

* Fri Jul 27 2012 Igor Vlasenko <viy@altlinux.ru> 0.43-alt3_16
- update to new release by fcimport

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

