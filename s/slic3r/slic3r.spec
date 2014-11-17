Name: slic3r
Version: 1.2.1
Release: alt1
Summary: G-code generator for 3D printers (RepRap, Makerbot, Ultimaker etc.)
# Images are CC-BY, code is AGPLv3
License: AGPLv3 and CC-BY
Group: Engineering
URL: http://slic3r.org/
Source0: %name-%version.tar
Source1: %name.desktop

BuildRequires: perl(Encode/Locale.pm)
BuildRequires: perl(ExtUtils/MakeMaker.pm)
BuildRequires: perl(ExtUtils/ParseXS.pm)
BuildRequires: perl(File/Basename.pm)
BuildRequires: perl(File/Spec.pm)
BuildRequires: perl(Getopt/Long.pm)
BuildRequires: perl(Math/Geometry/Voronoi.pm)
BuildRequires: perl(Math/PlanePath.pm)
BuildRequires: perl(Module/Build/WithXSpp.pm)
BuildRequires: perl(Moo.pm)
BuildRequires: perl(Scalar/Util.pm)
BuildRequires: perl(Test/Harness.pm)
BuildRequires: perl(Test/More.pm)
BuildRequires: perl(IO/Scalar.pm)
BuildRequires: perl(Time/HiRes.pm)

BuildRequires: perl(Class/XSAccessor.pm)
BuildRequires: perl(XML/SAX/ExpatXS.pm)

BuildRequires: perl(Wx.pm)

BuildRequires: perl(Growl/GNTP.pm)
BuildRequires: perl-Wx-GLCanvas
BuildRequires: perl(OpenGL.pm)

BuildRequires: perl(ExtUtils/Typemaps/Default.pm)
BuildRequires: perl(ExtUtils/Typemap.pm)

BuildRequires: libpolyclipping-devel
BuildRequires: desktop-file-utils
BuildRequires: gcc-c++

# To fix:
%add_findreq_skiplist %perl_vendor_privlib/Slic3r/Fill.pm
%add_findreq_skiplist %perl_vendor_privlib/Slic3r/Fill/Base.pm
%add_findreq_skiplist %perl_vendor_privlib/Slic3r/GCode/CoolingBuffer.pm
%add_findreq_skiplist %perl_vendor_privlib/Slic3r/GCode/MotionPlanner.pm
%add_findreq_skiplist %perl_vendor_privlib/Slic3r/GUI.pm
# %add_findreq_skiplist %perl_vendor_privlib/Slic3r/GUI/AboutDialog.pm
# %add_findreq_skiplist %perl_vendor_privlib/Slic3r/GUI/BedShapeDialog.pm
# %add_findreq_skiplist %perl_vendor_privlib/Slic3r/GUI/ConfigWizard.pm
# %add_findreq_skiplist %perl_vendor_privlib/Slic3r/GUI/MainFrame.pm
%add_findreq_skiplist %perl_vendor_privlib/Slic3r/GUI/*
%add_findreq_skiplist %perl_vendor_privlib/Slic3r/Layer/*
%add_findreq_skiplist %perl_vendor_privlib/Slic3r/Print/*
%add_findreq_skiplist %perl_vendor_privlib/Slic3r/SVG.pm
%add_findreq_skiplist %perl_vendor_privlib/Slic3r/Test/*

Requires: perl(ExtUtils/MakeMaker.pm)
Requires: perl(ExtUtils/ParseXS.pm)
Requires: perl(Math/Geometry/Voronoi.pm)
Requires: perl(Module/Build/WithXSpp.pm)
Requires: perl(Scalar/Util.pm)
Requires: perl(Test/Harness.pm)
Requires: perl(Test/More.pm)
Requires: perl(Class/XSAccessor.pm)
Requires: perl(Wx.pm)
Requires: perl(Growl/GNTP.pm)
Requires: perl-Wx-GLCanvas
Requires: perl(OpenGL.pm)
Requires: perl(ExtUtils/Typemaps/Default.pm)
Requires: perl(ExtUtils/Typemap.pm)
Requires: libpolyclipping

%description
Slic3r is a G-code generator for 3D printers. It is compatible with
RepRaps, Makerbots, Ultimakers and many more machines.

%prep
%setup -q

#%patch0 -p1
#%patch1 -p1

# Remove bundled clipper
#rm xs/src/clipper.*pp

%build
cd xs
%perl_vendor_build
cd -
# Building non XS part only runs test, so skip it and run it in tests

%install
cd xs
%perl_vendor_install
cd -
find %buildroot -type f -name '*.bs' -size 0 -exec rm -f {} \;

# I see no way of installing slic3r with it's build script
# So I copy the files around manually
mkdir -p %buildroot%_bindir
mkdir -p %buildroot%perl_vendorlib
mkdir -p %buildroot%_datadir/%name
mkdir -p %buildroot%_datadir/pixmaps

cp -a %name.pl %buildroot%_bindir/%name
cp -ar lib/* %buildroot%perl_vendorlib

cp -a var/* %buildroot%_datadir/%name
ln -s ../%name/Slic3r.ico %buildroot%_datadir/pixmaps/%name.ico
desktop-file-install --dir=%buildroot%_datadir/applications %SOURCE1

#%check
#cd xs
#./Build test
#cd -
#SLIC3R_NO_AUTO=1 perl Build.PL installdirs=vendor
## the --gui runs no tests, it only checks requires

%files
%doc README.md
%_bindir/%name
%perl_vendorlib/Slic3r*
%perl_vendorarch/Slic3r*
%perl_vendorarch/auto/Slic3r*
%_datadir/pixmaps/%name.ico
%_datadir/applications/%name.desktop
%_datadir/%name

%changelog
* Mon Nov 17 2014 Dmitry Derjavin <dd@altlinux.org> 1.2.1-alt1
- 1.2.1;
- BuildRequires errors work around.

* Mon Feb 24 2014 Dmitry Derjavin <dd@altlinux.org> 1.0.0-alt1.RC2
- Initial ALT Linux build.

