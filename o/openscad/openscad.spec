# BEGIN SourceDeps(oneline):
BuildRequires: gcc-c++ libqt4-devel python-devel rpm-macros-fedora-compat
# END SourceDeps(oneline)
BuildRequires: boost-filesystem-devel boost-program_options-devel cmake
%define fedora 21
Name:           openscad
%global shortversion 2014.03
Version:        %{shortversion}
Release:        alt2.1
Summary:        The Programmers Solid 3D CAD Modeller
# COPYING contains a linking exception for CGAL
# AppData is CC0
License:        GPLv2 with exceptions and CC0
Group:          Engineering
URL:            http://www.openscad.org/
Source0:        http://files.openscad.org/openscad-%{shortversion}.src.tar.gz
# https://github.com/openscad/openscad/pull/698
Patch0:         %{name}-desktop-valid.patch
BuildRequires:  libcgal-devel >= 3.6
BuildRequires:  ImageMagick
BuildRequires:  xvfb-run
BuildRequires:  bison >= 2.4
BuildRequires:  boost-devel >= 1.3.5
BuildRequires:  desktop-file-utils
BuildRequires:  eigen3
BuildRequires:  flex >= 2.5.35
BuildRequires:  libglew-devel >= 1.6
BuildRequires:  glib2-devel
BuildRequires: libgmp-devel libgmp_cxx-devel
BuildRequires: xorg-dri-intel xorg-dri-nouveau xorg-dri-radeon xorg-dri-swrast
BuildRequires:  libmpfr-devel >= 3.0.0
BuildRequires:  opencsg-devel >= 1.3.2
BuildRequires:  procps-ng
BuildRequires:  qt4-devel >= 4.4
Source44: import.info

%description
OpenSCAD is a software for creating solid 3D CAD objects.
Unlike most free software for creating 3D models (such as the famous
application Blender) it does not focus on the artistic aspects of 3D
modeling but instead on the CAD aspects. Thus it might be the application
you are looking for when you are planning to create 3D models of machine
parts but pretty sure is not what you are looking for when you are more
interested in creating computer-animated movies.

%prep
%setup -qn %{name}-%{shortversion}
%patch0 -p1

%build
qmake-qt4 VERSION=%{shortversion} PREFIX=%{_prefix}
make %{?_smp_mflags}

# TODO: fix x86_64 build
#*** No rule to make target `/usr/lib/libCGAL.so', needed by `openscad_nogui'.  Stop.
%if 0
# tests
cd tests
_cmake .
make %{?_smp_mflags}
cd -
%endif

%install
make install INSTALL_ROOT=%{buildroot}

# remove MCAD (separated package)
rm -rf %{buildroot}%{_datadir}/%{name}/libraries/MCAD

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop

# tests
cd tests
ctest %{?_smp_mflags} -C All || : # let the tests fail, as they probably won't work in Koji
cat sysinfo.txt || :
cat Testing/Temporary/LastTest.log || :
cd -

%files
%doc COPYING README.md RELEASE_NOTES
%attr(755,root,root) %{_bindir}/%{name}
%if 0%{?fedora} < 21
%{_datadir}/appdata
%else
%{_datadir}/appdata/*.xml
%endif
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.png
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/examples
%dir %{_datadir}/%{name}/libraries
%{_mandir}/man1/*

%changelog
* Sat Jan 03 2015 Ivan A. Melnikov <iv@altlinux.org> 2014.03-alt2.1
- rebuild with boost 1.57.0

* Wed Dec 24 2014 Dmitry Derjavin <dd@altlinux.org> 2014.03-alt2
- Revision up

* Thu May 08 2014 Igor Vlasenko <viy@altlinux.ru> 2014.03-alt1_1
- converted for ALT Linux by srpmconvert tools
- TODO: fixes for No rule to make target /usr/lib/libCGAL.so

