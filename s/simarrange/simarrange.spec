%global shortcommit 0f1fbef
%global relstring   git%{shortcommit}

Name:           simarrange
Version:        0.0
Release:        alt4.%{relstring}
Summary:        STL 2D plate packer with collision simulation

Group:		Engineering
License:        AGPLv3+
URL:            https://github.com/kliment/%name
Source0:        %{name}-%{version}.tar
Patch1:         simarrange-fedora-opencv4.patch
BuildRequires:  libadmesh-devel
BuildRequires:  libgomp-devel
BuildRequires:  libargtable2-devel
BuildRequires:  libopencv-devel
BuildRequires:  libuthash-devel
BuildRequires:  gcc-c++

%description
Simarrange is a program that simulates collisions between STL meshes in
2D in order to generate tightly packed sets of parts. It takes a
directory of STL files as input and outputs STL files with combined
plates of parts.  The parts are assumed to be in the correct printable
orientation already.

%prep
%setup -q
%patch1 -p1

mv simarrange.c simarrange.cpp

# bundling
rm utlist.h
rm admesh -rf

%build
# the build script is one line and would need patching, so just skip it
g++ %{optflags} simarrange.cpp -o ./%{name} -lm $(pkg-config opencv4 --cflags --libs) \
    -ladmesh -largtable2 -fopenmp -DPARALLEL

%install
install -Dpm0755 %name %buildroot%_bindir/%name
install -Dpm0644 %name.1 %buildroot%_man1dir/%name.1

%files
%doc COPYING Readme
%_bindir/%name
%_man1dir/%name.*

%changelog
* Tue Apr 07 2020 Aleksei Nikiforov <darktemplar@altlinux.org> 0.0-alt4.git0f1fbef
- Rebuilt with opencv-4.3.0.

* Tue Jun 05 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 0.0-alt3.git0f1fbef
- NMU: rebuilt with opencv 3.4.

* Fri Mar 20 2015 Andrey Cherepanov <cas@altlinux.org> 0.0-alt2.git0f1fbef
- New version from upstream Git

* Wed Feb 19 2014 Andrey Cherepanov <cas@altlinux.org> 0.0-alt1.20131019gitd52382f
- Import from Fedora
