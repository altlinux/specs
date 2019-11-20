Group: Engineering
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-perl
BuildRequires: /usr/bin/desktop-file-install boost-devel boost-filesystem-devel perl(Class/Accessor.pm) perl(Encode.pm) perl(IO/All.pm) perl(LWP/UserAgent.pm) perl(Math/Trig.pm) perl(OpenGL.pm) perl(PDF/API2.pm) perl(WebService/Prowl.pm) perl-podlators
# END SourceDeps(oneline)
%set_perl_req_method relaxed

%define fedora 30
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%global use_system_admesh 0
%global use_system_expat 1
%global use_system_polyclipping 1
%global use_system_poly2tri 1

Name:           slic3r
Version:        1.3.0
Release:        alt2_10
Summary:        G-code generator for 3D printers (RepRap, Makerbot, Ultimaker etc.)
License:        AGPLv3 and CC-BY
# Images are CC-BY, code is AGPLv3
URL:            http://slic3r.org/
Source0:        https://github.com/alexrj/Slic3r/archive/%{version}.tar.gz

# Modify Build.PL so we are able to build this on Fedora
Patch0:         %{name}-buildpl.patch

# Use /usr/share/slic3r as datadir
Patch1:         %{name}-datadir.patch
Patch2:         %{name}-english-locale.patch
Patch3:         %{name}-linker.patch
Patch4:         %{name}-clipper.patch
Patch5:         %{name}-1.3.0-fixtest.patch
Patch6:         %{name}-wayland.patch
Patch7:         %{name}-boost169.patch

Source1:        %{name}.desktop
Source2:        %{name}.appdata.xml

BuildRequires:  gcc-c++
BuildRequires:  perl-devel
BuildRequires:  rpm-build-perl
BuildRequires:  perl(Class/XSAccessor.pm)
BuildRequires:  perl(Devel/CheckLib.pm)
BuildRequires:  perl(Devel/Peek.pm)
BuildRequires:  perl(Encode/Locale.pm)
BuildRequires:  perl(ExtUtils/CppGuess.pm)
BuildRequires:  perl(ExtUtils/CBuilder.pm)
BuildRequires:  perl(ExtUtils/MakeMaker.pm)
BuildRequires:  perl(ExtUtils/Typemaps/Default.pm)
BuildRequires:  perl(ExtUtils/Typemaps.pm)
BuildRequires:  perl(File/Basename.pm)
BuildRequires:  perl(File/Spec.pm)
BuildRequires:  perl(Getopt/Long.pm)
BuildRequires:  perl(IO/Scalar.pm)
BuildRequires:  perl(IO/Uncompress/Unzip.pm)
BuildRequires:  perl(List/Util.pm)
BuildRequires:  perl(local/lib.pm)
BuildRequires:  perl(Module/Build/WithXSpp.pm)
BuildRequires:  perl(Moo.pm)
BuildRequires:  perl(parent.pm)
BuildRequires:  perl(POSIX.pm)
BuildRequires:  perl(Scalar/Util.pm)
BuildRequires:  perl(SVG.pm)
BuildRequires:  perl(Test/Harness.pm)
BuildRequires:  perl(Test/More.pm)
BuildRequires:  perl(Thread/Queue.pm)
BuildRequires:  perl(threads.pm)
BuildRequires:  perl(threads/shared.pm)
BuildRequires:  perl(Time/HiRes.pm)
BuildRequires:  perl(Unicode/Normalize.pm)
BuildRequires:  perl(Wx.pm)

%if %{use_system_admesh}
BuildRequires:  libadmesh-devel >= 0.98.1
Requires:       libadmesh >= 0.98.1
%else
Provides:       bundled(admesh) = 0.98
# Bundled admesh FTBFS with:
# error "admesh works correctly on little endian machines only!"
ExcludeArch:    ppc ppc64 s390 s390x
%endif

%if %{use_system_expat}
BuildRequires:  libexpat-devel >= 2.2.0
%else
Provides:       bundled(expat) = 2.2.0
%endif

%if %{use_system_polyclipping}
BuildRequires:  libpolyclipping-devel >= 6.4.2
%else
Provides:       bundled(polyclipping) = 6.4.2
%endif

%if %{use_system_poly2tri}
BuildRequires:  libpoly2tri-devel
%else
Provides:       bundled(poly2tri) = 0.0
%endif

BuildRequires:  boost-complete
BuildRequires:  libleatherman-devel
BuildRequires:  desktop-file-utils
BuildRequires:  ImageMagick-tools
Requires:       perl(Growl/GNTP.pm) >= 0.150
Requires:       perl(XML/SAX.pm)
Source44: import.info
# alt bug #34434
Requires:       perl(OpenGL.pm)
Requires:       perl(Class/Accessor.pm)
Requires:       perl(Math/Trig.pm)
Requires:       perl-Wx-GLCanvas

# Optional dependency. Not packaged in Fedora yet, hence we cannot list it.
# It's only used for magically finding octoprint servers.
# #Recommends:    perl(Net::Bonjour)

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
%patch3 -p1 -b .linker
%if %{use_system_polyclipping}
%patch4 -p1
%endif
%patch5 -p1 -b .fixtest
%patch6 -p1
%patch7 -p1

# Optional removals
%if %{use_system_admesh}
rm -rf xs/src/admesh
sed -i '/src\/admesh/d' xs/MANIFEST
%endif

%if %{use_system_expat}
rm -rf xs/src/expat
sed -i '/src\/expat/d' xs/MANIFEST
# These are the files with hardcoded expat/expat.h includes
sed -i 's|expat/expat.h|expat.h|g' xs/src/libslic3r/IO/AMF.cpp
sed -i 's|expat/expat.h|expat.h|g' xs/src/libslic3r/IO/TMF.hpp
%endif

%if %{use_system_polyclipping}
#rm xs/src/clipper.*pp
export SYSTEM_LIBS="${SYSTEM_LIBS} -lpolyclipping"
%endif

%if %{use_system_poly2tri}
rm -rf xs/src/poly2tri
sed -i '/src\/poly2tri/d' xs/MANIFEST
%endif

# We always do boost.
rm -rf xs/src/boost
sed -i '/src\/boost\/nowide/d' xs/MANIFEST
sed -i 's|\(ExtUtils::ParseXS\s\+\)3.35|\13.34|' Build.PL xs/Build.PL

%build
%if %{use_system_admesh}
export SYSTEM_LIBS="${SYSTEM_LIBS} -ladmesh"
%endif

%if %{use_system_expat}
export SYSTEM_LIBS="${SYSTEM_LIBS} -lexpat"
%endif

%if %{use_system_poly2tri}
export SYSTEM_LIBS="${SYSTEM_LIBS} -lpoly2tri"
%endif

cd xs
[[ ! -z "${SYSTEM_LIBS}" ]] && echo "SYSTEM_LIBS is ${SYSTEM_LIBS}"
perl ./Build.PL installdirs=vendor optimize="$RPM_OPT_FLAGS"
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
* Wed Nov 20 2019 Igor Vlasenko <viy@altlinux.ru> 1.3.0-alt2_10
- update to new release by fcimport

* Mon Jun 17 2019 Igor Vlasenko <viy@altlinux.ru> 1.3.0-alt2_8
- update to new release by fcimport

* Sat Feb 09 2019 Igor Vlasenko <viy@altlinux.ru> 1.3.0-alt2_6
- update to new release by fcimport

* Thu Jan 24 2019 Igor Vlasenko <viy@altlinux.ru> 1.3.0-alt2_3
- rebuild with new perl 5.28.1

* Sat Jul 14 2018 Igor Vlasenko <viy@altlinux.ru> 1.3.0-alt1_3
- new version
- added bliser@ patch (closes: #34434)

* Mon May 07 2018 Igor Vlasenko <viy@altlinux.ru> 1.2.9-alt1_18
- update to new release by fcimport

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

