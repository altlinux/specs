# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-fedora-compat
BuildRequires: gcc-c++ unzip
# END SourceDeps(oneline)
%global prerel rc1

Name:           blobby
Version:        1.0
Release:        alt2_0.1.rc1
Summary:        Volley-ball game
Group:          Games/Other
License:        GPLv2+
URL:            http://blobby.sourceforge.net
Source0:        http://downloads.sourceforge.net/%{name}/%{name}2-linux-%{version}%{prerel}.tar.gz
Source1:        blobby.desktop
Patch0:         blobby-1.0rc1-gcc47.patch
BuildRequires:  libSDL-devel libphysfs-devel zlib-devel ctest cmake boost-devel boost-filesystem-devel boost-wave-devel boost-graph-parallel-devel boost-math-devel boost-mpi-devel boost-program_options-devel boost-signals-devel boost-intrusive-devel boost-asio-devel zip
BuildRequires:  ImageMagick desktop-file-utils icon-theme-hicolor
Source44: import.info

%description
Blobby Volley is one of the most popular freeware games.
Blobby Volley 2 is the continuation of this lovely game.

%prep
%setup -q -n %{name}-%{version}%{prerel}
%patch0 -p1 -b .gcc47

%build
%{fedora_cmake} .
make %{?_smp_mflags}

%install
make install DESTDIR=$RPM_BUILD_ROOT

# Icon
unzip -o -j data/gfx.zip gfx/ball01.bmp
convert -size 48x48 -transparent black ball01.bmp blobby.png
install -p -m 644 -D blobby.png $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/48x48/apps/blobby.png

# Desktop file
mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications
desktop-file-install  --vendor "fedora" \
        --dir $RPM_BUILD_ROOT%{_datadir}/applications \
        %{SOURCE1}

%files
%doc AUTHORS README ChangeLog COPYING TODO
%{_bindir}/*
%{_datadir}/blobby
%{_datadir}/icons/hicolor/48x48/apps/*.png
%{_datadir}/applications/*.desktop

%changelog
* Tue Jun 26 2012 Igor Vlasenko <viy@altlinux.ru> 1.0-alt2_0.1.rc1
- fixed build

* Wed May 09 2012 Igor Vlasenko <viy@altlinux.ru> 1.0-alt1_0.1.rc1
- update to new release by fcimport

* Fri Mar 02 2012 Igor Vlasenko <viy@altlinux.ru> 0.9c-alt2_1
- rebuild with fixed sourcedep analyser (#27020)

* Mon Dec 19 2011 Igor Vlasenko <viy@altlinux.ru> 0.9c-alt1_1
- update to new release by fcimport

* Mon May 23 2011 Igor Vlasenko <viy@altlinux.ru> 0.9b-alt1_2
- converted from Fedora by srpmconvert script

