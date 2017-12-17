# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-perl
BuildRequires: /usr/bin/desktop-file-install ImageMagick-tools gcc-c++ perl(Class/Accessor.pm) perl(Encode.pm) perl(ExtUtils/CppGuess.pm) perl(IO/All.pm) perl(Math/Trig.pm) perl(OpenGL.pm) perl(PDF/API2.pm) perl(WebService/Prowl.pm) perl(XML/SAX/Base.pm) perl-podlators
# END SourceDeps(oneline)
%set_perl_req_method relaxed

%define fedora 26
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:           slic3r
Version:        1.2.9
Release:        alt1_15.1
Summary:        G-code generator for 3D printers (RepRap, Makerbot, Ultimaker etc.)
License:        AGPLv3 and CC-BY
# Images are CC-BY, code is AGPLv3
Group:          Engineering
URL:            http://slic3r.org/
Source0:        https://github.com/alexrj/Slic3r/archive/%{version}.tar.gz

# Modify Build.PL so we are able to build this on Fedora
Patch0:         %{name}-buildpl.patch

# Use /usr/share/slic3r as datadir
Patch1:         %{name}-datadir.patch
Patch2:         %{name}-english-locale.patch
Patch3:         %{name}-linker.patch
#Patch4:         %{name}-clipper.patch

# https://bugzilla.redhat.com/show_bug.cgi?id=1306668
# https://github.com/alexrj/Slic3r/issues/3117#issuecomment-187767676
Patch5:         %{name}-boost160.patch

# Patch to manually cast too bool, fix FTBFS
# Will report upstream
Patch6:         %{name}-boolcast.patch

# https://bugzilla.redhat.com/show_bug.cgi?id=1285807
# https://github.com/alexrj/Slic3r/commit/1a09ae81db06602050ae83620268efa33ed14da1
Patch7:         %{name}-wxclose.patch

# https://github.com/alexrj/Slic3r/pull/3575
Patch8:         %{name}-opengl070.patch

Source1:        %{name}.desktop
Source2:        %{name}.appdata.xml

BuildRequires:  perl-devel
BuildRequires:  rpm-build-perl
BuildRequires:  perl(Class/XSAccessor.pm)
BuildRequires:  perl(Encode/Locale.pm)
BuildRequires:  perl(ExtUtils/MakeMaker.pm)
BuildRequires:  perl(ExtUtils/ParseXS.pm)
BuildRequires:  perl(ExtUtils/Typemaps/Default.pm)
BuildRequires:  perl(ExtUtils/Typemaps.pm)
BuildRequires:  perl(File/Basename.pm)
BuildRequires:  perl(File/Spec.pm)
BuildRequires:  perl(Getopt/Long.pm)
BuildRequires:  perl(Growl/GNTP.pm)
BuildRequires:  perl(IO/Scalar.pm)
BuildRequires:  perl(List/Util.pm)
BuildRequires:  perl(Math/PlanePath.pm)
BuildRequires:  perl(Module/Build/WithXSpp.pm)
BuildRequires:  perl(Moo.pm)
BuildRequires:  perl(parent.pm)
BuildRequires:  perl(POSIX.pm)
BuildRequires:  perl(Scalar/Util.pm)
BuildRequires:  perl(Storable.pm)
BuildRequires:  perl(SVG.pm)
BuildRequires:  perl(Test/Harness.pm)
BuildRequires:  perl(Test/More.pm)
BuildRequires:  perl(Thread/Semaphore.pm)
BuildRequires:  perl(threads.pm)
BuildRequires:  perl(Time/HiRes.pm)
BuildRequires:  perl(Unicode/Normalize.pm)
BuildRequires:  perl(Wx.pm)
BuildRequires:  perl(XML/SAX.pm)
BuildRequires:  perl(XML/SAX/ExpatXS.pm)

BuildRequires:  libadmesh-devel >= 0.98.1
BuildRequires:  boost-asio-devel boost-context-devel boost-coroutine-devel boost-devel boost-devel-headers boost-filesystem-devel boost-flyweight-devel boost-geometry-devel boost-graph-parallel-devel boost-interprocess-devel boost-locale-devel boost-lockfree-devel boost-log-devel boost-math-devel boost-mpi-devel boost-msm-devel boost-multiprecision-devel boost-polygon-devel boost-program_options-devel boost-python-devel boost-python-headers boost-signals-devel boost-wave-devel
BuildRequires:  desktop-file-utils
BuildRequires:  libpoly2tri-devel
#BuildRequires:  polyclipping-devel >= 6.2.0
BuildRequires:  ImageMagick

Requires:       perl(XML/SAX.pm)
Requires:       libadmesh >= 0.98.1
Provides:       bundled(polyclipping) = 6.2.9
Source44: import.info


%description
Slic3r is a G-code generator for 3D printers. It's compatible with RepRaps,
Makerbots, Ultimakers and many more machines.
See the project homepage at slic3r.org and the documentation on the Slic3r wiki
for more information.

%prep
%setup -qn Slic3r-%{version}

%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
#%%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1
%patch8 -p1

# Remove bundled admesh, clipper, poly2tri and boost
rm -rf xs/src/admesh
#rm xs/src/clipper.*pp
rm -rf xs/src/poly2tri
rm -rf xs/src/boost

%build
cd xs
perl ./Build.PL --install_path bindoc=%_man1dir installdirs=vendor optimize="$RPM_OPT_FLAGS"
./Build
cd -
# Building non XS part only runs test, so skip it and run it in tests

# prepare pngs in mutliple sizes
for res in 16 32 48 128 256; do
  mkdir -p hicolor/${res}x${res}/apps
done
cd hicolor
convert ../var/Slic3r.ico %{name}.png
cp %{name}-0.png 256x256/apps/%{name}.png
cp %{name}-1.png 128x128/apps/%{name}.png
cp %{name}-2.png 48x48/apps/%{name}.png
cp %{name}-3.png 32x32/apps/%{name}.png
cp %{name}-4.png 16x16/apps/%{name}.png
rm %{name}-*.png
cd -

# To avoid "iCCP: Not recognized known sRGB profile that has been edited"
cd var
find . -type f -name "*.png" -exec convert {} -strip {} \;
cd -

%install
cd xs
./Build install destdir=%{buildroot} create_packlist=0
cd -
find %{buildroot} -type f -name '*.bs' -size 0 -exec rm -f {} \;

# I see no way of installing slic3r with it's build script
# So I copy the files around manually
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{perl_vendor_privlib}
mkdir -p %{buildroot}%{_datadir}/%{name}
mkdir -p %{buildroot}%{_datadir}/icons
mkdir -p %{buildroot}%{_datadir}/appdata

cp -a %{name}.pl %{buildroot}%{_bindir}/%{name}
cp -ar lib/* %{buildroot}%{perl_vendor_privlib}

cp -a var/* %{buildroot}%{_datadir}/%{name}
cp -r hicolor %{buildroot}%{_datadir}/icons
desktop-file-install --dir=%{buildroot}%{_datadir}/applications %{SOURCE1}

cp %{SOURCE2} %{buildroot}%{_datadir}/appdata/%{name}.appdata.xml

# %{_fixperms} %{buildroot}*

%check
cd xs
./Build test verbose=1
cd -
SLIC3R_NO_AUTO=1 perl Build.PL installdirs=vendor
# the --gui runs no tests, it only checks requires

%files
%doc README.md
%{_bindir}/%{name}
%{perl_vendor_privlib}/Slic3r*
%{perl_vendor_archlib}/Slic3r*
%{perl_vendor_archlib}/auto/Slic3r*
%{_datadir}/icons/hicolor/*/apps/%{name}.png
%{_datadir}/applications/%{name}.desktop
%if 0%{?fedora} < 21
%endif
%{_datadir}/appdata/%{name}.appdata.xml
%{_datadir}/%{name}

%changelog
* Fri Dec 15 2017 Igor Vlasenko <viy@altlinux.ru> 1.2.9-alt1_15.1
- rebuild with new perl 5.26.1

* Fri Oct 20 2017 Igor Vlasenko <viy@altlinux.ru> 1.2.9-alt1_15
- update to new release by fcimport

* Fri Feb 03 2017 Igor Vlasenko <viy@altlinux.ru> 1.2.9-alt1_8.1
- rebuild with new perl 5.24.1

* Mon Jan 30 2017 Igor Vlasenko <viy@altlinux.ru> 1.2.9-alt1_8
- converted for ALT Linux by srpmconvert tools

* Wed Nov 25 2015 Igor Vlasenko <viy@altlinux.ru> 1.2.1-alt1.1
- rebuild with new perl 5.22.0

* Mon Nov 17 2014 Dmitry Derjavin <dd@altlinux.org> 1.2.1-alt1
- 1.2.1;
- BuildRequires errors work around.

* Mon Feb 24 2014 Dmitry Derjavin <dd@altlinux.org> 1.0.0-alt1.RC2
- Initial ALT Linux build.

