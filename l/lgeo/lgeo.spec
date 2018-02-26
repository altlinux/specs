%define povraydir %_datadir/povray-3.6/include

Summary: LeoCAD POV-Ray visualisation helper utility
Name:    lgeo
Version: 0.20081215
Release: alt1

License: Distributable, for non-commercial use
Url:     http://www.digitalbricks.org/lgeo.html

#TODO: replace old ones with new ones.
#but it no more use .tab files
Source:  http://www.digitalbricks.org/data/lgeo.zip
#http://www.hassings.dk/l3/lgeofix.html
Source1: http://www.hassings.dk/l3/lgeo/lgeofix.zip
# old LGEO as found at ldraw.org
#http://www.ldraw.org/GetStarted-Win.html
# has .tab files required by leocad
Source2: lgeo-ldraw_setup_2006q3_full_j.zip

Group:   Games/Puzzles
Packager: Igor Vlasenko <viy@altlinux.org>

BuildArch: noarch
BuildRequires: unzip
Requires: povray

%description
The LGEO library is a fan created collection of definitions for LEGO Geometrical Equivalent
Objects (called parts from here on) to be used with POV-Ray. It is no way related or sponsored by
the LEGO Group and free of charge. It may be redistributed freely while copyright of the
intellectual property remains with the author. The LEGO logo displayed on the studs is under
copyright of the LEGO Group.

Use it together with LeoCAD to get LeoCAD projects visualised in POV-Ray.

%prep
%setup -q -n %name
find . -name .DS_Store -delete

%build

%install
mkdir -p %buildroot%povraydir
pushd %buildroot%povraydir
unzip -qqLL %{SOURCE2}
popd

mkdir -p %buildroot%povraydir/lgeo_fix
pushd %buildroot%povraydir/lgeo_fix
unzip -qqLL %{SOURCE1}
popd

mkdir -p %buildroot%povraydir/%name
cp -a  ar lg lg_*.lst %buildroot%povraydir/%name

%files
%doc LGEO.pdf lg_changes.txt
%povraydir/lgeo_fix
%povraydir/%name

%changelog
* Mon Sep 27 2010 Igor Vlasenko <viy@altlinux.ru> 0.20081215-alt1
- Initial build for ALT;
  TODO: integrate with povray properly
